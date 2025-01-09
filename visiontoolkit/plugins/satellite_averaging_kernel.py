#!/usr/bin/env python

"""
Implementation of the averaging kernel application for satellite data.
Translated to Python by SLB, */12/2024 from IDL code sa documented below.
Note that only relevant parts of that code were taken, and some refactoring
and consolidation has taken place for performance and to facilitate the
change to using numpy arrays as the underlying approach.

Leading documentation string from original algorithm:

    IMS_RD_CO4AK

    Read IMS L2 file to construct CO sub-columns and averaging kernels only
    (cut down from ims_rd_basic to serve as simple e.g. code for Vision project)

    From the resulting structure "s" averaging kernels can be applied to model
    c_vmr_model (ppmv on 101 fine grid levels) to obtain sub-columns accounting
    for the retrieval averaging kernel, c_sc_model (in ppmv) via

    c_sc_model = s.c_apc + matrix_multiply(s.ak,c_vmr_model)

    If required to apply to model profiles on a different grid then the AKs will
    need to be (a) normalised by dividing (in the fine vertical grid dimension)
    by the pressure differences between the fine grid (dpf)
    (b) interpolated in that dimension to the new model pressure grid.
    (c) multiplied by the layer pressure differences of the model grid.
    Pressure differences,dp can be obtained by
            dp1=pf(1:nz-1)-pf(0:nz-2)
            dpf=([0,dp1]+[dp1,0])/2

    PARAMETERS
             FILE   Name of IMS L2 file to read

    KEYWORDS
            APPROX  Compute sub-columns approximately
                    (mainly to illustrate basic approach, but
                    treats the bounds of the defined pressure layers
                    in an approximate way)


    R.S. 30/10/2024 (original IDL module)

"""


import sys
from pathlib import Path

import numpy as np
import cf  # only using for now to read in to get arrays


# START OF NEW FUNCS TO MAP IDL PROCEDURE NAMES TO EQUIVALENT PYTHON
# FUNCTIONALITY USING E.G. CF-PYTHON
# Start with the easiest to convert, e.g. to do the same via Python/cf-python


# Adapt appropriately to own path to dataset
DEFAULT_FILEPATH = (
    f"{Path(__file__).absolute().parent.parent.parent}/data/"
    "marias-satellite-example-data/satellite-data/"
    "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_"
    "20170703215054z_000_049-v1000.nc"  # all 6000 retrievals
    # "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_"
    # "20170703215054z_700_749-v1000.nc"  # only 5040 retreivals in this one
    # From orig IDL, used: "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-"
    # "20110718141155z_20110718155058z_000_049-v1000.nc"
)
APPROX_INTEGRATION_MATRIX = True
RET_CUTOFF_DEBUG = 20  # retrievals after which to stop, for dev purposes


def matrix_multiply(a, b, atr=False, btr=False):
    """Implement IDL 'matrix_multiply' function in Python.

    Note:
    https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator
    """
    if atr:
        a = a.transpose()

    if btr:
        b = b.transpose()

    return np.dot(a, b)


def ncdf_get(fi, varname, lun=False, noclo=False, undo=False, ova=False):
    """Implement IDL code 'ncdf_get' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    ; Get one variable from an NCDF file
    ;
    ; PARAMETERS
    ;	FI	Filename
    ;	VARNAME	Variable name (string)
    ;
    ; KEYWORDS
    ;	LUN	Set/return NCDF FILE ID
    ;	NOCLOSE Don't close file
    ;	A2	Return Attribute information in different (more complete) way
    ;	NOGET	Don't actually get values, just other stuff
    ;	TUC	If variable not found, try upper case version of variable name
    ;	UNDO	Undo scaling using scale_factor and add_offset if present
    ;	OVAL	Only return the values instead of structure with attributes etc
    ;	MISS	Set to value to be returned if VARNAME does not exist
    ;	CFLOAT	Convert value to float type
    ;	MV	Set values assigned to MISSING_VALUE or_FILLVALUE to MV (after scale/off applied)
    ;	OFFSET	As in ncdf_varget
    ;	COUNT	As in ncdf_varget
    ;	STRIDE	As in ncdf_varget
    ;       OC      Define structure which will lead to applying offset,count,stride to
    ;               specific dimensions (set to array of structures to apply these in multiple
    ;               dimensions). Structure should defined
    ;               idim: dimension index to be subset
    ;               count: number of contiguous samples to read
    ;               offset: first sample to read (starting at 0)
    ;               stride: sample interval
    ;	DIMS	Pass in result of ncdf_get_dims (needed when OC set in case dims need to
    ;		be inherited from a higher level group)
    ;	FMVAL	If not data is in variable, which would normally lead to
    ;		no value tag in the returned struct, add a value array of correct size, type
    ;		filled with missing value
    ;	NXD	Do not assume "." in variable name means a tag within a group (assume
    ;		variable name really has a "." in it)
    ;	QUIET	Suppress warning messages (e.g. cannot read due to unknown data type)
    ;       UNH5    Use h5_get to read a variable which has unknown data type for ncdf reader
    ;

    Ignoring IDL code implementation as this is trivial in cf-python so
    no need to copy/check their approach.
    """
    # Note: noclo arg to not close file irrelevant in cf-python
    # Undo and ova args also probably not relevant but check this later.
    fl = cf.read(
        fi, aggregate=False
    )  # DH advice: agg=False for speed and improv.
    v = fl.select_by_ncvar(varname)
    print("Returning fieldlist of:", len(v), v)

    # Unpacking stage, if a FieldList of length 1:
    if len(v) != 1:
        raise ValueError("Unexpected: have a FieldList of non-singular size.")
    else:
        v = v[0]

    # Return the data not the field! For the algorithm conversion, work in
    # numpy array space until we get it working, then can conert to cf-python
    # space.
    d = v.data
    d.persist(inplace=True)  # for performance
    return d


def setup_linear(
    x0,
    x1,
    i1=None,
    i2=None,
    w1=None,
    w2=None,
    wc=None,
    wd=None,
    zero=False,
    extra=False,
    nn=False,
    op=False,
    dwdx=False,
    vl=False,
    spline=False,
    dcdx=False,
    dddx=False,
):
    """Implement IDL code 'setup_linear' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows (SLB especially note the bit
        'VL ... ASSUMES X0 IS MONOTONICALLY ASCENDING'):

    ; This sets up parameters to allow rapid linear interpolation of a number of
    ; of functions y_n(x0) to a new grid, x1, assuming that the x0 and x1 are
    ; constant and only the values of y are changing.
    ;
    ; Interpolation can then be performed for all y_n:
    ;	y_n(x1) = w1.y_n(i1) + w2.y_n(i2)
    ;
    ; or for an array...
    ;
    ; 	di = f_matvec(d(i1,*),w1) + f_matvec(d(i2,*),w2)
    ;
    ; or 	di = f_matcol(d(*,i1),w1) + f_matcol(d(*,i2),w2)
    ; depending on order of d
    ;
    ; PARAMETERS
    ;	X0	Original grid
    ;	X1	New grid
    ;	I1	First index to Y
    ;	I2	Second index to Y
    ;	W1	Weight associated with I1
    ;	W2	Weight associated with I2
    ;	WC	See spline below
    ;	WD	See spline below
    ;
    ;
    ; KEYWORDS
    ;	ZERO	Set to zero extrapolations
    ;	EXTRA	Set to perform extrapolations
    ;	NN 	Set up to do nearest neighbour (still apply ZERO keyword)
    ;	OP	If n_elements(x1) eq 1, then return scaler not vector
    ;		results from I1,I2,W1,W2
    ;	DWDX	Return derivative of W2 wrt x (1- deriv W1 wrt X)
    ;	VL	Set to use IDL's value_locate function instead of get_nns
    ;		(may be faster). ASSUMES X0 IS MONOTONICALLY ASCENDING
    ;	SPLINE	Set to also compute weights to be applied to 2nd derivatives to
    ;		optain a cubic spline interpolation (see num recip in c s3.3).
    ;		In this case, arguments WC and WD will be defined,
    ;		giving coefs C and D in eqn 3.3.3. DCDX and DDDX are also returned, containing
    ;		the derivatives of WC and WD wrt X. Note
    ;		that  = w1*y(i1)+w2*y(i2)+wc*d2ydx2(i1)+wd*d2ydx2(i2)
    ;		where yi is spline interpolated value, and d2ydx2 are
    ;		the 2nd derivatives of y, obtained using SPL_INIT.
    ;	DCDX	Return derivative of spline parameter
    ;	DDDX	Return derivative of spline parameter

    """
    n1 = len(x1)  # list so len() is appropriately
    if spline:
        if extra.size == 0:
            extra = 1

    if x0.size == 0:
        raise ValueError("X0 undefined")
    if x0.size == 1:
        # Deal with case of only 1 element in input array
        if zero:
            raise ValueError(
                "ZERO extrapolation with only 1 data value not implemented !"
            )
        else:
            i1 = np.zeros(n1, dtype=int)
            i2 = np.zeros(n1, dtype=int)
            w2 = np.zeros(n1)
            w1 = w2 + 1
            dwdx = np.zeros(n1)
            if len(x1) == 1 and op:
                i1 = i1[0]
                i2 = i2[0]
                w1 = w1[0]
                w2 = w2[0]
                dwdx = dwdx[0]
            return

    if vl:
        n0 = x0.size
        # SLB ChatGPT's suggestion of Python equivalent to IDL value_locate,
        # I remain dubious but will check this at run-through time
        # NOTE PYTHON CONV to go from IDL value_locate to np.searchsorted,
        # based on the example in the IDL ref guide, we need to take one away
        # for every element:
        # >>> np.searchsorted([2, 5, 8, 10], [0, 3, 5, 6, 12])
        # array([0, 1, 1, 2, 4])
        # whereas the ref guide has result:
        # -1 0 1 1 3
        # so take away one.
        print("x0", x0, x0.shape, "x1", x1, len(x1), type(x1))
        #if isinstance(x0, cf.Data):
        #    print("CONVERT CF DATA TO NP ARRAY")
        #    x0 = x0.array
        ilow = np.searchsorted(x0, x1) - 1  # IDL: value_locate(x0, x1)
        ihigh = ilow + 1
        wh = np.where(ilow < 0)[0]
        nw = wh.size
        if nw > 0:
            ilow[wh] = 0

        wh = np.where(ihigh >= n0)[0]
        nw = wh.size
        if nw > 0:
            ihigh[wh] = n0 - 1
    else:
        nns = get_nns(x1, x0, ilow, ihigh, glh=True)

    sz = [x1.ndim,] + list(x1.shape)[::-1]
    # if sz(sz[0] + 1) == 5:
    w2 = np.zeros(n1)
    # else:
    #    w2 = np.zeros(n1)

    dwdx = w2
    if extra:
        n0 = x0.size
        whoor = np.where(ihigh == ilow)[0]
        noor = whoor.size
        if noor > 0:
            wh0 = np.where(ihigh(whoor) == 0)[0]
            if wh0[0] != -1:
                ihigh[whoor[wh0]] = 1

            wh0 = np.where(ihigh(whoor) == n0 - 1)[0]
            if wh0[0] != -1:
                ilow[whoor[wh0]] = n0 - 2

    i1 = ilow
    i2 = ihigh
    wh = np.where(ihigh != ilow)[0]
    nne = wh.size
    if nne != 0:
        ###print("ilow is", ilow, type(ilow), ilow[wh], ilow[wh] - 1)
        py_ilow = ilow[wh] - 1  # SLB NEW VARS
        py_ihigh = ihigh[wh] - 1
        dwdx[wh] = 1.0 / (x0[py_ihigh] - x0[py_ilow])
        w2[wh] = (x1[wh] - x0[py_ilow]) / (x0[py_ihigh] - x0[py_ilow])
    if nn:
        w2 = int(w2 + 0.5)
        # if sz(sz[0] + 1) == 5:
        #    w2 = double(w2)
        # else:
        w2 = float(w2)

    w1 = 1.0 - w2
    if zero:
        xmax = max(x0, min=xmin)
        wh = np.where(x1 > xmax or x1 < xmin)[0]
        if wh[0] != -1:
            w1[wh] = 0.0
            w2[wh] = 0.0
            dwdx[wh] = 0.0

    if x1.size == 1 and op:
        i1 = i1[0]
        i2 = i2[0]
        w1 = w1[0]
        w2 = w2[0]
        dwdx = dwdx[0]

    if spline:
        # Compute coefs of spline interpolation and derivatives wrt x
        if min(abs(dwdx)) == 0:
            raise ValueError("Issue! See code. Original IDL aborted ('stop').")

        dx2 = dwdx * dwdx * 6
        w12 = w1 * w1
        w22 = w2 * w2
        wc = (w12 * w1 - w1) / dx2
        dcdx = -dwdx * (3 * w12 - 1) / dx2
        wd = (w22 * w2 - w2) / dx2
        dddx = dwdx * (3 * w22 - 1) / dx2

        if noor > 0:
            # Do not apply spline out of range - do linear extrapolation
            wc[whoor] = 0
            wd[whoor] = 0
            dcdx[whoor] = 0
            dddx[whoor] = 0

    # x, xi, i0, i1, w0, w1
    return i1, i2, w1, w2


def sqrt_nz(a):
    """Implement IDL code 'sqrt_nz' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    ; Take sqrt of an array, checking for invalid values and setting
    ; the result of these to a no-data value
    ;
    ; PARAMETERS
    ;	A
    ;
    ; KEYWORDS
    ;	NO_DATA	Set no-data value
    ;	NND	Return number of points set to no-data
    ;

    """
    sqa = np.sqrt(a)
    sqa_mask = np.ma.masked_invalid(sqa)  # SLB update np and cf world mix
    print("Outcome of sqrt_nz, from:", a, "to:", sqa_mask)
    return sqa_mask


# added internal undefined vars to arguments: nw, i0, i1, w0, w1
def setup_integration_matrix(
        x1, orig_xrange=None, extra=False, tol=None, box=None, nw=None,
        i0=None, i1=None, w0=None, w1=None,
):
    """Implement IDL code 'setup_integration_matrix' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

        (SLB note renamed 'xrange' argument to avoid clash with Python built-in
        keyword name which would cause issue)

    ; SETUP_INTEGRATION_MATRIX
    ;
    ; Returns a vector which when matrix multiplied by an array of data values
    ; will give the integration of those values over the specified range
    ;
    ;      m=setup_integration_matrix(x)
    ;      result=matrix_multiply(y,m,/atr)
    ;
    ; RETURN Matrix to perform integration
    ;
    ; REFS sec:subcols
    ;
    ; PARAMETERS
    ;	X1	X-coords on which points specified
    ;		(can be in any order)
    ;
    ; KEYWORDS
    ;	XRANGE	Set to X-range over which to interpolate data
    ;		Returned matrix will then effectively linearly interpolate the data
    ;		to the given values of the range (which therefore do not need
    ;		to correspond to one of the given values of X)
    ;	_EXTRA	Sent to SETUP_LINEAR to control effective interpolation to
    ;		the defined RANGE values - e.g. by default extrapolation is not
    ;		performed but can be set by using /EXT
    ;	TOL	Set to return matrix to integrate from first level
    ;		down to each one of every other level
    ;	BOX	Setup matrix to do box-car integration assuming X1 define
    ;		layer boundaries and the matrix is to be applied to mean values
    ;		of each layer (i.e. given N values of X, this will return N-1 weights
    ;		for the N-1 layers defined by N levels).
    ;

    """
    # Sort into ascending order so this can be assumed throughout
    # SLB TODO - under VISION assumptions this is not required, because we
    # assume already monotonically increasing.
    so = np.argsort(x1)
    print("so", so)
    x = x1[so]

    if orig_xrange is not None:
        # Get matrix to perform interpolation...
        # TODO SLB was originally an 'and' here but that might be
        # problematic, DH advice to convert to ampersand which works
        # - see cf-python codebase examples.
        wh = np.where(
            np.logical_and(x > orig_xrange[0], x < orig_xrange[1])
        )[0]
        nw = wh.size
        if nw > 0:
            print("ISSUE", x[wh])
            xi = np.array([orig_xrange[0], x[wh].array[0], orig_xrange[1]])
            print("xi", xi)
        else:
            xi = orig_xrange

        # x is in ascending order so can use value locate to do this
        # as fast as possible
        i0, i1, w0, w1 = setup_linear(x, xi, vl=True, extra=extra)
        nx = x.size
        nxi = xi.size
        mi = np.zeros((nx, nxi))
        ###print("POINT 1", mi.shape, [i0, np.arange(nxi)], "i0", i0)
        ###print("THIS IS", np.concatenate((i0, np.arange(nxi))))
        mi[np.concatenate((i0, np.arange(nxi)))] = w0
        ###print("j:", )
        mi[np.concatenate((i1, np.arange(nxi)))] = mi[
            np.concatenate((i1, np.arange(nxi)))] + w1

        # Now get vector which would perform the integration
        # on interpolated array
        mii = setup_integration_matrix(xi, box=box)

        # Now combine the two operations into one vector
        # "The REFORM function changes the dimensions of an array without
        # changing the total number of elements."
        # "Return Value
        # If no dimensions are specified, REFORM returns a copy of
        # Array with all dimensions
        # of size 1 removed." therefore is a squeeze operation here
        m = np.squeeze(matrix_multiply(mii, mi, btr=True))
    else:
        ###print("x", x.shape, x[:1].shape)
        # Note that dx was in IDL array form [<this>] so wrap with np.array
        dx = np.array(x[1:][0] - x)  # IDL: [x(1: *) - x], [0] to unpack from shape (1,)
        if box:
            # need to sort based on 1 value per layer not level,
            # in order for sorting back to work below
            so = np.argsort(x1[1:])  # IDL: np.argsort(x1(1: *))
            if tol:
                nz = x.size
                m = np.zeros((nz - 1, nz - 1))
                for iz in np.arange(1, nz):
                    m[iz - 1, 0] = dx[0: iz - 1]
            else:
                m = dx
        else:
            if tol:
                nz = x.size
                m = np.zeros((nz, nz - 1))
                for iz in np.arange(1, nz):
                    m[iz - 1, 0] = 0.5 * (
                        [0.0, dx[0: iz - 1]] + [dx[0: iz - 1], 0.0]
                    )
            else:
                ###print("dx:", dx)
                m = 0.5 * (
                    np.concatenate((np.array([0.0]), dx)) +
                    np.concatenate((dx, np.array([0.0])))
                )
                ###print("FINAL m:", m)

    # Sort m back to original order
    bk = np.argsort(so)
    print("m:", m.shape, "bk:", bk.shape)  #, "m[:, bk]:", m[:, bk].shape)
    m = m[bk]  # IDL: m(bk, *)
    ###print("FINAL m:", m)

    return m


def iasimhs_vsx2cov(vsx, diag):
    """Implement IDL code 'iasimhs_vsx2cov' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    ;	Description
    ;       Reconstructs covariance matrix from vector of unwrapped half off-diagonals and diagonals
    ;
    ;	Use
    ;
    ;	Parameters
    ;	VSX	Matrices in compact form
    ;
    ;	Keywords
    ;	DIAG	Specify diagonals in case VSX defines only off-diagonals of correlation
    ;
    function iasimhs_vsx2cov, vsx,diag=diag
    ;
    ; Reconstruct covariance matrix from vector representing one half of covariance matrix unwrapped
    ;
    """
    print("vsx", vsx, type(vsx), vsx.shape)
    ###vsx = vsx.array
    print("diag", diag, type(diag), diag.shape)
    # Reconstruct covariance matrix from vector representing one half of
    # covariance matrix unwrapped
    sz = [vsx.ndim,] + list(vsx.shape)[::-1]
    print("vsx", vsx, vsx.shape)
    if sz[0] == 1:
        npi = 1
    else:
        npi = sz[2]

    nv = sz[1]
    if diag.size > 0:
        szd = [diag.ndim,] + list(diag.shape)[::-1]
        nd = szd[1]
        if szd[0] == 1:
            npid = 1
        else:
            npid = sz[2]
        print("npi", npi, "npid", npid)
        if npi != npid:
            raise ValueError("DIAG,VSX: not match!")

        nv = nv + nd
        covd = diag[0,] * 0 + 1  # array of 1s for diagonal of correlation
        correl = 1
    else:
        correl = 0

    # Find expected dimensions of covariance based on unwrapped
    # vector of half of the off-diagonals and the diagonals
    n = np.polynomial.polynomial.polyroots([2 * nv, -1, -1])
    # NOTE: 'roots' accounts for complex roots, so gives FOR EXAMPLE:
    # https://www.nv5geospatialsoftware.com/docs/FZ_ROOTS.html
    # says IDL gives:
    # IDL: ( -0.500000, 0.00000)( -0.333333, 0.00000)( 2.00000, 0.00000)
    # >>> import numpy as np
    # >>> coeffs = [-2.0, -9.0, -7.0, 6.0]
    # >>> roots = np.roots(coeffs)
    # >>> roots
    # array([-3. , -2. ,  0.5])
    # AH! arguments need to be reversed for equivalent output:
    # >>> np.roots([6, -7, -9, -2])
    # array([ 2.        , -0.5       , -0.33333333])
    # np.polynomial.polynomial.polyroots([6, -7, -9, -2])
    #array([-3. , -2. ,  0.5])
    # WHY IS THE IDL VERSION IS A WEIRD ORDER?
    # AH, this works: np.polynomial.polynomial.polyroots(<same order>)
    # So note, do *not* try older np.roots. Unreliable.
    print("N IS", n, n[0])
    n = int(n[1] + 0.1)  # IDL: long(n(1) + 0.1)
    sx = np.zeros((n, n, npi))
    print("sx", sx.shape)
    for ipi in range(npi):  # Do for more than one pixel
        j = 0
        vsx1 = vsx[ipi,]
        if correl:
            ### print("HERE", vsx1.shape, covd.shape)
            # Orig:
            print("VSX1 IS", vsx1.shape)
            print("COVD IS", covd.shape)
            #vsx1 = vsx1.squeeze()
            #covd = covd.squeeze()  # needed?
            # Applied implicit concat in IDL
            # https://www.nv5geospatialsoftware.com/docs/Creating_Arrays.html
            vsx1 = np.concatenate((covd, vsx1), axis=1)
            vsx1 = vsx1.squeeze()
            ###print("VSX1:", vsx1.shape)
            diag1 = diag[ipi,]
            diag2 = matrix_multiply(diag1, diag1, btr=True)
            ###print("Diags", diag1.shape, diag2.shape)

        print("N IS", n)
        for i in range(n):
            if i == 0:  # diagonals
                # IDL:  vsx1[j: j + n - i - 1] has but inclusive endpoints
                # therefore +1 -> - 1 + 1 = 0
                sx1 = np.diag(vsx1[j: j + n - i])
            else:
                # IDL:  vsx1[j: j + n - i - 1] has but inclusive endpoints
                # therefore +1 -> - 1 + 1 = 0
                print("expr attempt", np.diag(vsx1[j: j + n - i], i))
                sx1 = (
                    sx1
                    + np.diag(vsx1[j: j + n - i], i)
                    + np.diag(vsx1[j: j + n - i], -i)
                )  # off-diagonals
            j = j + n - i
            print("J IS", j)  ###, "sx1 is", sx1)

        if correl:
            sx1 = sx1 * diag2

        print("sx1", sx1.shape)  #, sx[ipi, 0, 0].shape)
        sx[: , :, ipi] = sx1  #sx[ipi, 0, 0] = sx1

    print("FINAL SX IS", sx, sx.shape)
    return sx


def iasimhs_sx_exp(s1, evecs, log=False, x=False):
    """Implement IDL code 'iasimhs_sx_exp' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    function iasimhs_sx_exp, s1, evecs, log=log, x=x
    ;
    ; loop over multiple covariances, reconstructing each
    ;

    """
    # Transpose input and output, 1. input
    sz = [s1.ndim,] + list(s1.shape)[::-1]
    print("SZ IS", sz)
    if sz[0] == 3:
        # NOTE: renaming 'np' var used here to avoid nameclash with numpy
        # alias, calling it orig_np now
        orig_np = sz[3]
    else:
        orig_np = 1

    print("sz", sz)
    if sz[-1] != sz[-2]:  # IDL: if sz[1] != sz[2], but Py dims reverse order
        raise ValueError(
            "Expected last (in Python - in IDL first) 2 dims to be same size!")

    sz = [evecs.ndim,] + list(evecs.shape)[::-1]
    print("evecs:", evecs)
    nz = sz[1]
    s = np.zeros((nz, nz, orig_np), dtype=np.float32)
    print("s shape:", s.shape, "orig_np int:", orig_np)
    for ip in range(orig_np):
        print("ip is:", ip)
        sipi = s1[:, :, ip]
        pre_sipi = matrix_multiply(evecs, sipi, atr=True, btr=True)
        sipi = matrix_multiply(pre_sipi, evecs)  # map to rttov levels
        if log:
            xipi = x[ip,]
            sipi = sipi * matrix_multiply(xipi, xipi, btr=True)  # Multiply out log unit

        print("Attempt", sipi.shape)
        # NOTE: relative to raw IDL, apply T to transpose whole result
        # so have shape (10, 45)
        # to fit s shape (10, 10, 45), not shape (45, 10)
        ###print("shape sipi", sipi.shape, "shape other", s[ip, :, :].shape)
        s[:, :, ip] = sipi

    return s


def f_diagonal(matrix, orig_input=False):
    """Implement IDL code 'f_diagonal' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    (SLB note renamed 'input' arg to avoid clash with Python
    built-in keyword names which would cause issue)

     ; Reads/writes diagonal of a matrix
    ;
    ; Arguments
    ;
    ;  I  matrix   matrix whose diagonal is to be read/written
    ;  I  \\input   input vector or single item  if diagonal to be written
    ;
    ;  Either one or both arguments may be passed.
    ;  If only an input vector is passed a matrix is created.
    ;

    """
    # dimensions
    nel = matrix.size
    if nel == 1:
        matrix_save = matrix
        # https://lweb.cfa.harvard.edu/~atripath/idlrefguide.pdf
        # "The REPLICATE function returns an array with the given dimensions, filled with the
        # scalar value specified as the first parameter"
        matrix = np.full((2, 2), matrix[0])  # IDL: replicate(matrix(0), 2, 2)

    # SLB: flake8 says this variable is not used, so comment out
    # dim_in = orig_input.shape
    # SLB use this to handle lack of orig_input variable
    if orig_input:
        nin = orig_input.size
    else:
        nin = 0
    dim_mat = [matrix.ndim,] + list(matrix.shape)[::-1]
    nmat = matrix.size

    if nin == 0:
        # SLB: think type is handled natively by Python so can drop 'type='
        # which uses a type code mapped to a type
        result = np.zeros(dim_mat[1])
        for i in range(dim_mat[1]):
            result[i] = matrix[i, i]
    elif nin == 1:
        result = matrix
        for i in range(dim_mat[1]):
            result[i, i] = orig_input
    else:
        if nmat != 0:
            result = matrix
        if nmat == 0:
            result = np.zeros((nin, nin))

        for i in range(nin):
            result[i, i] = orig_input[i]

    if nel == 1:
        result = result[0]
        matrix = matrix_save

    f_diagonal = result

    return f_diagonal


# END OF IDL CONVERSION
# START OF ORIGINAL IDL CODE CONVERTED, INCLUDING USE OF ABOVE NEW FUNCS


# TODO SLB: latitude is probably not relevant so we can ignore this!
# added internal undefined vars to arguments: i0, i1, w0, w1
def irc_interp_ap(xap, latitude):
    """Interpolate prior in 18 latitude bands to latitude of measurement

    Inputs
          xap    prior values
          latitude Latitudes
          SP      Surface pressure (only needed if e60 set)
    """
    # Latitude grid associated with the prior values
    lats_ap = np.arange(18.0) * 10 - 85  # IDL: dindgen(18) * 10 - 85d0
    print("lats_ap", lats_ap, lats_ap.shape)
    i0, i1, w0, w1 = setup_linear(lats_ap, latitude, vl=True)
    print(
        "i0", i0, len(i0), "i1", i1, len(i1), "w0", w0, len(w0),
        "w1", w1, len(w1)
    )

    # SLB: care, original IDL code has 'np' as variable, must use another to
    # avoid nameclash with numpy alias!
    orig_np = latitude.size
    print("orig_np", orig_np, latitude.shape)
    print("xap", xap.shape)
    nz = xap[0,].size  # IDL: xap(*,0)
    print("nz", nz)
    xapi = np.zeros((nz, orig_np))  # IDL: dblarr(nz, np)
    print("xapi", xapi, xapi.shape)

    for ip in range(0, orig_np):
        try:
            xapi[:, ip] = xap[i0[ip],] * w0[ip] + xap[i1[ip],] * w1[ip]
        except:
            xapi[:, ip] = cf.masked

    return xapi


# added internal undefined vars to arguments: ns, w0, i0, i1, w1
def irc_ak_exp(
        ak, evecs, pf, sp, nz, nev,
        ns=False, w0=False, i0=False, i1=False, w1=False
    ):
    """Recreate full averaging kernel from IASI-MHS state vector representation

    Inputs
        AK      Ak for state vector representation, wrt 51 "true levels" (every other RTTOV level)
        EVECS   Vectors to map to 101 RTTOV levels from state vector
        PF      Fine grid pressures / hPa
        SP      Surface pressure / hPa
        NZ      Number of fine vertical levels
        NEV     Number of eigenvectors
    """
    ak = ak.squeeze()

    # Index of PF used to store true grid perturbations in file
    # Python conv: need to take one away because from nz hence (nz - 1)
    # due to idx being prepared as indices and IDL indexing being
    # inclusive, so we need one less value.
    idx = np.arange((nz - 1) / 2 + 1) * 2  # IDL: lindgen(nz / 2 + 1) * 2
    print("IS", pf, pf.shape, idx, idx.shape)

    pfs = pf[idx]
    print("Xs are:", pfs, pfs.shape, pf, pf.shape)
    i0, i1, w0, w1 = setup_linear(pfs, pf, vl=True)
    print("ak", ak, type(ak))
    akt = ak.transpose()
    ak_101 = np.zeros((nev, nz))  # IDL: dblarr(nz, nev) Python reverse order

    for iev in range(nev):  # Interpolate to full grid
        # IDL: ak_101(0, iev) = akt(i0, iev) * w0 + akt(i1, iev) * w1
        # print(
        #     "ak_101", ak_101.shape,
        #     "akt", akt.shape,
        #     "akt[iev, i0]", akt[iev, i0].shape
        # )
        ak_101[iev, :] = akt[iev, i0] * w0 + akt[iev, i1] * w1

    ###print("evecs", evecs.shape, "ak_101", ak_101.shape)
    # NOTE THESE ARGS, opposite to IDL but tranpose necessitates, give
    # (101, 101) required shape
    ak_101 = matrix_multiply(evecs, ak_101, atr=True)

    # Make sure AK is zero below surface pressure
    ws = np.where(pf > sp)[0]
    ns = ws.size
    if ns > 0:  # Set levels below surface to 0
        ak_101[ws,] = 0

    print("FINAL ak_101", ak_101.shape, ak_101)
    return ak_101


# added internal undefined vars to arguments: n0, w0
def irc_integration_matrix(
        scs, pf, sp, nz, nsc, n0=False, w0=False, approx=False):
    """(No docstring in corresponding IDL procedure).
    """
    ###print("nz:", nz, "nsc:", nsc)
    msc = np.zeros((nz, nsc))  # IDL: dblarr(nz, nsc)

    if approx:
        # Approximate method uses the just the fine layer pressure differences between
        # the defined bounds as weights.
        # Full method treats the layer bounds more exactly, by also including interpolation
        # from the fine grid to the defined pressure bounds (and surface pressure).
        # IDL: =pf(1:nz-1)-pf(0:nz-2) - convert for Python exclusiveness by + 1
        dp1 = pf[1: nz] - pf[0: nz - 1]
        ###print("dp1", dp1.shape)
        # Use explicit concat form for Python/numpy from IDL implicit concat
        dpf = (np.concatenate((np.array([0.0]), dp1)) +
               np.concatenate((dp1, np.array([0.0])))) / 2
        ###print("dpf", dpf.shape, dpf)
        ###dpf = ([0.0, dp1] + [dp1, 0]) / 2

    for isc in range(nsc):
        # Pressure levels of this layer in ascending order
        ###print("isc:", isc)
        # NEEDS SCS IN
        sc1 = scs[[1, 0], isc - 1]  # scs[[1, 0], isc], minus one since inclusive
        ###print("sc1", sc1)
        # if lower bound indicated as 1000 or lower bound below surface then truncate layer to the surface
        if sc1[1] == 1000 or sc1[1] > sp:
            sc1[1] = sp
        if approx:
            msc1 = dpf
            ###print("HERE", pf < sc1[0], "AND", pf > sc1[1])
            w0 = np.where(np.logical_or(pf < sc1[0], pf > sc1[1])
            )[0]  # levels outside required layer
            ###print("w0", w0)
            n0 = w0.size
            ###print("n0", n0)
            if n0 > 0:
                ###print("msc1", msc1.shape, msc1)
                msc1[w0] = 0
        else:
            # used function to set up weights to do trapezoid integration over defined interval
            msc1 = setup_integration_matrix(pf, orig_xrange=sc1)
            ###print("%%%%% FINAL MSC1", msc1, msc1.shape)

        msc1 = msc1 / np.sum(
            msc1
        )  # this normalises result to sub-column average
        ###print("msc1", msc1.shape, "msc", msc.shape, "msc[0, isc]", msc[0, isc])
        msc[:, isc] = msc1

    print("IRC_INTEGRATION_MATRIX final shape:", msc.shape)
    return msc


# added internal undefined vars to arguments: lun, nret
def main(fi=None, lun=None, nret=None, approx=False):
    """
    Main function.

    Note this is named 'ims_rd_co4ak' in the original IDL algorithm.
    """
    # Default filename if one not defined
    # (this one co-located with FAAM over Canadian fire)
    if not fi:
        fi = DEFAULT_FILEPATH

    # Define subcolumns as pressure bounds in hpa of 3 layers
    # (total, 0-6km, 6-12km column amounts)
    # 1000hPa is treated as surface pressure (see irc_subcol)
    scs = np.array(
        [
            [1000.0, 0.01],  # i.e. total column
            [1000.0, 450.0],  # i.e. surface-6km (approx)
            [450.0, 170.0],
        ]
    )  # i.e. 6-12km (approx)
    print("scs:", scs, np.isfortran(scs))

    # Read necessary info from the file
    # ncdf_get will apply scale_factor and add offset (/undo keyword)
    # /ova makes it just return the values without any attributes
    pf = ncdf_get(fi, "p", lun=lun, noclo=True, undo=True, ova=True)
    print("Example netcdf variable got, pf:", pf)

    lat = ncdf_get(fi, "latitude", lun=lun, noclo=True, undo=True, ova=True)
    lon = ncdf_get(fi, "longitude", lun=lun, noclo=True, undo=True, ova=True)
    sensingtime_msec = ncdf_get(
        fi, "sensingtime_msec", lun=lun, noclo=True, ova=True
    )
    sensingtime_day = ncdf_get(
        fi, "sensingtime_day", lun=lun, noclo=True, ova=True
    )
    c_ap_lnvmr = ncdf_get(fi, "c_ap", lun=lun, noclo=True, undo=True, ova=True)
    evecs = ncdf_get(fi, "evecs_c", lun=lun, noclo=True, undo=True, ova=True)
    c_lnvmr = ncdf_get(fi, "c", lun=lun, noclo=True, undo=True, ova=True)
    sp = ncdf_get(fi, "sp", lun=lun, noclo=True, undo=True, ova=True)
    ak_lnvmr = ncdf_get(fi, "ak_c", lun=lun, noclo=True, undo=True, ova=True)
    dsx_ev = ncdf_get(fi, "dsx_c", lun=lun, noclo=True, undo=True, ova=True)
    csx_ev = ncdf_get(fi, "csx_c", lun=lun, noclo=True, undo=True, ova=True)
    do_ret = ncdf_get(fi, "do_retrieval", lun=lun, noclo=True)
    print("do_ret:", do_ret, np.isfortran(do_ret.array))
    print("pf:", pf.shape)  # (101,)
    dsn_ev = ncdf_get(fi, "dsxn_c", lun=lun, noclo=True, undo=True, ova=True)
    csn_ev = ncdf_get(fi, "csxn_c", lun=lun, undo=True, ova=True)

    # For dev purposes, only consider a subset of all retrievals
    do_ret = do_ret[:RET_CUTOFF_DEBUG]

    # Advice from RS:
    # nret is defined by the line iret=where(do_ret,nret)
    # In that do_ret is the variable do_retrieval from the L2 file which is an array of values 0,1 for each scene, where 1 indicates a retrieval was done.
    # (In most cases all values will be 1)
    # The IDL where function (see https://www.nv5geospatialsoftware.com/docs/WHERE.html)
    # returns (in iret) the indices of the elements of do_ret which are not zero (i.e. the scenes in the L2 files for which a retrieval is carried out)
    # It also returns nret which is the number of elements in iret (i.e. the number of retrievals).
    # Keep in numpy space (not cf/field space) since indices on
    # data is not a field-like operation
    # Numpy argwhere "Find the indices of array elements that are
    # non-zero, grouped by element" so works out the box here
    iret = np.argwhere(do_ret).flatten()  # flatten so not (1, 6000) shape
    nret = iret.size
    print("iret:", iret)
    print("nret:", nret)
    ###exit()

    if nret == 0:
        raise ValueError("No retrievals in file!")

    # Convert time to julian day
    # TODO SLB check with DH operation order intended here - for IDL
    # Orig. IDL: sensingtime_day+sensingtime_msec/1000d0/60d0/60d0/24d0+2451544.5d0
    print("sensingtime_day", sensingtime_day)
    print("sensingtime_msec", sensingtime_msec)
    # Processing as in satellite_compliance_converter!
    jday = (
        sensingtime_day
        + sensingtime_msec / (1000.0 * 60.0 * 60.0 * 24.0)  # msec - millisec
        + 2451544.5
    )
    print("jday", jday)

    # Subset lat/lon/time/sp to the pixels for which retrieval exist
    lat = lat[iret]
    lon = lon[iret]
    jday = jday[iret]
    sp = sp[iret]
    print("Example, lat:", lat)

    # Get dimensions
    nz = pf.size  # number of fine vertical levels
    nsc = scs[:, 0].size  # number of subcolumns
    print("nz:", nz)
    print("nsc:", nsc)

    # SLB: flake8 says this variable is not used, so comment out
    nev = evecs[:, 0].size  # number of Eigenvectors used to represent profile
    print("nev:", nev)

    print(
        "REPORT FOR S VARIABLES:",
        pf.shape, lat.shape, lon.shape, jday.shape, sp.shape
    )
    # Interpolate the set of prior profiles in latitude
    try:  # pre-calculated
        c_ap_lnvmr = np.load('c_ap_lnvmr.npy')
    except:  #if True:  #except:
        c_ap_lnvmr = irc_interp_ap(c_ap_lnvmr, lat)
        np.save('c_ap_lnvmr.npy', c_ap_lnvmr, allow_pickle=True)
    print("AFTER Found c_ap_lnvmr to be:", c_ap_lnvmr, c_ap_lnvmr.shape)
    # %%% shape: (101, 5040)

    # Expand the total and noise covariance matrices to full vertical grid (nz,nz) with units (ln(ppmv))^2
    try:  # pre-calculated
        sx_ev = np.load('sx_ev.npy')
    except:
        sx_ev = iasimhs_vsx2cov(csx_ev, diag=dsx_ev)  # nev,nev matrix
        np.save('sx_ev.npy', sx_ev, allow_pickle=True)
    print("Found sx_ev to be:", sx_ev, sx_ev.shape)
    # %%% shape: (10, 10, 5040)

    try:  # pre-calculated
        sx_lnvmr = np.load('sx_lnvmr.npy')
    except:
        sx_lnvmr = iasimhs_sx_exp(sx_ev, evecs)
        np.save('sx_lnvmr.npy', sx_lnvmr, allow_pickle=True)
    print("Found sx_lnvmr to be:", sx_lnvmr, sx_lnvmr.shape)
    # %%% shape: (101, 101, 10)

    try:  # pre-calculated
        sn_ev = np.load('sn_ev.npy')
    except:
        sn_ev = iasimhs_vsx2cov(csn_ev, diag=dsn_ev)  # nev,nev matrix
        np.save('sn_ev.npy', sn_ev, allow_pickle=True)
    print("Found sn_ev to be:", sn_ev, sn_ev.shape)
    # %%% shape: (10, 10, 5040)

    # UPTO
    try:  # pre-calculated
        sn_lnvmr = np.load('sn_lnvmr.npy')
    except:
        sn_lnvmr = iasimhs_sx_exp(sn_ev, evecs)
        np.save('sn_lnvmr.npy', sn_lnvmr, allow_pickle=True)
    print("Found sn_lnvmr to be:", sn_lnvmr, sn_lnvmr.shape)
    # %%% shape: ???

    # Make arrays to hold the results which are neeeded for model comparisons
    #
    # DESIRED SHAPES HAVE, FOR EXAMPLE:
    # nsc: 3
    # nz: 101
    # nret: 5040
    print("nsc", nsc, "nz", nz, "nret", nret)  # nsc 3 nz 101 nret 5040
    c_sc = np.zeros(
        (nsc, nret),  # (3, 5040)
    )  # IDL: dblarr(nsc, nret)  # CO sub-column average mixing ratios / ppmv
    ak_sc = np.zeros(
        (nsc, nz, nret), # (3, 101, 5040)
    )  # IDL: dblarr(nsc, nz, nret)  # Averaging kernels for retrieved sub-column wrt true profile vmr / ppmv/ppmv
    sx_sc = np.zeros(
        (nsc, nsc, nret),  # (3, 3, 5040)
    )  # IDL: dblarr(nsc, nsc, nret)  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs / ppmv^2
    sn_sc = np.zeros(
        (nsc, nsc, nret),  # (3, 3, 5040)
    )  # IDL: dblarr(nsc, nsc, nret)  # Noise covariance  / ppmv^2
    c_apc_sc = np.zeros(
        (nsc, nret),  # (3, 5040)
    )  # IDL: dblarr(nsc, nret)  # A priori contribution to each sub-column / ppmv
    c_err_sc = np.zeros(
        (nsc, nret),  # (3, 5040)
    )  # IDL: dblarr(nsc, nret)  # Estimated total standard deviation of retrieved sub-cols / ppmv
    c_noise_sc = np.zeros(
        (nsc, nret),  # (3, 5040)
    )  # IDL: dblarr(nsc, nret)  # Estimated noise standard deviation / ppmv

    # Loop individual retrievals
    print("STARTING ITERATION")
    # Rename iret to avoid confusion with iret variable above (no longer req'd)
    for orig_iret in np.arange(0, nret):
        ###orig_iret = np.arange(0, nret)
        print("+++++++++++++++++++++++ ONTO", orig_iret)
        # Get vmr from lnvmr
        print(orig_iret, "Before", c_lnvmr.shape, c_lnvmr[orig_iret,].shape)
        c_vmr = np.exp(c_lnvmr[orig_iret,])  # undo log unit
        ###print("OVERALL c_vmr:", c_vmr.shape, c_vmr)
        # %%% shape: (1, 101)
        ###c_vmr = c_vmr.squeeze()
        print("OVERALL c_vmr:", c_vmr.shape)  #, c_vmr)
        # %%% shape: (101,)

        # SLB FOR NOW USE SAME ARRAY IN EACH CASE
        # Calculate weights which will compute the subcolumn via matrix multiply
        try:  # pre-calculated
            try:
                msc = np.load('msc-isapprox.npy')
            except:
                msc = np.load('msc-isnotapprox.npy')
        except:  #if True:  #except:
            ###for orig_iret in np.arange(0, nret):
            msc = irc_integration_matrix(
                scs, pf, sp[orig_iret], nz, nsc,
                approx=APPROX_INTEGRATION_MATRIX
            )
            if APPROX_INTEGRATION_MATRIX:
                np.save('msc-isapprox.npy', msc, allow_pickle=True)
            else:
                np.save('msc-isnotapprox.npy', msc, allow_pickle=True)
            print("For intergration matrix, iteration number:", orig_iret)

        print("OVERALL msc:", msc.shape)  #, msc)
        # %%% shape: (101, 3)

        # Calculate the sub columns
        print("c_sc", c_sc.shape, )
        c_sc[:, orig_iret] = matrix_multiply(
            msc, c_vmr, atr=True, btr=True).squeeze()   ###.squeeze()
        print("OVERALL c_sc:", c_sc.shape)  #, c_sc)
        # %%% shape: (3, 5040)

        # Get corresponding prior profile and subcolumns
        c_ap_vmr = np.exp(c_ap_lnvmr[:, orig_iret])
        print("OVERALL c_ap_vmr:", c_ap_vmr.shape)
        # %%% shape: (101,)
        print(msc.shape)
        c_ap_sc = matrix_multiply(msc, c_ap_vmr, atr=True)
        print("OVERALL c_ap_sc:", c_ap_sc.shape)
        # %%% shape: (3,)

        # Make the square (nz,nz) AK array
        # IDL for first arg: ak_lnvmr(*,*,orig_iret)
        # IMPORTANT! fix relative to original code provided by RS, updated:
        # In doing this I found an error in ims_rd_co4ak - the modified
        # version is in also in that directory.
        # Wrong line was…
        # ak_vmr_sq=ak_lnvmr*matrix_multiply(c_vmr,1d0/c_vmr)
        # now corrected to
        # ak_vmr_sq=ak_lnvmr_sq*matrix_multiply(c_vmr,1d0/c_vmr)
        ak_lnvmr_sq = irc_ak_exp(
            ak_lnvmr[orig_iret, :, :], evecs, pf, sp[orig_iret], nz, nev
        )
        print("OVERALL ak_lnvmr_sq:", ak_lnvmr_sq.shape)
        # %%% shape: (101, 101)

        # Convert from ln(vmr)/ln(vmr) to vmr/vmr
        ak_vmr_sq = ak_lnvmr_sq * matrix_multiply(
            c_vmr, 1.0 / c_vmr, btr=True)
        print("OVERALL ak_vmr_sq:", ak_vmr_sq.shape)
        # %%% shape: (101, 101)

        # Convert AK to d_sub-columns/d_vmr
        #print(
        #    "^^^^^ msc", msc.shape, "ak_sc", ak_sc.shape, "orig_iret",
        #    orig_iret,
        #)
        fin_mm = matrix_multiply(
            msc, ak_vmr_sq, atr=True, btr=True)  ##.transpose()
        ak_sc[:, :, orig_iret] = fin_mm  ##.transpose()
        print("OVERALL ak_sc:", ak_sc.shape)
        # %%% shape: (3, 101, 5040)

        # Calculate a priori contribution so can layer apply AKs by doing simply
        # c_sc_model = c_apc + matrix_cultiply(ak_c,c_vmr_model)
        # for sub-columns, ak_c is non square and returned in units of
        # d_retrieved_subcolumn_average_vmr/d_true_profile_vmr
        c_apc_sc[:, orig_iret] = c_ap_sc - matrix_multiply(
            ak_sc[:, :, orig_iret], c_ap_vmr)
        print("OVERALL c_apc_sc:", c_apc_sc.shape)
        # %%% shape: (3, 5040)

        # Now deal with errors...
        # convert matrices to vmr from ln(vmr)  (error in ln(x) is
        # fractional error in x)
        vmr_sq = matrix_multiply(c_vmr, c_vmr, btr=True)
        vmr_sq = vmr_sq.squeeze()
        print("OVERALL vmr_sq:", vmr_sq.shape, vmr_sq)
        # %%% shape: (1, 1) -> (1,) after squeeze
        # Unpack vmr_sq to single value
        # UPTO
        print(
            "INDEX IS", orig_iret, "sx_lnvmr", sx_lnvmr.shape)
        # SLB HERE
        sx_vmr = sx_lnvmr[:, :, orig_iret] * vmr_sq
        print("OVERALL sx_vmr:", sx_vmr.shape)
        # %%% shape: (101, 10)
        sn_vmr = sn_lnvmr[:, :, orig_iret] * vmr_sq
        print("OVERALL sn_vmr:", sn_vmr.shape)
        # %%% shape: (101, 10)

        sx_sc[:, :, orig_iret] = matrix_multiply(
            matrix_multiply(sx_vmr, msc, atr=True).transpose(),
            msc.transpose(), btr=True,
        )
        print("OVERALL sx_sc:", sn_sc.shape)
        # %%% shape: (3, 3, 5040)

        # SLB Note, fixed likely issue where this is same as sx_sc, due to
        # input of sx_vmr when it is liekly to have meant to have been sn_vmr
        sn_sc[:, :, orig_iret] = matrix_multiply(
            matrix_multiply(sn_vmr, msc, atr=True).transpose(),
            msc.transpose(), btr=True,
        )
        print("OVERALL sn_sc:", sn_sc.shape)
        # %%% shape: (3, 3, 5040)

        # Just get sqrt-diagonals of the covariances (Estimated total random
        # error std.deviation and the noise std.deviation)
        c_err_sc[:, orig_iret] = sqrt_nz(f_diagonal(sx_sc[:, :, orig_iret]))
        print("OVERALL c_err_sc:", c_err_sc.shape)
        # %%% shape:
        c_noise_sc[:, orig_iret] = sqrt_nz(f_diagonal(sn_sc[:, :, orig_iret]))
        print("OVERALL c_noise_sc:", c_noise_sc.shape)
        # %%% shape:

    # Make result structure
    # Everything given for sub columns so drop the _sc in the tag names
    s = {
        # Fine grid pressures / hPa (nz = number of fine grid levels)
        "pf": pf,
        # Def. of the sub-column bounds / hPa (2,nsc = number of sub-columns)
        "scs": scs,
        # Latitude (np = number of retrievals in the file)
        "lat": lat,
        # Longitude (np)
        "lon": lon,
        # Julian day (np)
        "jday": jday,
        # Surface pressure / hPa (np)
        "sp": sp,
        # CO sub-column average mixing ratios (nsc,np) / ppmv
        "c": c_sc,
        # Averaging kernels for retrieved sub-column wrt true profile
        # vmr (nsc,nz,np) / ppmv/ppmv
        "ak": ak_sc,  # MAIN FOR AK
        # Total (Noise + smoothing) covariance for sub-col.avg.vmrs
        # (nsc,nsc) / ppmv^2
        "sx": sx_sc,
        # Noise covariance (nsc,nsc) / ppmv^2
        "sn": sn_sc,
        # A priori contribution to each sub-column (nsc,np) / ppmv
        "c_apc": c_apc_sc,  # MAIN FOR AK
        # Estimated total standard deviation of retrieved sub-cols (nsc,np) / ppmv
        "c_err": c_err_sc,
        # Estimated noise standard deviation (nsc,np) / ppmv
        "c_noise": c_noise_sc,
    }

    return s


def cf_field_result(fi, s, c_vmr_model):
    """Output a new CF-compliant field with the averaging kernel applied.

    Includes setting up appropriate bounds from 'scs' etc.

    Metadata wranlging!
    """
    # The code to apply the averaging kernel:
    c_sc_model = s["c_apc"] + matrix_multiply(s["ak"], c_vmr_model)

    # TODO create field with relevant data and metadata ab-inito
    f = None

    return f


# Temp whilst get working as script, then will incorporate into the VISION
# toolkit packaging as a plugin
if __name__ == "__main__":
    sys.exit(main())
