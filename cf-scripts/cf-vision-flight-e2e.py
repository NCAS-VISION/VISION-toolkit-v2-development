"""
End-to-end model-to-observational field co-location script for the VISION
flight digital twin, using cf-python and cf-plot.

Demonstration for the TWINE-funded (NCAS-)VISION project.

Requirements to run the script successfully (else the script needs fixes
so please get in touch with Sadie RE any issues, noting this is a WIP!):
* environment with versions, at least, Python 3.10 and cf-python 3.16.2;
* input data conforming to toolkit requirements (documentation TODO).

Note: this script assumes track data from a flight as the observational input,
where other inputs for the VISION project such as satellite data will be
considered in future later-stage updates only, so will not yet work for this
script.

"""

# NOTE: itertools.pairwise is only available in Python 3.10 plus, so >= v.3.10
import itertools
import logging
import numpy as np
import sys
import time

from pprint import pformat

import cfplot as cfp
import cf

# Define all inputs and output choices
# TODO eventually these can be set as command-line arguments (w/ manpage, etc.)
# configured and managed using getopts/getargs, etc.
#
# TODO: document assumptions about data that we use that the input data need
# to abide by, for it to work (input data quality requirements).
DATA_DIR_LOC = "data/main-workwith-test-ISO-simulator"
OBS_DATA_DIR = "../compliant-data/core_faam_20170703_c016_STANCO_CF.nc"
MODEL_DATA_DIR = "Model_Input"
# Set output information
OUTPUT_FILE_NAME = "cf_vision_result_field.nc"
HISTORY_MESSAGE = (  # gets added to the 'history' property on the output file
    "Processed using the NCAS VISION flight simulator script to colocate from "
    "model data to the observational flight data spatio-temporal location."
)

REGRID_METHOD = "linear"
REGRID_Z_COORD = "air_pressure"

# Configure messaging to STDOUT, which is very verbose if INFO=True, else
# as minimal as allows without log control in cf-plot (at present).
# TODO: Get ESMF logging via cf incoporated into Python logging system,
#       see Issue #286.
VERBOSE = True

# Plotting general config.
CSCALE = "plasma"  # "parula" also works well, as alternative for dev.

# Optionally, display plots of the input observational data, or its track
# only in one colour (if 'PLOT_OF_INPUT_OBS_TRACK_ONLY' is set to True).
# This could be useful for previewing the track to be colocated
# onto, to fail early if the user isn't happy with the track,
# or for demo'ing the code to compare the original observational data
# to the co-located data to see the differences.
SHOW_PLOT_OF_INPUT_OBS = True
PLOT_OF_INPUT_OBS_TRACK_ONLY = True


# TODO: for whole script, consider what is useful to persist (Dask-wise)
# for efficiency.

# ----------------------------------------------------------------------------
# STAGE 0: OPTIONAL DIAGNOSTICS REPORT
# ----------------------------------------------------------------------------
# Configure logging level

# NOTE we use 'CRITICAL' level to avoid seeing cf log level messaging which is
# a bit spammy and hides the output from this script.
logger = logging.getLogger(__name__)
if VERBOSE:
    logger.setLevel(logging.CRITICAL)
else:
    logger.setLevel(logging.CRITICAL + 1)  # prevents even critical log messages

obs_data_loc = f"{DATA_DIR_LOC}/{OBS_DATA_DIR}"
model_data_loc = f"{DATA_DIR_LOC}/{MODEL_DATA_DIR}"

logger.critical(f"Using Python and CF environment of: {cf.environment(display=False)}")
logger.critical(
    f"Using data locations of:\n"
    f"Obs data: '{obs_data_loc}'\n"
    f"Model data: '{model_data_loc}'"
)

# ----------------------------------------------------------------------------
# STAGE 1: READ IN INPUT DATA (format agnostic with cf!)
# ----------------------------------------------------------------------------
# 1.1: Read in datasets with cf

# 1.1.1 Observational data (from the FAAM aircraft flights in this case).
read_obs_starttime = time.time()
obs_data = cf.read(obs_data_loc)
read_obs_endtime = time.time()
read_obs_totaltime = read_obs_endtime - read_obs_starttime

# 1.1.2 Model data.
read_model_starttime = time.time()
model_data = cf.read(model_data_loc)
read_model_endtime = time.time()
read_model_totaltime = read_model_endtime - read_model_starttime

logger.critical("Data successfully read in.")
logger.critical(f"Time taken to read observational data was: {read_obs_totaltime}")
logger.critical(f"Time taken to read model data was: {read_model_totaltime}")

# 1.2: Inspection of read-in fields
logger.critical(f"Observational (flight) data is:\n {obs_data}")
logger.critical(f"For example, first obs. field is:\n")
logger.critical(obs_data[0].dump(display=False))
logger.critical(f"Model data is:\n {model_data}")
logger.critical(f"For example, model field we use is:\n")
logger.critical(model_data[-2].dump(display=False))

# 1.3 Take relevant fields from the list of fields read in
obs_field = obs_data[0]
model_field = model_data[-2]

# 1.4 Plots, if requested. First configure general settings for plot:
# a) Change the viewpoint to be over the UK only, with high-res map outline
cfp.mapset(lonmin=-2, lonmax=2, latmin=50, latmax=54, resolution="10m")
# b) Colour scale that better shows detail for typical flights
cfp.cscale(CSCALE)
if SHOW_PLOT_OF_INPUT_OBS:
    # Plot the *input* observational data for a preview, before doing any work
    # Min, max as determined using final_result_field.min(), .max():
    cfp.levs(min=-5, max=55, step=5)
    if PLOT_OF_INPUT_OBS_TRACK_ONLY:
        # Use the same field but set all data to zero so can plot the whole
        # track in the same colour to just display the path, not orig. data
        equal_data_obs_field = obs_field.copy()
        new_data = np.zeros(len(equal_data_obs_field.data))  # 0 -> force red
        equal_data_obs_field.set_data(new_data, inplace=True)
        cfp.cscale("scale28")  # has bright red for the lowest values
        cfp.gopen(file="obs_track_only.png")
        cfp.traj(
            equal_data_obs_field,
            verbose=VERBOSE,
            legend=True,
            colorbar=False,
            markersize=0.5,
            linewidth=0,  # effectively turn off lines to only have markers
            title=("Flight path from observational field to co-locate model "
                   "field onto"),
        )
        cfp.gclose()
        cfp.cscale(CSCALE)  # reset for normal (default-style) plots after
    else:
        cfp.gopen(file="obs_track_with_data.png")
        cfp.traj(
            obs_field,
            verbose=VERBOSE,
            legend=True,
            markersize=5,
            linewidth=0.4,
            title=("Observational field input (path, to be used for "
                   "co-location, with its corresponding data, to be ignored)",
                   )
        )
        cfp.gclose()


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

# ----------------------------------------------------------------------------
# STAGE 3: UNITS AND CALENDAR CONSISTENCY CONSIDERATIONS
#
# ----------------------------------------------------------------------------
# 3.1 Pre-process to get relevant constructs
obs_times = obs_field.auxiliary_coordinate("T")

model_times_key, model_times = model_field.dimension_coordinate("T", item=True)

# 3.2 Ensure the units of the obs and model datetimes are consistent - conform
#     them if they differ (if they don't, Units setting operation is harmless).
# NOTE: Change the units on the model (not obs) times since there are fewer
# data points on those, meaning less converting work.
obs_times_units = obs_times.Units
model_times_units = model_times.Units
model_times.Units = obs_times.Units

logger.critical(f"UNIT-CONFORMED MODEL FIELD IS: {model_field}")
same_units = (
    model_field.dimension_coordinate("T").data.Units
    == obs_field.auxiliary_coordinate("T").data.Units,
)
logger.critical(
    f"CONFIRMING: THE UNITS ON OBS AND MODEL DATETIMES ARE THE SAME: "
    f"{same_units};\n"
)

# 3.3 Ensure calendars are consistent, if not convert to equivalent.
# TODO what to do if calendar conversion means missing days when need them?
#      look at Maria's code as to how it is dealt with (e.g. in CIS)
#
# NOTE: in this case, they are the same (gregorian and standard are the same).
# TODO IGNORE FOR NOW (consistent in this case, but will need to generalise
# for when they are not).
model_calendar = model_times.calendar
obs_calendar = obs_times.calendar
logger.critical(
    f"Calendars for relevant times are:\n"
    f"MODEL: {model_calendar},\n"
    f"OBSERVATIONS: {obs_calendar}."
)


# ----------------------------------------------------------------------------
# STAGE 4: BOUNDING BOX, IN TIME AND SPACE: FIND THIS FOR THE FLIGHT PATH AND
#          'CROP' MODEL DATA TO IGNORE IRRELEVENT DATA OUTSIDE THE BOUNDARIES.
# ----------------------------------------------------------------------------

# TODO: ensure this works for flights that take off on one day and end on
# another e.g. 11 pm - 3 am flight.

bb_starttime = time.time()

# 3.1: prep. towards the BB component subspace.
# Find the spatial obs. path X-Y-Z boundaries to crop the model field to.
#     Note: avoid calling these 'bounds' since that has meaning in CF, so to
#           prevent potential ambiguity/confusion.

# For a DSG, the spatial coordinates will always be auxiliary:
obs_X = obs_field.auxiliary_coordinate("X")
obs_Y = obs_field.auxiliary_coordinate("Y")
obs_Z = obs_field.auxiliary_coordinate("Z")

logger.critical(
    "STATS ON SPATIAL BOUNARING BOX TO US ARE: "
    f"{obs_X.data.stats()}, {obs_Y.data.stats()}"
)

# 3.2: prep. towards the temporal BB component.
# TODO: are we assuming the model and obs data are strictly increasing, as we
# might be assuming for some of this. - > trajectories should be inc'ing with
# time with indices getting higher. Otherwise might need to use .sort() etc.
#
# NOTE: use max and min to account for any missing data even at endpoints,
#       as opposed to taking the values at first and last position/index.
logger.critical(
    "EARLIEST AND LATEST TIMES ARE: "
    f"{obs_times.data.minimum()}, {obs_times.data.maximum()}"
)

# 3.3 Perform the 4D spatio-temporal bounding box to reduce the model data down
#     to only that which is relevant for the calculations on the observational
#     data path in 4D space, that is:
#     * a spatial 3D X-Y-Z subspace to spatially bound to those values; plus
#     * a time 1D T subspace to bound it in time i.e. cover only relevant times

# Note: this requires a 'halo' config. feature introduced in cf-ython 3.16.2.
# TODO SLB: need to think about possible compications of cyclicity, etc.,
#           and account for those.
# Note: getting some dask arrays out instead of slices, due to Dask laziness.
# DH to look into.

# Note: can do the spatial and the temporal subspacing separately, and if
# want to do this make the call twice for each coordinate arg. Reasons we may
# want to do this include having separate halo sizes for each coordinate, etc.
model_field_bb = model_field.subspace(
    1,  # the halo size that extends the bounding box by 1 in index space
    X=cf.wi(obs_X.data.minimum(), obs_X.data.maximum()),
    Y=cf.wi(obs_Y.data.minimum(), obs_Y.data.maximum()),
    Z=cf.wi(obs_Z.data.minimum(), obs_Z.data.maximum()),
    T=cf.wi(obs_times.data.minimum(), obs_times.data.maximum()),
)

bb_endtime = time.time()
bb_totaltime = bb_endtime - bb_starttime

logger.critical(
    "4D bounding box calculated. Model data with BB applied is: "
    f"{model_field_bb}"
)
logger.critical(f"Time taken to create bounding box: {bb_totaltime}")

# ----------------------------------------------------------------------------
# STAGE 5: FULL XYZ/SPATIAL INTERPORLATION, I.E. INTERPOLATE THE
#          FLIGHT PATH LOCATIONS SPATIALLY, FOR THE XY HORIZONTAL AND THE Z
#          VERTICAL COORDINATES,
#          WITHIN THE MODEL DATA AND SAVE THESE FOR LATER (GET SPATIAL COORS).

#          WE DO THIS WITH ESMF LOCSTREAM, SEE:
#          https://xesmf.readthedocs.io/en/latest/notebooks/Using_LocStream.html

# ----------------------------------------------------------------------------

# TODO: UGRID grids might need some extra steps/work for this.

logger.critical(f"Starting spatial interpolation (regridding) step...")
spat_regrid_starttime = time.time()

# 5.0: Creating the spatial bounding box may have made some of the spatial
# dimensions singular, which would lead to an error or:
#     ValueError: Neither the X nor Y dimensions of the source field <field>
#     can be of size 1 for spherical 'linear' regridding.
# so we have to account for this.

# 5.1 Perform the spherical regrid which does the spatial interpolation
# NOTE: this requires recently-added support for ESMF LocStream
# functionality, hence cf-python version >= 3.16.1 to work.
#
# TODO: If there is a size 0 axes, the spatial bounding box could have
# collapsed axes down to a size 0, and halo-ing will get to size 1(???, or
# not, have nothing to work with) but
# regrids method can't work with a size-1.
# Can we use 'contains' or (better?) 'cellwi' method to do this?
spatially_colocated_field = model_field_bb.regrids(
    obs_field,
    method=REGRID_METHOD,
    z=REGRID_Z_COORD,
    ln_z=True,
)
post_spatregrid_cyclic = model_field_bb.cyclic()
spat_regrid_endtime = time.time()
spat_regrid_totaltime = spat_regrid_endtime - spat_regrid_starttime

logger.critical(f"Time taken to spatially regrid was: {spat_regrid_totaltime}")
logger.critical(f"XYZ-colocated data is:\n {spatially_colocated_field}")
logger.critical(spatially_colocated_field.dump(display=False))

# TODO: consider whether or not to persist the regridded / spatial interp
# before the next stage, or to do in a fully lazy way.

# ----------------------------------------------------------------------------
# STAGE 6: TIME INTERPOLATION: INTERPOLATE BETWEEN MODEL DATA TIME POINTS.

#          WE DO THIS USING A CONVOLUTION-BASED 'MERGE' OF RELEVANT
#          SEGMENTS OF THE FLIGHT PATHS FOR THE MODEL DATA X-Y COLOCATED
#          ONTO THE FLIGHT PATH FROM THE PREVIOUS STAGE.
#
# ----------------------------------------------------------------------------

logger.critical("\n\n\nStarting time interpolation step...\n\n\n")
time_interp_starttime = time.time()

# In our field after spatial interpolation, the Dimension Coord has the model
# time data and the Aux Coord has the observational time data
# NOTE: keep these calls in, desite earlier ones probably in-place.
model_times = spatially_colocated_field.dimension_coordinate("T")
obs_times = spatially_colocated_field.auxiliary_coordinate("T")
model_times_len = len(model_times.data)
obs_times_len = len(obs_times.data)

logger.critical(
    f"Number of model time data points: {model_times_len}\n"
    f"Number of observational time sample data points: {obs_times_len}"
)

# 6.1 Setup ready for iteration...
# ...6.1.1 Constructs
m = spatially_colocated_field.copy()
aux_time_key = m.auxiliary_coordinate("T", key=True)
dim_time_key = m.dimension_coordinate("T", key=True)
logger.critical(m.constructs())
logger.critical(f"Aux coor time key is: {aux_time_key}")
logger.critical(f"Dim coor time key is: {dim_time_key}")
# ...6.1.2 Empty objects ready to populate
datetime_segments = []
fieldlist_subspaces_by_segment = cf.FieldList()
pairwise_segments = {}
v_w = []

# 6.2 Find final index to skip in some cases later to avoid double counting
final_index = len(list(itertools.pairwise(model_times.datetime_array)))

# 6.3 Iterate over pairs of adjacent model datetimes, defining 'segments'.
#     Chop the flight path up into these *segments* and do a weighted merge
#     of data from segments adjacent in the model times to form the final
#     time-interpolated value.
for index, (t1, t2) in enumerate(itertools.pairwise(model_times.datetime_array)):
    # 6.3.1 Define the pairwise segment datetime endpoints
    logger.critical(f"\n\nTimes for segments are\n\n: {t1}, {t2}.")
    datetime_segments.append((t1, t2))

    # 6.3.2 Define a query which will find any datetimes within these times
    #       to map all observational times to the appropriate segment, later.
    q = cf.wi(cf.dt(t1), cf.dt(t2), open_upper=True)  # TODO is cf.dt wrapping necessary?
    logger.critical(f"Querying on query: {q} with field: {m}")

    # 6.3.3 Subspace the observational times to match the segments above,
    #       namely using the query created above.
    #       Use a direct subspace method, which works generally.
    #
    # NOTE: without the earlier bounding box step, this will fail due to
    #       not being able to find the subspace at irrelevant times.
    logger.critical({
            aux_time_key: q,
            dim_time_key: [index],
        })
    s0 = m.subspace(
        **{
            aux_time_key: q,
            dim_time_key: [index],
        }
    )
    s1 = m.subspace(
        **{
            aux_time_key: q,
            dim_time_key: [index + 1],
        }
    )

    # 6.3.4 Squeeze here to remove size 1 dim ready for calculations to come,
    #       i.e. to unpack from '[[ ]]' shape(1, N) structure.
    # NOTE: a=0 and b=1 from old/whiteboard schematic and notes).
    values_0 = s0.data.squeeze()
    values_1 = s1.data.squeeze()

    # 6.3.6 Calculate the arrays to be used in the weighting calculation.
    # All arithmetic done numpy-array wise, so no need to iterate over values.
    #
    # NOTE: converted to data to get data array not dim coord as output for
    #       weighted values.
    # TODO: take care using keys! We can't rely on keys being consistent
    #       between different fields, so may need to re-determine these at
    #       different steps, else (ideally) find a robust way not using keys
    #       to pick out the relevant time constructs.
    # NOTE: All calc variables are arrays, except this first one,
    #       a scalar (constant whatever the obs time)
    distance_01 = (s1.dimension_coordinate("T") - s0.dimension_coordinate("T")).data
    distances_0 = (
        s0.auxiliary_coordinate("T")[index] - s0.dimension_coordinate("T")
    ).data

    # 6.3.7 Calculate the datetime 'distances' to be used for the weighting
    distances_1 = distance_01 - distances_0
    weights_0 = distances_1 / distance_01
    weights_1 = distances_0 / distance_01

    logger.critical(
        "MASKED VALUE COUNTS ARE:\n"
        f"FOR DISTANCES (0, 1): {distances_0.count()}, {distances_1.count()}\n"
        f"FOR WEIGHTS (0, 1): {weights_0.count()}, {weights_1.count()}\n"
        f"FOR VALUES (0, 1): {values_0.count()}, {values_1.count()}"
    )

    # 6.3.8 Calculate the final weighted values using a basic weighting
    # formulae.
    # NOTE: by the maths, the sum of the two weights should be 1, so there
    #       is no need to divide by that, though confirm with a print-out
    logger.critical(f"WEIGHTS TOTAL IS: {weights_0 + weights_1}")

    values_weighted = weights_0 * values_0 + weights_1 * values_1
    v_w.append(values_weighted)


# NOTE: masked values are mostly/all to do with the pressure being below
#       when flight lands and takes off etc. on runway and close, cases
#       relating to the Heaviside function. So it is all good and expected
#       to have masked values in the data, at the end and/or start.
#       Eventually we will add an extrapolation option whereby user can choose
#       to extrapolate as well as interpolate, and therefore assign values to
#       the masked ones.

logger.critical("FINAL WEIGHTED VALUES ARE:")
logger.critical(pformat(v_w))
for v in v_w:
    logger.critical(f"GETTING: {v} WITH LEN {len(v)} AND NON-MASKED COUNT {v.count()}")

# 6.4 Concatenate the data values found above from each segment, to finally
#     get the full set of model-to-obs co-located data.
concatenated_weighted_values = cf.Data.concatenate(v_w)
logger.critical(
    f"WEIGHTED VALS ARE: {concatenated_weighted_values}, WITH LEN: "
    f"{len(concatenated_weighted_values)}"
)
logger.critical(
    "NUMBER OF NON-MASKED VALUES IN THIS ARE:\n"
    f"{concatenated_weighted_values.count()} VS MASKED:\n"
    f"{len(concatenated_weighted_values) - concatenated_weighted_values.count()}"
)

# 6.5 Finally, reattach that data to (a copy of) the obs field to get final
#     values on the right domain, though we still need to adapt the metadata to
#     reflect the new context so that the field with data set is contextually
#     correct.
final_result_field = obs_field.copy()
final_result_field.set_data(concatenated_weighted_values)
logger.critical(
    "FINAL RESULT FIELD AFTER DATA SETTING, PRE-METADATA PROPERTY EDIT: "
    f"{final_result_field}\n AND IN FULL DETAIL:"
)
logger.critical(final_result_field.dump(display=False))

# 6.6 Finally, re-set the properties on the final result field so it has model
# data properties not obs preoprties.
# 6.6.1: general properties
final_result_field.clear_properties()
final_result_field.set_properties(model_field.properties())
# 6.6.2 Add new, or append to if already exists, 'history' property
#       details to say that we colocated etc. with VISION / cf.
history_details = final_result_field.get_property("history")
history_details += " ~ " + HISTORY_MESSAGE  # include divider to previous info
final_result_field.set_property("history", history_details)

logger.critical(
    f"Final resultant field after data co-location is: {final_result_field}")
logger.critical(final_result_field.dump(display=False))
logger.critical(
    "The final result field has data statistics of:\n"
)
logger.critical(pformat(final_result_field.data.stats()))

# TODO: consider whether or not to persist the regridded / time interp.
# before the next stage, or to do in a fully lazy way.

time_interp_endtime = time.time()
time_interp_totaltime = time_interp_endtime - time_interp_starttime
logger.critical("Time interpolation done.")
logger.critical(f"Time taken to do time interpolation: {time_interp_totaltime}")

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

write_starttime = time.time()

# 8.1 Write straight out to file on-disk
cf.write(final_result_field, OUTPUT_FILE_NAME)

write_endtime = time.time()
write_totaltime = write_endtime - write_starttime
logger.critical("Writing of output file complete.")
logger.critical(f"Time taken to write output file: {write_totaltime}")

# ----------------------------------------------------------------------------
# STAGE 9: VISUALISE OUTPUT AND SHOW THE PLOT
# ----------------------------------------------------------------------------

vis_starttime = time.time()

# 9.0 Upgrade the aux coor to a dim coor, so we can plot the trajectory.
# TODO: avoid doing this, as is not 'proper', when there is a way to
#       just use the aux. coor for cfp.traj: the way to support in a new
#       cf-plot version is to check if the input is a featureType, then
#       if it is to look for aux coords not dim coords, since if it is one
#       there should never be dim coords.
# TODO: another cpflot feature that will help here: generalise the
#       trajectory function for not just contiguous ragged array, as
#       the present docs state, but for any *multidimensional orthogonal
#       arrays* e.g. DSGs, as here. Talking about 'ragged arrays' is a
#       massive red herring. In which case, generalise it so that the input
#       can be a field with a 2D *or* a 1D array to plot. If 1D, it means
#       it has a trajectory dimension leading, which can be dropped.
aux_coor_t = final_result_field.auxiliary_coordinate("T")
dim_coor_t = cf.DimensionCoordinate(source=aux_coor_t)
final_result_field.set_construct(dim_coor_t, axes="ncdim%obs")

# 9.2 Set levels for plotting of data in a colourmap
# Min, max as determined using final_result_field.min(), .max():
cfp.levs(min=5e-08, max=10e-08, step=0.25e-08)

# 9.3 Make and open the final plot
# NOTE: can try 'legend_lines=True' for the lines plotted with average between
#       the two scatter marker points, if preferable?
cfp.gopen(file="final_colocated_field.png")
cfp.traj(
    final_result_field,
    verbose=VERBOSE,
    legend=True,
    markersize=5,
    linewidth=0.4,
    title="Co-located field, with model data located onto observational path",
)
cfp.gclose()

vis_endtime = time.time()
vis_totaltime = vis_endtime - vis_starttime
logger.critical("Plot created.")
logger.critical(f"Time to create plot: {vis_totaltime}")

# [END]
