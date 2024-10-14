import argparse
import copy
import json
import logging
import os
from pprint import pformat

from .constants import CONFIG_DEFAULTS

logger = logging.getLogger(__name__)


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
        "-s",
        "--start-time-override",
        action="store",
        help=(
            "if given, a datetime in UTC timezone with which to override "
            "the observational datetimes so that the colocation is conducted "
            "with the spatial components of the observational path but "
            "assuming the given start time and not the actual one"
        ),
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
        "--source-axes",
        action="store",
        help=(
            "identifies the source grid’s X and Y dimensions if they "
            "cannot be inferred from the existence of 1D dimension "
            "coordinates"
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


def validate_config(final_config_namespace):
    """TODO"""
    # TODO add validation in incrementally to cover all input options & args

    # outputs_dir: create if does not exist
    if not os.path.exists(final_config_namespace.outputs_dir):
        logger.critical(
            "Output directory does not exist, creating it at: "
            f"{final_config_namespace.outputs_dir}"
        )
        os.makedirs(final_config_namespace.outputs_dir)


def process_config_file(config_file):
    """Process a configuration file.

    TODO: DETAILED DOCS
    """
    with open(config_file) as f:
        try:
            j = json.load(f)
        except (json.decoder.JSONDecodeError, AttributeError):
            raise ValueError("Bad JSON configuration file.")  # TODO better msg

    logger.critical(f"Succesfully read-in JSON config. file at: {config_file}")

    return j
