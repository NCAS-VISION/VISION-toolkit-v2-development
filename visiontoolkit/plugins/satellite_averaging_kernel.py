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
"""


import os
import time
import numpy as np


DEFAULT_FILENAME = (
    'ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20110718141155z_20110718155058z_000_049-v1000.nc'
)


def irc_interp_ap(xap, latitude):
    """
    Interpolate prior in 18 latitude bands to latitude of measurement 
    Inputs 
          xap    prior values 
          latitude Latitudes 
          SP      Surface pressure (only needed if e60 set) 
    """
    # Latitude grid associated with the prior values 
    lats_ap = dindgen(18) * 10 - 85d0
    setup_linear, lats_ap, double(latitude), i0, i1, w0, w1, /vl 
    w0 = double(w0) 
    w1 = double(w1) 
    np = len(latitude) 
    nz = len(xap(*, 0)) 
    xapi = dblarr(nz, np)

    for ip in np.arange(0l, np): 
        xapi(0, ip) = xap(*, i0(ip)) * w0(ip) + xap(*, i1(ip)) * w1(ip)

    return xapi


def irc_ak_exp(ak, evecs, pf, sp, nz, nev):
    """
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
    pfs = pf(idx)
    setup_linear, pfs, pf, i0, i1, w0, w1, /vl
    akt = transpose(ak)
    ak_101 = dblarr(nz,nev)

    for iev in range(nev):  # Interpolate to full grid 
        ak_101(0, iev) = akt(i0, iev) * w0 + akt(i1, iev) * w1

    ak_101 = matrix_multiply(evecs,ak_101, /btr)  # Map to rttov levels 
    # Make sure AK is zero below surface pressure 
    ws, = np.where(pf > sp, ns) 
    if ns > 0:  # Set levels below surface to 0 
        ak_101(*, ws) = 0

    return ak_101 


def irc_integration_matrix(scs, pf, sp, nz, nsc, approx=approx):
    """TODO."""
    msc = dblarr(nz,nsc)

    if keyword_set(approx): 
        # Approximate method uses the just the fine layer pressure differences between 
        # the defined bounds as weights. 
        # Full method treats the layer bounds more exactly, by also including interpolation 
        # from the fine grid to the defined pressure bounds (and surface pressure). 
        dp1 = pf(1: nz-1) - pf(0: nz-2) 
        dpf = ([0d0, dp1] + [dp1, 0]) / 2

    for isc in range(nsc):
        # Pressure levels of this layer in ascending order
        sc1 = scs([1, 0], isc)  
        # if lower bound indicated as 1000 or lower bound below surface then truncate layer to the surface 
        if sc1(1) == 1000 or sc1(1) > sp: 
            sc1(1) = sp 
        if keyword_set(approx): 
            msc1 = dpf 
            w0, = np.where(pf < sc1(0) or pf > sc1(1), n0)  # levels outside required layer 
            if n0 > 0 :
                msc1(w0) = 0 
        else: 
            # used function to set up weights to do trapezoid integration over defined interval 
            msc1 = setup_integration_matrix(pf, xran=sc1)

        msc1 = msc1 / np.sum(msc1, /pres)  # this normalises result to sub-column average 
        msc(0, isc) = msc1

    return msc 


def ims_rd_co4ak(fi, approx=approx):
    """Main function."""
    # Default filename if one not defined 
    # (this one co-located with FAAM over Candian fire) 
    if len(fi) == 0:
        fi = DEAFULT_FILENAME

    # Define subcolumns as pressure bounds in hpa of 3 layers 
    # (total, 0-6km, 6-12km column amounts) 
    # 1000hPa is treated as surface pressure (see irc_subcol) 
    scs = [[1000d0, 0.01], $  # i.e. total column 
    [1000d0, 450d0], $  # i.e. surface-6km (approx) 
    [450d0, 170d0]]  # i.e. 6-12km (approx)

    # Read necessary info from the file 
    # ncdf_get will apply scale_factor and add offset (/undo keyword) 
    # /ova makes it just return the values without any attributes 
    pf = ncdf_get(fi,'p',lun=lun, /noclo, /undo, /ova) 
    :_ret = (ncdf_get(fi, 'do_retrieval', lun=lun, /noclo)).value 
    lat = ncdf_get(fi, 'latitude', lun=lun, /noclo, /undo, /ova) 
    lon = ncdf_get(fi, 'longitude',lun=lun, /noclo, /undo, /ova) 
    sensingtime_msec = ncdf_get(fi, 'sensingtime_msec', lun=lun, /noclo, /ova) 
    sensingtime_day = ncdf_get(fi, 'sensingtime_day', lun=lun, /noclo, /ova) 
    c_ap_lnvmr = ncdf_get(fi, 'c_ap', lun=lun, /noclo, /undo, /ova) 
    evecs = ncdf_get(fi, 'evecs_c', lun=lun, /noclo, /undo, /ova) 
    c_lnvmr = ncdf_get(fi, 'c', lun=lun, /noclo, /undo, /ova) 
    sp = ncdf_get(fi, 'sp', lun=lun, /noclo, /undo, /ova) 
    ak_lnvmr = ncdf_get(fi, 'ak_c', lun=lun, /noclo, /undo, /ova) 
    dsx_ev = ncdf_get(fi, 'dsx_c', lun=lun, /noclo, /undo, /ova) 
    csx_ev = ncdf_get(fi, 'csx_c', lun=lun, /noclo, /undo, /ova) 
    dsn_ev = ncdf_get(fi, 'dsxn_c', lun=lun, /noclo, /undo, /ova) 
    csn_ev = ncdf_get(fi, 'csxn_c', lun=lun, /undo, /ova)

    # Get indices of retrieved scenes 
    # - code assumes all retrieved scenes have AK and covariance 
    # - this is true for all current ims files for co and o3 and minor gases (but not h2o or T) 
    iret, = np.where(do_ret, nret) 
    if nret == 0: 
        message, 'No retrievals in file!'

    # Convert time to julian day 
    jday = sensingtime_day + sensingtime_msec/1000d0/60d0/60d0/24d0+2451544.5d0

    # Subset lat/lon/time/sp to the pixels for which retrieval exist
    lat = lat(iret) 
    lon = lon(iret) 
    jday = jday(iret) 
    sp = sp(iret)

    # Get dimensions 
    nz = len(pf)  # number of fine vertical levels 
    nsc = len(scs(0, *))  # number of subcolumns 
    nev = len(evecs(0, *))  # number of Eigenvectors used to represent profile

    # Interpolate the set of prior profiles in latitude 
    c_ap_lnvmr = irc_interp_ap(c_ap_lnvmr, lat)

    # Expand the total and noise  covariance matrices to full vertical grid (nz,nz) with units (ln(ppmv))^2 
    sx_ev = iasimhs_vsx2cov(csx_ev, diag=dsx_ev)  # nev,nev matrix 
    sx_lnvmr = iasimhs_sx_exp(sx_ev, evecs)  # nz,nz matrix 
    sn_ev = iasimhs_vsx2cov(csn_ev, diag=dsn_ev)  # nev,nev matrix 
    sn_lnvmr = iasimhs_sx_exp(sn_ev, evecs)  # nz,nz matrix

    # Make arrays to hold the results which are neeeded for model comparisons 
    c_sc = dblarr(nsc, nret)  # CO sub-column average mixing ratios / ppmv 
    ak_sc = dblarr(nsc, nz, nret)  # Averaging kernels for retrieved sub-column wrt true profile vmr / ppmv/ppmv 
    sx_sc = dblarr(nsc, nsc, nret)  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs / ppmv^2 
    sn_sc = dblarr(nsc, nsc, nret)  # Noise covariance  / ppmv^2 
    c_apc_sc = dblarr(nsc, nret)  # A priori contribution to each sub-column / ppmv 
    c_err_sc = dblarr(nsc, nret)  # Estimated total standard deviation of retrieved sub-cols / ppmv 
    c_noise_sc = dblarr(nsc, nret)  # Estimated noise standard deviation / ppmv

    # Loop individual retrievals 
    for iret in np.arange(0l, nret): 
        # Get vmr from lnvmr 
        c_vmr = exp(c_lnvmr(*, iret))  # undo log unit

        # Calculate weights which will compute the subcolumn via matrix multiply 
        msc = irc_integration_matrix(scs, pf, sp(iret), nz, nsc, approx=approx)

        # Calculate the sub columns 
        c_sc(0, iret) = matrix_multiply(msc, c_vmr, /atr)

        # Get corresponding prior profile and subcolumns 
        c_ap_vmr = exp(c_ap_lnvmr(*, iret)) 
        c_ap_sc = matrix_multiply(msc, c_ap_vmr, /atr)

        # Make the square (nz,nz) AK array 
        ak_lnvmr_sq = irc_ak_exp(ak_lnvmr(*, *, iret), evecs, pf, sp(iret), nz, nev)

        # Convert from ln(vmr)/ln(vmr) to vmr/vmr 
        ak_vmr_sq = ak_lnvmr * matrix_multiply(c_vmr, 1d0/c_vmr)

        # Convert AK to d_sub-columns/d_vmr 
        ak_sc(0,0,iret) = matrix_multiply(msc, ak_vmr_sq, /atr) 

        # Calculate a priori contribution so can layer apply AKs by doing simply 
        # c_sc_model = c_apc + matrix_cultiply(ak_c,c_vmr_model) 
        # for sub-columns, ak_c is non square and returned in units of d_retrieved_subcolumn_average_vmr/d_true_profile_vmr 
        c_apc_sc(0,iret) = c_ap_sc-matrix_multiply(ak_sc(*, *, iret), c_ap_vmr)

        # Now deal with errors... 
        # convert matrices to vmr from ln(vmr)  (error in ln(x) is fractional error in x) 
        vmr_sq = matrix_multiply(c_vmr, c_vmr) 
        sx_vmr = sx_lnvmr(*, *, iret) * vmr_sq 
        sn_vmr = sn_lnvmr(*, *, iret) * vmr_sq

        # Convert these to (nsc,nsc) matrices for the sub-columns 
        sx_sc(0, 0, iret) = matrix_multiply(matrix_multiply(sx_vmr, msc), msc, /atr) 
        sn_sc(0, 0, iret) = matrix_multiply(matrix_multiply(sx_vmr, msc), msc, /atr)

        # Just get sqrt-diagonals of the covariances (Estimated total random error std.deviation and the noise std.deviation) 
        c_err_sc(0, iret) = sqrt_nz(f_diagonal(sx_sc(*, *, iret))) 
        c_noise_sc(0, iret) = sqrt_nz(f_diagonal(sn_sc(*, *, iret)))

    # Make result structure 
    # Everything given for sub columns so drop the _sc in the tag names 
    s = {
        pf: pf, $  # Fine grid pressures / hPa (nz = number of fine grid levels) 
        scs: scs, $  # Definition of the sub-column bounds / hPa (2,nsc = number of sub-columns) 
        lat: lat, $  # Latitude (np = number of retrievals in the file) 
        lon: lon, $  # Longitude (np) 
        jday: jday, $  # Julian day  (np) 
        sp: sp, $  # Surface pressure / hPa (np) 
        c: c_sc, $  # CO sub-column average mixing ratios (nsc,np) / ppmv 
        ak: ak_sc, $  # Averaging kernels for retrieved sub-column wrt true profile vmr (nsc,nz,np) / ppmv/ppmv 
        sx: sx_sc, $  # Total (Noise + smoothing) covariance for sub-col.avg.vmrs (nsc,nsc) / ppmv^2 
        sn: sn_sc, $  # Noise covariance (nsc,nsc) / ppmv^2 
        c_apc: c_apc_sc, $  # A priori contribution to each sub-column (nsc,np) / ppmv 
        c_err: c_err_sc, $  # Estimated total standard deviation of retrieved sub-cols (nsc,np) / ppmv 
        c_noise: c_noise_sc  # Estimated noise standard deviation (nsc,np) / ppmv
    }

    return s 
