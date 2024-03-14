"""
End-to-end model-to-observational field co-location script for the VISION
flight digital twin, using cf-python and cf-plot.

Demonstration for the TWINE-funded (NCAS-)VISION project.

"""

# NOTE: itertools.pairwise is only available in Python 3.10 plus, so >v3.10
import itertools
import logging
import numpy as np
import time

from pprint import pprint, pformat

import cfplot as cfp
import cf

# Define all inputs here:
# TODO eventually these can be set as command-line arguments (w/ manpage, etc.)
# configured and managed using getopts/getargs, etc.

DATA_DIR_LOC = "data/main-workwith-test-ISO-simulator"
OBS_DATA_DIR = "../compliant-data/core_faam_20170703_c016_STANCO_CF.nc"
MODEL_DATA_DIR = "Model_Input"

# TODO: Get ESMF logging via cf incoporated into Python logging system,
#       see Issue #286.
INFO = True

# ----------------------------------------------------------------------------
# STAGE 0: OPTIONAL DIAGNOSTICS REPORT
# ----------------------------------------------------------------------------
# Configure logging level
logging.basicConfig()
# NOTE we use 'CRITICAL' level to avoid seeing cf log level messaging which is
# a bit spammy and hides the output from this script.
logging.getLogger().setLevel(logging.CRITICAL)

OBS_DATA_LOC = f"{DATA_DIR_LOC}/{OBS_DATA_DIR}"
MODEL_DATA_LOC = f"{DATA_DIR_LOC}/{MODEL_DATA_DIR}"

if INFO:
    logging.critical(
        f"Using Python and CF environment of: {cf.environment(display=False)}"
    )
    logging.critical(
        f"Using data locations of:\n"
        f"Obs data: '{OBS_DATA_LOC}'\n"
        f"Model data: '{MODEL_DATA_LOC}'"
    )

# ----------------------------------------------------------------------------
# STAGE 1: READ IN INPUT DATA (format agnostic with cf!)
# ----------------------------------------------------------------------------
# 1.1: Read in datasets with cf

# 1.1.1 Observational data (from the FAAM aircraft flights in this case).
read_obs_starttime = time.time()
obs_data = cf.read(OBS_DATA_LOC)
read_obs_endtime = time.time()
read_obs_totaltime = read_obs_endtime - read_obs_starttime

# 1.1.2 Model data.
read_model_starttime = time.time()
model_data = cf.read(MODEL_DATA_LOC)
read_model_endtime = time.time()
read_model_totaltime = read_model_endtime - read_model_starttime

if INFO:
    logging.critical("Data successfully read in.")
    logging.critical(
        f"Time taken to read observational data was: {read_obs_totaltime}")
    logging.critical(
        f"Time taken to read observational data was: {read_model_totaltime}"
    )

# 1.2: Inspection of read-in fields
if INFO:
    logging.critical(f"Observational (flight) data is:\n {obs_data}")
    logging.critical(f"For example, first obs. field is:\n")
    obs_data[0].dump()
    logging.critical(f"Model data is:\n {model_data}")
    logging.critical(f"For example, first model field is:\n")
    model_data[0].dump()

# ----------------------------------------------------------------------------
# STAGE 2: ENSURE CF COMPLIANCE AND CORRECT FORMAT OF DATA READ-IN
#
#          SOME DATA PROCESSING AND VALIDATION, INCLUDING (ONLY?) ATTACHING
#          THE OROGRAPHY -> MANIPULATING THE FIELDS A BIT.
#
# INCLUDES FOR 'CORRECT FORMAT': E.G.:
# * SEE LATER TODO OF: are we assuming the model and obs data are strictly
# monotonically increasing, as we might be assuming for some of this ->
# since trajectories should be inc'ing this way, by definition.
# * VERTICAL COOR STUFF TO MAKE SURE IT IS ENCODED CORRECTLY.

# TODO: check that the obs inputs are compliant in way we need
# TODO: we need to make model data compliant and padding etc.
# Notes for future when done:
# * Get orography data, separate input, as per Maria's dir.
# ----------------------------------------------------------------------------

# TODO: IGNORE FOR NOW, USING FILES ALREADY MADE COMPLIANT BY DH
# (FOR NOW, 2.1 Take relevant fields from the list of fields read in)
obs_field = obs_data[0]
model_field = model_data[-2]

# ----------------------------------------------------------------------------
# STAGE 3: SPATIAL BOUNDING BOX: FIND THIS FOR THE FLIGHT PATH AND 'CROP'
#          MODEL DATA SO
#          WE ONLY CONSIDER THE BOUNDING BOX AND NOT IRRELEVENT DATA OUTSIDE
# ----------------------------------------------------------------------------

# TODO: might be best to do this before time bounding since it will mean you
#       only need to do thise once, not ~30 days for whole month. But
#       we don't need to worry about it being slow either way.
# IGNORE FOR NOW


# ----------------------------------------------------------------------------
# STAGE 4: TIME BOUNDING BOX: FIND RELEVANT DAYS FOR FLIGHT IN THE MODEL
#          DATA FOR COLOCATION
#
#          IS DIFFERENT TO THE SPATIAL B.B. CASE SINCE IT NEEDS TO BE DONE
#          DAILY TO ACCCOUNT FOR FLIGHTS BEING CONTAINED IN SEPARATE DAYS.
# ----------------------------------------------------------------------------

# TODO: ensure this works for flights that take off on one day and end on
# another e.g. 11 pm - 3 am flight.

# 4.1 pre-process to get relevant constructs
obs_times = obs_field.auxiliary_coordinate("time")
model_times_key, model_times = model_field.dimension_coordinate(
    "time", item=True)

# 4.2 Ensure the units of the obs and model datetimes are consistent - conform
#     them if they differ (if they don't, Units setting operation is harmless).
# NOTE: Change the units on the model (not obs) times since there are fewer
# data points on those, meaning less converting work.
obs_times_units = obs_times.Units
model_times_units = model_times.Units
model_times.Units = obs_times.Units

logging.critical(f"UNIT-CONFORMED MODEL FIELD IS: {model_field}")
same_units = (
    model_field.dimension_coordinate("time").data.Units
    == obs_field.auxiliary_coordinate("time").data.Units,
)
logging.critical(
    f"CONFIRMING: THE UNITS ON OBS AND MODEL DATETIMES ARE THE SAME: "
    f"{same_units};\n"
)

# 4.3 Ensure calendars are consistent, if not convert to equivalent.
# TODO what to do if calendar conversion means missing days when need them?
#      look at Maria's code as to how it is dealt with (e.g. in CIS)
#
# NOTE: in this case, they are the same (gregorian and standard are the same).
# TODO IGNORE FOR NOW (consistent in this case, but will need to generalise
# for when they are not).
model_calendar = model_times.calendar
obs_calendar = obs_times.calendar
logging.critical(
    f"Calendars for relevant times are:\n"
    f"MODEL: {model_calendar},\n"
    f"OBSERVATIONS: {obs_calendar}."
)

# TODO: are we assuming the model and obs data are strictly increasing, as we
# might be assuming for some of this. - > trajectories should be inc'ing with
# time with indices getting higher. Otherwise might need to use .sort() etc.
#
# NOTE: need the datetime array in order to do arithmetic with a TimeDuration
obs_earliest_dayhour = obs_times[0].datetime_array[0]
obs_latest_dayhour = obs_times[-1].datetime_array[0]
logging.critical(
    f"EARLIEST AND LATEST ARE: {obs_earliest_dayhour}, {obs_latest_dayhour}")
# Add an extra hour before the earliest, and after the latest
#
# TODO: if model data comes in less than hourly, need to adapt this to segment
# size, etc.
# TODO: it is the start of the hour we need to consider e.g. 11.00-12.00
# for 11.15 start, etc., so convert this to rounding to the nearest hour
# before (earliest) and after (latest), rather than using a whole hour
# for the worst case scenario
obs_earliest_dayhour -= cf.TimeDuration(1, "hour")
obs_latest_dayhour += cf.TimeDuration(1, "hour")

# Finally, perform the subspace to crop the field to the bounding box of time
model_field_bb = model_field.subspace(
    T=cf.wi(obs_earliest_dayhour, obs_latest_dayhour)
)
logging.critical(
    f"TIME BOUNDING BOX CALC'D, MODEL DATA FIELD AFTER BB IS: {model_field_bb}"
)

# ----------------------------------------------------------------------------
# STAGE 5: FULL XYZ/SPATIAL INTERPORLATION, I.E. INTERPOLATE THE
#          FLIGHT PATH LOCATIONS SPATIALLY, FOR THE XY HORIZONTAL AND THE Z
#          VERTICAL COORDINATES,
#          WITHIN THE MODEL DATA AND SAVE THESE FOR LATER (GET SPATIAL COORS).

#          WE DO THIS WITH ESMF LOCSTREAM, SEE:
#          https://xesmf.readthedocs.io/en/latest/notebooks/Using_LocStream.html
#
#          (WE ACHIEVE Z INTERP THS USING A (SPARSE) MATRIX METHOD BASED ON ESMF
#          WEIGHTS TO DOT PRODUCT WITH THE DATA, FOR EACH MODEL TIME.)
# ----------------------------------------------------------------------------

# TODO: UGRID grids might need some extra steps/work for this.

if INFO:
    logging.critical(f"Starting spatial interpolation (regridding) step...")
spat_regrid_starttime = time.time()

# NOTE: this requires recently-added support for ESMF LocStream
# functionality, hence cf-python version >= 3.16.1 to work.
spatially_colocated_data = model_field_bb.regrids(
    obs_field,
    method="linear",
    z="air_pressure",
    ln_z=True,
)
spat_regrid_endtime = time.time()
spat_regrid_totaltime = spat_regrid_endtime - spat_regrid_starttime

if INFO:
    logging.critical(
        f"Time taken to spatially regrid was: {spat_regrid_totaltime}")
    logging.critical(f"XYZ-colocated data is:\n {spatially_colocated_data}")
    logging.critical(spatially_colocated_data.dump())

# TODO: consider whether or not to persist the regridded / spatial interp
# before the next stage, or to do in a fully lazy way.

# ----------------------------------------------------------------------------
# STAGE 6: TIME INTERPOLATION: INTERPOLATE BETWEEN MODEL DATA TIME POINTS.

#          WE DO THIS USING A CONVOLUTION-BASED 'MERGE' OF RELEVANT
#          SEGMENTS OF THE FLIGHT PATHS FOR THE MODEL DATA X-Y COLOCATED
#          ONTO THE FLIGHT PATH FROM THE PREVIOUS STAGE.
#
# ----------------------------------------------------------------------------

if INFO:
    logging.critical("\n\n\nStarting time interpolation step...\n\n\n")
time_interp_starttime = time.time()

# In our fild after spatial interpolation, the Dimension Coord has the model
# time data and the Aux Coord has the observational time data
# NOTE: keep these calls in , desite earlier ones probably in place.
model_times = spatially_colocated_data.dimension_coordinate("time")
obs_times = spatially_colocated_data.auxiliary_coordinate("time")
model_times_len = len(model_times.data)
obs_times_len = len(obs_times.data)
if INFO:
    logging.critical(
        f"Number of model time data points: {model_times_len}\n"
        f"Number of observational time sample data points: {obs_times_len}"
    )

# Using a direct subspace method, which works generally.
# 1. Chop the flight path up into *segments*. Find the segment endpoints.
m = spatially_colocated_data.copy()

datetime_segments = []
fieldlist_subspaces_by_segment = cf.FieldList()
key = m.auxiliary_coordinate("T", key=True)
subsidiary_key = m.dimension_coordinate("T", key=True)

logging.critical(m.constructs())
logging.critical(f"Key (aux coor time) )is: {key}")
logging.critical(f"Subsidiary key (dim coor key) is: {subsidiary_key}")


final_4d_colocated_field = m.copy()  # TODO add dimension and squeeze.
key = final_4d_colocated_field.auxiliary_coordinate("T", key=True)
pairwise_segments = {}
v_w = []

# Find first and last indicdes - to not merge those?
final_index = len(list(itertools.pairwise(model_times.datetime_array)))
# TODO: do we need the 'datetime_array' bit here -investigat? YES.
# Iterate over pairs of adjacent model datetimes, defining 'segments'.
for index, (t1, t2) in enumerate(itertools.pairwise(model_times.datetime_array)):
    # 1. Define the pairwise segment endpoints
    logging.critical(f"\n\nTimes for segments are\n\n: {t1}, {t2}.")
    datetime_segments.append((t1, t2))

    q = cf.wi(cf.dt(t1), cf.dt(t2))  # had cf.dt wrapping these before, but no need now?
    logging.critical(f"Querying on query: {q} with field: {m}")
    # 2. *Subspace* the observational times to match the segments above:
    #    Subspace the field for the segment time range

    # NOTE: without the earlier bounding box step, this will fail due to
    #       not being able to find the subspace at irrelevant times.
    s0 = m.subspace(
        **{
            key: q,
            subsidiary_key: [index],
        }
    )
    s1 = m.subspace(
        **{
            key: q,
            subsidiary_key: [index + 1],
        }
    )

    # Squeeze here to remove size 1 dimension rady for calc's below?
    pairwise_segments[index] = (s0, s1)

    # (a=0, b=1 from old/whiteboard schematic and notes).
    # to unpack from '[[ ]]' shape(1, N) structure
    # TODO: best place to squeeze.
    values_0 = s0.data.squeeze()
    values_1 = s1.data.squeeze()
    # REMOVE FINAL VALUE AS THAT GETS INCLUDED FROM NEXT SEGMENT! via [:-1]
    # EXCEPT IN THE CASE OF THE FINAL SEGMENT, WHERE IT DOESN'T GET DOUBLE
    # COUNTED!
    #
    # TODO: add some assertion which will check the double counting.
    if index != (final_index - 1):
        values_0 = s0.data.squeeze()[:-1]
        values_1 = s1.data.squeeze()[:-1]

    # All arithmetic done numpy array wise! SO no need to iterate over values!
    # But this first one is uniqeuly a scalar.
    # CONVERT TO DATA TO GET DATA ARRAY NOT DIM COORD AS OUTPUT FOR WEIGHTED VALS
    # TODO: do ew need to re-find the keys? ULTIMATELY WANT A WAY THAT ISN'T KEY-
    # BASED COSTUCT CALL FOR MORE ROBUSTNESS - BECAUSE THE FIELD HAS CHANGED, BEEN
    # OPERATED ON ETC. SO CAN'T RELY ON THE KEYS BEING THE SAME.
    # 'CAN'T RELY ON KEYS BEING CONSISTENT BETWEEN DIFFERENT FIELDS'

    # TODO tidy up "time" to "T"
    distance_01 = (
        s1.dimension_coordinate("T") - s0.dimension_coordinate("T")
    ).data
    distances_0 = (
        s0.auxiliary_coordinate("T")[index] -
        s0.dimension_coordinate("T")
    ).data

    # X.2 Calculate these vales
    distances_1 = distance_01 - distances_0
    weights_0 = distances_1 / distance_01
    weights_1 = distances_0 / distance_01

    logging.critical(
        "MASKED VALUE COUNTS ARE:\n"
        f"FOR DISTANCES (0, 1): {distances_0.count()}, {distances_1.count()}\n"
        f"FOR WEIGHTS (0, 1): {weights_0.count()}, {weights_1.count()}\n"
        f"FOR VALUES (0, 1): {values_0.count()}, {values_1.count()}"
    )

    # X.3 Calculate the final value using a basic weighting formulae
    print("WEIGHTS TOTAL IS:", weights_0 + weights_1)  # should be 1, no need to div
    values_weighted = (weights_0 * values_0 + weights_1 * values_1)

    v_w.append(values_weighted)


logging.critical("FINAL WEIGHTED VALUES ARE:")
logging.critical(pformat(v_w))

# NOTE SADIE: masked values are mostly/all to do with the pressure being below
# when lands and takes off etc. on runway and close, cases realting to heavusde
# function. so all good and normal. Eventually we will add an extrapolation
# option.

for v in v_w:
    logging.critical(
        f"GETTING: {v} WITH LEN {len(v)} AND NON-MASKED COUNT {v.count()}"
    )

# Finally, reattach to (the copy of) the obs. field to get final values
# on the right domain, though we still need to adapt the metadata to reflect
# the new context.
concatenated_weighted_values = cf.Data.concatenate(v_w)
logging.critical(
    f"WEIGHTED VALS ARE: {concatenated_weighted_values}, WITH LEN: "
    f"{len(concatenated_weighted_values)}"
)
logging.critical(
    "NUMBER OF NON-MASKED VALUES IN THIS ARE:\n"
    f"{concatenated_weighted_values.count()} VS MASKED:\n"
    f"{len(concatenated_weighted_values) - concatenated_weighted_values.count()}"
)

# Set the data onto the observational field domain after spatial interpolation
final_result_field = obs_field.copy()
final_result_field.set_data(concatenated_weighted_values)
logging.critical(
    "FINAL RESULT FIELD AFTER DATA SETTING, PRE-METADATA PROPERTY EDIT: "
    f"{final_result_field}\n AND IN FULL DETAIL:")
final_result_field.dump()

# Making the aux coor for time a dimension coord. too, so we can plot it.
# TODO: there is probably a better way to plot from aux coor?
# TODO: ideally don't want to be convertig it to a dim coor. -> DH: way is
# check if it is featuretype, then lok for aux coords not dim coords. if it
# is not, fail on trajectory plot stuff.
# another cpflot issue: generalise the trajectory function for
# not just contiguouos ragged array, e.g. *multidimensional orthogonal arrays* also
# e.g. with our DSG. Ragged aray is a massive red herring.
# FOR OUR CASE, SB HACK OF AH TRAJ CODE,o generalise trajsectory so can take
# leading dimension or not, for both cases of 1D OR 2D. If ID, means have a
#trajectory dimension and it can be dropped.
aux_coor_t = final_result_field.auxiliary_coordinate("time")
dim_coor_t = cf.DimensionCoordinate(source=aux_coor_t)
final_result_field.set_construct(dim_coor_t, axes="ncdim%obs")

# Finally, re-set the properties on the final result field so it has model
# data properties not obs preoprties.
final_result_field.clear_properties()
final_result_field.set_properties(model_field.properties())
# TODO: add new, or append to if already exists, to 'history' property
# to say that we colocated etc. with VISION / cf.

logging.critical(
    f"2. FINAL RESULT FIELD AFTER DATA SETTING (DONE) {final_result_field}")
final_result_field.dump()

logging.critical(
    "The final result field has:\n"
    f"DATA STATS: {final_result_field.data.stats()}\n"
)

# TODO: consider whether or not to persist the regridded / time interp
# before the next stage, or to do in a fully lazy way.

# ----------------------------------------------------------------------------
# STAGE 7: CREATE OUTPUTS AS A CONCATENATED CONTIGUOUS RAGGED ARRAY OF ALL
#          FLIGHT PATH PROJECTIONS FOR THE VARIOUS DAYS.
#
#          THIS INVOLVES AGGREGATING AND COMPRESSING.
# ----------------------------------------------------------------------------

# TODO IGNORE FOR NOW

# ----------------------------------------------------------------------------
# STAGE 8: WRITE OUT FINAL OUTPUT WHICH HAS BEEN CO-LOCATED
#          FOR X, Y, Z AND T.
# ----------------------------------------------------------------------------
cf.write(final_result_field, "cf_vision_result_field.nc")

# ----------------------------------------------------------------------------
# STAGE 9: VISUALISE OUTPUT AND SHOW THE PLOT?
# ----------------------------------------------------------------------------

# 9.1 Change the viewpoint to be over the UK only, with high-res map outline
cfp.mapset(lonmin=-2, lonmax=2, latmin=50, latmax=54, resolution="10m")

# 9.2
# Min, max as determined using final_result_field.min(), .max():
cfp.levs(min=5e-08, max=10e-08, step=0.25e-08)
cfp.cscale("viridis")

# 9.3 Make and open the final plot
# NOTE: can try 'legend_lines=True' for the lines plotted with average between
# the two scatter marker points, if preferable?
cfp.traj(final_result_field, verbose=True, legend=True)


# [END]
