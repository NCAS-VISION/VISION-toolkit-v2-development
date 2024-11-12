# Test configurations

These are configurations that are known to work assuming you have the right data and
environment. The key aspects of each are listed below under headings which cover the core
nature, though see the configuration JSON keys themselves for full details.

## Flight cases

### UM model data onto flight observations (FAAM flight, STANCO campaign)

#### Fixed pressure levels

* um-faam-stanco-1.json: basic test for this case, not setting a start time override to keep the actual
   observational times.
* um-faam-stanco-2.json: applying a start time override so the actual observational times are
   ignored except for their spacing.
* um-faam-stanco-3.json: applying a different start time override to the '2' case above, so we can
   see that the overall results are different for these two cases.

TODO the same case as above but testing/exploring more config. options


#### Not fixed pressure levels

TODO


### WRF model data onto flight observations (FAAM flight, STANCO campaign)

* wrf-faam-stanco-1.json: basic test for this case, setting a start time override since the data doesn't
   match up in time with the model data so can't run without that.
* wrf-faam-stanco-2.json: applying a different start time override to the '2' case above, so we can
   see that the overall results are different for these two cases.
* wrf-faam-stanco-3.json: same as above. TODO add further changes to justify whole new config.
* wrf-faam-stanco-4.json:  same as above. TODO add further changes to justify whole new config.

TODO the same case as above but testing/exploring more config. options


## Satellite case 

### UM model data onto satellite observations

* um-satellite-1.json: basic test for this case, setting a start time override since the data doesn't
   match up in time with the model data so can't run without that.
* um-satellite-2.json: same as above except for different start time override and applying a different
   cf-plot projection since the swath in question from the given dataset is polar on the South Pole.
* um-satellite-3.json: same as um-satellite-1 case but for obs satellite data from different date
   but on same swath region.
* um-satellite-4.json: dataset corresponding to different swath (swath over region), also shown
   in the robinson projection for a different view, and a different start time.
* um-satellite-5.json: dataset corresponding to a different swath (swath over region), also shown
   in the robinson projection, and a different start time. TODO add further changes to justify
   whole new config.
* um-satellite-6.json: dataset corresponding to a different swath (swath over region), also shown
   in the robinson projection, and a different start time. TODO add further changes to justify
   whole new config.
* um-satellite-7.json: adds trivial satellite-plugin-config value. TODO apply actual not trivial
   satellite plugin setting i.e. to change a variable name to process from the default.
* um-satellite-8.json: whole orbit worth of swaths (multiple satellite datasets i.e.
   read form of (ending) `20170703201158z_20170703215054z_*.nc`
* um-satellite-8.json: multiple whole orbits worth of swaths (multiple satellite datasets i.e.
   read form of (ending) `201707032*.nc` corresponding to three full orbits.

TODO the same case as above but testing/exploring more config. options


### WRF model data onto satellite observations

TODO


*****
