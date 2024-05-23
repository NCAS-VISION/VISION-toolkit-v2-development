# Using 'wrf-python' and `xarray` to process WRF data towards compliance

## 1. Basis

To process all datasets using netCDF4 (as used by wrf-python), list all file
names in the directory ready to add them to a list in Dataset form (note: use the
setup indicated in `raw-wrf-data-cf-aggregate.md` for the directory location and
Python environment, else get a similar environment).

```python
>>> import os
>>> import sys
>>> datadir = os.listdir(".")
>>> datadir
['all_d01_aggregate.nc', 'core_faam_20230711.nc', 'test-sadie.nc', 'wrfout_d01_2023-07-10_12:00:00', 'wrfout_d01_2023-07-10_13:00:00', 'wrfout_d01_2023-07-10_14:00:00', 'wrfout_d01_2023-07-10_15:00:00', 'wrfout_d01_2023-07-10_16:00:00', 'wrfout_d01_2023-07-10_17:00:00', 'wrfout_d01_2023-07-10_18:00:00', 'wrfout_d01_2023-07-10_19:00:00', 'wrfout_d01_2023-07-10_20:00:00', 'wrfout_d01_2023-07-10_21:00:00', 'wrfout_d01_2023-07-10_22:00:00', 'wrfout_d01_2023-07-10_23:00:00', 'wrfout_d01_2023-07-11_00:00:00', 'wrfout_d01_2023-07-11_01:00:00', 'wrfout_d01_2023-07-11_02:00:00', 'wrfout_d01_2023-07-11_03:00:00', 'wrfout_d01_2023-07-11_04:00:00', 'wrfout_d01_2023-07-11_05:00:00', 'wrfout_d01_2023-07-11_06:00:00', 'wrfout_d01_2023-07-11_07:00:00', 'wrfout_d01_2023-07-11_08:00:00', 'wrfout_d01_2023-07-11_09:00:00', 'wrfout_d01_2023-07-11_10:00:00', 'wrfout_d01_2023-07-11_11:00:00', 'wrfout_d01_2023-07-11_12:00:00', 'wrfout_d01_2023-07-11_13:00:00', 'wrfout_d01_2023-07-11_14:00:00', 'wrfout_d01_2023-07-11_15:00:00', 'wrfout_d01_2023-07-11_16:00:00', 'wrfout_d01_2023-07-11_17:00:00', 'wrfout_d01_2023-07-11_18:00:00', 'wrfout_d01_2023-07-11_19:00:00', 'wrfout_d01_2023-07-11_20:00:00', 'wrfout_d01_2023-07-11_21:00:00', 'wrfout_d01_2023-07-11_22:00:00', 'wrfout_d01_2023-07-11_23:00:00', 'wrfout_d01_2023-07-12_00:00:00', 'wrfout_d01_2023-07-12_01:00:00', 'wrfout_d01_2023-07-12_02:00:00', 'wrfout_d01_2023-07-12_03:00:00', 'wrfout_d01_2023-07-12_04:00:00', 'wrfout_d01_2023-07-12_05:00:00', 'wrfout_d01_2023-07-12_06:00:00', 'wrfout_d01_2023-07-12_07:00:00', 'wrfout_d01_2023-07-12_08:00:00', 'wrfout_d01_2023-07-12_09:00:00', 'wrfout_d01_2023-07-12_10:00:00', 'wrfout_d01_2023-07-12_11:00:00', 'wrfout_d01_2023-07-12_12:00:00', 'wrfout_d01_2023-07-12_13:00:00', 'wrfout_d01_2023-07-12_14:00:00', 'wrfout_d01_2023-07-12_15:00:00', 'wrfout_d01_2023-07-12_16:00:00', 'wrfout_d01_2023-07-12_17:00:00', 'wrfout_d01_2023-07-12_18:00:00', 'wrfout_d01_2023-07-12_19:00:00', 'wrfout_d01_2023-07-12_20:00:00', 'wrfout_d01_2023-07-12_21:00:00', 'wrfout_d01_2023-07-12_22:00:00', 'wrfout_d01_2023-07-12_23:00:00', 'wrfout_d01_2023-07-13_00:00:00', 'wrfout_d02_2023-07-10_12:00:00', 'wrfout_d02_2023-07-10_13:00:00', 'wrfout_d02_2023-07-10_14:00:00', 'wrfout_d02_2023-07-10_15:00:00', 'wrfout_d02_2023-07-10_16:00:00', 'wrfout_d02_2023-07-10_17:00:00', 'wrfout_d02_2023-07-10_18:00:00', 'wrfout_d02_2023-07-10_19:00:00', 'wrfout_d02_2023-07-10_20:00:00', 'wrfout_d02_2023-07-10_21:00:00', 'wrfout_d02_2023-07-10_22:00:00', 'wrfout_d02_2023-07-10_23:00:00', 'wrfout_d02_2023-07-11_00:00:00', 'wrfout_d02_2023-07-11_01:00:00', 'wrfout_d02_2023-07-11_02:00:00', 'wrfout_d02_2023-07-11_03:00:00', 'wrfout_d02_2023-07-11_04:00:00', 'wrfout_d02_2023-07-11_05:00:00', 'wrfout_d02_2023-07-11_06:00:00', 'wrfout_d02_2023-07-11_07:00:00', 'wrfout_d02_2023-07-11_08:00:00', 'wrfout_d02_2023-07-11_09:00:00', 'wrfout_d02_2023-07-11_10:00:00', 'wrfout_d02_2023-07-11_11:00:00', 'wrfout_d02_2023-07-11_12:00:00', 'wrfout_d02_2023-07-11_13:00:00', 'wrfout_d02_2023-07-11_14:00:00', 'wrfout_d02_2023-07-11_15:00:00', 'wrfout_d02_2023-07-11_16:00:00', 'wrfout_d02_2023-07-11_17:00:00', 'wrfout_d02_2023-07-11_18:00:00', 'wrfout_d02_2023-07-11_19:00:00', 'wrfout_d02_2023-07-11_20:00:00', 'wrfout_d02_2023-07-11_21:00:00', 'wrfout_d02_2023-07-11_22:00:00', 'wrfout_d02_2023-07-11_23:00:00', 'wrfout_d02_2023-07-12_00:00:00', 'wrfout_d02_2023-07-12_01:00:00', 'wrfout_d02_2023-07-12_02:00:00', 'wrfout_d02_2023-07-12_03:00:00', 'wrfout_d02_2023-07-12_04:00:00', 'wrfout_d02_2023-07-12_05:00:00', 'wrfout_d02_2023-07-12_06:00:00', 'wrfout_d02_2023-07-12_07:00:00', 'wrfout_d02_2023-07-12_08:00:00', 'wrfout_d02_2023-07-12_09:00:00', 'wrfout_d02_2023-07-12_10:00:00', 'wrfout_d02_2023-07-12_11:00:00', 'wrfout_d02_2023-07-12_12:00:00', 'wrfout_d02_2023-07-12_13:00:00', 'wrfout_d02_2023-07-12_14:00:00', 'wrfout_d02_2023-07-12_15:00:00', 'wrfout_d02_2023-07-12_16:00:00', 'wrfout_d02_2023-07-12_17:00:00', 'wrfout_d02_2023-07-12_18:00:00', 'wrfout_d02_2023-07-12_19:00:00', 'wrfout_d02_2023-07-12_20:00:00', 'wrfout_d02_2023-07-12_21:00:00', 'wrfout_d02_2023-07-12_22:00:00', 'wrfout_d02_2023-07-12_23:00:00', 'wrfout_d02_2023-07-13_00:00:00', 'wrfout_d03_2023-07-10_12:00:00', 'wrfout_d03_2023-07-10_13:00:00', 'wrfout_d03_2023-07-10_14:00:00', 'wrfout_d03_2023-07-10_15:00:00', 'wrfout_d03_2023-07-10_16:00:00', 'wrfout_d03_2023-07-10_17:00:00', 'wrfout_d03_2023-07-10_18:00:00', 'wrfout_d03_2023-07-10_19:00:00', 'wrfout_d03_2023-07-10_20:00:00', 'wrfout_d03_2023-07-10_21:00:00', 'wrfout_d03_2023-07-10_22:00:00', 'wrfout_d03_2023-07-10_23:00:00', 'wrfout_d03_2023-07-11_00:00:00', 'wrfout_d03_2023-07-11_01:00:00', 'wrfout_d03_2023-07-11_02:00:00', 'wrfout_d03_2023-07-11_03:00:00', 'wrfout_d03_2023-07-11_04:00:00', 'wrfout_d03_2023-07-11_05:00:00', 'wrfout_d03_2023-07-11_06:00:00', 'wrfout_d03_2023-07-11_07:00:00', 'wrfout_d03_2023-07-11_08:00:00', 'wrfout_d03_2023-07-11_09:00:00', 'wrfout_d03_2023-07-11_10:00:00', 'wrfout_d03_2023-07-11_11:00:00', 'wrfout_d03_2023-07-11_12:00:00', 'wrfout_d03_2023-07-11_13:00:00', 'wrfout_d03_2023-07-11_14:00:00', 'wrfout_d03_2023-07-11_15:00:00', 'wrfout_d03_2023-07-11_16:00:00', 'wrfout_d03_2023-07-11_17:00:00', 'wrfout_d03_2023-07-11_18:00:00', 'wrfout_d03_2023-07-11_19:00:00', 'wrfout_d03_2023-07-11_20:00:00', 'wrfout_d03_2023-07-11_21:00:00', 'wrfout_d03_2023-07-11_22:00:00', 'wrfout_d03_2023-07-11_23:00:00', 'wrfout_d03_2023-07-12_00:00:00', 'wrfout_d03_2023-07-12_01:00:00', 'wrfout_d03_2023-07-12_02:00:00', 'wrfout_d03_2023-07-12_03:00:00', 'wrfout_d03_2023-07-12_04:00:00', 'wrfout_d03_2023-07-12_05:00:00', 'wrfout_d03_2023-07-12_06:00:00', 'wrfout_d03_2023-07-12_07:00:00', 'wrfout_d03_2023-07-12_08:00:00', 'wrfout_d03_2023-07-12_09:00:00', 'wrfout_d03_2023-07-12_10:00:00', 'wrfout_d03_2023-07-12_11:00:00', 'wrfout_d03_2023-07-12_12:00:00', 'wrfout_d03_2023-07-12_13:00:00', 'wrfout_d03_2023-07-12_14:00:00', 'wrfout_d03_2023-07-12_15:00:00', 'wrfout_d03_2023-07-12_16:00:00', 'wrfout_d03_2023-07-12_17:00:00', 'wrfout_d03_2023-07-12_18:00:00', 'wrfout_d03_2023-07-12_19:00:00', 'wrfout_d03_2023-07-12_20:00:00', 'wrfout_d03_2023-07-12_21:00:00', 'wrfout_d03_2023-07-12_22:00:00', 'wrfout_d03_2023-07-12_23:00:00', 'wrfout_d03_2023-07-13_00:00:00']
```

## 2. Using wrf-python and xarray to attempt to extract some vertical coordinates

Do the following for all three domains:

```python
>>> VAR_OF_INTEREST = "z"
>>> wrflist_1 = [netCDF4.Dataset(file) for file in datadir if file.startswith("wrfout_d01")]
>>> var_cat = getvar(wrflist_1, VAR_OF_INTEREST, timeidx=wrf.ALL_TIMES, method="cat")
>>> var_cat
<xarray.DataArray 'height' (Time: 61, bottom_top: 50, south_north: 179,
                            west_east: 139)> Size: 304MB
array([[[[   25.717283,    25.712137,    25.703722, ...,    26.407124,
             26.406319,    26.412611],
         [   25.734287,    25.729204,    25.725092, ...,    26.394024,
             26.390318,    26.393867],
         [   25.756775,    25.75674 ,    25.750471, ...,    26.366976,
             26.368664,    26.378977],
         ...,
         [ 2494.801   ,  2510.2651  ,  2510.8958  , ...,   467.355   ,
            542.69617 ,   576.5188  ],
         [ 2438.032   ,  2466.4321  ,  2493.0686  , ...,   379.76865 ,
            413.70346 ,   454.85715 ],
         [ 2376.294   ,  2406.047   ,  2439.0173  , ...,   226.00238 ,
            248.77585 ,   328.42172 ]],

        [[   84.298676,    84.2837  ,    84.25945 , ...,    86.56548 ,
             86.579056,    86.62281 ],
         [   84.35692 ,    84.34054 ,    84.32718 , ...,    86.52171 ,
             86.51143 ,    86.563934],
         [   84.42908 ,    84.4275  ,    84.40828 , ...,    86.43502 ,
             86.44531 ,    86.503334],
...
         [20402.055   , 20401.832   , 20401.096   , ..., 20374.67    ,
          20374.973   , 20374.342   ],
         [20400.547   , 20403.236   , 20403.762   , ..., 20374.941   ,
          20375.729   , 20378.492   ],
         [20402.912   , 20406.828   , 20409.23    , ..., 20373.395   ,
          20374.244   , 20376.105   ]],

        [[20690.45    , 20689.29    , 20688.875   , ..., 20721.732   ,
          20721.379   , 20723.46    ],
         [20694.727   , 20693.57    , 20693.451   , ..., 20725.227   ,
          20723.967   , 20723.504   ],
         [20697.725   , 20695.83    , 20695.832   , ..., 20727.738   ,
          20726.627   , 20725.225   ],
         ...,
         [20871.807   , 20870.996   , 20869.969   , ..., 20848.955   ,
          20849.465   , 20848.432   ],
         [20870.002   , 20872.33    , 20872.588   , ..., 20849.314   ,
          20849.982   , 20852.38    ],
         [20872.123   , 20875.846   , 20878.092   , ..., 20847.695   ,
          20848.336   , 20849.934   ]]]], dtype=float32)
Coordinates:
    XLONG     (south_north, west_east) float32 100kB -22.84 -22.63 ... 20.62
    XLAT      (south_north, west_east) float32 100kB 36.98 37.03 ... 69.81 69.76
    XTIME     (Time) float64 488B 0.0 60.0 120.0 ... 3.48e+03 3.54e+03 3.6e+03
  * Time      (Time) datetime64[ns] 488B 2023-07-10T12:00:00 ... 2023-07-13
    datetime  (Time) datetime64[ns] 488B 2023-07-10T12:00:00 ... 2023-07-13
Dimensions without coordinates: bottom_top, south_north, west_east
Attributes:
    FieldType:    104
    MemoryOrder:  XYZ
    description:  model height - [MSL] (mass grid)
    units:        m
    stagger:      
    coordinates:  XLONG XLAT XTIME
    projection:   LambertConformal(stand_lon=-2.5, moad_cen_lat=55.0000076293...
>>> import xarray as xr
>>> ds = xr.Dataset({VAR_OF_INTEREST + "_cat": var_cat})
>>> ds
<xarray.Dataset> Size: 304MB
Dimensions:   (south_north: 179, west_east: 139, Time: 61, bottom_top: 50)
Coordinates:
    XLONG     (south_north, west_east) float32 100kB -22.84 -22.63 ... 20.62
    XLAT      (south_north, west_east) float32 100kB 36.98 37.03 ... 69.81 69.76
    XTIME     (Time) float64 488B 0.0 60.0 120.0 ... 3.48e+03 3.54e+03 3.6e+03
  * Time      (Time) datetime64[ns] 488B 2023-07-10T12:00:00 ... 2023-07-13
    datetime  (Time) datetime64[ns] 488B 2023-07-10T12:00:00 ... 2023-07-13
Dimensions without coordinates: south_north, west_east, bottom_top
Data variables:
    z_cat     (Time, bottom_top, south_north, west_east) float32 304MB 25.72 ...
```

Now note an issue, which https://github.com/pydata/xarray/issues/2252 covers with a suggested (but not ideal - for a workaround at least let's use it for now):

```python
>>> ds.to_netcdf(VAR_OF_INTEREST + "_cat_1.nc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/dataset.py", line 2298, in to_netcdf
    return to_netcdf(  # type: ignore  # mypy cannot resolve the overloads:(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/backends/api.py", line 1292, in to_netcdf
    _validate_attrs(dataset, invalid_netcdf=invalid_netcdf and engine == "h5netcdf")
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/backends/api.py", line 208, in _validate_attrs
    check_attr(k, v, valid_types)
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/backends/api.py", line 195, in check_attr
    raise TypeError(
TypeError: Invalid value for attr 'projection': LambertConformal(stand_lon=-2.5, moad_cen_lat=55.00000762939453, truelat1=60.0, truelat2=50.0, pole_lat=90.0, pole_lon=0.0). For serialization to netCDF files, its value must be of one of the following types: str, Number, ndarray, number, list, tuple
>>> # See https://github.com/pydata/xarray/issues/2252 for this issue
>>> # Solution it suggests is:
>>> del ds[VAR_OF_INTEREST + "_cat"].attrs['projection']
>>> # Optionally can also do: ds_cf = xr.decode_cf(ds) but not sure it has any effect here
>>> ds_cf.to_netcdf(VAR_OF_INTEREST + "_cat_d01.nc")
```

THe last line writes this out to netCDF which can go on to inspect with cf-python.

TODO add to report findings from reading this in with cf-python.


### TODO: do for next three domains

TODO
