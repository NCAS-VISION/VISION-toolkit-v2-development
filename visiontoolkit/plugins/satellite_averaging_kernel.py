#!/usr/bin/env python

"""

SLB TODOs:
- once converted IDL -> Python:
  - lint
  - look for ways to improve Python
  - look for ways to use cf-python to simplify/streamline
  - look for ways to Daskify instead of use plain numpy

***

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
Translated to Python by SLB, */12/2024

CONVERSION NOTES:
1. Used package to auto-convert as much as possible:
   https://github.com/dnidever/idl2py
2. Applied basic linting to view better - manually since 'black'
   or other linter would fail on invalid Python at this stage
3. Using IDL reference to convert some undefined keywords e.g.
  https://lweb.cfa.harvard.edu/~atripath/idlrefguide.pdf
  e.g. KEYWORD_SET "It returns a True (1) if its argument is defined
  and nonzero, and False (0) otherwise"
4. Using this 'NumPy for IDL users' to convert precision and array stuff,
   really helpful resource!:
   https://mathesaurus.sourceforge.net/idl-numpy.html
5. This explains constant setting, esp. how double precision objs are set,
   useful for converting numbers with letters in e.g. '85d0':
   https://www.nv5geospatialsoftware.com/docs/Defining_and_Using_Const.html
   and this one:
   https://www.irya.unam.mx/computo/sites/manuales/IDL/Content/Creating%20IDL%20Programs/Components%20of%20the%20IDL%20Language/IDL_Data_Types.html
6. 'matrix_multiply' is a bit tricky, see:
   https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator
7. Further complications, see:
https://stackoverflow.com/questions/78656111/converting-idl-into-python-taking-verbatim-translation-and-making-it-pythonic
"IDL slice endpoints are inclusive, while Python slice endpoints are exclusive. For example, in IDL, x[1:4] extracts a subarray of length 4 (elements at indices 1, 2, 3, 4), while in Python, x[1:4] extracts a sub-array of length 3 (elements at indices 1, 2, 3)."
8. Slicing! Parentheses in Python indicate a function call but in IDL they
   indicate an array slice, at least most or all of the time for this script
   context. Note asterisks e.g. a(*, N) or a(N, *) including with
   multiple asterisk e.g.
   a(*, *, N) have special slice meaning, see 'Indexing and accessing elements
   (Python: slicing)' in https://mathesaurus.sourceforge.net/idl-numpy.html
   for tips on how to convert. Examples there:
a(2,1) -> a[1,2]
a(*,0) -> a[0,]
a(0,*) ->       a[:,0]
a(*,1:*) ->     a[1:,]

Assuming ak_lnvmr(*,*,iret) therefore ->
but need to check. ChatGPT says:
In IDL, a[*, *, 0] selects a 2D slice from a 3D array a. The * acts as a wildcard, meaning "include all elements along this dimension." Specifically:

    The first * selects all elements along the first dimension (rows).
    The second * selects all elements along the second dimension (columns).
    The 0 selects the first slice (index 0) along the third dimension (depth).

This is equivalent to indexing a 3D NumPy array in Python as:

a[:, :, 0]

BUT I think it is instead a[0, :, :] somehow - due to reversal w.r.t
Python order specified.

9. 'flake8' is returning a lot of 'F821 undefined name' failures which are
   caused by variables not being defined in function (and nothing globally) so
   there is scope to consider (quoting from ChatGPT):
   ```
   1. Inheritance of Scope from the Caller

   If a procedure is called without defining all its variables internally or passing them as arguments, it can access variables from the calling scope. This behavior is unique to IDL and can lead
   to implicit dependencies.
   Example:

   PRO my_procedure
     PRINT, a  ; Accesses 'a' from the caller's scope if it exists
   END

   a = 42
   my_procedure  ; Outputs: 42

   So to get around this, add these as function arguments and go edit code
   appropriately.
   2. Common Blocks

   IDL allows variables to be shared among multiple procedures or functions using common blocks. A common block acts like a shared memory space that multiple procedures can use to access and modify the same variables.
   ```
10. SLB: care, original IDL code has 'np' as variable, must use another to
    # avoid nameclash with numpy alias!
So renamed these orig_np

11. IDL case statement, see:
https://www.nv5geospatialsoftware.com/docs/CASE_Versus_SWITCH.html
12. SORTED fz_roots is actually built-in IDL - see here:
https://www.nv5geospatialsoftware.com/docs/FZ_ROOTS.html
13. Note converted keyword arguments to arguments where the argument is
    undefined gloally e.g. tol=tol, box=box. Can be input as args anyway
    so should be harmless but necessary to work in Python script.

14. NOTE IDL is DL is a zero-index language - was good to check

15. SLB TODO
"IDL slice endpoints are inclusive, while Python slice endpoints are exclusive. For example, in IDL, x[1:4] extracts a subarray of length 4 (elements at indices 1, 2, 3, 4), while in Python, x[1:4] extracts a sub-array of length 3 (elements at indices 1, 2, 3)."
so go and account for that.

16. Does the IDL ncdf_get return everything in Fortran major - since
    we are in C major, but resources like (as ref#'d for matrix_multiply);
https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator
imply we deal with this via the transpose operations.
As for more general case, check ncdf_get for row-column major bit.
-> potetnially query in numpy to see what row-column thing we have
and be careful with it.
e.g. https://numpy.org/doc/2.1/reference/generated/numpy.isfortran.html
numpy.isfortran(a)

17. Also check slowest-moving indexing part - is it always first?

18. Intpreting the output structure in terms of size.

19. Add statement at top to include STFC OSS notes.

20. Include the fix for the error RS pointed out!
"""


import numpy as np


# START OF NEW FUNCS TO MAP IDL PROCEDURE NAMES TO EQUIVALENT PYTHON
# FUNCTIONALITY USING E.G. CF-PYTHON

import cf  # only using for now to read in to get arrays


# Start with the easiest to do in Python/cf-python!


def matrix_multiply(a, b, atr=False, btr=False):
    """Implement IDL 'matrix_multiply' function in Python.

    Note:
    https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator
    """
    a_dot = a
    if not atr:
        a_dot = a.T

    b_dot = b
    if not btr:
        b_dot = b.T

    return np.dot(a_dot, b_dot).T


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
    IGNORING IDL CODE AS THIS IS TRIVIAL IN CF-PYTHON SO NO NEED TO CHECK THEIR APPROACH
    """
    # Note: noclo arg to not close file irrelevant in cf-python
    # Undo and ova args also probably not relevant but check this later.
    fl = cf.read(fi, aggregate=False)  # DH advice: agg=False for speed and improv.
    v = fl.select_by_ncvar(varname)
    return v


def setup_linear(x0, x1, i0, i1, w0, w1, vl=False, extra=False):
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
    ;	EXT	Set to perform extrapolations
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

    IGNORING IDL CODE AS THIS IS TRIVIAL IN CF-PYTHON SO NO NEED TO CHECK THEIR APPROACH
    """
    # SLB TODO: how to deal with specified existing weights? Gues via
    # RegridOperator(weights, ...) somehow, but not yet sure.
    # SLB TODO what are these 'indexes to y' and how to deal with?
    r = x0.regrids(x1, method="linear")
    return r


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

    function sqrt_nz,a,no_data=no_data,nnd=nnd
            if n_elements(no_data) eq 0 then no_data=-999
            sz=size(a)
            if sz(0) eq 0 then begin
                    if a ge 0 then return,sqrt(a) else return,no_data
            endif
            c=make_array(size=sz,value=no_data)
            wh=where(a gt 0,nw,ncom=nnd)
            if nw gt 0 then c(wh)=sqrt(a(wh))
            return,c
    end
    """
    sqa = np.sqrt(a)
    sqa.masked_invalid()  # SLB update np and cf world mix
    return sqa


# added internal undefined vars to arguments: nw, i0, i1, w0, w1
def setup_integration_matrix(
        x1, orig_xrange, extra, tol, box, nw, i0, i1, w0, w1):
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
    function setup_integration_matrix,x1,xrange=xrange,_EXTRA=extra,tol=tol,box=box
    ;
    ; sort into ascending order so this can be assumed throughout
    ;
            so=sort(x1)
            x=x1(so)
            if keyword_set(xrange) then begin
    ;
    ; get matrix to perform interpolation...
    ;
                    wh=where(x gt xrange(0) and x lt xrange(1),nw)
                    if nw gt 0 then xi=[xrange(0),x(wh),xrange(1)] else xi=xrange
                    setup_linear,x,xi,i0,i1,w0,w1,/vl,_EXTRA=extra	; x is in ascending order so can use value locate to do this as fast as possible
                    nx=n_elements(x)
                    nxi=n_elements(xi)
                    mi=dblarr(nxi,nx)
                    mi(lindgen(nxi),i0)=w0
                    mi(lindgen(nxi),i1)=mi(lindgen(nxi),i1)+w1
    ;
    ; now get vector which would perform the integration on interpolated array
    ;
                    mii=setup_integration_matrix(xi,box=box)
    ;
    ; now combine the two operations into one vector
    ;
                    m=reform(matrix_multiply(mii,mi))
            endif else begin
                    dx=[x(1:*)-x]
                    if keyword_set(box) then begin
                            so=sort(x1(1:*)) ; need to sort based on 1 value per layer not level, in order for sorting back to work below
                            if keyword_set(tol) then begin
                                    nz=n_elements(x)
                                    m=dblarr(nz-1,nz-1)
                                    for iz=1,nz-1 do m(0,iz-1)=dx(0:iz-1)
                            endif else m=dx
                    endif else begin
                            if keyword_set(tol) then begin
                                    nz=n_elements(x)
                                    m=dblarr(nz,nz-1)
                                    for iz=1,nz-1 do begin
                                            m(0,iz-1)=0.5d0*([0d0,dx(0:iz-1)]+[dx(0:iz-1),0d0])
                                    endfor
                            endif else m=0.5d0*([0d0,dx]+[dx,0d0])
                    endelse
            endelse
    ;
    ; sort m back to original order
    ;
            bk=sort(so)
            m=m(bk,*)
            return,m
    end
    """
    # Sort into ascending order so this can be assumed throughout
    so = np.argsort(x1)
    x = x1[so]

    if orig_xrange:
        # Get matrix to perform interpolation...
        # TODO SLB was originally an 'and' here but that might be
        # problematic, DH advice to convert to ampersand which works
        # - see cf-python codebase examples.
        (wh,) = np.where((x > orig_xrange[0]) & (x < orig_xrange[1], nw))
        if nw > 0:
            xi = [orig_xrange[0], x[wh], orig_xrange[1]]
        else:
            xi = orig_xrange

        # x is in ascending order so can use value locate to do this
        # as fast as possible
        setup_linear(x, xi, i0, i1, w0, w1, vl=True, extra=extra)
        nx = len(x)
        nxi = len(xi)
        mi = np.zeros((nxi, nx))
        mi[i0, np.arange(nxi)] = w0
        mi[i1, np.arange(nxi)] = mi[i1, np.array(nxi)] + w1

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
        m = np.squeeze(matrix_multiply(mii, mi))
    else:
        dx = [x[:, 1:] - x]  # IDL: [x(1: *) - x]
        if box:
            # need to sort based on 1 value per layer not level,
            # in order for sorting back to work below
            so = np.argsort(x1[:, 1:])  # IDL: np.argsort(x1(1: *))
            if tol:
                nz = len(x)
                m = np.zeros((nz - 1, nz - 1))
                for iz in np.arange(1, nz):
                    m[iz - 1, 0] = dx[0: iz - 1]
            else:
                m = dx
        else:
            if tol:
                nz = len(x)
                m = np.zeros((nz, nz - 1))
                for iz in np.arange(1, nz):
                    m[iz - 1, 0] = 0.5 * (
                        [0.0, dx[0: iz - 1]] + [dx[0: iz - 1], 0.0]
                    )
            else:
                m = 0.5 * ([0.0, dx] + [dx, 0.0])

    # Sort m back to original order
    bk = np.argsort(so)
    m = m[:, bk]  # IDL: m(bk, *)

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
            sz=size(vsx)
            if sz(0) eq 1 then npi=1 else npi=sz(2)
            nv=sz(1)
            if n_elements(diag) gt 0 then begin
                    szd=size(diag)
                    nd=szd(1)
                    if szd(0) eq 1 then npid=1 else npid=sz(2)
                    if npi ne npid then message,'DIAG,VSX do not match!'
                    nv=nv+nd
                    covd=diag(*,0)*0+1	; array of 1s for diagonal of correlation
                    correl=1
            endif else correl=0

            n=fz_roots([2*nv,-1,-1]) ; Find expected dimensions of covariance based on unwrapped vector of half of the off-diagonals and the diagonals
            n=long(n(1)+0.1)
            sx=fltarr(n,n,npi)
            for ipi=0,npi-1 do begin ; Do for more than one pixel
                    j=0
                    vsx1=vsx(*,ipi)
                    if correl then begin
                            vsx1=[covd,vsx1]
                            diag1=diag(*,ipi)
                            diag2=matrix_multiply(diag1,diag1)
                    endif
                    for i=0, n-1 do begin
                            if i eq 0 then sx1=diag_matrix(vsx1(j:j+n-i-1)) $;  diagonals
                            else sx1=sx1+diag_matrix(vsx1(j:j+n-i-1),i)+diag_matrix(vsx1(j:j+n-i-1),-i) ; off-diagonals
                            j=j+n-i
                    endfor
                    if correl then sx1=sx1*diag2
                    sx(0,0,ipi)=sx1
            endfor

            return, sx
    end
    """
    # Reconstruct covariance matrix from vector representing one half of
    # covariance matrix unwrapped
    sz = vsx.shape
    if sz[0] == 1:
        npi = 1
    else:
        npi = sz[2]

    nv = sz[1]
    if len(diag) > 0:
        szd = diag.shape
        nd = szd[1]
        if szd[0] == 1:
            npid = 1
        else:
            npid = sz[2]
        if npi != npid:
            raise ValueError("DIAG,VSX: not match!")

        nv = nv + nd
        covd = diag[0,] * 0 + 1  # array of 1s for diagonal of correlation
        correl = 1
    else:
        correl = 0

    # Find expected dimensions of covariance based on unwrapped
    # vector of half of the off-diagonals and the diagonals
    n = np.roots([2 * nv, -1, -1])
    n = int(n[1] + 0.1)
    sx = np.zeros((n, n, npi), dtype=np.float32)
    for ipi in range(npi):  # Do for more than one pixel
        j = 0
        vsx1 = vsx[ipi,]
        if correl:
            vsx1 = [vsx1, covd]
            diag1 = diag[ipi,]
            diag2 = matrix_multiply(diag1, diag1)

        for i in range(n):
            if i == 0:  # diagonals
                sx1 = np.diag(vsx1[j: j + n - i - 1])
            else:
                sx1 = (
                    sx1
                    + np.diag(vsx1[j: j + n - i - 1], i)
                    + np.diag(vsx1[j: j + n - i - 1], -i)
                )  # off-diagonals
            j = j + n - i
        if correl:
            sx1 = sx1 * diag2

        sx[ipi, 0, 0] = sx1

    return sx


def iasimhs_sx_exp(s1, evecs, log, x):
    """Implement IDL code 'iasimhs_sx_exp' function in Python.

        This procedure was stored in its own module, with the functional code
        and important docs as follows:

    function iasimhs_sx_exp, s1, evecs, log=log, x=x
    ;
    ; loop over multiple covariances, reconstructing each
    ;
            sz=size(s1)
            if sz(0) eq 3 then np=sz(3) else np=1
            if sz(1) ne sz(2) then message,'Expected first 2 dims to be same size!'
            sz=size(evecs)
            nz=sz(1)
            s=fltarr(nz,nz,np)
            for ip=0,np-1 do begin
                    sipi=s1(*,*,ip)
                    sipi=matrix_multiply(matrix_multiply(evecs,sipi),evecs,/btr) ; map to rttov levels
                    if keyword_set(log) then begin
                            xipi=x(*,ip)
                            sipi=sipi*matrix_multiply(xipi,xipi) ; Multiply out log unit
                    endif
                    s(0,0,ip)=sipi
            endfor
            return,s
    end
    """
    sz = s1.shape
    if sz[0] == 3:
        np = sz[3]
    else:
        np = 1

    if sz[1] != sz[2]:
        raise ValueError("Expected first 2 dims to be same size!")

    sz = evecs.shape
    nz = sz[1]
    s = np.zeros((nz, nz, np), dtype=np.float32)
    for ip in range(np):
        sipi = s1[ip, :, :]
        sipi = matrix_multiply(
            matrix_multiply(evecs, sipi), evecs, btr=True
        )  # map to rttov levels
        if log:
            xipi = x[ip,]
            sipi = sipi * matrix_multiply(xipi, xipi)  # Multiply out log unit

        s[ip, 0, 0] = sipi

    return s


def f_diagonal(matrix, orig_input):
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

    function f_diagonal,matrix,input=in

    nel=n_elements(matrix)
    if (nel eq 1) then begin
       matrix_save=matrix  & matrix=replicate(matrix(0),2,2)
    endif
    dim_in  = size(in)      &  nin = n_elements(in)
    dim_mat = size(matrix)  &  nmat = n_elements(matrix)

    case nin of
        0 : begin
              result = make_array(dim_mat(1),type=dim_mat(dim_mat(0)+1))
              for i=0,dim_mat(1)-1 do result(i) = matrix(i,i)
            end
        1 : begin
              result = matrix
              for i=0,dim_mat(1)-1 do result(i,i) = in
            end
      else: begin
              if (nmat ne 0) then result = matrix
              if (nmat eq 0) then $
                 result = make_array(nin,nin,type=dim_in(dim_in(0)+1))
              for i=0,nin-1 do result(i,i) = in(i)
            end
    endcase

    if (nel eq 1) then begin & result=result(0) & matrix=matrix_save & endif

    f_diagonal = result
    return,f_diagonal
    end
    """
    # dimensions
    nel = len(matrix)
    if nel == 1:
        matrix_save = matrix
        # https://lweb.cfa.harvard.edu/~atripath/idlrefguide.pdf
        # "The REPLICATE function returns an array with the given dimensions, filled with the
        # scalar value specified as the first parameter"
        matrix = np.full((2, 2), matrix[0])  # IDL: replicate(matrix(0), 2, 2)

    # SLB: flake8 says this variable is not used, so comment out
    # dim_in = orig_input.shape
    nin = len(orig_input)
    dim_mat = matrix.shape
    nmat = len(matrix)

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

DEFAULT_FILEPATH = (
    "../../data/marias-satellite-example-data/satellite-data/"
    "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_"
    "20170703215054z_000_049-v1000.nc"
    # From orig IDL, used: "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-"
    #"20110718141155z_20110718155058z_000_049-v1000.nc"
)


# TODO SLB: latitude is probably not relevant so we can ignore this!
# added internal undefined vars to arguments: i0, i1, w0, w1
def irc_interp_ap(xap, latitude, i0, i1, w0, w1):
    """CONV DONE
    Interpolate prior in 18 latitude bands to latitude of measurement

    Inputs
          xap    prior values
          latitude Latitudes
          SP      Surface pressure (only needed if e60 set)
    """
    # Latitude grid associated with the prior values
    lats_ap = np.arange(18.0) * 10 - 85  # IDL: dindgen(18) * 10 - 85d0
    setup_linear(lats_ap, latitude, i0, i1, w0, w1, vl=True)

    # SLB: care, original IDL code has 'np' as variable, must use another to
    # avoid nameclash with numpy alias!
    orig_np = len(latitude)
    nz = len(xap[0,])  # IDL: xap(*,0)
    xapi = np.zeros((nz, orig_np))  # IDL: dblarr(nz, np)

    for ip in np.arange(0, orig_np):
        # IDL: xapi(0, ip) = xap(*,i0(ip)) * w0(ip) + xap(*,i1(ip)) * w1(ip)
        xapi[ip, 0] = xap[i0[ip]] * w0[ip] + xap[i1[ip]] * w1[ip]

    return xapi


# added internal undefined vars to arguments: ns, w0, i0, i1, w1
def irc_ak_exp(ak, evecs, pf, sp, nz, nev, ns, w0, i0, i1, w1):
    """CONV DONE
    Recreate full averaging kernel from IASI-MHS state vector representation

    Inputs
        AK      Ak for state vector representation, wrt 51 "true levels" (every other RTTOV level)
        EVECS   Vectors to map to 101 RTTOV levels from state vector
        PF      Fine grid pressures / hPa
        SP      Surface pressure / hPa
        NZ      Number of fine vertical levels
        NEV     Number of eigenvectors
    """
    # Index of PF used to store true grid perturbations in file
    idx = np.arange(nz / 2 + 1) * 2  # IDL: lindgen(nz / 2 + 1) * 2
    pfs = pf[idx]
    setup_linear(pfs, pf, i0, i1, w0, w1, vl=True)
    akt = ak.T
    ak_101 = np.zeros((nz, nev))  # IDL: dblarr(nz, nev)

    for iev in range(nev):  # Interpolate to full grid
        # IDL: ak_101(0, iev) = akt(i0, iev) * w0 + akt(i1, iev) * w1
        ak_101[iev, 0] = akt[iev, i0] * w0 + akt[iev, i1] * w1

    ak_101 = matrix_multiply(evecs, ak_101, btr=True)

    # Make sure AK is zero below surface pressure
    (ws,) = np.where(pf > sp, ns)  # TODO SLB is the comma / unpacking needed?
    if ns > 0:  # Set levels below surface to 0
        ak_101[ws,] = 0

    return ak_101


# added internal undefined vars to arguments: n0, w0
def irc_integration_matrix(scs, pf, sp, nz, nsc, n0, w0, approx=False):
    """CONV DONE
    (No docstring in corresponding IDL procedure).
    """
    msc = np.zeros((nz, nsc))  # IDL: dblarr(nz, nsc)

    if approx:
        # Approximate method uses the just the fine layer pressure differences between
        # the defined bounds as weights.
        # Full method treats the layer bounds more exactly, by also including interpolation
        # from the fine grid to the defined pressure bounds (and surface pressure).
        dp1 = pf[1: nz - 1] - pf[0: nz - 2]  # IDL: =pf(1:nz-1)-pf(0:nz-2)
        dpf = ([0.0, dp1] + [dp1, 0]) / 2

    for isc in range(nsc):
        # Pressure levels of this layer in ascending order
        sc1 = scs[[1, 0], isc]
        # if lower bound indicated as 1000 or lower bound below surface then truncate layer to the surface
        if sc1[1] == 1000 or sc1(1) > sp:
            sc1[1] = sp
        if approx:
            msc1 = dpf
            (w0,) = np.where(
                pf < sc1[0] or pf > sc1[1], n0
            )  # levels outside required layer
            if n0 > 0:
                msc1[w0] = 0
        else:
            # used function to set up weights to do trapezoid integration over defined interval
            msc1 = setup_integration_matrix(pf, xran=sc1)

        msc1 = msc1 / np.sum(
            msc1
        )  # this normalises result to sub-column average
        msc[0, isc] = msc1

    return msc


# added internal undefined vars to arguments: lun, nret
def ims_rd_co4ak(fi, lun, nret, approx=False):
    """
    Main function.
    """
    # Default filename if one not defined
    # (this one co-located with FAAM over Canadian fire)
    if len(fi) == 0:
        fi = DEFAULT_FILENAME

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

    # Read necessary info from the file
    # ncdf_get will apply scale_factor and add offset (/undo keyword)
    # /ova makes it just return the values without any attributes
    pf = ncdf_get(fi, "p", lun=lun, noclo=True, undo=True, ova=True)
    do_ret = (ncdf_get(fi, "do_retrieval", lun=lun, noclo=True)).value
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

    # SLB: flake8 says this variable is not used, so comment out
    # dsn_ev = ncdf_get(fi, "dsxn_c", lun=lun, noclo=True, undo=True, ova=True)
    # csn_ev = ncdf_get(fi, "csxn_c", lun=lun, undo=True, ova=True)

    # Get indices of retrieved scenes
    # - code assumes all retrieved scenes have AK and covariance
    # - this is true for all current ims files for co and o3 and minor gases (but not h2o or T)
    (iret,) = np.where(do_ret, nret)
    if nret == 0:
        raise ValueError("No retrievals in file!")

    # Convert time to julian day
    # TODO SLB check with DH operation order intended here - for IDL
    # Orig. IDL: sensingtime_day+sensingtime_msec/1000d0/60d0/60d0/24d0+2451544.5d0
    jday = (
        sensingtime_day
        + sensingtime_msec / (1000.0 * 60.0 * 60.0 * 24.0)  # msec - millisec
        + 2451544.5
    )

    # Subset lat/lon/time/sp to the pixels for which retrieval exist
    lat = lat[iret]
    lon = lon[iret]
    jday = jday[iret]
    sp = sp[iret]

    # Get dimensions
    nz = len(pf)  # number of fine vertical levels
    nsc = len(scs[:, 0])  # number of subcolumns

    # SLB: flake8 says this variable is not used, so comment out
    # nev = len(evecs[:, 0])  # number of Eigenvectors used to represent profile

    # Interpolate the set of prior profiles in latitude
    c_ap_lnvmr = irc_interp_ap(c_ap_lnvmr, lat)

    # Expand the total and noise  covariance matrices to full vertical grid (nz,nz) with units (ln(ppmv))^2
    sx_ev = iasimhs_vsx2cov(csx_ev, diag=dsx_ev)  # nev,nev matrix
    sx_lnvmr = iasimhs_sx_exp(sx_ev, evecs)  # nz,nz matrix

    # SLB: flake8 says this variable is not used, so comment out
    # sn_ev = iasimhs_vsx2cov(csn_ev, diag=dsn_ev)  # nev,nev matrix

    # SLB: flake8 says this variable is not used, so comment out
    # sn_lnvmr = iasimhs_sx_exp(sn_ev, evecs)  # nz,nz matrix

    # Make arrays to hold the results which are neeeded for model comparisons
    c_sc = np.zeros(
        (nsc, nret),
    )  # IDL: dblarr(nsc, nret)  # CO sub-column average mixing ratios / ppmv
    ak_sc = np.zeros(
        (nsc, nz, nret),
    )  # IDL: dblarr(nsc, nz, nret)  # Averaging kernels for retrieved sub-column wrt true profile vmr / ppmv/ppmv
    sx_sc = np.zeros(
        (nsc, nsc, nret),
    )  # IDL: dblarr(nsc, nsc, nret)  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs / ppmv^2
    sn_sc = np.zeros(
        (nsc, nsc, nret),
    )  # IDL: dblarr(nsc, nsc, nret)  # Noise covariance  / ppmv^2
    c_apc_sc = np.zeros(
        (nsc, nret),
    )  # IDL: dblarr(nsc, nret)  # A priori contribution to each sub-column / ppmv
    c_err_sc = np.zeros(
        (nsc, nret),
    )  # IDL: dblarr(nsc, nret)  # Estimated total standard deviation of retrieved sub-cols / ppmv
    c_noise_sc = np.zeros(
        (nsc, nret),
    )  # IDL: dblarr(nsc, nret)  # Estimated noise standard deviation / ppmv

    # Loop individual retrievals
    for iret in np.arange(0, nret):
        # Get vmr from lnvmr
        c_vmr = np.exp(c_lnvmr[iret,])  # undo log unit

        # Calculate weights which will compute the subcolumn via matrix multiply
        msc = irc_integration_matrix(scs, pf, sp[iret], nz, nsc, approx=approx)

        # Calculate the sub columns
        c_sc[iret, 0] = matrix_multiply(msc, c_vmr, atr=True)

        # Get corresponding prior profile and subcolumns
        c_ap_vmr = np.exp(c_ap_lnvmr[iret,])
        c_ap_sc = matrix_multiply(msc, c_ap_vmr, atr=True)

        # Make the square (nz,nz) AK array
        # IDL for first arg: ak_lnvmr(*,*,iret)

        # SLB: flake8 says this variable is not used, so comment out
        # ak_lnvmr_sq = irc_ak_exp(
        #     ak_lnvmr[iret, :, :], evecs, pf, sp[iret], nz, nev
        # )

        # Convert from ln(vmr)/ln(vmr) to vmr/vmr
        ak_vmr_sq = ak_lnvmr * matrix_multiply(c_vmr, 1.0 / c_vmr)

        # Convert AK to d_sub-columns/d_vmr
        ak_sc[iret, 0, 0] = matrix_multiply(msc, ak_vmr_sq, atr=True)

        # Calculate a priori contribution so can layer apply AKs by doing simply
        # c_sc_model = c_apc + matrix_cultiply(ak_c,c_vmr_model)
        # for sub-columns, ak_c is non square and returned in units of
        # d_retrieved_subcolumn_average_vmr/d_true_profile_vmr
        c_apc_sc[iret, 0] = c_ap_sc - matrix_multiply(
            ak_sc[iret, :, :], c_ap_vmr
        )

        # Now deal with errors...
        # convert matrices to vmr from ln(vmr)  (error in ln(x) is
        # fractional error in x)
        vmr_sq = matrix_multiply(c_vmr, c_vmr)
        sx_vmr = sx_lnvmr[iret, :, :] * vmr_sq
        # flake8: below variable not used and is dupe to above, so ignore
        # SLB sn_vmr = sn_lnvmr[iret, :, :] * vmr_sq

        # Convert these to (nsc,nsc) matrices for the sub-columns
        sx_sc[iret, 0, 0] = matrix_multiply(
            matrix_multiply(sx_vmr, msc), msc, atr=True
        )
        sn_sc[iret, 0, 0] = matrix_multiply(
            matrix_multiply(sx_vmr, msc), msc, atr=True
        )

        # Just get sqrt-diagonals of the covariances (Estimated total random
        # error std.deviation and the noise std.deviation)
        c_err_sc[iret, 0] = sqrt_nz(f_diagonal(sx_sc[iret, :, :]))
        c_noise_sc[iret, 0] = sqrt_nz(f_diagonal(sn_sc[iret, :, :]))

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
        "ak": ak_sc,
        # Total (Noise + smoothing) covariance for sub-col.avg.vmrs
        # (nsc,nsc) / ppmv^2
        "sx": sx_sc,
        # Noise covariance (nsc,nsc) / ppmv^2
        "sn": sn_sc,
        # A priori contribution to each sub-column (nsc,np) / ppmv
        "c_apc": c_apc_sc,
        # Estimated total standard deviation of retrieved sub-cols (nsc,np) / ppmv
        "c_err": c_err_sc,
        # Estimated noise standard deviation (nsc,np) / ppmv
        "c_noise": c_noise_sc,
    }

    return s


def cf_field_result(fi, s):
    """Output a new CF-compliant field with the averaging kernel applied.

    Includes setting up appropriate bounds from 'scs' etc.

    Metadata wranlging!
    """
    # The code to apply the averaging kernel:
    c_sc_model = s["c_apc"] + matrix_multiply(s["ak"], c_vmr_model)

    # TODO create field with relevant data and metadata ab-inito
    f = None

    return f
