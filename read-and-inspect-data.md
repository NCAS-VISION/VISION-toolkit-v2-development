This document demonstrates reading in and inspecting data related to the VISION
project using cf-python. The work was done on a 'sci' node on JASMIN where a
Python environment with cf-python had been pre-loaded using the command
'module add jaspy'.

[slb93@sci4 workwith-test-flight-simulator]$ pwd
/home/users/slb93/vision-twine/workwith-test-flight-simulator
[slb93@sci4 workwith-test-flight-simulator]$ # This dir is a direct copy of Maria's
[slb93@sci4 workwith-test-flight-simulator]$ ls
Code  flight_simulator.py  Model_Input  Model_Output  Obs_Input
[slb93@sci4 workwith-test-flight-simulator]$ tree
.
├── Code
│   └── flight_simulator_v2.py
├── flight_simulator.py -> Code/flight_simulator_v2.py
├── Model_Input
│   ├── cu445a.po20170703.pp
│   ├── cu445a.po20170704.pp
│   ├── cu445a.po20170711.pp
│   ├── cu445a.po20170712.pp
│   ├── cu445a.po20170713.pp
│   ├── cu445a.po20170717.pp
│   ├── cu445a.po20170719.pp
│   ├── cu445a.po20170720.pp
│   ├── cu445a.po20170731.pp
│   ├── cu445a.pp20170703.pp
│   ├── cu445a.pp20170704.pp
│   ├── cu445a.pp20170711.pp
│   ├── cu445a.pp20170712.pp
│   ├── cu445a.pp20170713.pp
│   ├── cu445a.pp20170717.pp
│   ├── cu445a.pp20170719.pp
│   ├── cu445a.pp20170720.pp
│   └── cu445a.pp20170731.pp
├── Model_Output
│   ├── atmos_cu445a_1h_20170701-20170801_linp_stash51001.nc
│   ├── atmos_cu445a_1h_20170701-20170801_linp_stash51010.nc
│   ├── atmos_cu445a_1h_20170701-20170801_linz_stash34001.nc
│   └── Daily
└── Obs_Input
    ├── core_faam_20170703_c016_STANCO.nc
    ├── core_faam_20170704_c017_STANCO.nc
    ├── core_faam_20170704_c018_STANCO.nc
    ├── core_faam_20170711_c019_Oil.nc
    ├── core_faam_20170712_c020_ICARE_2_EMeRGe.nc
    ├── core_faam_20170713_c021_ICARE_2_EMeRGe.nc
    ├── core_faam_20170717_c022_EMeRGe.nc
    ├── core_faam_20170717_c023_EMeRGe.nc
    ├── core_faam_20170719_c024_EMeRGe.nc
    ├── core_faam_20170720_c025_EMeRGe.nc
    ├── core_faam_20170731_c026_CLARIFY.nc
    └── orography.pp -> /gws/nopw/j04/ukca_vol2/mrrusso/orography.pp

5 directories, 35 files
[slb93@sci4 workwith-test-flight-simulator]$ python
Python 3.10.8 | packaged by conda-forge | (main, Nov 22 2022, 08:23:14) [GCC 10.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cf
>>> cf.__version__
'3.15.1'
>>> # Model Inputs, call them 'mi' for short
>>> mi = cf.read("Model_Input/*.pp")
>>> mi
[<CF Field: id%UM_m01s34i001_vn1105(time(216), atmosphere_hybrid_height_coordinate(27), latitude(144), longitude(192)) 1>,
 <CF Field: id%UM_m01s34i010_vn1105(time(216), atmosphere_hybrid_height_coordinate(27), latitude(144), longitude(192)) 1>,
 <CF Field: id%UM_m01s51i001_vn1105(time(216), air_pressure(19), latitude(144), longitude(192)) 1>,
 <CF Field: id%UM_m01s51i010_vn1105(time(216), air_pressure(19), latitude(144), longitude(192)) 1>,
 <CF Field: id%UM_m01s51i999_vn1105(time(216), air_pressure(19), latitude(144), longitude(192))>]
>>> # To inspect a particular field from this field list
>>> print(mi[0])
/apps/jasmin/jaspy/mambaforge_envs/jaspy3.10/mf-22.11.1-4/envs/jaspy3.10-mf-22.11.1-4-r20230718/lib/python3.10/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Field: id%UM_m01s34i001_vn1105 (ncvar%UM_m01s34i001_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s34i001_vn1105(time(216), atmosphere_hybrid_height_coordinate(27), latitude(144), longitude(192)) 1
Cell methods    : time(216): point
Dimension coords: time(216) = [2017-07-03 01:00:00, ..., 2017-08-01 00:00:00] gregorian
                : atmosphere_hybrid_height_coordinate(27) = [0.003696857951581478, ..., 0.9648799300193787] 1
                : latitude(144) = [-89.375, ..., 89.375] degrees_north
                : longitude(192) = [0.9375, ..., 359.0625] degrees_east
Auxiliary coords: model_level_number(atmosphere_hybrid_height_coordinate(27)) = [1, ..., 27] 1
Coord references: standard_name:atmosphere_hybrid_height_coordinate
Domain ancils   : id%UM_atmosphere_hybrid_height_coordinate_a(atmosphere_hybrid_height_coordinate(27)) = [19.999998092651367, ..., 5219.99951171875] m
                : id%UM_atmosphere_hybrid_height_coordinate_b(atmosphere_hybrid_height_coordinate(27)) = [0.9977412819862366, ..., 0.4971233606338501] 1
>>> 
>>> # Model Outputs, call them 'mo' for short
>>> mo = cf.read("Model_Output/*.nc")
>>> mo
[<CF Field: air_pressure(ncdim%obs(155419)) hPa>,
 <CF Field: air_pressure(ncdim%obs(155419)) hPa>,
 <CF Field: air_pressure(ncdim%obs(155419)) hPa>,
 <CF Field: altitude(ncdim%obs(155419)) m>,
 <CF Field: altitude(ncdim%obs(155419)) m>,
 <CF Field: altitude(ncdim%obs(155419)) m>,
 <CF Field: latitude(ncdim%obs(155419)) degree_north>,
 <CF Field: latitude(ncdim%obs(155419)) degree_north>,
 <CF Field: latitude(ncdim%obs(155419)) degree_north>,
 <CF Field: longitude(ncdim%obs(155419)) degree_east>,
 <CF Field: longitude(ncdim%obs(155419)) degree_east>,
 <CF Field: longitude(ncdim%obs(155419)) degree_east>,
 <CF Field: long_name=O3 MASS MIXING RATIO AFTER TIMESTEP(ncdim%obs(155419)) 1>,
 <CF Field: long_name=O3 MASS MIXING RATIO ON PRESS LEVS(ncdim%obs(155419)) 1>,
 <CF Field: long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%obs(155419)) 1>,
 <CF Field: region(ncdim%obs(155419)) 1>,
 <CF Field: region(ncdim%obs(155419)) 1>,
 <CF Field: region(ncdim%obs(155419)) 1>,
 <CF Field: time(ncdim%obs(155419)) days since 1900-01-01 standard>,
 <CF Field: time(ncdim%obs(155419)) days since 1900-01-01 standard>,
 <CF Field: time(ncdim%obs(155419)) days since 1900-01-01 standard>]
>>> # To inspect a particular field from this field list
>>> print(mo[12])
Field: long_name=O3 MASS MIXING RATIO AFTER TIMESTEP (ncvar%m01s34i001)
-----------------------------------------------------------------------
Data            : long_name=O3 MASS MIXING RATIO AFTER TIMESTEP(ncdim%obs(155419)) 1

>>> print(mo[15])
Field: region (ncvar%region)
----------------------------
Data            : region(ncdim%obs(155419)) 1

>>> print(mo[18])
Field: time (ncvar%time)
------------------------
Data            : time(ncdim%obs(155419)) days since 1900-01-01 standard

>>> 
>>> # Observational Inputs, call them 'oi' for short
>>> oi = cf.read("Obs_Input/*.nc")
>>> oi
[<CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(11160)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(12741)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(13054)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(15764)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(9715)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(17504)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(12318)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(13225)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(18545)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(15663)) ppb>,
 <CF Field: mole_fraction_of_ozone_in_air(ncdim%obs(15730)) ppb>,
 <CF Field: air_pressure(ncdim%obs(11160)) hPa>,
 <CF Field: air_pressure(ncdim%obs(12741)) hPa>,
 <CF Field: air_pressure(ncdim%obs(13054)) hPa>,
 <CF Field: air_pressure(ncdim%obs(15764)) hPa>,
 <CF Field: air_pressure(ncdim%obs(9715)) hPa>,
 <CF Field: air_pressure(ncdim%obs(17504)) hPa>,
 <CF Field: air_pressure(ncdim%obs(12318)) hPa>,
 <CF Field: air_pressure(ncdim%obs(13225)) hPa>,
 <CF Field: air_pressure(ncdim%obs(18545)) hPa>,
 <CF Field: air_pressure(ncdim%obs(15663)) hPa>,
 <CF Field: air_pressure(ncdim%obs(15730)) hPa>,
 <CF Field: altitude(ncdim%obs(11160)) m>,
 <CF Field: altitude(ncdim%obs(12741)) m>,
 <CF Field: altitude(ncdim%obs(13054)) m>,
 <CF Field: altitude(ncdim%obs(15764)) m>,
 <CF Field: altitude(ncdim%obs(9715)) m>,
 <CF Field: altitude(ncdim%obs(17504)) m>,
 <CF Field: altitude(ncdim%obs(12318)) m>,
 <CF Field: altitude(ncdim%obs(13225)) m>,
 <CF Field: altitude(ncdim%obs(18545)) m>,
 <CF Field: altitude(ncdim%obs(15663)) m>,
 <CF Field: altitude(ncdim%obs(15730)) m>,
 <CF Field: long_name=campaign(ncdim%obs(11160)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(12741)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(13054)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(15764)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(9715)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(17504)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(12318)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(13225)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(18545)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(15663)) 1>,
 <CF Field: long_name=campaign(ncdim%obs(15730)) 1>,
 <CF Field: latitude(ncdim%obs(11160)) degree_north>,
 <CF Field: latitude(ncdim%obs(12741)) degree_north>,
 <CF Field: latitude(ncdim%obs(13054)) degree_north>,
 <CF Field: latitude(ncdim%obs(15764)) degree_north>,
 <CF Field: latitude(ncdim%obs(9715)) degree_north>,
 <CF Field: latitude(ncdim%obs(17504)) degree_north>,
 <CF Field: latitude(ncdim%obs(12318)) degree_north>,
 <CF Field: latitude(ncdim%obs(13225)) degree_north>,
 <CF Field: latitude(ncdim%obs(18545)) degree_north>,
 <CF Field: latitude(ncdim%obs(15663)) degree_north>,
 <CF Field: latitude(ncdim%obs(15730)) degree_north>,
 <CF Field: longitude(ncdim%obs(11160)) degree_east>,
 <CF Field: longitude(ncdim%obs(12741)) degree_east>,
 <CF Field: longitude(ncdim%obs(13054)) degree_east>,
 <CF Field: longitude(ncdim%obs(15764)) degree_east>,
 <CF Field: longitude(ncdim%obs(9715)) degree_east>,
 <CF Field: longitude(ncdim%obs(17504)) degree_east>,
 <CF Field: longitude(ncdim%obs(12318)) degree_east>,
 <CF Field: longitude(ncdim%obs(13225)) degree_east>,
 <CF Field: longitude(ncdim%obs(18545)) degree_east>,
 <CF Field: longitude(ncdim%obs(15663)) degree_east>,
 <CF Field: longitude(ncdim%obs(15730)) degree_east>,
 <CF Field: time(ncdim%obs(11160)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(12741)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(13054)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(15764)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(9715)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(17504)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(12318)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(13225)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(18545)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(15663)) days since 1900-01-01 00:00:00 standard>,
 <CF Field: time(ncdim%obs(15730)) days since 1900-01-01 00:00:00 standard>]
>>> # To inspect a particular field from this field list
>>> print(oi[0])
Field: mole_fraction_of_ozone_in_air (ncvar%O3_TECO)
----------------------------------------------------
Data            : mole_fraction_of_ozone_in_air(ncdim%obs(11160)) ppb

>>> print(oi[10])
Field: mole_fraction_of_ozone_in_air (ncvar%O3_TECO)
----------------------------------------------------
Data            : mole_fraction_of_ozone_in_air(ncdim%obs(15730)) ppb

>>> print(oi[20])
Field: air_pressure (ncvar%air_pressure)
----------------------------------------
Data            : air_pressure(ncdim%obs(15663)) hPa

>>> 
>>> # From here, you can access fields via mi[N], mo[L] or oi[M] for relevant
>>> # integer N, L, M in range and apply cf operations to view, analyse or
>>> # edit the fields.
>>> 
>>> # END
