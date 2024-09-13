# Further WRF data CF compliance pre-processing

To make the WRF data more compliant so that it can be better processed by tools such as cf-python and by our
VISION toolkit end-to-end script:

* To get time coordinates distinguished, we need to add some standard names to differentiate between the time
  constructs with a full array of times and one with just the first time value
* To allow the 'X' and 'Y' axes to be recognised, we need the standard lat and lon units to be assigned to those.

See below for how to do a lot of this fixing up:

```
>>> import cf
>>> f = cf.read("../wrf-vert-coords/e2e-ready-wrf.nc")
>>> f
[<CF Field: ncvar%T(ncdim%Time(61), atmosphere_hybrid_sigma_pressure_coordinate(50), ncdim%south_north(179), ncdim%west_east(139))>]
>>> f = f[0]
>>> f.construct("ncdim%Time")
<CF DomainAxis: size(61)>
>>> f.construct("ncvar%Time")
<CF DimensionCoordinate: ncvar%Time(61) hours since 2023-07-10 12:00:00 proleptic_gregorian>
>>> f.construct("ncvar%Time").standard_name = "time"
>>> f.construct("ncvar%Time")
<CF DimensionCoordinate: time(61) hours since 2023-07-10 12:00:00 proleptic_gregorian>
>>> print(f)
Field: ncvar%T (ncvar%T)
------------------------
Data            : ncvar%T(time(61), atmosphere_hybrid_sigma_pressure_coordinate(50), ncdim%south_north(179), ncdim%west_east(139))
Dimension coords: time(61) = [2023-07-10 12:00:00, ..., 2023-07-13 00:00:00] proleptic_gregorian
                : atmosphere_hybrid_sigma_pressure_coordinate(50) = [0.9969073534011841, ..., 0.0019467439269647002]
                : ncvar%datetime(key%domainaxis4(1)) = [2023-07-10 12:00:00] proleptic_gregorian
Auxiliary coords: ncvar%XLAT(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[36.98377990722656, ..., 69.75613403320312]]]
                : ncvar%XLONG(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[-22.838226318359375, ..., 20.62158203125]]]
                : ncvar%XTIME(time(61)) = [0.0, ..., 3600.0]
Coord references: standard_name:atmosphere_hybrid_sigma_pressure_coordinate
Domain ancils   : ncvar%A(atmosphere_hybrid_sigma_pressure_coordinate(50)) = [0.00019427388906478882, ..., 0.05119684338569641]
                : ncvar%B(atmosphere_hybrid_sigma_pressure_coordinate(50)) = [0.9968656897544861, ..., 0.0]
                : ncvar%p0() = 1013.25 hPa
                : ncvar%ps(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[1024.52978515625, ..., 972.4573364257812]]] hPa
>>> # SN of 'forecast_reference_time' (see CF Standard Name table)
>>> f.construct("ncvar%datetime")
<CF DimensionCoordinate: ncvar%datetime(1) days since 2023-07-10 12:00:00 proleptic_gregorian>
>>> f.construct("ncvar%datetime").standard_name = "forecast_reference_time"
>>> f.construct("ncvar%XLAT").units = "degrees_north"
>>> f.construct("ncvar%XLONG").units = "degrees_east"
>>> f.dump()
------------------------
Field: ncvar%T (ncvar%T)
------------------------
Conventions = 'CF-1.11'
_FillValue = nan

Data(time(61), atmosphere_hybrid_sigma_pressure_coordinate(50), ncdim%south_north(179), ncdim%west_east(139)) = [[[[-8.230499267578125, ..., 228.87506103515625]]]]

Domain Axis: atmosphere_hybrid_sigma_pressure_coordinate(50)
Domain Axis: forecast_reference_time(1)
Domain Axis: ncdim%south_north(179)
Domain Axis: ncdim%west_east(139)
Domain Axis: time(61)

Dimension coordinate: time
    calendar = 'proleptic_gregorian'
    standard_name = 'time'
    units = 'hours since 2023-07-10 12:00:00'
    Data(time(61)) = [2023-07-10 12:00:00, ..., 2023-07-13 00:00:00] proleptic_gregorian

Dimension coordinate: atmosphere_hybrid_sigma_pressure_coordinate
    _FillValue = nan
    computed_standard_name = 'air_pressure'
    standard_name = 'atmosphere_hybrid_sigma_pressure_coordinate'
    Data(atmosphere_hybrid_sigma_pressure_coordinate(50)) = [0.9969073534011841, ..., 0.0019467439269647002]

Dimension coordinate: forecast_reference_time
    calendar = 'proleptic_gregorian'
    standard_name = 'forecast_reference_time'
    units = 'days since 2023-07-10 12:00:00'
    Data(forecast_reference_time(1)) = [2023-07-10 12:00:00] proleptic_gregorian

Auxiliary coordinate: ncvar%XLAT
    _FillValue = nan
    units = 'degrees_north'
    Data(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[36.98377990722656, ..., 69.75613403320312]]] degrees_north

Auxiliary coordinate: ncvar%XLONG
    _FillValue = nan
    units = 'degrees_east'
    Data(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[-22.838226318359375, ..., 20.62158203125]]] degrees_east

Auxiliary coordinate: ncvar%XTIME
    _FillValue = nan
    Data(time(61)) = [0.0, ..., 3600.0]

Domain ancillary: ncvar%A
    _FillValue = nan
    Data(atmosphere_hybrid_sigma_pressure_coordinate(50)) = [0.00019427388906478882, ..., 0.05119684338569641]

Domain ancillary: ncvar%B
    _FillValue = nan
    Data(atmosphere_hybrid_sigma_pressure_coordinate(50)) = [0.9968656897544861, ..., 0.0]

Domain ancillary: ncvar%p0
    _FillValue = nan
    units = 'hPa'
    Data() = 1013.25 hPa

Domain ancillary: ncvar%ps
    _FillValue = nan
    units = 'hPa'
    Data(time(61), ncdim%south_north(179), ncdim%west_east(139)) = [[[1024.52978515625, ..., 972.4573364257812]]] hPa

Coordinate reference: standard_name:atmosphere_hybrid_sigma_pressure_coordinate
    Coordinate conversion:computed_standard_name = air_pressure
    Coordinate conversion:standard_name = atmosphere_hybrid_sigma_pressure_coordinate
    Coordinate conversion:a = Domain Ancillary: ncvar%A
    Coordinate conversion:b = Domain Ancillary: ncvar%B
    Coordinate conversion:p0 = Domain Ancillary: ncvar%p0
    Coordinate conversion:ps = Domain Ancillary: ncvar%ps
    Dimension Coordinate: atmosphere_hybrid_sigma_pressure_coordinate
```
