# Note: Sphinx autodoc requires dict object docstring to go *after* the
# dict itself, so see below for the docs!
CONFIG_DEFAULTS = {
    # *** Script running options ***
    # Configure messaging to STDOUT, which is very verbose if INFO=True, else
    # as minimal as allows without log control in cf-plot (at present).
    # TODO: Get ESMF logging via cf incorporated into Python logging system,
    # see Issue #286.
    "verbose": 0,  # corresponds to a count of 0 (-v would be 1, -vv 2, etc.)
    # *** Run mode with time override(s) ***
    # Specify the mode on which to run the E2E, where valid choices are:
    # 1. a mode to take data as-is assuming the model input data spans the
    #    datetimes of the observational input data (set "False"),
    # 2. where the times on the observations are ignored so that they are
    #    set and assumed to take a given start time, as specified as one
    #    datetime string. Datetimes are assumed to be UTC and should be
    #    pre-converted from another timezones before input if applicable.
    #
    #    TODO: could have a shortcut if want to assume start time of model?
    # 3. TODO include a whole climatology to calculate, specifying
    #    multiple datetime overrides as a sequence (input API for this TODO)
    "start-time-override": False,
    # *** Input data choices ***
    "obs-data-path": ".",
    "model-data-path": ".",
    # Extract input fields from input FieldList.
    # If these are set to False, then the whole FieldList will be taken.
    # Otherwise should be set to a valid index or slice, to be taken on the
    # FieldList.
    # TODO allow this to be a filter keyword, too! If is a string assume this?
    "chosen-obs-field": False,
    "chosen-model-field": False,
    # Pre-processing modes
    "preprocess-mode-obs": None,
    "preprocess-mode-model": None,
    # Orography inputs where model data is PP
    "orography": None,
    # *** Output choices ***
    # A given directory must exist already, if specified.
    "outputs-dir": ".",
    "output-file-name": "vision_toolkit_result_field.nc",
    "history-message": (
        "Processed using the NCAS VISION Toolkit to "
        "co-locate from model data to the observational data "
        "spatio-temporal location."
    ),
    # *** Subspacing options ***
    "halo-size": 1,
    # *** Interpolation options, to configure the 4D interpolation ***
    "spatial-colocation-method": "linear",
    # Note this option except in rare cases won't be required, as should almost
    # always be able to determine what z-coordinate want given it must be
    # present in both the model and the observational data, so match those.
    # Only if both data have more than one of identical z-coordinate do we need
    # to ask for this info.
    # Pressure will always be the ideal case, so that is our default and if
    # it can't be found, we look for other ways forward for the vertical.
    "vertical-colocation-coord": "air_pressure",
    "source-axes": False,
    # *** Plotting: what to plot and how to minimally configure it ***
    "plot-mode": 0,  # NEW DEFAULT, SLB ENSURE BACK COMPAT.
    "plotname-start": "vision_toolkit",
    # "parula" also works well, as alternative for dev. work:
    "cfp-cscale": "plasma",
    "cfp-mapset-config": {},
    "cfp-input-levs-config": {},
    "cfp-input-track-only-config": {
        "legend": True,  # TODO separate into setvars config and plot opts
        "colorbar": False,
        "markersize": 0.5,
        "linewidth": 0.0,  # turn off line plotting to only have markers
        "title": (
            "Input: flight track from observational field to co-locate model "
            "field onto"
        ),
    },
    "cfp-input-general-config": {
        "legend": True,  # TODO separate into setvars config and plot opts
        "markersize": 5,
        "linewidth": 0.0,
        "title": (
            "Input: observational field (path, to be used for "
            "co-location, with its corresponding data, to be ignored)"
        ),
    },
    "cfp-output-levs-config": {},
    "cfp-output-general-config": {
        "legend": True,
        "markersize": 5,
        "linewidth": 0.0,
        "title": "Result: model co-located onto observational path",
    },
    # Note, deprecations:
    # Bool but for dev. purposes, if set to 2 then it shows both plots:
    #"plot-of-input-obs-track-only": True,
    #
    # Optionally, display plots of the input observational data, or its track
    # only in one colour (if 'plot-of-input-obs-track-only' is set to True).
    # This could be useful for previewing the track to be colocated
    # onto, to fail early if the user isn't happy with the track,
    # or for demo'ing the code to compare the original observational data
    # to the co-located data to see the differences.
    #"show-plot-of-input-obs": True,
    #"skip-all-plotting": False,
}
"""Configuration default values, applied if the user does not set otherwise.

This is a constant, in the form of a dictionary defining the configuration
names as keys and their default values as the corresponding value for each.

**Output in pretty-printed format**

>>> from pprint import pprint
>>> pprint(visiontoolkit.constants.CONFIG_DEFAULTS)
{'cfp-cscale': 'plasma',
 'cfp-input-general-config': {'legend': True,
                              'linewidth': 0.0,
                              'markersize': 5,
                              'title': 'Input: observational field (path, to '
                                       'be used for co-location, with its '
                                       'corresponding data, to be ignored)'},
 'cfp-input-levs-config': {},
 'cfp-input-track-only-config': {'colorbar': False,
                                 'legend': True,
                                 'linewidth': 0.0,
                                 'markersize': 0.5,
                                 'title': 'Input: flight track from '
                                          'observational field to co-locate '
                                          'model field onto'},
 'cfp-mapset-config': {},
 'cfp-output-general-config': {'legend': True,
                               'linewidth': 0.0,
                               'markersize': 5,
                               'title': 'Result: model co-located onto '
                                        'observational path'},
 'cfp-output-levs-config': {},
 'chosen-model-field': False,
 'chosen-obs-field': False,
 'halo-size': 1,
 'history-message': 'Processed using the NCAS VISION Toolkit to co-locate from '
                    'model data to the observational data spatio-temporal '
                    'location.',
 'model-data-path': '.',
 'obs-data-path': '.',
 'orography': None,
 'output-file-name': 'vision_toolkit_result_field.nc',
 'outputs-dir': '.',
 'plot-mode': 0,
 'plotname-start': 'vision_toolkit',
 'preprocess-mode-model': None,
 'preprocess-mode-obs': None,
 'source-axes': False,
 'spatial-colocation-method': 'linear',
 'start-time-override': False,
 'verbose': 0,
 'vertical-colocation-coord': 'air_pressure'}

"""


def toolkit_banner():
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

    return banner_text
