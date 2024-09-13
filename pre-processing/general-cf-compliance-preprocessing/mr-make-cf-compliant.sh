#!/bin/bash

# Script to fix CF compliance issues for select FAAM datasets.
#
# This script has been adapted by SB from one created by MR. The original
# script was written to fix-up, particularly, some STANCO campaign data.

# Specify the directory containing the files
in_path="data/compliant-data/"
out_path="Processed_Flights_step2/"


# Iterate over each file in the directory
for file in "$in_path"/*.nc; do
    echo $file
    # Check if it's a file (not a directory)
    if [ -f "$file" ]; then
        # Process file
        outfile=$out_path$(basename "$file")
        echo $outfile
        ncatted -O \
            -a featureType,global,c,c,"trajectory" \
            -a coordinates,O3_TECO,c,c,"time altitude air_pressure latitude longitude" \
            -o $outfile $file
    fi
done
