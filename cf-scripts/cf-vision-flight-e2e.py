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

TODOS, SCRIPT-WIDE/GENERAL:
* document assumptions about data that we use that the input data need
  to abide by, for it to work (input data quality requirements), and quote
  that documentation here and in the script run CLI initial print-out.
* for whole script, consider what is useful to persist (Dask-wise)
  for efficiency.

"""

from itertools import pairwise  # requires Python 3.10+
from pprint import pformat
from time import time

import argparse
import functools
import json
import logging
import numpy as np
import sys

import cfplot as cfp
import cf


def timeit(func):
    """A decorator to measure and report function execution time."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time()
        output = func(*args, **kwargs)
        endtime = time()
        totaltime = endtime - starttime
        print(
            f"\n_____ Time taken (in s) for {func.__name__!r} to run: "
            f"{round(totaltime, 4)} _____\n"
        )
        return output

    return wrapper


def configure_logging():
    """Configure logging.

    TODO: DETAILED DOCS
    """
    # NOTE we use 'CRITICAL' level to avoid seeing cf log level messaging
    # which is a bit spammy and hides the output from this script.
    logger = logging.getLogger(__name__)
    if True:  ###if VERBOSE:  # TODO: SUB-CONFIG.
        logger.setLevel(logging.CRITICAL)
    else:
        logger.setLevel(
            logging.CRITICAL + 1
        )  # prevents even critical log messages
    return logger

logger = configure_logging()


# ----------------------------------------------------------------------------
# Define and parse configuration e.g. inputs, outputs.
# ----------------------------------------------------------------------------

# TODO this will be input as a config. file external to the script, eventually
# This, in particular, is the custom config. input for FAAM STANCO data.
CONFIG_CUSTOM_INPUT = {
    # Note (for dev. using repo) the values given here assume we run the
    # script from the repo root i.e. via
    # 'python cf-scripts/cf-vision-flight-e2e.py'
    # where the data has been placed under a 'data' directory as follows:
    "DATA_DIR_LOC": "data",
    "OBS_DATA_DIR": "compliant-data/core_faam_20170703_c016_STANCO_CF.nc",
    "MODEL_DATA_DIR": "main-workwith-test-ISO-simulator/Model_Input",
    "CHOSEN_OBS_FIELDS": 0,
    "CHOSEN_MODEL_FIELDS": -2,
    "OUTPUTS_DIR": "cf-script-outputs",
    "OUTPUT_FILE_NAME": "cf_vision_result_field.nc",
    "REGRID_Z_COORD": "air_pressure",
    "PLOT_OF_INPUT_OBS_TRACK_ONLY": 2,
    "CFP_MAPSET_CONFIG": {
        "lonmin": -2,
        "lonmax": 2,
        "latmin": 50,
        "latmax": 54,
        "resolution": "10m",
    },
    "CFP_INPUT_LEVS_CONFIG": {
        "min": -5,
        "max": 55,
        "step": 5,
    },
    "CFP_OUTPUT_LEVS_CONFIG": {
        "min": 5e-08,
        "max": 10e-08,
        "step": 0.25e-08,
    },
}

CONFIG_DEFAULTS = {
    # *** Script running options ***
    # Configure messaging to STDOUT, which is very verbose if INFO=True, else
    # as minimal as allows without log control in cf-plot (at present).
    # TODO: Get ESMF logging via cf incoporated into Python logging system,
    # see Issue #286.
    "VERBOSE": True,
    # *** Input data choices ***
    "DATA_DIR_LOC": ".",
    "OBS_DATA_DIR": ".",
    "MODEL_DATA_DIR": ".",
    # Extract input fields from input FieldList.
    # If these are set to False, then the whole FieldList will be taken.
    # Otherwise should be set to a valid index or slice, to be taken on the
    # FieldList.
    "CHOSEN_OBS_FIELDS": False,
    "CHOSEN_MODEL_FIELDS": False,
    # *** Output choices ***
    # A given directory must exist already, if specified.
    "OUTPUTS_DIR": ".",
    "OUTPUT_FILE_NAME": "vision_toolkit_result_field.nc",
    # Gets added to the 'history' property on the output file:
    "HISTORY_MESSAGE": (
        "Processed using the NCAS VISION Toolkit to "
        "colocate from model data to the observational data "
        "spatio-temporal location."
    ),
    # *** Regridding options, to configure the 4D interpolation ***
    "REGRID_METHOD": "linear",
    # Note this option except in rare cases won't be required, as should almost
    # always be able to determine what z-coordinate want given it must be
    # present in both the model and the observational data, so match those.
    # Only if both data have more than one of identical z-coord do we need
    # to ask for this info.
    "REGRID_Z_COORD": None,  # default to None given above note
    # *** Plotting: what to plot and how to minimally configure it ***
    "PLOTNAME_START": "vision_toolkit",
    # Optionally, display plots of the input observational data, or its track
    # only in one colour (if 'PLOT_OF_INPUT_OBS_TRACK_ONLY' is set to True).
    # This could be useful for previewing the track to be colocated
    # onto, to fail early if the user isn't happy with the track,
    # or for demo'ing the code to compare the original observational data
    # to the co-located data to see the differences.
    "SHOW_PLOT_OF_INPUT_OBS": True,
    # Bool but for dev. purposes, if set to 2 then it shows both plots:
    "PLOT_OF_INPUT_OBS_TRACK_ONLY": True,
    # "parula" also works well, as alternative for dev. work:
    "CFP_CSCALE": "plasma",
    "CFP_MAPSET_CONFIG": {},
    "CFP_INPUT_LEVS_CONFIG": {},
    "CFP_INPUT_TRACK_ONLY_CONFIG": {
        ###"verbose": VERBOSE  # TODO: SUB-CONFIG.
        "legend": True,
        "colorbar": False,
        "markersize": 0.5,
        "linewidth": 0,  # turn off line plotting to only have markers
        "title": (
            "Flight track from observational field to co-locate model "
        "field onto"
        ),
    },
    "CFP_OUTPUT_LEVS_CONFIG": {},
    "CFP_OUTPUT_GENERAL_CONFIG": {
        ###"verbose": VERBOSE  # TODO: SUB-CONFIG.
        "legend": True,
        "markersize": 5,
        "linewidth": 0.4,
        "title": "Co-located result: model co-located onto observational path",
    },
}


def process_config():
    """Process a configuration file.

    TODO: DETAILED DOCS
    """
    parser = argparse.ArgumentParser(prog="VISION TOOLKIT")
    process_config_file(parser)
    args = process_cli_arguments(parser)

    print(args.__dir__())
    logger.critical(
        f"Parsed configuration arguments are:\n{pformat(args)}\n")
    return args


def process_config_file(parser):
    """Process a configuration file.

    TODO: DETAILED DOCS
    """
    # Overwrite default config. with any custom supplied config., so that
    # the CONFIG_CUSTOM_INPUT replaces values for keys in CONFIG_DEFAULTS.
    config_input = {**CONFIG_DEFAULTS, **CONFIG_CUSTOM_INPUT}
    logger.critical(
        "Raw (before argparse processing) input config. comprising custom "
        f"config. overriding defaults dict is:\n{pformat(config_input)}\n"
    )

    # Use this dict to update the CLI defaults. For tracing external
    # config. we use capitalised keys when defining in dicts/json but need
    # these as lower case for the CLI, hence case conversion.
    config_cli_input = {k.lower(): v for k, v in config_input.items()}
    parser.set_defaults(**dict(config_cli_input))


def process_cli_arguments(parser):
    """Parse and process all command-line arguments.

    TODO: DETAILED DOCS
    """
    # Add arguments with basic type check (string is default, so no need for
    # type=str)
    parser.add_argument(
        "--data_dir_loc", action="store", help="HELP TODO")
    parser.add_argument(
        "--obs_data_dir", action="store", help="HELP TODO")
    parser.add_argument(
        "--model_data_dir", action="store", help="HELP TODO")

    # Need an index or slice for thes e2, hence integer or slice object, but given
    # argparse isn't degined to handle this, accept as string and parse later.
    parser.add_argument(
        "--chosen_obs_fields", action="store", help="HELP TODO")
    parser.add_argument(
        "--chosen_model_fields", action="store", help="HELP TODO")

    parser.add_argument(
        "--outputs_dir", action="store", help="HELP TODO")
    parser.add_argument(
        "--output_file_name", action="store", help="HELP TODO")
    parser.add_argument(
        "--history_message", action="store", help="HELP TODO")
    parser.add_argument(
        "--regrid_method", action="store", help="HELP TODO")
    parser.add_argument(
        "--regrid_z_coord", action="store", help="HELP TODO")
    parser.add_argument(
        "--plotname_start", action="store", help="HELP TODO")
    parser.add_argument(
        "--show_plot_of_input_obs", action="store", help="HELP TODO")
    parser.add_argument(
        "--plot_of_input_obs_track_only", action="store",
        help="HELP TODO"
    )
    parser.add_argument(
        "--cfp_cscale", action="store", help="HELP TODO")

    # These config. parameters are compound, and argparse can't handle multiple
    # key-values e.g. dicts well, so use 'json.loads' (or e.g. 'yaml.load') to
    # input sub-config. as a working method.
    parser.add_argument(
        "--cfp_mapset_config", action="store", help="HELP TODO",
        type=json.loads
    )
    parser.add_argument(
        "--cfp_input_levs_config", action="store", help="HELP TODO",
        type=json.loads
    )
    parser.add_argument(
        "--cfp_input_track_only_config", action="store", help="HELP TODO",
        type=json.loads
    )
    parser.add_argument(
        "--cfp_output_levs_config", action="store", help="HELP TODO",
        type=json.loads
    )
    parser.add_argument(
        "--cfp_output_general_config", action="store", help="HELP TODO",
        type=json.loads
    )

    # 'bool() function is not recommended as a type converter, see
    # https://docs.python.org/3/library/argparse.html#argparse-type
    parser.add_argument("--verbose", action="store", help="HELP TODO")

    return parser.parse_args()


# ----------------------------------------------------------------------------
# Main functions
# ----------------------------------------------------------------------------

def get_env_and_diagnostics_report():
    """Provide an optional report of environment and diagnostics.

    TODO: DETAILED DOCS
    """
    logger.critical(
        "Using Python and CF environment of:\n"
        f"{cf.environment(display=False)}\n"
    )


@timeit
def read_obs_input_data(data_dir_loc, obs_data_dir):
    """Read in all observational input data.

    TODO: DETAILED DOCS
    """
    obs_data_loc = f"{data_dir_loc}/{obs_data_dir}"
    return cf.read(obs_data_loc), obs_data_loc


@timeit
def read_model_input_data(data_dir_loc, model_data_dir):
    """Read in all model input data.

    TODO: DETAILED DOCS
    """
    model_data_loc = f"{data_dir_loc}/{model_data_dir}"
    return cf.read(model_data_loc), model_data_loc


def read_input_data(data_dir_loc, obs_data_dir, model_data_dir):
    """Read in all input data.

    TODO: DETAILED DOCS
    """
    get_env_and_diagnostics_report()
    obs_data, obs_data_loc = read_obs_input_data(
        data_dir_loc, obs_data_dir)
    model_data, model_data_loc = read_model_input_data(
        data_dir_loc, model_data_dir)

    # Reporting
    logger.critical("All input data successfully read in.")
    logger.critical(
        f"Input data locations are:\n"
        f"Observational data: '{obs_data_loc}'\n"
        f"Model data: '{model_data_loc}'"
    )
    report_about_input_data(obs_data, model_data)

    return obs_data, model_data


def report_about_input_data(obs_data, model_data):
    """Read in all input data.

    TODO: DETAILED DOCS
    """
    logger.critical(f"Observational data is:\n {obs_data}")
    logger.critical("For example, first observational field is:\n")
    logger.critical(obs_data[0].dump(display=False))

    logger.critical(f"Model data is:\n {model_data}")
    logger.critical("For example, first model field is:\n")
    logger.critical(model_data[0].dump(display=False))


@timeit
def get_input_fields_of_interest(
        obs_data, model_data, chosen_obs_fields, chosen_model_fields):
    """Return fields of interest from input datasets.

    TODO: DETAILED DOCS
    """
    # Take only relevant fields from the list of fields read in
    obs_field = obs_data[chosen_obs_fields]
    model_field = model_data[chosen_model_fields]

    return obs_field, model_field


@timeit
def make_preview_plots(
    obs_field, show_plot_of_input_obs,
    plot_of_input_obs_track_only,
    outputs_dir, plotname_start,
    cfp_mapset_config, cfp_cscale, cfp_input_levs_config,
    cfp_input_track_only_config,
    cfp_input_general_config, verbose
):
    """Generate plots of the flight track for a pre-colocation preview.

    TODO: DETAILED DOCS
    """
    # First configure general settings for plot:
    # Change the viewpoint to be over the UK only, with high-res map outline
    cfp.mapset(**cfp_mapset_config)
    cfp.cscale(cfp_cscale)

    if show_plot_of_input_obs:
        # Plot *input* observational data for a preview, before doing anything
        # Min, max as determined using final_result_field.min(), .max():
        cfp.levs(**cfp_input_levs_config)
        if plot_of_input_obs_track_only in (1, 2):
            # Use the same field but set all data to zero so can plot the whole
            # track in the same colour to just display the path, not orig. data
            equal_data_obs_field = obs_field.copy()
            new_data = np.zeros(
                len(equal_data_obs_field.data)
            )  # 0 -> force red with colour scheme set later
            equal_data_obs_field.set_data(new_data, inplace=True)

            # Not configurable, always use since it gives red for zero values
            cfp.cscale("scale28")
            cfp.gopen(
                file=f"{outputs_dir}/{plotname_start}_obs_track_only.png"
            )
            cfp.traj(equal_data_obs_field, **cfp_input_track_only_config)
            cfp.gclose()
            cfp.cscale(cfp_cscale)  # reset for normal (default-style) plots after
        if plot_of_input_obs_track_only in (0, 2):
            cfp.gopen(
                file=f"{outputs_dir}/{plotname_start}_obs_track_with_data.png"
            )
            cfp_input_general_config = {
                "verbose": verbose,
                "legend": True,
                "markersize": 5,
                "linewidth": 0.4,
                "title": (
                    "Observational field input (path, to be used for "
                    "co-location, with its corresponding data, to be ignored)"
                ),
            }
            cfp.traj(obs_field, **cfp_input_general_config)
            cfp.gclose()


@timeit
def ensure_cf_compliance(obs_field, model_field):
    """Ensure the chosen fields are CF compliant with the correct format.

    TODO: DETAILED DOCS
    """
    # SOME DATA PROCESSING AND VALIDATION, INCLUDING (ONLY?) ATTACHING
    # THE OROGRAPHY -> MANIPULATING THE FIELDS A BIT.
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
    #
    # TODO: IGNORE FOR NOW, USING FILES ALREADY MADE COMPLIANT
    pass


def get_time_coords(obs_field, model_field):
    """Return the relevant time coordinates from the fields.

    TODO: DETAILED DOCS
    """
    # Observational data is a DSG so should always have T as an aux. coord.
    obs_times = obs_field.auxiliary_coordinate("T")
    model_times = model_field.dimension_coordinate("T")

    return obs_times, model_times


@timeit
def ensure_unit_calendar_consistency(obs_field, model_field):
    """Ensure the chosen fields have consistent units and calendars.

    TODO: DETAILED DOCS
    """
    obs_times, model_times = get_time_coords(obs_field, model_field)

    # Ensure the units of the obs and model datetimes are consistent - conform
    # them if they differ (if they don't, Units setting operation is harmless).
    obs_times_units = obs_times.Units
    logger.critical(f"Units on obs. time coordinate are: {obs_times_units}")

    model_times_units = model_times.Units
    logger.critical(f"Units on model time coordinate are: {model_times_units}")

    # Change the units on the model (not obs) times since there are fewer
    # data points on those, meaning less converting work.
    model_times.Units = obs_times_units

    logger.critical(f"Unit-conformed model time coord. is: {model_times}")
    # Get the time coordinates again to ensure/assert conversion on field
    same_units = (
        get_time_coords(obs_field, model_field)[0].data.Units,
        get_time_coords(obs_field, model_field)[1].data.Units,
    )
    logger.critical(
        f"Units on observational and model time coords. are the same?: "
        f"{same_units}\n"
    )

    # Ensure calendars are consistent, if not convert to equivalent.
    #
    # TODO what to do if calendar conversion means missing days when need them?
    #      look at Maria's code as to how it is dealt with (e.g. in CIS)
    #
    # NOTE: in this case, they are the same (gregorian and standard are the
    # same).
    # TODO IGNORE FOR NOW (consistent in this case, but will need to generalise
    # for when they are not).
    obs_calendar = obs_times.calendar
    logger.critical(f"Calendar on obs. time coordinate is: {obs_calendar}")

    model_calendar = model_times.calendar
    logger.critical(f"Calendar on model time coordinate is: {model_calendar}")

    same_calendar = (
        get_time_coords(obs_field, model_field)[0].calendar,
        get_time_coords(obs_field, model_field)[1].calendar,
    )
    logger.critical(
        f"Calendars on observational and model time coords. are the same?: "
        f"{same_calendar}\n"
    )


@timeit
def subspace_to_spatiotemporal_bounding_box(obs_field, model_field):
    """Extract only relevant data in the model field via a 4D subspace.

    Relevant data is extracted in the form of a field comprising the model
    field reduced to a 'bounding box' in space and in time, such that data
    outside the scope of the observational data track, with an extra
    index-space 'halo' added to include points of relevance to the outer-most
    points, is removed, because it is not relevant to the colocation.

    TODO: DETAILED DOCS
    """
    obs_times, model_times = get_time_coords(obs_field, model_field)

    # TODO: ensure this works for flights that take off on one day and end on
    # another e.g. 11 pm - 3 am flight.

    # Prep. towards the BB component subspace.
    # Find the spatial obs. path X-Y-Z boundaries to crop the model field to.
    #     Note: avoid calling these 'bounds' since that has meaning in CF, so
    #           to prevent potential ambiguity/confusion.

    # For a DSG, the spatial coordinates will always be auxiliary:
    obs_X = obs_field.auxiliary_coordinate("X")
    obs_Y = obs_field.auxiliary_coordinate("Y")
    obs_Z = obs_field.auxiliary_coordinate("Z")

    # Prep. towards the temporal BB component.
    # TODO: are we assuming the model and obs data are strictly increasing, as
    # we might be assuming for some of this. - > trajectories should be
    # including with time with indices getting higher. Otherwise might need
    # to use .sort() etc.
    #
    # NOTE: use max and min to account for any missing data even at endpoints,
    #       as opposed to taking the values at first and last position/index.

    # Perform the 4D spatio-temporal bounding box to reduce the model data down
    # to only that which is relevant for the calculations on the observational
    # data path in 4D space, that is:
    #     * a spatial 3D X-Y-Z subspace to spatially bound to those values;
    #     * a time 1D T subspace to bound it in time i.e. cover only
    #       relevant times

    # Note: this requires a 'halo' config. feature introduced in
    #       cf-python 3.16.2.
    # TODO SLB: need to think about possible compications of cyclicity, etc.,
    #           and account for those.
    # Note: getting some dask arrays out instead of slices, due to Dask
    # laziness. DH to look into.

    x_coord_tight_bounds = obs_X.data.minimum(), obs_X.data.maximum()
    y_coord_tight_bounds = obs_Y.data.minimum(), obs_Y.data.maximum()
    z_coord_tight_bounds = obs_Z.data.minimum(), obs_Z.data.maximum()
    t_coord_tight_bounds = obs_times.data.minimum(), obs_times.data.maximum()
    logger.critical(
        "Set to create 4D bounding box onto model field, based on obs. field "
        "tight boundaries of (4D: X, Y, Z, T):\n"
        f"X: {x_coord_tight_bounds}\n"
        f"Y: {y_coord_tight_bounds}\n"
        f"Z: {z_coord_tight_bounds}\n"
        f"T: {t_coord_tight_bounds}\n"
    )
    if VERBOSE:  # conditional avoids this calculation twice unless VERBOSE
        model_field_bb_indices = model_field.indices(
            1,  # the halo size that extends the bounding box by 1 in index space
            X=cf.wi(*x_coord_tight_bounds),
            Y=cf.wi(*y_coord_tight_bounds),
            Z=cf.wi(*z_coord_tight_bounds),
            T=cf.wi(*t_coord_tight_bounds),
        )
        logger.critical(
            "Indices of model field bounding box subspace are:"
            f"{model_field_bb_indices}"
        )

    # Note: can do the spatial and the temporal subspacing separately, and if
    # want to do this make the call twice for each coordinate arg. Reasons we
    # may want to do this include having separate halo sizes for each
    # coordinate, etc.
    model_field_bb = model_field.subspace(
        1,  # the halo size that extends the bounding box by 1 in index space
        X=cf.wi(*x_coord_tight_bounds),
        Y=cf.wi(*y_coord_tight_bounds),
        Z=cf.wi(*z_coord_tight_bounds),
        T=cf.wi(*t_coord_tight_bounds),
    )

    logger.critical(
        "4D bounding box calculated. Model data with bounding box applied is: "
        f"{model_field_bb}"
    )

    return model_field_bb


@timeit
def spatial_interpolation(obs_field, model_field_bb):
    """Interpolate the flight path spatially (3D for X-Y and vertical Z).

    Horizontal X-Y and vertical Z coordinates are interpolated. This is
    done under-the-hood in cf-python with the ESMF LocStream feature, see:
    https://xesmf.readthedocs.io/en/latest/notebooks/Using_LocStream.html

    TODO: DETAILED DOCS
    """
    # TODO: UGRID grids might need some extra steps/work for this.

    logger.critical("Starting spatial interpolation (regridding) step...")

    # Creating the spatial bounding box may have made some of the spatial
    # dimensions singular, which would lead to an error or:
    #     ValueError: Neither the X nor Y dimensions of the source field
    #     <field> can be of size 1 for spherical 'linear' regridding.
    # so we have to account for this.

    # Perform the spherical regrid which does the spatial interpolation
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

    # TODO: consider whether or not to persist the regridded / spatial interp
    # before the next stage, or to do in a fully lazy way.

    logger.critical("\nSpatial interpolation (regridding) complete.\n")
    logger.critical(f"XYZ-colocated data is:\n {spatially_colocated_field}")

    return spatially_colocated_field


@timeit
def time_interpolation(
    obs_times, model_times, obs_field, model_field, spatially_colocated_field
):
    """Interpolate the flight path temporally (in time T).

    This co-locates between model data time points to match the time
    coordinate sampling of the flight path and is done using a method that
    performs a convolution-based merge of relevant segments of the
    (bouding box subspaced) model field already interpolated spatially onto
    the flight path.

    TODO: DETAILED DOCS
    """
    logger.critical("Starting time interpolation step.\n")

    # In our field after spatial interpolation, the Dimension Coord has the
    # model time data and the Aux Coord has the observational time data
    # NOTE: keep these calls in, desite earlier ones probably in-place.
    model_times = spatially_colocated_field.dimension_coordinate("T")
    obs_times = spatially_colocated_field.auxiliary_coordinate("T")
    model_times_len = len(model_times.data)
    obs_times_len = len(obs_times.data)

    logger.critical(
        f"Number of model time data points: {model_times_len}\n"
        f"Number of observational time sample data points: {obs_times_len}\n"
    )

    # Setup ready for iteration...
    # Constructs
    m = spatially_colocated_field.copy()
    # Observations, if DSG, will always be the auxiliary coordinate time
    obs_time_key = m.auxiliary_coordinate("T", key=True)
    # Model data time must always be a dimension coordinate
    model_time_key = m.dimension_coordinate("T", key=True)
    logger.critical(f"Observational (aux) coord. time key is: {obs_time_key}")
    logger.critical(f"Model (dim) time key is: {model_time_key}\n")

    # Empty objects ready to populate - TODO make these FieldLists if approp.?
    datetime_segments = []
    v_w = []

    # Iterate over pairs of adjacent model datetimes, defining 'segments'.
    # Chop the flight path up into these *segments* and do a weighted merge
    # of data from segments adjacent in the model times to form the final
    # time-interpolated value.
    logger.critical("*** Begin iteration over pairwise 'segments'. ***")
    for index, (t1, t2) in enumerate(pairwise(model_times.datetime_array)):
        logger.critical(f"\n*** Segment {index} ***\n")
        # Define the pairwise segment datetime endpoints
        logger.critical(
            f"Datetime endpoints for this segment are: {t1}, {t2}.\n"
        )
        datetime_segments.append((t1, t2))

        # Define a query which will find any datetimes within these times
        # to map all observational times to the appropriate segment, later.
        q = cf.wi(
            cf.dt(t1), cf.dt(t2), open_upper=True
        )  # TODO is cf.dt wrapping necessary?
        logger.critical(f"Querying with query: {q} on field:\n{m}\n")

        # Subspace the observational times to match the segments above,
        # namely using the query created above.
        # Use a direct subspace method, which works generally.
        #
        # NOTE: without the earlier bounding box step, this will fail due to
        #       not being able to find the subspace at irrelevant times.
        s0_subspace_args = {
            obs_time_key: q,
            model_time_key: [index],
        }
        logger.critical(
            f"\nUsing subspace arguments for i=0 of: {s0_subspace_args}\n"
        )
        s0 = m.subspace(**s0_subspace_args)

        s1_subspace_args = {
            obs_time_key: q,
            model_time_key: [index + 1],
        }
        logger.critical(
            f"Using subspace arguments for i=1 of: {s1_subspace_args}\n"
        )
        s1 = m.subspace(**s1_subspace_args)

        # Squeeze here to remove size 1 dim ready for calculations to come,
        # i.e. to unpack from '[[ ]]' shape(1, N) structure.
        # NOTE: a=0 and b=1 from old/whiteboard schematic and notes).
        values_0 = s0.data.squeeze()
        values_1 = s1.data.squeeze()

        # Calculate the arrays to be used in the weighting calculation. All
        # arithmetic done numpy-array wise, so no need to iterate over values.
        #
        # NOTE: converted to data to get data array not dim coord as output for
        #       weighted values.
        # TODO: take care using keys! We can't rely on keys being consistent
        #       between different fields, so may need to re-determine these at
        #       different steps, else (ideally) find a robust way not using
        #       keys to pick out the relevant time constructs.
        # NOTE: All calc. variables are arrays, except this first one,
        #       a scalar (constant whatever the obs time)
        distance_01 = (
            s1.dimension_coordinate("T") - s0.dimension_coordinate("T")
        ).data
        distances_0 = (
            s0.auxiliary_coordinate("T")[index] - s0.dimension_coordinate("T")
        ).data

        # Calculate the datetime 'distances' to be used for the weighting
        distances_1 = distance_01 - distances_0
        weights_0 = distances_1 / distance_01
        weights_1 = distances_0 / distance_01

        # Calculate the final weighted values using a basic weighting
        # formulae.
        # NOTE: by the maths, the sum of the two weights should be 1, so there
        #       is no need to divide by that, though confirm with a print-out
        logger.critical(
            "Weights total (should be 1.0, as a validation check) is: "
            f"{(weights_0 + weights_1).array[0]}\n"
        )

        values_weighted = weights_0 * values_0 + weights_1 * values_1
        v_w.append(values_weighted)

    # NOTE: masked values are mostly/all to do with the pressure being below
    #       when flight lands and takes off etc. on runway and close, cases
    #       relating to the Heaviside function. So it is all good and expected
    #       to have masked values in the data, at the end and/or start.
    #       Eventually we will add an extrapolation option whereby user can
    #       choose to extrapolate as well as interpolate, and therefore assign
    #       values to the masked ones.
    logger.critical("Final per-segment weighted value arrays are:")
    logger.critical(pformat(v_w))

    # Concatenate the data values found above from each segment, to finally
    # get the full set of model-to-obs co-located data.
    concatenated_weighted_values = cf.Data.concatenate(v_w)
    logger.critical(
        "\nFinal concatenated weighted value array is: "
        f"{concatenated_weighted_values.array}, with length: "
        f"{len(concatenated_weighted_values)}\n"
    )

    # For info, report on number of masked and unmasked data points
    masked_value_count = (
        len(concatenated_weighted_values)
        - concatenated_weighted_values.count()
    ).array[0]
    logger.critical(
        f"Masking: {concatenated_weighted_values.count().array[0]} "
        f"non-masked values vs. {masked_value_count} masked."
    )

    # Finally, reattach that data to (a copy of) the obs field to get final
    # values on the right domain, though we still need to adapt the metadata to
    # reflect the new context so that the field with data set is contextually
    # correct.
    final_result_field = obs_field.copy()
    final_result_field.set_data(concatenated_weighted_values)

    # Finally, re-set the properties on the final result field so it has model
    # data properties not obs preoprties.
    # * General properties
    final_result_field.clear_properties()
    final_result_field.set_properties(model_field.properties())
    # * Add new, or append to if already exists, 'history' property
    #   details to say that we colocated etc. with VISION / cf.
    history_details = final_result_field.get_property("history")
    history_details += (
        " ~ " + HISTORY_MESSAGE
    )  # include divider to previous info
    final_result_field.set_property("history", history_details)
    logger.critical(
        "\nNew history message reads: "
        f"{final_result_field.get_property('history')}\n"
    )

    logger.critical("\nFinal result field is:\n" f"\n{final_result_field}\n")
    logger.critical("The final result field has data statistics of:\n")
    logger.critical(pformat(final_result_field.data.stats()))

    # TODO: consider whether or not to persist the regridded / time interp.
    # before the next stage, or to do in a fully lazy way.

    logger.critical("\nTime interpolation complete.")

    return final_result_field


@timeit
def create_cra_outputs():
    """Create a compressed contiguous ragged array DSG output.

    Concatenates and aggregates the colocated flight path results across all
    of the relevant days sepcified, creating a discrete sampling
    geometry (DSG), specifically a contiguous ragged array, to encompass all
    of these. This is compressed and returned.

    TODO: ARGS
    TODO: DETAILED DOCS
    """
    # TODO IGNORE FOR NOW
    pass


@timeit
def write_output_data(final_result_field):
    """Write out the 4D (XYZT) colocated result as output data.

    TODO: DETAILED DOCS
    """

    # Write final field result out to file on-disk
    cf.write(final_result_field, OUTPUT_FILE_NAME)

    logger.critical("Writing of output file complete.")


@timeit
def make_outputs_plots(final_result_field):
    """Generate plots of the flight track for a pre-colocation preview.

    The plots may optionally be displayed duering script execution, else
    saved to disk.

    TODO: DETAILED DOCS
    """

    # Upgrade the aux coor to a dim coor, so we can plot the trajectory.
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

    # Set levels for plotting of data in a colourmap
    # Min, max as determined using final_result_field.min(), .max():
    cfp.levs(**CFP_OUTPUT_LEVS_CONFIG)

    # Make and open the final plot
    # NOTE: can try 'legend_lines=True' for the lines plotted with average
    #       between the two scatter marker points, if preferable?
    cfp.gopen(file=f"{OUTPUTS_DIR}/{PLOTNAME_START}_final_colocated_field.png")

    cfp.traj(final_result_field, **CFP_OUTPUT_GENERAL_CONFIG)
    cfp.gclose()

    logger.critical("Plot created.")


@timeit
def main():
    """Perform end-to-end model-to-observational co-location."""
    # Manage inputs from CLI and from configuration file, if present.
    args = process_config()
    # Now set variables so they can be passed only to fucntions that need them
    data_dir_loc = args.data_dir_loc
    obs_data_dir = args.obs_data_dir
    model_data_dir = args.model_data_dir
    chosen_obs_fields = args.chosen_obs_fields
    chosen_model_fields = args.chosen_model_fields
    outputs_dir = args.outputs_dir
    output_file_name = args.output_file_name
    history_message = args.history_message
    regrid_method = args.regrid_method
    regrid_z_coord = args.regrid_z_coord
    plotname_start = args.plotname_start
    show_plot_of_input_obs = args.show_plot_of_input_obs
    plot_of_input_obs_track_only = args.plot_of_input_obs_track_only
    cfp_cscale = args.cfp_cscale
    cfp_mapset_config = args.cfp_mapset_config
    cfp_input_levs_config = args.cfp_input_levs_config
    cfp_input_track_only_config = args.cfp_input_track_only_config
    cfp_output_levs_config = args.cfp_output_levs_config
    cfp_output_general_config = args.cfp_output_general_config
    verbose = args.verbose

    # Process and validate inputs, including optional flight track preview plot
    obs_data, model_data = read_input_data(
        data_dir_loc, obs_data_dir, model_data_dir)
    obs_field, model_field = get_input_fields_of_interest(
        obs_data, model_data, chosen_obs_fields, chosen_model_fields)

    # TODO: this has too many parametres for one function, separate out
    make_preview_plots(
        obs_field, show_plot_of_input_obs,
        plot_of_input_obs_track_only,
        outputs_dir, plotname_start,
        cfp_mapset_config, cfp_cscale, cfp_input_levs_config,
        cfp_input_track_only_config,
        cfp_input_general_config, verbose
    )
    ensure_cf_compliance(obs_field, model_field)  # TODO currently does nothing

    # Time coordinate considerations, pre-colocation
    obs_times, model_times = get_time_coords(obs_field, model_field)
    ensure_unit_calendar_consistency(obs_field, model_field)

    # Subspacing to remove irrelavant information, pre-colocation
    model_field_bb = subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field
    )

    # Perform spatial and then temporal interpolation to colocate
    spatially_colocated_field = spatial_interpolation(
        obs_field, model_field_bb
    )
    final_result_field = time_interpolation(
        obs_times,
        model_times,
        obs_field,
        model_field,
        spatially_colocated_field,
    )

    # Create and process outputs
    create_cra_outputs()  # TODO currently does nothing
    write_output_data(final_result_field)
    make_outputs_plots(final_result_field)


if __name__ == "__main__":
    sys.exit(main())
