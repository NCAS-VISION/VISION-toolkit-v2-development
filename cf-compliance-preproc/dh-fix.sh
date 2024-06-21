# Script to fix CF compliance issues for select FAAM datasets.
#
# This script has been adapted by SB from one created by DH. The original
# script was written to fix-up, particularly, some STANCO campaign data.

# Select variable of interest
var_choice=ACLD_GIN

infile=$1
basedir=$(dirname "$0")
tmpfile=$(basename "$1" ".nc")
ncatted -O \
	-a featureType,global,c,c,"trajectory" \
	-a coordinates,"$var_choice",c,c,"time altitude air_pressure latitude longitude" \
	-a cf_role,campaign,c,c,"trajectory_id" \
	-a units,campaign,d,, \
	-a missing_value,campaign,d,, \
	-a _FillValue,campaign,d,, \
	-a frequency,campaign,d,, \
	-o $tmpfile $infile

# Preview
ncdump -h $tmpfile 

python $basedir/dh-fix.py $tmpfile
