COMPUTE_VERT_COORS = True
WRITE_OUT_NAME = "final-wrf-with-vert-coords.nc"
CHECK_AGGREGATES_TO_ONE = True


import cf

# 0. Read in data pre-processed with wrf-python to get relevant vars
f = cf.read("wrf-data-processed/wrf-press-test.nc")

# Take out the fields of relevance
a = f[0]
b = f[1]
t = f[2]
z = f[3]
p0 = f[4]
ps = f[5]

# 1. Set up the domain ancils
a_da = cf.DomainAncillary(source=a)
b_da = cf.DomainAncillary(source=b)
p0_da = cf.DomainAncillary(source=p0)
ps_da = cf.DomainAncillary(source=ps)

# 2. Add these as constructs to t, our main field
ket_t_a = t.set_construct(a_da)
key_t_b = t.set_construct(b_da)
key_t_p0 = t.set_construct(p0_da)
key_t_ps = t.set_construct(ps_da)
print("\n\nAfter domain ancil setting, t is:", t)

# 3. Create the coordinate reference
c = cf.CoordinateReference()
# Set the standard name which we get from App. D of the CF Conventions doc
c.coordinate_conversion.set_parameter(
    "standard_name", "atmosphere_hybrid_sigma_pressure_coordinate")
# Get the computed standard name from App D. section 'formula terms'
c.coordinate_conversion.set_parameter(
    "computed_standard_name", "air_pressure")
# Get the variables from the 'formula terms' equation and match them to
# the keys from the set_construct() call above.
dom_ancils = {
    "a": ket_t_a,
    "b": key_t_b,
    "p0": key_t_p0,
    "ps": key_t_ps,
}
c.coordinate_conversion.set_domain_ancillaries(dom_ancils)
print("\n\nCoordinate reference about to add is:")
c.dump()
# All ready to add!

# 4. Add the coordinate reference to the field t
c_key = t.set_construct(c)
print("\n\nField t after coordinate reference setting is:", t)

# 5. There is some unit processing to do, since we can't yet do the computation
# of t.compute_vertical_coordinates() which ultimately needs to work
# Do the unit addition required:
# No units on the domain ancils - pulled in from wrf-python - should
# find a way to get those in via the script
p0 = t.construct("ncvar%p0")
ps = t.construct("ncvar%ps")
p0.override_units("hPa", inplace=True)
ps.override_units("hPa", inplace=True)
print("\n\nField after unit processing is:", t)
# Units now added as desired

# 6. Now the call to compute_vertical_coordinates should work!
if COMPUTE_VERT_COORS:
    t1 = t.compute_vertical_coordinates()
    print("\n\nComputing of vertical coordinates worked, giving:", t1)
    # Note there is now an 'air_pressure' aux coord! We have done it!

# Note we should only write out the field without the computed vert coord
# since that will double the size of the data. Calculate when need, don't save
# e.g. we will calculate it at the start of the VISION script.

# 7. Finally, we need to deal with the z coordinate which is presently
#    just a separate field
print("\n\nVertical coordinates from original field z are:", z)
print("\n\nWith array of:", z.array)

# Note these are all the same across the times, so take just the first
z0 = z[0].squeeze()
# Create a dimension coordinate of this
d = cf.DimensionCoordinate(source=z0)
d.set_property("standard_name", "atmosphere_hybrid_sigma_pressure_coordinate")
d.set_property("computed_standard_name", "air_pressure")
print("\n\nAdding a dimension coordinate of the squeezed first z element:")
d.dump()

# Now set this on t, to incorporate the z into t as a dim. coord.
d_key = t.set_construct(d)
# Now added!
print("\n\nAdded dimension coord. to t:", t)

# 8. Also need to add it to the coordinate reference as its coordinate
c = t.construct(c_key)
c.set_coordinate(d_key)
print("\n\nSet the dimension coord. on the coord. ref. in t:")
c.dump()

# 9. Now everything should be ready. Inspect the field and write it out
print("\n\nDone, now writing out this t field:")
t.dump()
cf.write(t, WRITE_OUT_NAME)
print(f"\n\nWriting out done: see {WRITE_OUT_NAME}!")

if CHECK_AGGREGATES_TO_ONE:
    # 10. Check everything is OK by aggregating the current FieldList, should
    # now be aggregatable to one field so emerge as a single field now.
    g = cf.aggregate(t)
    print("\n\nLength of aggregated final FieldList is:", len(g))
    print("Final zeroth field is:")
    g[0].dump()
    # NOTE: check all is good by using 'ncdump -h <filename>' on the output
    # netCDF file, shoudl see a 'formula_terms' e.g:
    #     ZNU:formula_terms = "a: A b: B p0: p0 ps: ps" ;
    # attached to the z coordinate (ZNU in this example).
