CONFIG_DEFAULTS = {
    # *** Script running options ***
    # Configure messaging to STDOUT, which is very verbose if INFO=True, else
    # as minimal as allows without log control in cf-plot (at present).
    # TODO: Get ESMF logging via cf incoporated into Python logging system,
    # see Issue #286.
    "verbose": True,
    "skip-all-plotting": False,
    # *** Run mode with time override(s) ***
    # Specify the mode on which to run the E2E, where valid choices are:
    # 1. a mode to take data as-is assuming the model input data spans the
    #    datetimes of the observational input data (set "False"),
    # 2. where the times on the observations are ignored so that they are
    #    set and assumed to take a given start time, as specified as one
    #    datetime string. Datetimes are assuemd to be UTC and should be
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
    # *** Subspacing options ***
    "halo-size": 1,
    # *** Regridding options, to configure the 4D interpolation ***
    "regrid-method": "linear",
    # Note this option except in rare cases won't be required, as should almost
    # always be able to determine what z-coordinate want given it must be
    # present in both the model and the observational data, so match those.
    # Only if both data have more than one of identical z-coord do we need
    # to ask for this info.
    "regrid-z-coord": None,  # default to None given above note
    "source-axes": False,
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
            "Input: flight track from observational field to co-locate model "
            "field onto"
        ),
    },
    "cfp-input-general-config": {
        "legend": True,  # TODO sepaarte into setvars config and plot opts
        "markersize": 5,
        "linewidth": 0.4,
        "title": (
            "Input: observational field (path, to be used for "
            "co-location, with its corresponding data, to be ignored)"
        ),
    },
    "cfp-output-levs-config": {},
    "cfp-output-general-config": {
        "legend": True,
        "markersize": 5,
        "linewidth": 0.4,
        "title": "Result: model co-located onto observational path",
    },
}