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
import copy
import functools
import json
import logging
import numpy as np
import sys

import cfplot as cfp
import cf


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


def timeit(func):
    """A decorator to measure and report function execution time."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time()
        output = func(*args, **kwargs)
        endtime = time()
        totaltime = endtime - starttime
        # TODO use logging instead of a direct print
        print(
            f"\n_____ Time taken (in s) for {func.__name__!r} to run: "
            f"{round(totaltime, 4)} _____\n"
        )
        return output

    return wrapper


# ----------------------------------------------------------------------------
# Define custom errors
# ----------------------------------------------------------------------------

class CFComplianceIssue(Exception):
    """Raised for cases of errors caused by lack of CF Compliance."""
    pass


# ----------------------------------------------------------------------------
# Define and parse configuration e.g. inputs, outputs.
# ----------------------------------------------------------------------------

CONFIG_DEFAULTS = {
    # *** Script running options ***
    # Configure messaging to STDOUT, which is very verbose if INFO=True, else
    # as minimal as allows without log control in cf-plot (at present).
    # TODO: Get ESMF logging via cf incoporated into Python logging system,
    # see Issue #286.
    "verbose": True,
    # *** Input data choices ***
    "input-data-dir-loc": ".",
    "obs-data-dir": ".",
    "model-data-dir": ".",
    # Extract input fields from input FieldList.
    # If these are set to False, then the whole FieldList will be taken.
    # Otherwise should be set to a valid index or slice, to be taken on the
    # FieldList.
    "chosen-obs-fields": False,
    "chosen-model-fields": False,
    # *** Output choices ***
    # A given directory must exist already, if specified.
    "outputs-dir": ".",
    "output-file-name": "vision_toolkit_result_field.nc",
    "history-message": (
        "Processed using the NCAS VISION Toolkit to "
        "colocate from model data to the observational data "
        "spatio-temporal location."
    ),
    # *** Regridding options, to configure the 4D interpolation ***
    "regrid-method": "linear",
    # Note this option except in rare cases won't be required, as should almost
    # always be able to determine what z-coordinate want given it must be
    # present in both the model and the observational data, so match those.
    # Only if both data have more than one of identical z-coord do we need
    # to ask for this info.
    "regrid-z-coord": None,  # default to None given above note
    # *** Plotting: what to plot and how to minimally configure it ***
    "plotname-start": "vision_toolkit",
    # Optionally, display plots of the input observational data, or its track
    # only in one colour (if 'plot-of-input-obs-track-only' is set to True).
    # This could be useful for previewing the track to be colocated
    # onto, to fail early if the user isn't happy with the track,
    # or for demo'ing the code to compare the original observational data
    # to the co-located data to see the differences.
    "show-plot-of-input-obs": True,
    # Bool but for dev. purposes, if set to 2 then it shows both plots:
    "plot-of-input-obs-track-only": True,
    # "parula" also works well, as alternative for dev. work:
    "cfp-cscale": "plasma",
    "cfp-mapset-config": {},
    "cfp-input-levs-config": {},
    "cfp-input-track-only-config": {
        "legend": True,  # TODO sepaarte into setvars config and plot opts
        "colorbar": False,
        "markersize": 0.5,
        "linewidth": 0,  # turn off line plotting to only have markers
        "title": (
            "Flight track from observational field to co-locate model "
            "field onto"
        ),
    },
    "cfp-input-general-config": {
        "legend": True,  # TODO sepaarte into setvars config and plot opts
        "markersize": 5,
        "linewidth": 0.4,
        "title": (
            "Observational field input (path, to be used for "
            "co-location, with its corresponding data, to be ignored)"
        ),
    },
    "cfp-output-levs-config": {},
    "cfp-output-general-config": {
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
    parser = argparse.ArgumentParser(
        prog="VISION TOOLKIT",
        description=(
            "Virtual Integration of Satellite and In-Situ Observation "
            "Networks (VISION) toolkit flight simulator"
        ),
    )

    # Set CLI defaults for anything not specified via CLI
    #
    # Want config. file input to have identical key names to the CLI ones,
    # namely with underscores as word delimiters, but for processing defaults
    # have to use hyphens since argparse converts to these for valid attr names
    config_cli_input = {
        k.replace("-", "_"): v for k, v in CONFIG_DEFAULTS.items()
    }
    parser.set_defaults(**config_cli_input)

    args = process_cli_arguments(parser)
    # Can't print pre-parsed config. until here, else this logging message
    # will appear to spam the '--help' option output.
    logger.critical(
        f"Default configuration is:\n{pformat(config_cli_input)}\n"
    )
    logger.critical(
        f"Parsed CLI configuration arguments are:\n{pformat(args)}\n"
    )

    config_file = args.config_file
    if config_file:
        config_from_file = process_config_file(config_file)

    # Overwrite config. provided via the CLI with any config. specified by
    # in the config. file given with --config-file argument:
    final_config_namespace = copy.copy(args)
    for key, value in vars(args).items():
        match_key = key.replace("_", "-")
        if match_key in config_from_file:
            setattr(final_config_namespace, key, config_from_file[match_key])

    logger.critical(
        "Final input configuration, considering CLI inputs including "
        "application of config from specified config. file via "
        "--config-file is:"
        f"\n{pformat(final_config_namespace)}\n"
    )
    return final_config_namespace


def process_config_file(config_file):
    """Process a configuration file.

    TODO: DETAILED DOCS
    """
    with open(config_file) as f:
        try:
            j = json.load(f)
        except:
            raise ValueError("Bad JSON configuration file.")  # TODO better msg

    logger.critical(f"Succesfully read-in JSON config. file at: {config_file}")

    # TODO validation on keys
    # TODO allow YAML config. format as well.

    return j


def process_cli_arguments(parser):
    """Parse and process all command-line arguments.

    TODO: DETAILED DOCS
    """
    # Add arguments with basic type check (string is default, so no need for
    # type=str)
    # 'bool() function is not recommended as a type converter, see
    # https://docs.python.org/3/library/argparse.html#argparse-type
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="provide detailed output [TODO ENABLE VARIOUS LEVELS VIA LOGGING]",
    )
    parser.add_argument(
        "-c",
        "--config-file",
        action="store",
        help=(
            "configuration file in JSON format to supply configuration, "
            "which overrides any configuration provided by other "
            "command-line options, if duplication of input occurs"
        ),
    )
    parser.add_argument(
        "-i",
        "--input-data-dir-loc",
        action="store",
        help="path location of the top-level data directory [TODO CLARIFY]",
    )
    parser.add_argument(
        "-o",
        "--obs-data-dir",
        action="store",
        help="path location of the observational data directory [TODO CLARIFY]",
    )
    parser.add_argument(
        "-m",
        "--model-data-dir",
        action="store",
        help="path location of the model data directory [TODO CLARFIY]",
    )
    # Need an index or slice for these next 2, hence integer or slice object,
    # but given argparse isn't degined to handle this, accept as string
    # and validate later.
    parser.add_argument(
        "--chosen-obs-fields",
        action="store",
        help=(
            "index or slice to select fields from the FieldList "
            "corresponding to the read-in observational data, else "
            "the entire FieldList is used"
        ),
    )
    parser.add_argument(
        "--chosen-model-fields",
        action="store",
        help=(
            "index or slice to select fields from the FieldList "
            "corresponding to the read-in model data, else "
            "the entire FieldList is used"
        ),
    )
    parser.add_argument(
        "-d",
        "--outputs-dir",
        action="store",
        help="path location of the top-level directory to create outputs in",
    )
    parser.add_argument(
        "-f",
        "--output-file-name",
        action="store",
        help="name including extension to give the result output file",
    )
    parser.add_argument(
        "--history-message",
        action="store",
        help=(
            "message that gets added to the 'history' property on the "
            "output file"
        ),
    )
    parser.add_argument(
        "-r",
        "--regrid-method",
        action="store",
        help=(
            "regridding interpolation method to apply, see 'method' "
            "parameter to 'cf.regrids' method for options: "
            "https://ncas-cms.github.io/cf-python/method/cf.Field.regrids.html"
        ),
    )
    parser.add_argument(
        "-z",
        "--regrid-z-coord",
        action="store",
        help=(
            "vertical (z) coordinate to use as the vertical component in "
            "the spatial interpolation step"
        ),
    )
    parser.add_argument(
        "--plotname-start",
        action="store",
        help="initial text to use in the names of all plots generated",
    )
    parser.add_argument(
        "-p",
        "--show-plot-of-input-obs",
        action="store_true",
        help=(
            "flag to indicate whether to show plots of the input "
            "observational data before the colocation logic begins, as "
            "a preview"
        ),
    )
    parser.add_argument(
        "-t",
        "--plot-of-input-obs-track-only",
        action="store_true",
        help=(
            "flag to indicate whether only the track/trajectory "
            "of the observational data is shown, as opposed to the data "
            "on the track, for the input observational data preview plots"
        ),
    )
    parser.add_argument(
        "--cfp-cscale",
        action="store",
        help=(
            "cf-plot plotting configuration as a string to set the "
            "colour scale for the (input preview and) output plots, "
            "ee: https://ncas-cms.github.io/cf-plot/build/cscale.html#cscale"
        ),
    )
    parser.add_argument(
        "--cfp-mapset-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "mapping parameters for the (input preview and) output plots, "
            "see: https://ncas-cms.github.io/cf-plot/build/mapset.html#mapset"
        ),
    )
    parser.add_argument(
        "--cfp-input-levs-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "contour levels for the input preview plots, "
            "see: https://ncas-cms.github.io/cf-plot/build/levs.html#levs"
        ),
    )
    parser.add_argument(
        "--cfp-input-general-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "general plotting variables for the input preview full plot, see:"
            "https://ncas-cms.github.io/cf-plot/build/setvars.html#setvars"
            "[TODO CLARIFY/SEPARATE SETVARS AND PLOT CALL CONFIG.]"
        ),
    )
    parser.add_argument(
        "--cfp-input-track-only-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the general"
            " plotting variables for track-only input preview plot, see:"
            "https://ncas-cms.github.io/cf-plot/build/setvars.html#setvars"
        ),
    )
    parser.add_argument(
        "--cfp-output-levs-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "contour levels for the output plots, "
            "see: https://ncas-cms.github.io/cf-plot/build/levs.html#levs"
        ),
    )
    parser.add_argument(
        "--cfp-output-general-config",
        type=json.loads,
        action="store",
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "general plotting variables for the output plots, see:"
            "https://ncas-cms.github.io/cf-plot/build/setvars.html#setvars"
            "[TODO CLARIFY/SEPARATE SETVARS AND PLOT CALL CONFIG.]"
        ),
    )

    return parser.parse_args()


# ----------------------------------------------------------------------------
# Main functions
# ----------------------------------------------------------------------------
def print_toolkit_banner():
    """Provide an optional report of environment and diagnostics.

    TODO: DETAILED DOCS
    """
    # Use short variable names here to not clog up ASCII art preview below
    bhc = "\033[31m"  # bhc == banner_highlight_colour
    bfc = "\33[34m"  # bfc == banner_foreground_colour
    # Leave this at end so that the toolkit STDOUT gets this colour to
    # distinguish from other terminal text.
    rsc = "\33[32m"

    # ASCII text art was created using: http://www.patorjk.com/software/taag
    # Note '\' characters need to be escaped twice to avoid a warning of:
    # 'SyntaxWarning: invalid escape sequence', which makes the preview
    # less clear as to the overall ASCII art output, but is necessary.
    banner_text = f"""{bfc}
.______________________________________________.
|{bhc}   _     _  _   ______  _  _______  _______   {bfc}|
|{bhc}  (_)   (_)| | / _____)| |(_______)(_______)  {bfc}|
|{bhc}   _     _ | |( (____  | | _     _  _     _   {bfc}|
|{bhc}  | |   | || | \\____ \\ | || |   | || |   | |  {bfc}|
|{bhc}   \\ \\ / / | | _____) )| || |___| || |   | |  {bfc}|
|{bhc}    \\___/  |_|(______/ |_| \\_____/ |_|   |_|  {bfc}|
|   _______             _   _      _           {bfc}|
|  (_______)           | | | |    (_)   _      {bfc}|
|      _   ___    ___  | | | |  _  _  _| |_    {bfc}|
|     | | / _ \\  / _ \\ | | | |_/ )| |(_   _)   {bfc}|
|     | || |_| || |_| || | |  _ ( | |  | |_    {bfc}|
|     |_| \\___/  \\___/  \\_)|_| \\_)|_|   \\__)   {bfc}|
.______________________________________________.{rsc}                                         
    """

    print(banner_text)


def get_env_and_diagnostics_report():
    """Provide an optional report of environment and diagnostics.

    TODO: DETAILED DOCS
    """
    logger.critical(
        "Using Python and CF environment of:\n"
        f"{cf.environment(display=False)}\n"
    )


@timeit
def read_obs_input_data(input_data_dir_loc, obs_data_dir):
    """Read in all observational input data.

    TODO: DETAILED DOCS
    """
    obs_data_loc = f"{input_data_dir_loc}/{obs_data_dir}"
    return cf.read(obs_data_loc), obs_data_loc


@timeit
def read_model_input_data(input_data_dir_loc, model_data_dir):
    """Read in all model input data.

    TODO: DETAILED DOCS
    """
    model_data_loc = f"{input_data_dir_loc}/{model_data_dir}"
    return cf.read(model_data_loc), model_data_loc


def read_input_data(input_data_dir_loc, obs_data_dir, model_data_dir):
    """Read in all input data.

    TODO: DETAILED DOCS
    """
    get_env_and_diagnostics_report()
    obs_data, obs_data_loc = read_obs_input_data(
        input_data_dir_loc, obs_data_dir
    )
    model_data, model_data_loc = read_model_input_data(
        input_data_dir_loc, model_data_dir
    )

    # Reporting
    logger.critical("All input data successfully read in.")
    logger.critical(
        f"\nInput data locations are:\n"
        f"Observational data: '{obs_data_loc}'\n"
        f"Model data: '{model_data_loc}'\n"
    )
    report_about_input_data(obs_data, model_data)

    return obs_data, model_data


def report_about_input_data(obs_data, model_data):
    """Read in all input data.

    TODO: DETAILED DOCS
    """
    logger.critical(f"Observational FieldList is:\n {obs_data}")
    logger.critical("For example, first observational field is:\n")
    logger.critical(obs_data[0].dump(display=False))

    logger.critical(f"Model FieldList is:\n {model_data}")
    logger.critical("For example, first model field is:\n")
    logger.critical(model_data[0].dump(display=False))


@timeit
def get_input_fields_of_interest(
    obs_data, model_data, chosen_obs_fields, chosen_model_fields
):
    """Return fields of interest from input datasets.

    TODO: DETAILED DOCS
    """
    # Take only relevant fields from the list of fields read in
    obs_field = obs_data[chosen_obs_fields]
    model_field = model_data[chosen_model_fields]

    return obs_field, model_field


@timeit
def make_preview_plots(
    obs_field,
    show_plot_of_input_obs,
    plot_of_input_obs_track_only,
    outputs_dir,
    plotname_start,
    cfp_mapset_config,
    cfp_cscale,
    cfp_input_levs_config,
    cfp_input_track_only_config,
    cfp_input_general_config,
    verbose,
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
            cfp_input_track_only_config.update(verbose=verbose)
            cfp.traj(equal_data_obs_field, **cfp_input_track_only_config)
            cfp.gclose()
            cfp.cscale(
                cfp_cscale
            )  # reset for normal (default-style) plots after
        if plot_of_input_obs_track_only in (0, 2):
            cfp.gopen(
                file=f"{outputs_dir}/{plotname_start}_obs_track_with_data.png"
            )
            print("HOLA")
            cfp_input_general_config.update(verbose=verbose)
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
    # Observational time axis processing
    if obs_field.construct("T", default=False):
        obs_t_identifier = "T"
    elif model_field.construct("time", default=False):
        obs_t_identifier = "time"
    else:
        raise CFComplianceIssue(
            "An identifiable and unique time coordinate is needed but "
            "was not found for the observational input. Got for "
            f"obs_field.constructs('T'):\n {obs_field.constructs('T')}\n"
        )
    # Observational data is a DSG so should always have T as an aux. coord.
    obs_times = obs_field.auxiliary_coordinate(obs_t_identifier)

    # Model time axis processing
    if model_field.construct("T", default=False):
        model_t_identifier = "T"
    elif model_field.construct("time", default=False):
        model_t_identifier = "time"
    else:
        raise CFComplianceIssue(
            "An identifiable and unique time coordinate is needed but "
            "was not found for the model input. Got for "
            f"model_field.constructs('T'):\n {model_field.constructs('T')}\n"
        )
    model_times = model_field.dimension_coordinate(model_t_identifier)
    # WRF data for now: use model_field.dimension_coordinate( ncvar%Time")

    return (obs_times, model_times), (obs_t_identifier, model_t_identifier)


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
        get_time_coords(obs_field, model_field)[0].data.Units
        == get_time_coords(obs_field, model_field)[1].data.Units
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
        get_time_coords(obs_field, model_field)[0].calendar
        == get_time_coords(obs_field, model_field)[1].calendar
    )
    logger.critical(
        f"Calendars on observational and model time coords. are the same?: "
        f"{same_calendar}\n"
    )


@timeit
def subspace_to_spatiotemporal_bounding_box(obs_field, model_field, verbose):
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

    if verbose:  # conditional avoids this calculation twice unless VERBOSE
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
def spatial_interpolation(
    obs_field, model_field_bb, regrid_method, regrid_z_coord
):
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
        method=regrid_method,
        z=regrid_z_coord,
        ln_z=True,
    )

    # TODO: consider whether or not to persist the regridded / spatial interp
    # before the next stage, or to do in a fully lazy way.

    logger.critical("\nSpatial interpolation (regridding) complete.\n")
    logger.critical(f"XYZ-colocated data is:\n {spatially_colocated_field}")

    return spatially_colocated_field


@timeit
def time_interpolation(
    obs_times,
    model_times,
    obs_t_identifier,
    model_t_identifier,
    obs_field,
    model_field,
    spatially_colocated_field,
    history_message,
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
    model_times = spatially_colocated_field.dimension_coordinate(
        model_t_identifier)
    obs_times = spatially_colocated_field.auxiliary_coordinate(
        obs_t_identifier)
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
    obs_time_key = m.auxiliary_coordinate(obs_t_identifier, key=True)
    # Model data time must always be a dimension coordinate
    model_time_key = m.dimension_coordinate(model_t_identifier, key=True)
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
            s1.dimension_coordinate(model_t_identifier) -
            s0.dimension_coordinate(model_t_identifier)
        ).data
        distances_0 = (
            s0.auxiliary_coordinate(
                obs_t_identifier)[index] -
            s0.dimension_coordinate(obs_t_identifier)
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
        " ~ " + history_message
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
def write_output_data(final_result_field, output_file_name):
    """Write out the 4D (XYZT) colocated result as output data.

    TODO: DETAILED DOCS
    """

    # Write final field result out to file on-disk
    cf.write(final_result_field, output_file_name)

    logger.critical("Writing of output file complete.")


@timeit
def make_outputs_plots(
    final_result_field,
    obs_t_identifier,
    cfp_output_levs_config,
    outputs_dir,
    plotname_start,
    cfp_output_general_config,
    verbose,
):
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
    aux_coor_t = final_result_field.auxiliary_coordinate(obs_t_identifier)
    dim_coor_t = cf.DimensionCoordinate(source=aux_coor_t)
    final_result_field.set_construct(dim_coor_t, axes="ncdim%obs")

    # Set levels for plotting of data in a colourmap
    # Min, max as determined using final_result_field.min(), .max():
    cfp.levs(**cfp_output_levs_config)

    # Make and open the final plot
    # NOTE: can try 'legend_lines=True' for the lines plotted with average
    #       between the two scatter marker points, if preferable?
    cfp.gopen(file=f"{outputs_dir}/{plotname_start}_final_colocated_field.png")

    cfp_output_general_config.update(verbose=verbose)
    cfp.traj(final_result_field, **cfp_output_general_config)
    cfp.gclose()

    logger.critical("Plot created.")


@timeit
def main():
    """Perform end-to-end model-to-observational co-location."""
    print_toolkit_banner()

    # Manage inputs from CLI and from configuration file, if present.
    args = process_config()

    # Set variables in case that multiple functions use a given argument value
    outputs_dir = args.outputs_dir
    plotname_start = args.plotname_start
    verbose = args.verbose

    # Process and validate inputs, including optional flight track preview plot
    obs_data, model_data = read_input_data(
        args.input_data_dir_loc, args.obs_data_dir, args.model_data_dir
    )
    obs_field, model_field = get_input_fields_of_interest(
        obs_data, model_data, args.chosen_obs_fields, args.chosen_model_fields
    )

    # TODO: this has too many parameters for one function, separate out
    make_preview_plots(
        obs_field,
        args.show_plot_of_input_obs,
        args.plot_of_input_obs_track_only,
        outputs_dir,
        plotname_start,
        args.cfp_mapset_config,
        args.cfp_cscale,
        args.cfp_input_levs_config,
        args.cfp_input_track_only_config,
        args.cfp_input_general_config,
        verbose,
    )
    ensure_cf_compliance(obs_field, model_field)  # TODO currently does nothing

    # Time coordinate considerations, pre-colocation
    times, time_identifiers = get_time_coords(
        obs_field, model_field)
    obs_times, model_times = times
    obs_t_identifier, model_t_identifier = time_identifiers
    # TODO apply obs_t_identifier, model_t_identifier in further logic
    ensure_unit_calendar_consistency(obs_field, model_field)

    # Subspacing to remove irrelavant information, pre-colocation
    model_field_bb = subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field, verbose
    )

    # Perform spatial and then temporal interpolation to colocate
    spatially_colocated_field = spatial_interpolation(
        obs_field,
        model_field_bb,
        args.regrid_method,
        args.regrid_z_coord,
    )
    final_result_field = time_interpolation(
        obs_times,
        model_times,
        obs_t_identifier,
        model_t_identifier,
        obs_field,
        model_field,
        spatially_colocated_field,
        args.history_message,
    )

    # Create and process outputs
    create_cra_outputs()  # TODO currently does nothing
    write_output_data(final_result_field, args.output_file_name)
    make_outputs_plots(
        final_result_field,
        args.cfp_output_levs_config,
        outputs_dir,
        plotname_start,
        args.cfp_output_general_config,
        verbose,
    )


if __name__ == "__main__":
    sys.exit(main())
