# Script to fix CF compliance issues for select FAAM datasets.
#
# This script has been adapted by SB from one created by DH. The original
# script was written to fix-up, particularly, some STANCO campaign data.

import os
import sys

import cf

tmpfile = sys.argv[1]

f = cf.read(tmpfile)
print("FieldList is:")
print(f)
print("Field 0 is:")
print(f[0])

properties = c.clear_properties()
a = cf.AuxiliaryCoordinate(source=c)[0]
for prop in ('cf_role', 'long_name'):
    a.set_property(prop, properties[prop])

f = f.insert_dimension(None)
f.set_construct(a)
f = f.squeeze()

outfile = f"{tmpfile}_CF.nc"
cf.write(f, outfile)

os.remove(tmpfile)

g = cf.read(outfile)
assert len(g) == 1
print(g[0])
