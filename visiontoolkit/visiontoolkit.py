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

import copy
import functools
import logging
import numpy as np
import os
import sys

import cfplot as cfp
import cf

from .cli import process_config, validate_config


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


logger = logging.getLogger(__name__)


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
        if cfp_input_levs_config:
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


@timeit
def set_start_datetime(obs_times, obs_t_identifier, new_obs_starttime):
    """Replace observational time data with those starting from a new value.

    TODO: DETAILED DOCS
    """
    # 0. Check is a valid datetime input
    try:
        new_dt_start = cf.dt(new_obs_starttime)
    except (ValueError, TypeError):
        raise ValueError(
            "Value for 'start-time-override' must be a valid datetime "
            f"accepted by cf.dt(), but got: {new_obs_starttime}. See "
            "https://ncas-cms.github.io/cf-python/function/cf.dt.html "
            "for valid inputs."
        )

    # 1. If it is, change the observational time data to have the same
    #    spacings but starting from the specified start datetime
    # 1a) Find difference from original starttime to new starttime
    shift_to_startime = obs_times[0] - new_dt_start
    # 1b) Apply this shift to all time data
    new_obs_times = obs_times - shift_to_startime
    obs_times.set_data(new_obs_times)

    # TODO should we update the metadata to reflect the previous operation?

    logger.critical(
        f"Applied override to observational times, now have: {obs_times}, "
        f"with data of: {obs_times.data}"
    )
    return obs_times


@timeit
def check_time_coverage(obs_times, model_times):
    """TODO
    """

    msg_start = (
        "Model data datetimes must cover the whole of the datetime range "
        "spanned by the observational data, but got"
    )
    model_min = model_times.minimum()
    obs_min = obs_times.minimum()
    model_max = model_times.maximum()
    obs_max = obs_times.maximum()
    logger.critical(
        f"Model data has maxima {model_max} and minima {model_min}"
    )
    logger.critical(
        f"Obs data has maxima {obs_max} and minima {obs_min}"
    )

    if model_min > obs_min:
        raise ValueError(
            f"{msg_start} minima of {model_min} for the model > {obs_min} "
            "for the observations."
        )
    if model_max < obs_max:
        raise ValueError(
            f"{msg_start} maxima of {model_max} for the model < {obs_max} "
            "for the observations."
        )

def get_time_coords(obs_field, model_field, return_identifiers=True):
    """Return the relevant time coordinates from the fields.

    TODO: DETAILED DOCS
    """
    # Observational time axis processing
    if obs_field.coordinate("T", default=False):
        obs_t_identifier = "T"
    elif obs_field.coordinate("time", default=False):
        obs_t_identifier = "time"
    else:
        raise CFComplianceIssue(
            "An identifiable and unique time coordinate is needed but "
            "was not found for the observational input. Got for "
            f"obs_field.constructs('T'):\n {obs_field.coordinates('T')}\n"
        )
    # Observational data is a DSG so should always have T as an aux. coord.
    obs_times = obs_field.auxiliary_coordinate(obs_t_identifier)

    # Model time axis processing
    if model_field.coordinate("T", default=False):
        model_t_identifier = "T"
    elif model_field.coordinate("time", default=False):
        model_t_identifier = "time"
    else:
        raise CFComplianceIssue(
            "An identifiable and unique time coordinate is needed but "
            "was not found for the model input. Got for "
            f"model_field.constructs('T'):\n {model_field.coordinates('T')}\n"
        )

    model_times = model_field.dimension_coordinate(model_t_identifier)

    if return_identifiers:
        return (obs_times, model_times), (obs_t_identifier, model_t_identifier)
    else:
        return obs_times, model_times


@timeit
def ensure_unit_calendar_consistency(obs_field, model_field):
    """Ensure the chosen fields have consistent units and calendars.

    TODO: DETAILED DOCS
    """
    obs_times, model_times = get_time_coords(
        obs_field, model_field, return_identifiers=False
    )

    # Ensure the units of the obs and model datetimes are consistent - conform
    # them if they differ (if they don't, Units setting operation is harmless).
    obs_times_units = obs_times.Units
    logger.critical(f"Units on obs. time coordinate are: {obs_times_units}")

    model_times_units = model_times.Units
    logger.critical(f"Units on model time coordinate are: {model_times_units}")

    # Change the units on the model (not obs) times since there are fewer
    # data points on those, meaning less converting work.
    ###model_times.Units = obs_times_units

    logger.critical(f"Unit-conformed model time coord. is: {model_times}")
    same_units = obs_times.data.Units == model_times.data.Units
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

    # Some custom calendar consistency logic, necessary for e.g. WRF data
    before_pg_cutoff = cf.gt(cf.dt(1582, 10, 15))
    if (
            obs_calendar == "standard" and
            model_calendar == "proleptic_gregorian" and
            before_pg_cutoff.evaluate(model_times.minimum())
    ):
        # 'A calendar with the Gregorian rules for leap-years extended to
        #  dates before 1582-10-15', see:
        # https://cfconventions.org/Data/cf-conventions/
        # cf-conventions-1.11/cf-conventions.html#calendar
        # so it unless the data is before 1582, e.g. very historical runs,
        # it i equivalent to have 'standard' set (and can match up).
        logger.critical(
            f"Changing {model_times} calendar from '{model_calendar}' to "
            "'standard' (equivalent given all times are after 1582-10-15) "
            "to enable the time co-location to work."
        )
        model_times.override_calendar("standard", inplace=True)

    logger.critical(
        f"Calendars on observational and model time coords. are the same?: "
        f"{obs_times.calendar == model_times.calendar}\n"
    )


@timeit
def subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field, halo_size, verbose):
    """Extract only relevant data in the model field via a 4D subspace.

    Relevant data is extracted in the form of a field comprising the model
    field reduced to a 'bounding box' in space and in time, such that data
    outside the scope of the observational data track, with an extra
    index-space 'halo' added to include points of relevance to the outer-most
    points, is removed, because it is not relevant to the colocation.

    TODO: DETAILED DOCS
    """
    times, t_ids = get_time_coords(
        obs_field, model_field, return_identifiers=True
    )
    obs_times, model_times = times
    model_t_id = t_ids[1]

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

    bb_kwargs = {
        "X": cf.wi(*x_coord_tight_bounds),
        "Y": cf.wi(*y_coord_tight_bounds),
        "Z": cf.wi(*z_coord_tight_bounds),
        # Can't just use 'T' here since we might have a different name
        model_t_id: cf.wi(*t_coord_tight_bounds),
    }

    # Attempt to do a full bounding box subspace immediately (if indices call
    # works, the subspace call will work) - if it works, great! But probably it
    # won't work and we deal with that next...
    immediate_subspace_works = False
    try:
        model_field_bb_indices = model_field_bb_subspace(**bb_kwargs)
        immediate_subspace_works = True
        if verbose:
            logger.critical(
                "Immediate full indices calculation attempt WORKED, "
                f"proceeding using {model_field_bb_indices}"
            )
    except Exception as exc:
        logger.critical(
            f"Immediate full subspace attempt FAILED, with '{exc}',"
            "so we will now do it in a more careful way..."
        )

    # Since we always use the same arguments for subspace mode and halo size
    # TODO can't use partial for now, DH has explained subspace is actually a
    # property and not a method and that causes error and complication.
    # DH will raise an issue and PR to simplify subspace back to being a
    # standard method, then we can use the partial here, to consolidate.
    """
    model_field_bb_subspace = functools.partial(
        model_field.subspace,
        "envelope",
        # the halo size that extends the bounding box by 1 in index space
        halo_size,
    )
    """

    if immediate_subspace_works:
        logger.critical(
            "Set to create 4D bounding box onto model field, based on obs. field "
            f"tight boundaries of (4D: X, Y, Z, T):\n{pformat(bb_kwargs)}\n"
        )

        # Note: can do the spatial and the temporal subspacing separately, and if
        # want to do this make the call twice for each coordinate arg. Reasons we
        # may want to do this include having separate halo sizes for each
        # coordinate, etc.
        model_field_bb = model_field.subspace(
            "envelope", halo_size, **bb_kwargs)
    else:  # more likely case, so be more careful and treat axes separately
        logger.critical("1. Time subspace step")
        time_kwargs = {model_t_id: cf.wi(*t_coord_tight_bounds)}
        # Now we set model_field -> model_field_bb, as this is our
        # last separate subspace.
        # TODO partial also not working here - clues, clues.
        ###model_field_bb = model_field_bb_subspace(**time_kwargs)
        model_field = model_field.subspace(
            "envelope", halo_size, **time_kwargs)
        logger.critical(
            f"Time ('{model_t_id}') bounding box calculated. It is: "
            f"{model_field}"
        )

        # Horizontal
        logger.critical("2. Horizontal subspace step")
        # For this case where we do 3 separate subspaces, we reassign to
        # the same field and only at the end create 'model_field_bb' variable
        # We should be safe to do the horizontal subspacing as one
        model_field = model_field.subspace(
            "envelope", halo_size,
            X=cf.wi(*x_coord_tight_bounds),
            Y=cf.wi(*y_coord_tight_bounds),
        )
        logger.critical(
            "Horizontal ('X' and 'Y') bounding box calculated. It is: "
            f"{model_field}"
        )

        # Vertical
        logger.critical("3. Vertical subspace step")
        # First, need to calculate the vertical coordinates if there are
        # parametric vertical dimension coordinates to handle.
        # TODO cater for case where are > 1 coord refs (ValueError for now)
        coord_ref = model_field.coordinate_reference(default=None)
        if not coord_ref:  # no parametric coords, simple case
            model_field_bb = model_field.subspace(
                "envelope", halo_size,
                Z=cf.wi(*z_coord_tight_bounds),
            )
            vertical_sn = False
        else:
            logger.critical(
                "Need to calculate parametric vertical coordinates. "
                "Attempting...")
            model_field_w_vertical = model_field.compute_vertical_coordinates()   

            # TODO: see Issue 802, after closure will have better way to know
            # the vertical coordinate added by the calc, if it added it at all:
            # https://github.com/NCAS-CMS/cf-python/issues/802
            added_vertical = not model_field_w_vertical.equals(model_field)
            # If a vertical dim coord was added, we need to use that for our
            # z coordinate from now onwards
            # TODO move vertical calc. out of this method more generally for
            # better processing going forward
            # TODO handle lack of, will currently give ValueError
            vertical_sn = model_field_w_vertical.coordinate_reference(
                ).coordinate_conversion.get_parameter(
                    "computed_standard_name")
            new_z_coord = model_field_w_vertical.coordinate(vertical_sn)
            logger.critical(
                "Added vertical coordinates from parameters: "
                f"{new_z_coord.dump(display=False)}."
            )

            # Reset model_field to one with vertical coord now
            # TODO use in-place before so no need to create new one?
            model_field = model_field_w_vertical
            logger.critical(
                "Model field with vertical coords is: "
                f"{model_field.dump(display=False)}"
            )

            # Unit conforming: convert units on new cal'd Z to obs Z units
            # TODO can deal with further unit conformance using query units
            # for the queries we subspace on!
            new_z_coord.Units = obs_Z.Units
            logger.critical(
                "Units conformed for computed vertical coordinates:"
                f"{new_z_coord} with same units as {obs_Z}"
            )

            vert_kwargs = {vertical_sn: cf.wi(*z_coord_tight_bounds)}
            # TODO: partial case commented below is breaking things here! WHY!?
            ### model_field = model_field_bb_subspace(**vert_kwargs)
            model_field_bb = model_field.subspace(
                "envelope", halo_size, **vert_kwargs,
            )

        logger.critical(
            f"Vertical ('Z') bounding box calculated. It is: {model_field_bb}"
        )

    logger.critical(
        "4D bounding box calculated. Model data with bounding box applied is: "
        f"{model_field_bb}"
    )

    return model_field_bb, vertical_sn


@timeit
def spatial_interpolation(
        obs_field, model_field_bb, regrid_method, regrid_z_coord, source_axes,
        model_t_identifier, vertical_sn
):
    """Interpolate the flight path spatially (3D for X-Y and vertical Z).

    Horizontal X-Y and vertical Z coordinates are interpolated. This is
    done under-the-hood in cf-python with the ESMF LocStream feature, see:
    https://xesmf.readthedocs.io/en/latest/notebooks/Using_LocStream.html

    TODO: DETAILED DOCS
    """
    # TODO: UGRID grids might need some extra steps/work for this.

    logger.critical(
        "Starting spatial interpolation (regridding) step..."
        f"WITH {model_field_bb}"
    )

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
    immediate_regrid_works = True
    try:
        spatially_colocated_field = model_field_bb.regrids(
            obs_field,
            method=regrid_method,
            z=regrid_z_coord,
            ln_z=True,
            src_axes=source_axes,
        )
    except ValueError:
        immediate_regrid_works = False
        # We have to be more clever, probably we have a case with 4D Z coords
        # so we need to iterate over times to effectively get 3D Z coords
        # and then squeeze out the time axis from it.

    # TODO could put this in exception code above but nicer out here?
    if not immediate_regrid_works:
        model_bb_t_key, model_bb_t = model_field_bb.coordinate(
            model_t_identifier, item=True)

        # Get the axes positions first before we iterate
        z_coord = model_field_bb.coordinate(vertical_sn)
        data_axes = model_field_bb.get_data_axes()
        time_da = model_field_bb.domain_axis(model_t_identifier, key=True)
        time_da_index = data_axes.index(time_da)

        # TODO possible bug in WRF pre-proc or in cf whereby aux coord axes
        # are not in compatible order with the data axes, so do a HACKY SWAP:
        new_z_coord = z_coord.swapaxes(1, 0)  # TODO NOT WORKING?
        model_field_bb.del_construct(vertical_sn)
        # TODO rename vertical_sn to z_id or z_key or similar
        new_vertical_id = model_field_bb.set_construct(
            new_z_coord, axes=[model_t_identifier, "Z",
                               source_axes["Y"], source_axes["X"]],
        )
        z_coord = model_field_bb.coordinate(new_vertical_id)
        z_coord.set_property('standard_name', value=vertical_sn)

        spatially_colocated_fields = cf.FieldList()
        for time in model_bb_t:
            kwargs = {model_t_identifier: time}
            # TODO what subspace args might we want here?
            model_field_z_per_time = model_field_bb.subspace(**kwargs)
            z_coord_per_time = model_field_z_per_time.coordinate(vertical_sn)

            # Need to squeeze out the time coordinate, but ONLY from the
            # vertical_sn (computer vertical coords) z coordinate, not the
            # data axes overall.
            model_field_z_per_time.del_construct(vertical_sn)
            fin_z_coord = z_coord_per_time.squeeze(time_da_index)
            model_field_z_per_time.set_construct(
                fin_z_coord, axes=["Z", source_axes["Y"], source_axes["X"]],
            )

            logger.critical(
                f"Squeezed Z coordinate: {z_coord_per_time},"
                f"{z_coord_per_time.data}"
            )
            logger.critical(
                f"Model field per time data is: {model_field_z_per_time}"
            )

            # ALSO NEED TO SQUEEZE X AND Y AUX COORDS! for those 2d aux
            # lat and lons! Then everything is all set up for the 3D Z regrids
            # HACK FIRST USE DIRECT NAMES TO GET WORKIN: ncvar%XLAT, ncvar%XLONG
            for a_name in ("ncvar%XLAT", "ncvar%XLONG"):
                a_coord = model_field_z_per_time.coordinate(a_name)
                model_field_z_per_time.del_construct(a_name)
                fin_a_coord = a_coord.squeeze()  # safe - can other dim be size 1?
                model_field_z_per_time.set_construct(
                    fin_a_coord, axes=[source_axes["Y"], source_axes["X"]],
                )

            # Do the regrids weighting operation for the 3D Z in each case
            spatially_colocated_field_comp = model_field_z_per_time.regrids(
                obs_field,
                method=regrid_method,
                z=vertical_sn,
                ln_z=True,  # TODO should we use a log here in this case?
                src_axes=source_axes,
            )
            logger.critical(
                f"3D Z colocated field component for {time} is "
                f"{spatially_colocated_field_comp} "
            )
            spatially_colocated_fields.append(spatially_colocated_field_comp)
        # Finally, need to concatenate the individually-regridded per-time
        # components
        spatially_colocated_field = cf.Field.concatenate(
            spatially_colocated_fields
        )
        logger.critical(
            f"Final concatenated field (from 3D Z colocated fields) is "
            f"{spatially_colocated_field} "
        )

    # TODO: consider whether or not to persist the regridded / spatial interp
    # before the next stage, or to do in a fully lazy way.

    logger.critical("\nSpatial interpolation (regridding) complete.\n")
    logger.critical(f"XYZ-colocated data is:\n {spatially_colocated_field}")

    return spatially_colocated_field


def time_subspace_per_segment(
        index, model_times_len, t1, t2, m, obs_time_key, model_time_key,
        model_t_identifier
):
    """TODO."""
    # Define the pairwise segment datetime endpoints
    logger.critical(
        f"Datetime endpoints for this segment are: {t1}, {t2}.\n"
    )

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
        s1.dimension_coordinate(model_t_identifier)
        - s0.dimension_coordinate(model_t_identifier)
    ).data
    distances_0 = (
        s0.auxiliary_coordinate(model_t_identifier)[index]
        - s0.dimension_coordinate(model_t_identifier)
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
    return values_weighted


@timeit
def time_interpolation(
    obs_times,
    model_times,
    obs_t_identifier,
    model_t_identifier,
    obs_field,
    model_field,
    halo_size,
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

    # Setup ready for iteration...
    m = spatially_colocated_field.copy()

    # In our field after spatial interpolation, the Dimension Coord has the
    # model time data and the Aux Coord has the observational time data
    # NOTE: keep these calls in, desite earlier ones probably in-place.
    # Model data time must always be a dimension coordinate.
    model_time_key, model_times = m.dimension_coordinate(
        model_t_identifier, item=True
    )
    # Observations, if DSG, will always be the auxiliary coordinate time
    obs_time_key, obs_times = m.auxiliary_coordinate(
        obs_t_identifier, item=True
    )
    model_times_len = len(model_times.data)
    obs_times_len = len(obs_times.data)

    logger.critical(
        f"Number of model time data points: {model_times_len}\n"
        f"Number of observational time sample data points: {obs_times_len}\n"
    )
    logger.critical(f"Observational (aux) coord. time key is: {obs_time_key}")
    logger.critical(f"Model (dim) time key is: {model_time_key}\n")

    # Empty objects ready to populate - TODO make these FieldLists if approp.?
    v_w = []

    # Iterate over pairs of adjacent model datetimes, defining 'segments'.
    # Chop the flight path up into these *segments* and do a weighted merge
    # of data from segments adjacent in the model times to form the final
    # time-interpolated value.
    logger.critical(
        "*** Begin iteration over pairwise 'segments'. ***\n"
        f"Segments to loop over are, pairwise: {model_times.datetime_array}"
    )
    # Note the length of (pairwise(model_times.datetime_array) is equal to
    # model_times_len - 1 by its nature, e.g. A, B, C -> (A, B), (B, C)).
    for index, (t1, t2) in enumerate(pairwise(model_times.datetime_array)):
        logger.critical(f"\n*** Segment {index} ***\n")
        # Rarely, when we apply a halo and the start or end time is on the
        # boundary where there is a model time point, there will be no
        # points captured by the outermost subspaces. Therefore, for the
        # segments corresponding to the halo ONLY we use a try/except to
        # account for this:
        permit_null_subspace = False
        # Here want the outermost segments corresponding to the halo_size.
        # The '-1' for both elements is to account for indices starting at 0
        # whereas halo sizes begin at 1 to have significance, where the
        # second item in the tuple uses length of pairwise iterator being
        # equal to model_times_len - 1, so is:
        # (model_times_len - 1) - 1 - (halo_size - 1), and -1+1-1 = -1 overall.
        if index in (halo_size - 1, model_times_len - 1 - halo_size):
            permit_null_subspace = True
            logger.critical(
                "Allowing potential null-return subspace for segment emerging "
                f"from halo size of {halo_size}, equivalent halo position in "
                f"time segment array of: {index + 1}/{model_times_len - 1}"
            )

        if permit_null_subspace:
            try:
                values_weighted = time_subspace_per_segment(
                    index, model_times_len, t1, t2, m, obs_time_key,
                    model_time_key, model_t_identifier
                )
                v_w.append(values_weighted)
            except IndexError:
                logger.critical(
                    f"Null-return subspce for segment with: {t1}, {t2}.\n"
                    "This is a result of the halo_size set, so not a cause "
                    "for concern!"
                )
        else:
            values_weighted = time_subspace_per_segment(
                index, model_times_len, t1, t2, m, obs_time_key,
                model_time_key, model_t_identifier
            )
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
    history_details = final_result_field.get_property("history", default="")
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
def write_output_data(final_result_field, output_path_name):
    """Write out the 4D (XYZT) colocated result as output data.

    TODO: DETAILED DOCS
    """

    # Write final field result out to file on-disk
    cf.write(final_result_field, output_path_name)

    logger.critical("Writing of output file complete.")


@timeit
def make_outputs_plots(
    final_result_field,
    obs_t_identifier,
    cfp_output_levs_config,
    outputs_dir,
    plotname_start,
    new_obs_starttime,
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
    if cfp_output_levs_config:
        cfp.levs(**cfp_output_levs_config)

    # Make and open the final plot
    # NOTE: can try 'legend_lines=True' for the lines plotted with average
    #       between the two scatter marker points, if preferable?
    cfp.gopen(file=f"{outputs_dir}/{plotname_start}_final_colocated_field.png")

    cfp_output_general_config.update(verbose=verbose)
    # Note the set start time of the obs on the plot title as key info.
    if new_obs_starttime:
        update_title = f"assuming starting time of {new_obs_starttime}"
        orig_title = cfp_output_general_config.get("title", None)
        if orig_title:
            cfp_output_general_config.update(
                title=f"{orig_title} {update_title}")
        else:
            cfp_output_general_config["title"] = update_title.title()
    cfp.traj(final_result_field, **cfp_output_general_config)
    cfp.gclose()

    logger.critical("Plot created.")


@timeit
def main():
    """Perform end-to-end model-to-observational co-location."""
    print_toolkit_banner()

    # Manage inputs from CLI and from configuration file, if present.
    args = process_config()
    # Check all inputs are valid else error before starting toolkit logic
    validate_config(args)

    # Set variables for cases where multiple functions need to use values
    outputs_dir = args.outputs_dir
    plotname_start = args.plotname_start
    verbose = args.verbose
    halo_size = args.halo_size
    skip_all_plotting = args.skip_all_plotting

    # Process and validate inputs, including optional flight track preview plot
    obs_data, model_data = read_input_data(
        args.input_data_dir_loc, args.obs_data_dir, args.model_data_dir
    )
    obs_field, model_field = get_input_fields_of_interest(
        obs_data, model_data, args.chosen_obs_fields, args.chosen_model_fields
    )

    # TODO: this has too many parameters for one function, separate out
    if not skip_all_plotting:
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
    times, time_identifiers = get_time_coords(obs_field, model_field)
    obs_times, model_times = times
    obs_t_identifier, model_t_identifier = time_identifiers

    new_obs_starttime = args.start_time_override
    if new_obs_starttime:
        # TODO can just do in-place rather than re-assign, might be best?
        obs_times = set_start_datetime(
            obs_times, obs_t_identifier, new_obs_starttime)

    # TODO apply obs_t_identifier, model_t_identifier in further logic
    ensure_unit_calendar_consistency(obs_field, model_field)

    # Ensure the model time axes covers the entire time axes span of the
    # obs track - else we can't go forward - if so inform about this clearly
    check_time_coverage(obs_times, model_times)

    # Subspacing to remove irrelavant information, pre-colocation
    # TODO tidy passing through of computer vertical coord identifier
    model_field_bb, vertical_sn = subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field, halo_size, verbose
    )

    # Perform spatial and then temporal interpolation to colocate
    spatially_colocated_field = spatial_interpolation(
        obs_field,
        model_field_bb,
        args.regrid_method,
        args.regrid_z_coord,
        args.source_axes,
        model_t_identifier,
        vertical_sn,
    )
    final_result_field = time_interpolation(
        obs_times,
        model_times,
        obs_t_identifier,
        model_t_identifier,
        obs_field,
        model_field,
        halo_size,
        spatially_colocated_field,
        args.history_message,
    )

    # Create and process outputs
    create_cra_outputs()  # TODO currently does nothing
    # TODO improve path handling with PathLib library
    output_path_name = f"{outputs_dir}/{args.output_file_name}"
    write_output_data(final_result_field, output_path_name)
    if not skip_all_plotting:
        make_outputs_plots(
            final_result_field,
            obs_t_identifier,
            args.cfp_output_levs_config,
            outputs_dir,
            plotname_start,
            new_obs_starttime,
            args.cfp_output_general_config,
            verbose,
        )


if __name__ == "__main__":
    sys.exit(main())
