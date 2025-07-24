import argparse
import copy
import json
import logging
import os
from pprint import pformat

from .constants import CONFIG_DEFAULTS


logger = logging.getLogger(__name__)


def setup_logging(verbosity):
    """Configure the package log level assuming CLI counted `-v` flag input.

    TODO: DETAILED DOCS
    """
    # Maximum of 3 (-vvv i.e. -v -v -v) calls to have an effect, use min()
    # to ensure the log level never goes below DEBUG value (10), with a
    # minimum of ERROR (40)
    numeric_log_level = 40 - (min(verbosity, 3) * 10)

    # logging.basicConfig()  #level=numeric_log_level)
    # logging.getLogger(__name__).setLevel(numeric_log_level)  # VISION logger
    # logging.getLogger().setLevel(numeric_log_level)  # root logger e.g. for cf

    # Want to set all VISION toolkit and cf* library log levels, without
    # affecting other Python module ones, so this logic is necessary since the
    # more elegant way above doesn't seem to work whatever variation I try...
    loggers = [
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("visiontoolkit")
        or name.startswith("cf")
        or name.startswith("cfdm")  # note cf-plot does not yet have logging
    ]
    for logger in loggers:
        logger.setLevel(numeric_log_level)


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
        default=0,  # in this case can't set default later else NoneType issues
        action="count",
        help=(
            "provide more detailed output, where multiple calls will "
            "increase the verbosity yet further to a maximum at -vvv (3 v)"
            "corresponding to logging level 'DEBUG', where no specification "
            "gives a default of logging level 'WARNING' (0 v)"
        ),
    )
    parser.add_argument(
        "-c",
        "--config-file",
        action="store",
        help=(
            "configuration file in JSON format to supply configuration, "
            "where any configuration provided by other command-line options "
            "will take precedence over the configuration file "
            "input, if duplication should occur"
        ),
    )
    parser.add_argument(
        "-p",
        "--preprocess-mode-obs",
        action="store",
        help=(
            "specify a pre-processing mode so a set plugin is applied "
            "to pre-process the observational data in an appropriate way, "
            "current options being 'flight' and 'satellite' where by default "
            "no pre-processing is applied"
        ),
    )
    parser.add_argument(
        "--preprocess-mode-model",
        action="store",
        help=(
            "specify a pre-processing mode so a set plugin is applied "
            "to pre-process the model data in an appropriate way, current "
            "options being 'UM' and 'WRF' where by default no "
            "pre-processing is applied"
        ),
    )
    parser.add_argument(
        "--orography",
        action="store",
        help=(
            "if the model data input is in PP format and has vertical "
            "coordinates in terms of atmosphere hybrid height then specify "
            "the path to the external orography data applicable to the model "
            "data required for calculation of the vertical coordinates"
        ),
    )
    parser.add_argument(
        "-s",
        "--start-time-override",
        action="store",
        help=(
            "if given, a datetime in the UTC timezone with which to override "
            "the observational datetimes so that the co-location is conducted "
            "with the same spatial components of the observational path but "
            "assuming the given start time instead of the actual timestamped "
            "one when the data was collected/sampled"
        ),
    )
    parser.add_argument(
        "-o",
        "--obs-data-path",
        action="store",
        help=(
            "path location of the observational data, which can be provided "
            "in any form accepted by the 'cf.read' files argument, see: "
            "https://ncas-cms.github.io/cf-python/function/cf.read.html"
        ),
    )
    parser.add_argument(
        "-m",
        "--model-data-path",
        action="store",
        help=(
            "path location of the model data, which can be provided "
            "in any form accepted by the 'cf.read' files argument, see: "
            "https://ncas-cms.github.io/cf-python/function/cf.read.html"
        ),
    )
    parser.add_argument(
        "--chosen-obs-field",
        action="store",
        help=(
            "string corresponding to a valid 'select_field' argument to "
            "select a unique field from the FieldList of the read-in "
            "observational data, else if not specified the FieldList is "
            "assumed to be of size one and the single field extracted"
        ),
    )
    parser.add_argument(
        "--chosen-model-field",
        action="store",
        help=(
            "string corresponding to a valid 'select_field' argument to "
            "select a unique field from the FieldList of the read-in "
            "model data, else if not specified the FieldList is "
            "assumed to be of size one and the single field extracted"
        ),
    )
    parser.add_argument(
        "-d",
        "--outputs-dir",
        action="store",
        help=(
            "path location of the top-level directory in which to put the "
            "toolkit output(s)"
        ),
    )
    parser.add_argument(
        "-f",
        "--output-file-name",
        action="store",
        help="name including extension to call the toolkit result output file",
    )
    parser.add_argument(
        "--history-message",
        action="store",
        help=(
            "message that is added to the 'history' property on the "
            "toolkit result output file"
        ),
    )
    parser.add_argument(
        "--halo-size",
        action="store",
        help=(
            "size of the halo to apply for subspacing, see the section "
            "'Halos' under 'https://ncas-cms.github.io/cf-python/method/"
            "cf.Domain.subspace.html?highlight=halos' for context"
        ),
    )
    parser.add_argument(
        "-i",
        "--spatial-colocation-method",
        action="store",
        # Note: the temporal colocation is always linear, even if the spatial
        # colocation isn't, so there is no equivalent option for temporal case
        help=(
            "interpolation method to apply for the spatial co-location, see "
            "the 'method' parameter to "
            "'cf.regrids' method used under-the-hood to do this for options: "
            "https://ncas-cms.github.io/cf-python/method/cf.Field.regrids.html"
        ),
    )
    parser.add_argument(
        "-z",
        "--vertical-colocation-coord",
        action="store",
        help=(
            "vertical (Z) coordinate to use as the vertical component in "
            "the spatial interpolation step of co-location, where either "
            "a pressure or an altitude CF standard name is expected"
        ),
    )
    parser.add_argument(
        "--source-axes",
        action="store",
        help=(
            "a dictionary to identify the source grid’s X and Y "
            "dimensions if they cannot be inferred from the existence of "
            "1D dimension coordinates, for context see: "
            "https://ncas-cms.github.io/cf-python/method/cf.Field.regrids."
            "html?highlight=src_axes"
        ),
    )
    parser.add_argument(
        "--plotname-start",
        action="store",
        help="initial text to preface the names of all plots generated",
    )
    parser.add_argument(
        "--plot-mode",
        action="store",
        help=(
            "what if anything to plot with the toolkit (note this requires "
            "cf-plot to be installed at suitable version), where integer "
            "inputs represent the supported modes, which are: "
            "[0] to not plot anything (the default); [1] to plot "
            "both the outputs and, before starting co-location, as a "
            "means of verification and/or quick inspection, the observational "
            "input (with its data); [2] to plot only the outputs (the default "
            "mode, if plot-mode is not specified); and [3] to plot both the "
            "outputs and observational input but only show the track/swath "
            "of the inputs without the data on it to indicate the track/swath "
            "which the model field will then be co-located onto (the most "
            "relevant part of the observational input for VISION purposes)"
        ),
    )
    parser.add_argument(
        "--cfp-cscale",
        action="store",
        help=(
            "cf-plot plotting configuration as a string to set the "
            "colour scale for the (input preview and) output plots, "
            "see: https://ncas-cms.github.io/cf-plot/build/cscale.html#cscale"
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
        # TODO clarify/separate setvars and plot call config.
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "general plotting variables for the input preview full plot, see:"
            "https://ncas-cms.github.io/cf-plot/build/setvars.html#setvars"
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
        # TODO clarify/separate setvars and plot call config.
        help=(
            "cf-plot plotting configuration as a dictionary to set the "
            "general plotting variables for the output plots, see:"
            "https://ncas-cms.github.io/cf-plot/build/setvars.html#setvars"
        ),
    ),
    # Plugin specific config. items - each has no effect if not applying
    # the relevant plugin through setting the relevant string value for
    # the preprocess-mode-obs and/or
    # preprocess-mode-model plugin specifying configuration items.
    parser.add_argument(
        "--satellite-plugin-config",
        action="store",
        help=(
            "dictionary to set the configuration values for the satellite "
            "plugin, where valid keys to set are 'latitude', 'longitude', "
            "'sensingtime', 'do_retrieval', 'sensingtime_msec', "
            "'sensingtime_day', 'npres' and 'npi'."
        ),
    )

    # Effectively deprecated CLI input names - these have been replaced by
    # better names for the same item, but to allow folk to continue to use
    # the under-development toolkit at a 'frozen API' stage, keep them as
    # working alternatives (the logic accepts either at present). Before the
    # first proper release these will be removed as possibilities.
    parser.add_argument(
        "--regrid-z-coord",
        action="store",
        help=(
            "DEPRECATED: use '--vertical-colocation-coord' instead "
            "[vertical (z) coordinate to use as the vertical component in "
            "the spatial interpolation step]"
        ),
    )
    parser.add_argument(
        "-r",
        "--regrid-method",
        action="store",
        help=(
            "DEPRECATED: use '--spatial-colocation-method' instead "
            "[regridding interpolation method to apply, see 'method' "
            "parameter to 'cf.regrids' method for options: "
            "https://ncas-cms.github.io/cf-python/method/cf.Field.regrids.html]"
        ),
    )
    parser.add_argument(
        "--chosen-obs-fields",
        action="store",
        help=(
            "DEPRECATED: use '--chosen-obs-field' (non-plural) instead "
            "and note that we no longer accept an integer corresponding to a "
            "FieldList index to take a field from like this keyword "
            "permitted, now we require a valid 'select_field' string argument."
        ),
    )
    parser.add_argument(
        "--chosen-model-fields",
        action="store",
        help=(
            "DEPRECATED: use '--chosen-model-field' (non-plural) instead "
            "and note that we no longer accept an integer corresponding to a "
            "FieldList index to take a field from like this keyword "
            "permitted, now we require a valid 'select_field' string argument"
        ),
    )
    # All three below replaced by plot-mode:
    parser.add_argument(
        "-t",
        "--plot-of-input-obs-track-only",
        action="store_true",
        help=(
            "DEPRECATED: use '--plot-mode' instead "
            "[flag to indicate whether only the track/trajectory "
            "of the observational data is shown, as opposed to the data "
            "on the track, for the input observational data preview plots]"
        ),
    )
    parser.add_argument(
        "--skip-all-plotting",
        action="store_true",
        help=(
            "DEPRECATED: use '--plot-mode' instead "
            "[Do not generate plots to preview the input or show the output "
            "fields]"
        ),
    )
    parser.add_argument(
        "--show-plot-of-input-obs",
        action="store_true",
        help=(
            "DEPRECATED: use '--plot-mode' instead "
            "[flag to indicate whether to show plots of the input "
            "observational data before the co-location logic begins, as "
            "a preview]"
        ),
    )


def cli_parser():
    """Return a configured argument parser object for the VISION Toolkit.

    TODO: DETAILED DOCS
    """
    parser = argparse.ArgumentParser(
        prog="VISION Toolkit",
        description=(
            "Virtual Integration of Satellite and In-Situ Observation "
            "Networks (VISION) Toolkit Version 2"
        ),
    )
    process_cli_arguments(parser)

    return parser  # note: need to return explicitly for CLI Ref. docs


def process_config():
    """Process all configuration, from CLI, file or a default if neither set.

    Order values are set in:
      1. Defaults set first, to ensure everything has a valid value, then...
      2. Overidden by any config. file specifications, which are in turn...
      3. Overidden by any CLI options provided, which are always applied over
         the former.

    Overwrite any config. specified in the config. file given with the CLI
    --config-file argument with any other CLI options given, excluding the
    config. file option, processed above. This means that the CLI is the
    overriding input, e.g. for a config. file with
    '"halo-size": 1' set and a CLI option of 'halo-size=2', the value 2
    will be taken and used.

    TODO: DETAILED DOCS
    """
    # 0. Set up parser and get args
    parser = cli_parser()

    # First parse: just to get the config file specification so we can
    # process that, we then re-parse later to apply the config. file
    # otherwise constant default values as defaults to the CLI arguments
    # to fill in whatever is not provided from the command.
    parsed_args = parser.parse_args()

    # Configure logging - do this now since otherwise following log messages
    # get missed!
    setup_logging(parsed_args.verbose)

    logger.info(
        f"Parsed CLI configuration arguments are:\n{pformat(parsed_args)}\n"
    )

    # 1. Defaults
    # Want config. file input to have identical key names to the CLI ones,
    # namely with underscores as word delimiters, but for processing defaults
    # have to use hyphens since argparse converts to these for valid attr names
    logger.debug(f"Default configuration is:\n{pformat(CONFIG_DEFAULTS)}\n")

    # 2.  Get configuration from file, if provided
    config_file = parsed_args.config_file
    config_from_file = {}
    if config_file:
        config_from_file = process_config_file(config_file)
        logger.info(
            f"Configuration from file is:\n{pformat(config_from_file)}\n"
        )

    # Combining 1 and 2: apply config. file values to override defaults
    pre_cli_config = {**CONFIG_DEFAULTS, **config_from_file}  # keeps leftmost
    pre_cli_config_replace = {
        k.replace("-", "_"): v for k, v in pre_cli_config.items()
    }

    # 3. Finally, apply the config and defaults as values wherever a CLI
    # option has not been set explicitly:
    parser.set_defaults(**pre_cli_config_replace)
    # Re-parse, now we have applied the final defaults (had to parse once first
    # to get the process the config. file from the CLI)
    final_args = parser.parse_args()
    logger.info(
        "Final input configuration, considering CLI and file inputs (with "
        "CLI overriding the file values) is:"
        f"\n{pformat(final_args)}\n"
    )

    return final_args


def validate_config(final_config_namespace):
    """Perform validations on the configuration input by the user.

    TODO: DETAILED DOCS
    """
    # TODO add validation in incrementally to cover all input options & args

    print("final_config_namespace is", final_config_namespace)

    # outputs_dir: create if does not exist
    if not os.path.exists(final_config_namespace.outputs_dir):
        logger.info(
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
            raise ValueError(
                "The configuration file specified is not valid JSON: "
                f"{config_file}"
            )

    logger.info(f"Successfully read-in JSON config. file at: {config_file}")

    return j
