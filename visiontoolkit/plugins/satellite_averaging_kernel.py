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

https://www.johnny-lin.com/cdat_tips/tips_array/idl2num.html
 Order of indices in Numeric/numarray is opposite of IDL! For a 2-dimension array:
a[i,j] in IDL is equivalent to a[j,i] in Python
ANOTHER SOURCE SAYS:
i:j 	i:j (except for different interpretation for j)
i:* 	i:
*:i 	:i
a[i,*] 	a[:,i]

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

MAINFESTS AS, E.G:
Traceback (most recent call last):
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/plugins/satellite_averaging_kernel.py", line 1280, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/plugins/satellite_averaging_kernel.py", line 1127, in main
    c_ap_lnvmr = irc_interp_ap(c_ap_lnvmr, lat)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/plugins/satellite_averaging_kernel.py", line 934, in irc_interp_ap
    setup_linear(lats_ap, latitude, vl=True)
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/plugins/satellite_averaging_kernel.py", line 412, in setup_linear
    dwdx[wh] = 1.0 / (x0[ihigh[wh]] - x0[ilow[wh]])
                                      ~~^^^^^^^^^^
IndexError: index 18 is out of bounds for axis 0 with size 18

so must change from IDL [n] to Python [n + 1] ???


16. Does the IDL ncdf_get return everything in Fortran major - since
    we are in C major, but resources like (as ref#'d for matrix_multiply);
https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator
imply we deal with this via the transpose operations.
As for more general case, check ncdf_get for row-column major bit.
-> potetnially query in numpy to see what row-column thing we have
and be careful with it.
e.g. https://numpy.org/doc/2.1/reference/generated/numpy.isfortran.html
numpy.isfortran(a)

Row major vs colum major:
https://stackoverflow.com/questions/20341614/numpy-array-row-major-and-column-major


17. Also check slowest-moving indexing part - is it always first?

18. Intpreting the output structure in terms of size.

19. Add statement at top to include STFC OSS notes.

20. Include the fix for the error RS pointed out!
-> done.

21. For IDL where, a variable is defined via the 'call'! I.e. with
    (A,) = where(C, D) in IDL creates A as where query and a new variable called
    D as the the number of elements in iret, and need to unpack from a resultant
    tuple (use 0 index), so convert that to:
        A = np.where(C)[0]
        D = len(A)

22. Care with use of len()! n_elements from IDL is better to do to .size for
    arrays, since len can given misleading results e.g. 1 where size is 101
    etc.

23. CONVERTING SIZE!
Note that (from https://lweb.cfa.harvard.edu/~atripath/idlrefguide.pdf, p2385):

If no keywords are set, SIZE returns a vector of integer type. The first element is
equal to the number of dimensions of Expression. This value is zero if Expression is
scalar or undefined. The next elements contain the size of each dimension, one
element per dimension (none if Expression is scalar or undefined). After the
dimension sizes, the last two elements contain the type code (zero if undefined) and
the number of elements in Expression, respectively. The type codes are listed below.
If a keyword is set, SIZE returns the specified information

Therefore IDL size(N) becomes Python
(N.ndim, [unpacked] N.shape, [ignore last one if can, is a type code])
so use:
ALSO NOTE YOU NEED TO REVERSE THE SHAPE! SINCE IN IDL THE COLUMNS ARE
QUOTED FIRST RELATIVE TO NP.SHAPE WHICH QUOTES ROWS FIRST. Hence the [-1]:

size(a) -> [a.ndim,] + list(a.shape)[::-1]

24. Rename 'np' var to avoid obvious clash!

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
    "20170703215054z_700_749-v1000.nc"  # nret is 5040, better
    # "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_"
    # "20170703215054z_000_049-v1000.nc"  # all 6000 retrievals, try another,
    # From orig IDL, used: "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-"
    # "20110718141155z_20110718155058z_000_049-v1000.nc"
)


def matrix_multiply(a, b, atr=False, btr=True):
    """Implement IDL 'matrix_multiply' function in Python.

    Note:
    https://stackoverflow.com/questions/23128788/what-is-the-python-numpy-equivalent-of-the-idl-operator

    Note: having B tranposed as default to ensure shapes are compatible for
    dot operation from IDL code conversion.
    """
    a_dot = a.copy()
    print("a", a.shape, type(a))
    if atr:
        if isinstance(a_dot, cf.Data):  # cf to np space, cf transpose issues
            print("a.T applied")
            a_dot = a_dot.array
        a_dot = a_dot.T

    b_dot = b.copy()
    print("b", b.shape, type(b))
    if btr:
        if isinstance(b_dot, cf.Data):  # cf to np space
            print("b.T applied")
            b_dot = b_dot.array
        b_dot = b_dot.T

    return np.dot(a_dot, b_dot)  #.transpose() need final one for overall res?


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
    fl = cf.read(
        fi, aggregate=False
    )  # DH advice: agg=False for speed and improv.
    v = fl.select_by_ncvar(varname)
    print("Returning fieldlist of:", len(v), v)

    # Unpacking stage, if a FieldList of length 1:
    if len(v) != 1:
        raise ValueError("!!! Have a FieldList of non-singular size.")
    else:
        v = v[0]

    # Return the data not the field! For the algorithm conversion, work in
    # numpy array space until we get it working, then can conert to cf-python
    # space.
    d = v.data
    d.persist(inplace=True)  # for speed
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
    n1 = len(x1)
    if spline:
        if len(extra) == 0:
            extra = 1

    if len(x0) == 0:
        raise ValueError("X0 undefined")
    if len(x0) == 1:
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
        n0 = len(x0)
        # SLB ChatGPT's suggestion of Python equivalent to IDL value_locate,
        # I remain dubious but will check this at run-through time
        ilow = np.searchsorted(x0, x1)  # IDL: value_locate(x0, x1)
        ihigh = ilow + 1
        wh = np.where(ilow < 0)[0]
        nw = len(wh)
        if nw > 0:
            ilow[wh] = 0

        wh = np.where(ihigh >= n0)[0]
        nw = len(wh)
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
        n0 = len(x0)
        whoor = np.where(ihigh == ilow)[0]
        noor = len(whoor)
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
    print("WH", wh, type(wh), len(wh))
    nne = len(wh)
    if nne != 0:
        print("ilow is", ilow, type(ilow), ilow[wh], ilow[wh] - 1)
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

    if len(x1) == 1 and op:
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
        nw = len(wh)
        if nw > 0:
            xi = [orig_xrange[0], x[wh], orig_xrange[1]]
        else:
            xi = orig_xrange
        print("wh:", wh.shape, wh, "xi:", xi.shape)

        # x is in ascending order so can use value locate to do this
        # as fast as possible
        i0, i1, w0, w1 = setup_linear(x, xi, vl=True, extra=extra)
        nx = len(x)
        nxi = len(xi)
        mi = np.zeros((nx, nxi))
        print("POINT 1", mi.shape, [i0, np.arange(nxi)], "i0", i0)
        print("THIS IS", np.concatenate((i0, np.arange(nxi))))
        mi[np.concatenate((i0, np.arange(nxi)))] = w0
        print("j:", )
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
        m = np.squeeze(matrix_multiply(mii, mi))
    else:
        print("x", x.shape, x[:1].shape)
        # Note that dx was in IDL array form [<this>] so wrap with np.array
        dx = np.array(x[1:][0] - x)  # IDL: [x(1: *) - x], [0] to unpack from shape (1,)
        if box:
            # need to sort based on 1 value per layer not level,
            # in order for sorting back to work below
            so = np.argsort(x1[1:])  # IDL: np.argsort(x1(1: *))
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
                print("dx:", dx)
                m = 0.5 * (
                    np.concatenate((np.array([0.0]), dx)) +
                    np.concatenate((dx, np.array([0.0])))
                )
                print("FINAL m:", m)

    # Sort m back to original order
    bk = np.argsort(so)
    print("m:", m.shape, "bk:", bk.shape, bk)  #, "m[:, bk]:", m[:, bk].shape)
    m = m[bk]  # IDL: m(bk, *)
    ###print("FINAL m:", m)

    return m


def iasimhs_vsx2cov(vsx, diag):
    """CONV DONE
    Implement IDL code 'iasimhs_vsx2cov' function in Python.

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
    if len(diag) > 0:
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
            print("VSX1 IS", vsx1, vsx1.shape)
            diag1 = diag[ipi,]
            diag2 = matrix_multiply(diag1, diag1)
            print("Diags", diag1.shape, diag2.shape)

        print("N IS", n)
        for i in range(n):
            if i == 0:  # diagonals
                # IDL:  vsx1[j: j + n - i - 1] has but inclusive endpoints
                # therefore +1 -> - 1 + 1 = 0
                sx1 = np.diag(vsx1[j: j + n - i])
                print("1. Shapes are:", "sx1:", sx1.shape)
            else:
                # IDL:  vsx1[j: j + n - i - 1] has but inclusive endpoints
                # therefore +1 -> - 1 + 1 = 0
                print("Shapes are", i, ": sx1:", sx1.shape)
                print("expr attempt", np.diag(vsx1[j: j + n - i], i))
                sx1 = (
                    sx1
                    + np.diag(vsx1[j: j + n - i], i)
                    + np.diag(vsx1[j: j + n - i], -i)
                )  # off-diagonals
            j = j + n - i
            print("J IS", j)  ###, "sx1 is", sx1)

        if correl:
            print("yes", sx1, diag2)
            sx1 = sx1 * diag2

        print("sx1", sx1.shape)  #, sx[ipi, 0, 0].shape)
        sx[: , :, ipi] = sx1  #sx[ipi, 0, 0] = sx1

    print("FINAL SX IS", sx, sx.shape)
    return sx


def iasimhs_sx_exp(s1, evecs, log=False, x=False):
    """CONV DONE
    Implement IDL code 'iasimhs_sx_exp' function in Python.

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
    if sz[1] != sz[2]:  # IDL: if sz[1] != sz[2, but Py dims reverse order
        raise ValueError("Expected first 2 dims to be same size!")

    sz = [evecs.ndim,] + list(evecs.shape)[::-1]
    print("evecs:", evecs)
    nz = sz[1]
    s = np.zeros((nz, nz, orig_np), dtype=np.float32)
    print("s shape:", s.shape, "orig_np int:", orig_np)
    for ip in range(orig_np):
        print("ip is:", ip)
        sipi = s1[:, :, ip]
        pre_sipi = matrix_multiply(evecs, sipi, atr=True, btr=True)
        sipi = matrix_multiply(
            pre_sipi, evecs, atr=False, btr=False
        )  # map to rttov levels
        if log:
            xipi = x[ip,]
            sipi = sipi * matrix_multiply(xipi, xipi)  # Multiply out log unit

        print("Attempt", sipi.shape)
        # NOTE: relative to raw IDL, apply T to transpose whole result
        # so have shape (10, 45)
        # to fit s shape (10, 10, 45), not shape (45, 10)
        print("shape sipi", sipi.shape, "shape other", s[ip, :, :].shape)
        s[:, :, ip] = sipi

    print("Final return value s:", s.shape)
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


# TODO SLB: latitude is probably not relevant so we can ignore this!
# added internal undefined vars to arguments: i0, i1, w0, w1
def irc_interp_ap(xap, latitude):
    """CONV DONE
    Interpolate prior in 18 latitude bands to latitude of measurement

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
        print("ITER:", ip)
        # IDL: xapi(0, ip) = xap(*,i0(ip)) * w0(ip) + xap(*,i1(ip)) * w1(ip)
        ###res = xap[i0[ip]] * w0[ip] + xap[i1[ip]] * w1[ip]
        ###print("RES", res, res.shape, type(res))
        ###print("OUTCOME", xapi[ip, 0], type(xapi[ip, 0]))
        # SLB PY: got immediate error:
        # aging_kernel.py", line 973, in irc_interp_ap
        # xapi[ip, 0] = xap[i0[ip]] * w0[ip] + xap[i1[ip]] * w1[ip]
        # ~~~~^^^^^^^
        # ValueError: setting an array element with a sequence.
        # So to fix, for now calulcate the array immediately
        ###print("BIT IS", w0[ip], "AND", xap[i0[ip],])

        # SLB DEBUGGED BASED ON SHAPES FITTING, THOUGHT IT SHOULD BE
        # xapi[ip, 0] = result logically but that wouldn't broadcast,
        # go with this for now
        ###result = xap[i0[ip],] * w0[ip] + xap[i1[ip],] * w1[ip]  ##.flatten()
        ###print("RESULT", result, type(result), result.shape)
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
    ak_101 = matrix_multiply(evecs, ak_101, atr=True, btr=False)

    # Make sure AK is zero below surface pressure
    ws = np.where(pf > sp)[0]
    ns = len(ws)
    if ns > 0:  # Set levels below surface to 0
        ak_101[ws,] = 0

    print("FINAL ak_101", ak_101.shape, ak_101)
    return ak_101


# added internal undefined vars to arguments: n0, w0
def irc_integration_matrix(
        scs, pf, sp, nz, nsc, n0=False, w0=False, approx=False):
    """CONV DONE
    (No docstring in corresponding IDL procedure).
    """
    msc = np.zeros((nz, nsc))  # IDL: dblarr(nz, nsc)

    if approx:
        # Approximate method uses the just the fine layer pressure differences between
        # the defined bounds as weights.
        # Full method treats the layer bounds more exactly, by also including interpolation
        # from the fine grid to the defined pressure bounds (and surface pressure).
        # IDL: =pf(1:nz-1)-pf(0:nz-2) - convert for Python exclusiveness by + 1
        dp1 = pf[1: nz] - pf[0: nz - 1]
        print("dp1", dp1.shape)
        # Use explicit concat form for Python/numpy from IDL implicit concat
        dpf = (np.concatenate((np.array([0.0]), dp1)) +
               np.concatenate((dp1, np.array([0.0])))) / 2
        print("dpf", dpf.shape, dpf)
        ###dpf = ([0.0, dp1] + [dp1, 0]) / 2

    for isc in range(nsc):
        # Pressure levels of this layer in ascending order
        # SLB UPTO
        print("isc:", isc)
        sc1 = np.array([1, 0, isc])  # scs[[1, 0], isc]
        print("sc1", sc1)
        # if lower bound indicated as 1000 or lower bound below surface then truncate layer to the surface
        if sc1[1] == 1000 or sc1[1] > sp:
            sc1[1] = sp
        if approx:
            msc1 = dpf
            print("HERE", pf < sc1[0], "AND", pf > sc1[1])
            w0 = np.where(np.logical_or(pf < sc1[0], pf > sc1[1])
            )[0]  # levels outside required layer
            print("w0", w0)
            n0 = len(w0)
            print("n0", n0)
            if n0 > 0:
                print("msc1", msc1.shape, msc1)
                msc1[w0] = 0
        else:
            # used function to set up weights to do trapezoid integration over defined interval
            msc1 = setup_integration_matrix(pf, orig_xrange=sc1)

        msc1 = msc1 / np.sum(
            msc1
        )  # this normalises result to sub-column average
        print("msc1", msc1.shape, "msc", msc.shape, "msc[0, isc]", msc[0, isc])
        msc[:, isc] = msc1

    ###print("FINAL IRC_INTEGRATION_MATRIX VAR MSC IS:", msc)
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
    print("Example netcdf variable got, pf:", pf)
    do_ret = ncdf_get(fi, "do_retrieval", lun=lun, noclo=True)
    print("do_ret:", do_ret, np.isfortran(do_ret.array))
    print("pf:", pf.shape)  # (101,)

    # SLB: flake8 says this variable is not used, so comment out
    # dsn_ev = ncdf_get(fi, "dsxn_c", lun=lun, noclo=True, undo=True, ova=True)
    # csn_ev = ncdf_get(fi, "csxn_c", lun=lun, undo=True, ova=True)

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
    nret = len(iret)
    print("iret:", iret)
    print("nret:", nret)

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
    nz = len(pf)  # number of fine vertical levels
    nsc = len(scs[:, 0])  # number of subcolumns
    print("nz:", nz)
    print("nsc:", nsc)

    # SLB: flake8 says this variable is not used, so comment out
    nev = len(evecs[:, 0])  # number of Eigenvectors used to represent profile
    print("nev:", nev)

    # Interpolate the set of prior profiles in latitude
    print("ORIG SHAPE", c_ap_lnvmr.shape)  # (18, 101)
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
    print("STARTING ITERATION")
    for iret in np.arange(0, nret):
        # Get vmr from lnvmr
        print(iret, "Before", c_lnvmr.shape, c_lnvmr[iret,].shape)
        c_vmr = np.exp(c_lnvmr[iret,])  # undo log unit
        print("c_vmr:", c_vmr.shape)  #, c_vmr)
        # %%% shape: (1, 101)

        # Calculate weights which will compute the subcolumn via matrix multiply
        msc = irc_integration_matrix(scs, pf, sp[iret], nz, nsc)  #, approx=True)
        print("OVERALL msc:", msc.shape)  #, msc)
        # %%% shape: (101, 3)

        # Calculate the sub columns
        res = matrix_multiply(msc, c_vmr, atr=True)
        print("OVERALL res:", res.shape)  #, res)
        # %%% shape: (3, 1)

        c_sc[:, iret] = res.squeeze()
        print("OVERALL c_sc:", c_sc.shape)  #, c_sc)
        # %%% shape: (3, 5040)

        # Get corresponding prior profile and subcolumns
        # SLB IMPORTANT! c_ap_lnvmr is output from irc_interp_ap
        # and has shape (101, 5040) when that is called but above for
        # equivalent call c_lnvmr has shape '0 Before (5040, 101) (1, 101)'
        # so need to transpose overall!
        c_ap_lnvmr = c_ap_lnvmr.T
        print("BEFORE", c_ap_lnvmr.shape, c_ap_lnvmr[iret,].shape)
        c_ap_vmr = np.exp(c_ap_lnvmr[iret,])
        print("OVERALL c_ap_vmr:", c_ap_vmr.shape, c_ap_vmr)
        # %%% shape: (101,)

        print(msc.shape)
        c_ap_sc = matrix_multiply(msc, c_ap_vmr, atr=True)
        print("OVERALL msc:", c_ap_sc.shape)
        # %%% shape: (3,)

        # Make the square (nz,nz) AK array
        # IDL for first arg: ak_lnvmr(*,*,iret)
        # IMPORTANT! fix relative to original code provided by RS, updated:
        # In doing this I found an error in ims_rd_co4ak - the modified
        # version is in also in that directory.
        # Wrong line was…
        # ak_vmr_sq=ak_lnvmr*matrix_multiply(c_vmr,1d0/c_vmr)
        # now corrected to
        # ak_vmr_sq=ak_lnvmr_sq*matrix_multiply(c_vmr,1d0/c_vmr)
        print("UPTO args are:",
              ak_lnvmr[iret, :, :].shape, evecs.shape, pf.shape,
              sp[iret].shape, nz, nev  # final two are ints
              )
        ak_lnvmr_sq = irc_ak_exp(
            ak_lnvmr[iret, :, :], evecs, pf, sp[iret], nz, nev
        )
        print("OVERALL ak_lnvmr_sq:", ak_lnvmr_sq.shape)
        # %%% shape: (101, 101)

        # Convert from ln(vmr)/ln(vmr) to vmr/vmr
        ak_vmr_sq = ak_lnvmr_sq * matrix_multiply(c_vmr, 1.0 / c_vmr)
        print("OVERALL ak_vmr_sq:", ak_vmr_sq.shape)
        # %%% shape: (101, 101)

        # UPTO
        # Convert AK to d_sub-columns/d_vmr
        ak_sc[iret, 0, 0] = matrix_multiply(msc, ak_vmr_sq, atr=True)
        print("OVERALL ak_sc:", ak_sc.shape)
        # %%% shape:

        # Calculate a priori contribution so can layer apply AKs by doing simply
        # c_sc_model = c_apc + matrix_cultiply(ak_c,c_vmr_model)
        # for sub-columns, ak_c is non square and returned in units of
        # d_retrieved_subcolumn_average_vmr/d_true_profile_vmr
        c_apc_sc[iret, 0] = c_ap_sc - matrix_multiply(
            ak_sc[iret, :, :], c_ap_vmr
        )
        print("OVERALL c_apc_sc:", c_apc_sc.shape)
        # %%% shape:

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
