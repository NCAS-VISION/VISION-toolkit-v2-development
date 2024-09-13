from wrf import getvar, extract_vars
from  netCDF4 import Dataset
from statistics import mean, median
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools
import xarray as xr


path = '/home/force-blencathra/blencathra/uk/data/2024052412/wrfout_d03_2024-05-26*'
all_files = glob.glob(path)

datasets = [Dataset(file) for file in all_files]
# Surface pressure p_s
psfc = extract_vars(datasets, varnames='PSFC', timeidx=None)['PSFC'][:]/100
# Pressure at top of model domain p_t
pt = extract_vars(datasets, varnames='P_TOP', timeidx=None)['P_TOP']/100
# B, function of eta coord (znu) from WRF coords,
# substitutes directly for B function in 'atmosphere hybrid sigma 
# pressure coordinate'
b = extract_vars(datasets, varnames='C3H', timeidx=None)['C3H'][:]
# Eta, vertical coord
znu = extract_vars(datasets, varnames='ZNU', timeidx=None)['ZNU'][:]
# Horizontal coords
xlat= extract_vars(datasets, varnames='XLAT', timeidx=None)['XLAT']
xlong = extract_vars(datasets, varnames='XLONG', timeidx=None)['XLONG']
# Temperature
t = extract_vars(datasets, varnames='T', timeidx=None)['T']
# Reference sea level pressure p_0
p0 = 1013.25
# A, function of eta (znu), derived for AHSP coords
A = (znu - b + (1 - znu) * (pt/p0))

ds = xr.Dataset()
ds['A'] = A[0]
ds['B'] = b[0]
ds['B'].attrs = {}
ds['ps'] = psfc
ds['p0'] = p0
ds['T'] = t
ds['T'].attrs = {}
ds['ZNU'] = znu
ds['ZNU'].attrs = {}
ds['XLAT'] = xlat
ds['XLAT'].attrs = {}
ds['XLONG'] = xlong
ds['XLONG'].attrs = {}
ds.to_netcdf('wrf-press-test.nc')

