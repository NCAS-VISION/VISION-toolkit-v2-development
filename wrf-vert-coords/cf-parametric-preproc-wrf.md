# cf-python parametric pre-prcoessing of WRF data

Working in the following directory on JASMIN:

```console
[slb93@sci4 c345]$ pwd
/gws/nopw/j04/vision/WRF_testdata/c345
```

I copied Laurents' script at
`https://github.com/NCAS-VISION/vision-project-resources/blob/wrf-vert-coords/wrf-vert-coords/cf-p-coords-wrf.py`
and make some tweaks just to the start to read in the data in that directory
instead of other data. My script is located under a new directory
`sadie-temp-scripts` and should be run via, from the directory above:

```console
[slb93@sci4 c345]$ python sadie-temp-scripts/cf-p-coords-wrf.py
```

See the code contained in that script for details, but the only difference to
Laurents' script is that I've edited the start to read this data:

```python
import os
path = os.listdir('.')
datasets = [Dataset(file) for file in path if file.startswith("wrfout_d01")]
# d01 only for now, to avoid broadcasting issues?
```

Note I have only read in the `wrfout_d01` data for now, since if all three
domains are read in (`d01`, `d02`, `d0`) to read in all `file.startswith("wrfout_d0")`
data, then shape broadcasting errors occur.

The main part - now run the following analysis in interactive Python:

```python
Python 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
[slb93@sci4 c345]$ python
Python 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cf
>>> f = cf.read("wrf-press-test.nc")
>>> f
[<CF Field: ncvar%A(ncdim%bottom_top(50))>,
 <CF Field: ncvar%B(ncdim%bottom_top(50))>,
 <CF Field: ncvar%T(ncdim%Time(61), ncdim%bottom_top(50), ncdim%south_north(179), ncdim%west_east(139))>,
 <CF Field: ncvar%ZNU(ncdim%Time(61), ncdim%bottom_top(50))>,
 <CF Field: ncvar%p0>,
 <CF Field: ncvar%ps(ncdim%Time(61), ncdim%south_north(179), ncdim%west_east(139))>]
>>> f[0]
<CF Field: ncvar%A(ncdim%bottom_top(50))>
>>> print(f[0])
Field: ncvar%A (ncvar%A)
------------------------
Data            : ncvar%A(ncdim%bottom_top(50))
Dimension coords: ncvar%datetime(key%domainaxis1(1)) = [2023-07-10 12:00:00] proleptic_gregorian
>>> # We have the right fields with the rihr variables, now we want to combine them according to
>>> # our formulae to get the pressure ('Atmosphere hybrid sigma pressure coordinate') as a field
>>> # - this should be as follows, given te FieldList order above:
>>> p = f[0]*f[4] + f[1]*f[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/cf/mixin/propertiesdata.py", line 173, in __mul__
    return self._binary_operation(y, "__mul__")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/cf/field.py", line 1254, in _binary_operation
    new_data = field0.data._binary_operation(field1.data, method)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/cf/data/data.py", line 3767, in _binary_operation
    result = getattr(dx0, method)(dx1)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/dask/array/core.py", line 222, in wrapper
    return f(self, other)
           ^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/dask/array/core.py", line 2365, in __mul__
    return elemwise(operator.mul, self, other)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/dask/array/core.py", line 4795, in elemwise
    broadcast_shapes(*shapes)
  File "/apps/jasmin/jaspy/miniforge_envs/jaspy3.11/mf3-23.11.0-0/envs/jaspy3.11-mf3-23.11.0-0-r20240508/lib/python3.11/site-packages/dask/array/core.py", line 4723, in broadcast_shapes
    raise ValueError(
ValueError: operands could not be broadcast together with shapes (50, 1, 1) (61, 179, 139)
>>> # OK, there is a broadcasting of shapes issue - how do we match these up?
```

*****
