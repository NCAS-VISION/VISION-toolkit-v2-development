#!/usr/bin/env python

"""
IMS_RD_CO4AK 

Read IMS L2 file to construct CO sub-columns and averaging kernels only 
(cut down from ims_rd_basic to serve as simple e.g. code for Vision project) 

From the resulting structure "s" averaging kernels can be applied to model 
c_vmr_model (ppmv on 101 fine grid levels) to obtain sub-columns accounting 
for the retrieval averaging kernel, c_sc_model (in ppmv) via 

c_sc_model = s.c_apc + matrix_cultiply(s.ak,c_vmr_model) 

If required to apply to model profiles on a different grid then the AKs will 
need to be (a) normalised by dividing (in the fine vertical grid dimension) 
by the pressure differences between the fine grid (dpf) 
(b) interpolated in that dimension to the new model pressure grid. 
(c) multiplied by the layer pressure differences of the model grid. 
Pressure differences,dp can be obtained by 
	dp1=pf(1:nz-1)-pf(0:nz-2) 
	dpf=([0,dp1]+[dp1,0])/2 

PARAMETERS 
	 FILE	Name of IMS L2 file to read 

KEYWORDS 
	APPROX	Compute sub-columns approximately 
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
a(0,*) ->	a[:,0]
a(*,1:*) ->	a[1:,]

Assuming ak_lnvmr(*,*,iret) therefore ->
but need to check. ChatGPT says:
In IDL, a[*, *, 0] selects a 2D slice from a 3D array a. The * acts as a wildcard, meaning "include all elements along this dimension." Specifically:

    The first * selects all elements along the first dimension (rows).
    The second * selects all elements along the second dimension (columns).
    The 0 selects the first slice (index 0) along the third dimension (depth).

This is equivalent to indexing a 3D NumPy array in Python as:

a[:, :, 0]

BUT I think it is instead a[0, :, :] somehow - due to reversal w.r.t Python order
specified.
9.
10.

"""


import os
import time
import numpy as np


# START OF NEW FUNCS TO MAP IDL PROCEDURE NAMES TO EQUIVALENT PYTHON
# FUNCTIONALITY USING E.G. CF-PYTHON


def ncdf_get(fi, varname, lun=False, noclo=False, undo=False, ova=False):
    """Implement IDL code 'ncdf_get' function in Python."""
    pass


def setup_linear(lats_ap, latitude, i0, i1, w0, w1, vl=False):
    """Implement IDL code 'TODO' function in Python."""
    pass


def setup_integration_matrix():
    """Implement IDL code 'TODO' function in Python."""
    pass


def iasimhs_vsx2cov():
    """Implement IDL code 'TODO' function in Python."""
    pass


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


def sqrt_nz():
    """Implement IDL code 'sqrt_nz' function in Python."""
    pass


def iasimhs_sx_exp():
    """Implement IDL code 'iasimhs_sx_exp' function in Python."""
    pass


# END OF IDL CONVERSION
# START OF ORIGINAL IDL CODE CONVERTED, INCLUDING USE OF ABOVE NEW FUNCS

DEFAULT_FILENAME = "ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20110718141155z_20110718155058z_000_049-v1000.nc"


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
    setup_linear(lats_ap, latitude, i0, i1, w0, w1, vl=True)
    np = len(latitude)
    nz = len(xap[0,])  # IDL: xap(*,0)
    xapi = np.zeros((nz, np), Float)  # IDL: dblarr(nz, np)

    for ip in np.arange(0, np):
        # IDL: xapi(0, ip) = xap(*,i0(ip)) * w0(ip) + xap(*,i1(ip)) * w1(ip)
        xapi[ip, 0] = xap[i0[ip]] * w0[ip] + xap[i1[ip]] * w1[ip]

    return xapi


def irc_ak_exp(ak, evecs, pf, sp, nz, nev):
    """CONV DONE
    Recreate full averaging kernel from IASI-MHS state vector representation

    Inputs
        AK	Ak for state vector representation, wrt 51 "true levels" (every other RTTOV level)
        EVECS	Vectors to map to 101 RTTOV levels from state vector
        PF	Fine grid pressures / hPa
        SP	Surface pressure / hPa
        NZ 	Number of fine vertical levels
        NEV	Number of eigenvectors
    """
    # Index of PF used to store true grid perturbations in file
    idx = lindgen(nz / 2 + 1) * 2
    pfs = pf[idx]
    setup_linear(pfs, pf, i0, i1, w0, w1, vl=True)
    akt = ak.T
    ak_101 = np.zeros((nz, nev), Float)  # IDL: dblarr(nz, nev)

    for iev in range(nev):  # Interpolate to full grid
        # IDL: ak_101(0, iev) = akt(i0, iev) * w0 + akt(i1, iev) * w1
        ak_101[iev, 0] = akt[iev, i0] * w0 + akt[iev, i1] * w1

    ak_101 = matrix_multiply(evecs, ak_101, btr=True)

    # Make sure AK is zero below surface pressure
    (ws,) = np.where(pf > sp, ns)  # TODO SLB is the comma / unpacking needed?
    if ns > 0:  # Set levels below surface to 0
        ak_101[ws,] = 0

    return ak_101


def irc_integration_matrix(scs, pf, sp, nz, nsc, approx=approx):
    """CONV DONE
    (No docstring in corresponding IDL procedure).
    """
    msc = np.zeros((nz, nsc), Float)  # IDL: dblarr(nz, nsc)

    if approx:
        # Approximate method uses the just the fine layer pressure differences between
        # the defined bounds as weights.
        # Full method treats the layer bounds more exactly, by also including interpolation
        # from the fine grid to the defined pressure bounds (and surface pressure).
        dp1 = pf[1 : nz - 1] - pf[0 : nz - 2]  # IDL: =pf(1:nz-1)-pf(0:nz-2)
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


def ims_rd_co4ak(fi, approx=approx):
    """
    Main function.
    """
    # Default filename if one not defined
    # (this one co-located with FAAM over Candian fire)
    if len(fi) == 0:
        fi = DEAFULT_FILENAME

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
    dsn_ev = ncdf_get(fi, "dsxn_c", lun=lun, noclo=True, undo=True, ova=True)
    csn_ev = ncdf_get(fi, "csxn_c", lun=lun, undo=True, ova=True)

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
        + sensingtime_msec / (1000.0 * 60.0 * 60.0 * 24.0)
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
    nev = len(evecs[:, 0])  # number of Eigenvectors used to represent profile

    # Interpolate the set of prior profiles in latitude
    c_ap_lnvmr = irc_interp_ap(c_ap_lnvmr, lat)

    # Expand the total and noise  covariance matrices to full vertical grid (nz,nz) with units (ln(ppmv))^2
    sx_ev = iasimhs_vsx2cov(csx_ev, diag=dsx_ev)  # nev,nev matrix
    sx_lnvmr = iasimhs_sx_exp(sx_ev, evecs)  # nz,nz matrix
    sn_ev = iasimhs_vsx2cov(csn_ev, diag=dsn_ev)  # nev,nev matrix
    sn_lnvmr = iasimhs_sx_exp(sn_ev, evecs)  # nz,nz matrix

    # Make arrays to hold the results which are neeeded for model comparisons
    c_sc = np.zeros(
        (nsc, nret), Float
    )  # IDL: dblarr(nsc, nret)  # CO sub-column average mixing ratios / ppmv
    ak_sc = np.zeros(
        (nsc, nz, nret), Float
    )  # IDL: dblarr(nsc, nz, nret)  # Averaging kernels for retrieved sub-column wrt true profile vmr / ppmv/ppmv
    sx_sc = np.zeros(
        (nsc, nsc, nret), Float
    )  # IDL: dblarr(nsc, nsc, nret)  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs / ppmv^2
    sn_sc = np.zeros(
        (nsc, nsc, nret), Float
    )  # IDL: dblarr(nsc, nsc, nret)  # Noise covariance  / ppmv^2
    c_apc_sc = np.zeros(
        (nsc, nret), Float
    )  # IDL: dblarr(nsc, nret)  # A priori contribution to each sub-column / ppmv
    c_err_sc = np.zeros(
        (nsc, nret), Float
    )  # IDL: dblarr(nsc, nret)  # Estimated total standard deviation of retrieved sub-cols / ppmv
    c_noise_sc = np.zeros(
        (nsc, nret), Float
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
        ak_lnvmr_sq = irc_ak_exp(
            ak_lnvmr[iret, :, :], evecs, pf, sp[iret], nz, nev
        )

        # Convert from ln(vmr)/ln(vmr) to vmr/vmr
        ak_vmr_sq = ak_lnvmr * matrix_multiply(c_vmr, 1.0 / c_vmr)

        # Convert AK to d_sub-columns/d_vmr
        ak_sc[iret, 0, 0] = matrix_multiply(msc, ak_vmr_sq, atr=True)

        # Calculate a priori contribution so can layer apply AKs by doing simply
        # c_sc_model = c_apc + matrix_cultiply(ak_c,c_vmr_model)
        # for sub-columns, ak_c is non square and returned in units of d_retrieved_subcolumn_average_vmr/d_true_profile_vmr
        c_apc_sc[iret, 0] = c_ap_sc - matrix_multiply(
            ak_sc[iret, :, :], c_ap_vmr
        )

        # SLB UPTO
        # Now deal with errors...
        # convert matrices to vmr from ln(vmr)  (error in ln(x) is fractional error in x)
        vmr_sq = matrix_multiply(c_vmr, c_vmr)
        sx_vmr = sx_lnvmr[iret, :, :] * vmr_sq
        sn_vmr = sn_lnvmr[iret, :, :] * vmr_sq

        # Convert these to (nsc,nsc) matrices for the sub-columns
        sx_sc[iret, 0, 0] = matrix_multiply(
            matrix_multiply(sx_vmr, msc), msc, atr=True
        )
        sn_sc[iret, 0, 0] = matrix_multiply(
            matrix_multiply(sx_vmr, msc), msc, atr=True
        )

        # Just get sqrt-diagonals of the covariances (Estimated total random error std.deviation and the noise std.deviation)
        c_err_sc[iret, 0] = sqrt_nz(f_diagonal(sx_sc[iret, :, :]))
        c_noise_sc[iret, 0] = sqrt_nz(f_diagonal(sn_sc[iret, :, :]))

    # Make result structure
    # Everything given for sub columns so drop the _sc in the tag names
    s = {
        pf: pf,  # Fine grid pressures / hPa (nz = number of fine grid levels)
        scs: scs,  # Definition of the sub-column bounds / hPa (2,nsc = number of sub-columns)
        lat: lat,  # Latitude (np = number of retrievals in the file)
        lon: lon,  # Longitude (np)
        jday: jday,  # Julian day  (np)
        sp: sp,  # Surface pressure / hPa (np)
        c: c_sc,  # CO sub-column average mixing ratios (nsc,np) / ppmv
        ak: ak_sc,  # Averaging kernels for retrieved sub-column wrt true profile vmr (nsc,nz,np) / ppmv/ppmv
        sx: sx_sc,  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs (nsc,nsc) / ppmv^2
        sn: sn_sc,  # Noise covariance (nsc,nsc) / ppmv^2
        c_apc: c_apc_sc,  # A priori contribution to each sub-column (nsc,np) / ppmv
        c_err: c_err_sc,  # Estimated total standard deviation of retrieved sub-cols (nsc,np) / ppmv
        c_noise: c_noise_sc,  # Estimated noise standard deviation (nsc,np) / ppmv
    }

    return s
