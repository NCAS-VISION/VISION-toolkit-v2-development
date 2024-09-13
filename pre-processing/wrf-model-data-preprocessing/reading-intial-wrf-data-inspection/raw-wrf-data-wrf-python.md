# Attempts using 'wrf-python' to process WRF data towards compliance

## 0. Libraries required

```python
>>> import wrf
>>> import netCDF4
>>> import os
>>> import sys
>>> import xarray as xr
>>> import cf
```

## 1. Basis

To process all datasets using netCDF4 (as used by wrf-python), list all file
names in the directory ready to add them to a list in Dataset form (note: use the
setup indicated in `raw-wrf-data-cf-aggregate.md` for the directory location and
Python environment, else get a similar environment).

```python
>>> datadir = os.listdir(".")
>>> datadir
['all_d01_aggregate.nc', 'core_faam_20230711.nc', 'test-sadie.nc', 'wrfout_d01_2023-07-10_12:00:00', 'wrfout_d01_2023-07-10_13:00:00', 'wrfout_d01_2023-07-10_14:00:00', 'wrfout_d01_2023-07-10_15:00:00', 'wrfout_d01_2023-07-10_16:00:00', 'wrfout_d01_2023-07-10_17:00:00', 'wrfout_d01_2023-07-10_18:00:00', 'wrfout_d01_2023-07-10_19:00:00', 'wrfout_d01_2023-07-10_20:00:00', 'wrfout_d01_2023-07-10_21:00:00', 'wrfout_d01_2023-07-10_22:00:00', 'wrfout_d01_2023-07-10_23:00:00', 'wrfout_d01_2023-07-11_00:00:00', 'wrfout_d01_2023-07-11_01:00:00', 'wrfout_d01_2023-07-11_02:00:00', 'wrfout_d01_2023-07-11_03:00:00', 'wrfout_d01_2023-07-11_04:00:00', 'wrfout_d01_2023-07-11_05:00:00', 'wrfout_d01_2023-07-11_06:00:00', 'wrfout_d01_2023-07-11_07:00:00', 'wrfout_d01_2023-07-11_08:00:00', 'wrfout_d01_2023-07-11_09:00:00', 'wrfout_d01_2023-07-11_10:00:00', 'wrfout_d01_2023-07-11_11:00:00', 'wrfout_d01_2023-07-11_12:00:00', 'wrfout_d01_2023-07-11_13:00:00', 'wrfout_d01_2023-07-11_14:00:00', 'wrfout_d01_2023-07-11_15:00:00', 'wrfout_d01_2023-07-11_16:00:00', 'wrfout_d01_2023-07-11_17:00:00', 'wrfout_d01_2023-07-11_18:00:00', 'wrfout_d01_2023-07-11_19:00:00', 'wrfout_d01_2023-07-11_20:00:00', 'wrfout_d01_2023-07-11_21:00:00', 'wrfout_d01_2023-07-11_22:00:00', 'wrfout_d01_2023-07-11_23:00:00', 'wrfout_d01_2023-07-12_00:00:00', 'wrfout_d01_2023-07-12_01:00:00', 'wrfout_d01_2023-07-12_02:00:00', 'wrfout_d01_2023-07-12_03:00:00', 'wrfout_d01_2023-07-12_04:00:00', 'wrfout_d01_2023-07-12_05:00:00', 'wrfout_d01_2023-07-12_06:00:00', 'wrfout_d01_2023-07-12_07:00:00', 'wrfout_d01_2023-07-12_08:00:00', 'wrfout_d01_2023-07-12_09:00:00', 'wrfout_d01_2023-07-12_10:00:00', 'wrfout_d01_2023-07-12_11:00:00', 'wrfout_d01_2023-07-12_12:00:00', 'wrfout_d01_2023-07-12_13:00:00', 'wrfout_d01_2023-07-12_14:00:00', 'wrfout_d01_2023-07-12_15:00:00', 'wrfout_d01_2023-07-12_16:00:00', 'wrfout_d01_2023-07-12_17:00:00', 'wrfout_d01_2023-07-12_18:00:00', 'wrfout_d01_2023-07-12_19:00:00', 'wrfout_d01_2023-07-12_20:00:00', 'wrfout_d01_2023-07-12_21:00:00', 'wrfout_d01_2023-07-12_22:00:00', 'wrfout_d01_2023-07-12_23:00:00', 'wrfout_d01_2023-07-13_00:00:00', 'wrfout_d02_2023-07-10_12:00:00', 'wrfout_d02_2023-07-10_13:00:00', 'wrfout_d02_2023-07-10_14:00:00', 'wrfout_d02_2023-07-10_15:00:00', 'wrfout_d02_2023-07-10_16:00:00', 'wrfout_d02_2023-07-10_17:00:00', 'wrfout_d02_2023-07-10_18:00:00', 'wrfout_d02_2023-07-10_19:00:00', 'wrfout_d02_2023-07-10_20:00:00', 'wrfout_d02_2023-07-10_21:00:00', 'wrfout_d02_2023-07-10_22:00:00', 'wrfout_d02_2023-07-10_23:00:00', 'wrfout_d02_2023-07-11_00:00:00', 'wrfout_d02_2023-07-11_01:00:00', 'wrfout_d02_2023-07-11_02:00:00', 'wrfout_d02_2023-07-11_03:00:00', 'wrfout_d02_2023-07-11_04:00:00', 'wrfout_d02_2023-07-11_05:00:00', 'wrfout_d02_2023-07-11_06:00:00', 'wrfout_d02_2023-07-11_07:00:00', 'wrfout_d02_2023-07-11_08:00:00', 'wrfout_d02_2023-07-11_09:00:00', 'wrfout_d02_2023-07-11_10:00:00', 'wrfout_d02_2023-07-11_11:00:00', 'wrfout_d02_2023-07-11_12:00:00', 'wrfout_d02_2023-07-11_13:00:00', 'wrfout_d02_2023-07-11_14:00:00', 'wrfout_d02_2023-07-11_15:00:00', 'wrfout_d02_2023-07-11_16:00:00', 'wrfout_d02_2023-07-11_17:00:00', 'wrfout_d02_2023-07-11_18:00:00', 'wrfout_d02_2023-07-11_19:00:00', 'wrfout_d02_2023-07-11_20:00:00', 'wrfout_d02_2023-07-11_21:00:00', 'wrfout_d02_2023-07-11_22:00:00', 'wrfout_d02_2023-07-11_23:00:00', 'wrfout_d02_2023-07-12_00:00:00', 'wrfout_d02_2023-07-12_01:00:00', 'wrfout_d02_2023-07-12_02:00:00', 'wrfout_d02_2023-07-12_03:00:00', 'wrfout_d02_2023-07-12_04:00:00', 'wrfout_d02_2023-07-12_05:00:00', 'wrfout_d02_2023-07-12_06:00:00', 'wrfout_d02_2023-07-12_07:00:00', 'wrfout_d02_2023-07-12_08:00:00', 'wrfout_d02_2023-07-12_09:00:00', 'wrfout_d02_2023-07-12_10:00:00', 'wrfout_d02_2023-07-12_11:00:00', 'wrfout_d02_2023-07-12_12:00:00', 'wrfout_d02_2023-07-12_13:00:00', 'wrfout_d02_2023-07-12_14:00:00', 'wrfout_d02_2023-07-12_15:00:00', 'wrfout_d02_2023-07-12_16:00:00', 'wrfout_d02_2023-07-12_17:00:00', 'wrfout_d02_2023-07-12_18:00:00', 'wrfout_d02_2023-07-12_19:00:00', 'wrfout_d02_2023-07-12_20:00:00', 'wrfout_d02_2023-07-12_21:00:00', 'wrfout_d02_2023-07-12_22:00:00', 'wrfout_d02_2023-07-12_23:00:00', 'wrfout_d02_2023-07-13_00:00:00', 'wrfout_d03_2023-07-10_12:00:00', 'wrfout_d03_2023-07-10_13:00:00', 'wrfout_d03_2023-07-10_14:00:00', 'wrfout_d03_2023-07-10_15:00:00', 'wrfout_d03_2023-07-10_16:00:00', 'wrfout_d03_2023-07-10_17:00:00', 'wrfout_d03_2023-07-10_18:00:00', 'wrfout_d03_2023-07-10_19:00:00', 'wrfout_d03_2023-07-10_20:00:00', 'wrfout_d03_2023-07-10_21:00:00', 'wrfout_d03_2023-07-10_22:00:00', 'wrfout_d03_2023-07-10_23:00:00', 'wrfout_d03_2023-07-11_00:00:00', 'wrfout_d03_2023-07-11_01:00:00', 'wrfout_d03_2023-07-11_02:00:00', 'wrfout_d03_2023-07-11_03:00:00', 'wrfout_d03_2023-07-11_04:00:00', 'wrfout_d03_2023-07-11_05:00:00', 'wrfout_d03_2023-07-11_06:00:00', 'wrfout_d03_2023-07-11_07:00:00', 'wrfout_d03_2023-07-11_08:00:00', 'wrfout_d03_2023-07-11_09:00:00', 'wrfout_d03_2023-07-11_10:00:00', 'wrfout_d03_2023-07-11_11:00:00', 'wrfout_d03_2023-07-11_12:00:00', 'wrfout_d03_2023-07-11_13:00:00', 'wrfout_d03_2023-07-11_14:00:00', 'wrfout_d03_2023-07-11_15:00:00', 'wrfout_d03_2023-07-11_16:00:00', 'wrfout_d03_2023-07-11_17:00:00', 'wrfout_d03_2023-07-11_18:00:00', 'wrfout_d03_2023-07-11_19:00:00', 'wrfout_d03_2023-07-11_20:00:00', 'wrfout_d03_2023-07-11_21:00:00', 'wrfout_d03_2023-07-11_22:00:00', 'wrfout_d03_2023-07-11_23:00:00', 'wrfout_d03_2023-07-12_00:00:00', 'wrfout_d03_2023-07-12_01:00:00', 'wrfout_d03_2023-07-12_02:00:00', 'wrfout_d03_2023-07-12_03:00:00', 'wrfout_d03_2023-07-12_04:00:00', 'wrfout_d03_2023-07-12_05:00:00', 'wrfout_d03_2023-07-12_06:00:00', 'wrfout_d03_2023-07-12_07:00:00', 'wrfout_d03_2023-07-12_08:00:00', 'wrfout_d03_2023-07-12_09:00:00', 'wrfout_d03_2023-07-12_10:00:00', 'wrfout_d03_2023-07-12_11:00:00', 'wrfout_d03_2023-07-12_12:00:00', 'wrfout_d03_2023-07-12_13:00:00', 'wrfout_d03_2023-07-12_14:00:00', 'wrfout_d03_2023-07-12_15:00:00', 'wrfout_d03_2023-07-12_16:00:00', 'wrfout_d03_2023-07-12_17:00:00', 'wrfout_d03_2023-07-12_18:00:00', 'wrfout_d03_2023-07-12_19:00:00', 'wrfout_d03_2023-07-12_20:00:00', 'wrfout_d03_2023-07-12_21:00:00', 'wrfout_d03_2023-07-12_22:00:00', 'wrfout_d03_2023-07-12_23:00:00', 'wrfout_d03_2023-07-13_00:00:00']
>>> # Separate into lists split by domain
>>> wrflist_1 = [netCDF4.Dataset(file) for file in datadir if file.startswith("wrfout_d01")]
>>> wrflist_2 = [netCDF4.Dataset(file) for file in datadir if file.startswith("wrfout_d02")]
>>> wrflist_3 = [netCDF4.Dataset(file) for file in datadir if file.startswith("wrfout_d03")]
```

## 2. Using wrf-python and xarray to attempt to extract some vertical coordinates

Do a `getvar` as follows for all three domains, separately (can't do together or in as same dataset due to
different dimensions):

```python
>>> # Core operation: a 'getvar' on the 'z' (height) variable across a concatenation of all times
>>> z_cat_1 = wrf.getvar(wrflist_1, "z", timeidx=wrf.ALL_TIMES, method="cat")
>>> z_cat_2 = wrf.getvar(wrflist_2, "z", timeidx=wrf.ALL_TIMES, method="cat")
>>> z_cat_3 = wrf.getvar(wrflist_3, "z", timeidx=wrf.ALL_TIMES, method="cat")
>>> z_cat_1
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
>>> z_cat_2
<xarray.DataArray 'height' (Time: 61, bottom_top: 50, south_north: 300,
                            west_east: 250)> Size: 915MB
array([[[[   25.356077,    25.357845,    25.35962 , ...,   119.49241 ,
            123.99215 ,   128.98744 ],
         [   25.353632,    25.355284,    25.357492, ...,   117.874374,
            121.99189 ,   126.719284],
         [   25.35109 ,    25.353193,    25.35534 , ...,   116.22594 ,
            119.81695 ,   124.10868 ],
         ...,
         [   24.93509 ,    24.936573,    24.936762, ...,    25.246788,
             25.251822,    25.256693],
         [   24.932936,    24.934643,    24.934704, ...,    25.249073,
             25.254538,    25.25907 ],
         [   24.93061 ,    24.932016,    24.932734, ...,    25.251242,
             25.256907,    25.26148 ]],

        [[   83.12916 ,    83.133896,    83.136696, ...,   178.60654 ,
            183.10944 ,   188.08546 ],
         [   83.119385,    83.12462 ,    83.12831 , ...,   177.01254 ,
            181.08325 ,   185.7927  ],
         [   83.10874 ,    83.11511 ,    83.11977 , ...,   175.45528 ,
            178.91423 ,   183.15234 ],
...
         [20253.379   , 20253.254   , 20253.105   , ..., 20254.242   ,
          20254.668   , 20255.025   ],
         [20253.496   , 20253.357   , 20253.193   , ..., 20254.555   ,
          20254.945   , 20255.268   ],
         [20253.607   , 20253.436   , 20253.271   , ..., 20254.848   ,
          20255.18    , 20255.521   ]],

        [[20713.979   , 20714.06    , 20714.143   , ..., 20703.453   ,
          20703.617   , 20703.797   ],
         [20714.01    , 20713.89    , 20713.959   , ..., 20703.312   ,
          20703.525   , 20703.672   ],
         [20714.01    , 20713.959   , 20714.002   , ..., 20703.143   ,
          20703.383   , 20703.557   ],
         ...,
         [20719.018   , 20718.898   , 20718.758   , ..., 20714.35    ,
          20714.744   , 20715.068   ],
         [20719.135   , 20718.994   , 20718.836   , ..., 20714.646   ,
          20714.996   , 20715.283   ],
         [20719.242   , 20719.07    , 20718.904   , ..., 20714.918   ,
          20715.21    , 20715.516   ]]]], dtype=float32)
Coordinates:
    XLONG     (south_north, west_east) float32 300kB -10.79 -10.74 ... 4.571
    XLAT      (south_north, west_east) float32 300kB 49.07 49.07 ... 60.0 59.99
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
>>> z_cat_3
<xarray.DataArray 'height' (Time: 61, bottom_top: 50, south_north: 300,
                            west_east: 425)> Size: 2GB
array([[[[   25.372759,    25.372913,    25.373579, ...,    25.514746,
             25.51089 ,    25.506945],
         [   25.37249 ,    25.372608,    25.373257, ...,    25.510063,
             25.506346,    25.502556],
         [   25.372232,    25.372835,    25.372948, ...,    25.504889,
             25.50132 ,    25.497686],
         ...,
         [   25.304062,    25.303196,    25.302866, ...,   143.69699 ,
            141.89676 ,   140.2108  ],
         [   25.302937,    25.302073,    25.30121 , ...,   146.16078 ,
            144.51962 ,   143.04057 ],
         [   25.301826,    25.300945,    25.300083, ...,   148.96654 ,
            147.55946 ,   146.31947 ]],

        [[   83.17254 ,    83.173096,    83.1747  , ...,    83.717804,
             83.70569 ,    83.69327 ],
         [   83.17165 ,    83.17209 ,    83.17363 , ...,    83.7023  ,
             83.69063 ,    83.67871 ],
         [   83.17028 ,    83.17166 ,    83.1721  , ...,    83.68583 ,
             83.674644,    83.663216],
...
         [20243.334   , 20243.3     , 20243.266   , ..., 20242.846   ,
          20242.852   , 20242.867   ],
         [20243.295   , 20243.256   , 20243.22    , ..., 20242.87    ,
          20242.883   , 20242.889   ],
         [20243.258   , 20243.215   , 20243.166   , ..., 20242.883   ,
          20242.904   , 20242.914   ]],

        [[20706.197   , 20706.215   , 20706.23    , ..., 20698.844   ,
          20698.871   , 20698.9     ],
         [20706.174   , 20706.195   , 20706.215   , ..., 20698.76    ,
          20698.791   , 20698.826   ],
         [20706.154   , 20706.17    , 20706.19    , ..., 20698.693   ,
          20698.719   , 20698.75    ],
         ...,
         [20703.605   , 20703.58    , 20703.55    , ..., 20699.795   ,
          20699.76    , 20699.744   ],
         [20703.576   , 20703.545   , 20703.514   , ..., 20699.797   ,
          20699.773   , 20699.75    ],
         [20703.549   , 20703.514   , 20703.473   , ..., 20699.795   ,
          20699.785   , 20699.76    ]]]], dtype=float32)
Coordinates:
    XLONG     (south_north, west_east) float32 510kB -5.862 -5.851 ... -1.063
    XLAT      (south_north, west_east) float32 510kB 49.83 49.83 ... 52.02 52.02
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
```

Noting that you can't add these all to one xarray `Dataset`, add them to separate `Dataset`s to write out to netCDF:

```python
>>> ds = xr.Dataset({"z_cat_1": z_cat_1, "z_cat_2": z_cat_2, "z_cat_3": z_cat_3})Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/dataset.py", line 693, in __init__
    variables, coord_names, dims, indexes, _ = merge_data_and_coords(
                                               ^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/dataset.py", line 422, in merge_data_and_coords
    return merge_core(
           ^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/merge.py", line 692, in merge_core
    aligned = deep_align(
              ^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/alignment.py", line 946, in deep_align
    aligned = align(
              ^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/alignment.py", line 882, in align
    aligner.align()
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/alignment.py", line 575, in align
    self.assert_unindexed_dim_sizes_equal()
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/xarray/core/alignment.py", line 476, in assert_unindexed_dim_sizes_equal
    raise ValueError(
ValueError: cannot reindex or align along dimension 'south_north' because of conflicting dimension sizes: {179, 300}
>>> # Fine, write out separately:
>>> ds_1 = xr.Dataset({"z_cat_1": z_cat_1})
>>> ds_2 = xr.Dataset({"z_cat_2": z_cat_2})
>>> ds_3 = xr.Dataset({"z_cat_3": z_cat_3})
```

Now note an issue, which https://github.com/pydata/xarray/issues/2252 covers with a suggested (but not ideal - for a workaround at least let's use it for now):

```python
>>> ds_1_cf = xr.decode_cf(ds_1, decode_coords="all")
>>> ds_2_cf = xr.decode_cf(ds_2, decode_coords="all")
>>> ds_3_cf = xr.decode_cf(ds_3, decode_coords="all")
>>> 
>>> ds_1
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
    z_cat_1   (Time, bottom_top, south_north, west_east) float32 304MB 25.72 ...
>>> ds_1_cf.to_netcdf("z_cat_1_cf.nc")
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
>>> 
>>> # Trying to use this solution from:
>>> # https://github.com/NCAR/wrf-python/issues/91#issuecomment-516317353
>>> def write_xarray_to_netcdf(xarray_array, output_path,mode='w', format='NETCDF4', group=None, engine=None,
...                            encoding=None):
...     """writes and xarray in a netcdf format outputfile
...     Uses the xarray typical for wrf-python. The projection objects are transformed into strings
...     to be able to use them as netcdf attributes
...     :param xarray_array: xarray.DataArray
...     :param output_path: str
...     :param format: 'NETCDF4', 'NETCDF4_CLASSIC', 'NETCDF3_64BIT' or 'NETCDF3_CLASSIC'
...                     default: 'NETCDF4'
...     :param group: str, default None
...     :param engine: 'netcdf4', 'scipy' or 'h5netcdf'
...     :param encoding: dict, default: None
...     """
...     xarray_array_out = xarray_array.copy(deep=True)
...     # coordinates are extracted from variable
...     del xarray_array_out.attrs['coordinates']
...     # wrf-python projection object cannot be processed
...     xarray_array_out.attrs['projection'] = str(xarray_array_out.attrs['projection'])
...     xarray_array_out.to_netcdf(path=output_path, mode=mode, format=format, group=group, engine=engine, encoding=encoding)
... 
>>> write_xarray_to_netcdf(ds_1_cf, "d01_z_cat_cf.nc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 16, in write_xarray_to_netcdf
KeyError: 'coordinates'
>>> 
>>> # Seems like the only option w/ xarray at the moment to write out is
>>> # as advised in https://github.com/pydata/xarray/issues/2252
>>> del ds_1_cf["z_cat_1"].attrs["projection"]
>>> del ds_2_cf["z_cat_2"].attrs["projection"]
>>> del ds_3_cf["z_cat_3"].attrs["projection"]
>>> 
>>> ds_1_cf.to_netcdf("z_cat_d01_cf.nc")
>>> ds_2_cf.to_netcdf("z_cat_d02_cf.nc")
>>> ds_3_cf.to_netcdf("z_cat_d03_cf.nc")
```

The last three lines write these out to netCDF which can go on to inspect with cf-python.

```python
>>> # Now interpret the above datasets with cf to compare
>>> f = cf.read("z_cat_*_cf.nc")
>>> f
[<CF Field: ncvar%datetime(ncdim%Time(61)) hours since 2023-07-10 12:00:00 proleptic_gregorian>,
 <CF Field: ncvar%datetime(ncdim%Time(61)) hours since 2023-07-10 12:00:00 proleptic_gregorian>,
 <CF Field: ncvar%datetime(ncdim%Time(61)) hours since 2023-07-10 12:00:00 proleptic_gregorian>,
 <CF Field: ncvar%z_cat_1(ncdim%Time(61), ncdim%bottom_top(50), ncdim%south_north(179), ncdim%west_east(139)) m>,
 <CF Field: ncvar%z_cat_2(ncdim%Time(61), ncdim%bottom_top(50), ncdim%south_north(300), ncdim%west_east(250)) m>,
 <CF Field: ncvar%z_cat_3(ncdim%Time(61), ncdim%bottom_top(50), ncdim%south_north(300), ncdim%west_east(425)) m>]
>>> As an example from the more useful half of these (the second half), we have:
>>> print(f[-1])
Field: ncvar%z_cat_3 (ncvar%z_cat_3)
------------------------------------
Data            : ncvar%z_cat_3(ncdim%Time(61), ncdim%bottom_top(50), ncdim%south_north(300), ncdim%west_east(425)) m
Dimension coords: ncvar%Time(ncdim%Time(61)) = [2023-07-10 12:00:00, ..., 2023-07-13 00:00:00] proleptic_gregorian
Auxiliary coords: ncvar%XLONG(ncdim%south_north(300), ncdim%west_east(425)) = [[-5.862396240234375, ..., -1.062896728515625]]
                : ncvar%XLAT(ncdim%south_north(300), ncdim%west_east(425)) = [[49.825931549072266, ..., 52.0231819152832]]
                : ncvar%XTIME(ncdim%Time(61)) = [0.0, ..., 3600.0]
>>> # Fields f[3] to f[5] are OK forms for the z/vertical coordinate, but
>>> # still not what we need because the XTIME coordinates are just
>>> # context-less values, with the time in the separate fields f[0] to
>>> # f[2], and the grid mapping information from the original file is
>>> # in a weird format that xarray and cf can't properly interpret.
>>> 
>>> exit()
```
