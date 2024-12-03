import functools
import logging
import os
import sys

from glob import glob
from itertools import pairwise  # requires Python 3.10+
from pprint import pformat
from time import time

# NOTE: keep this order (cfp then cf imported) to avoid Seg Fault issues
import cfplot as cfp
import cf

import numpy as np

from .cli import process_config, validate_config, setup_logging
from .constants import toolkit_banner
from .plugins import satellite_compliance_plugin


# ----------------------------------------------------------------------------
# Set up timing and logging
# ----------------------------------------------------------------------------

logger = logging.getLogger(__name__)


def timeit(func):
    """A decorator to measure and report function execution time."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time()
        output = func(*args, **kwargs)
        endtime = time()
        totaltime = endtime - starttime

        # Note: using a print not log call here, so they always emerge. At
        # release time we can subsume this into the logging system.
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

def get_env_and_diagnostics_report():
    """Provide an optional report of environment and diagnostics.

    TODO: DETAILED DOCS
    """
    logger.info(
        "Using Python and CF environment of:\n"
        f"{cf.environment(display=False)}\n"
    )


@timeit
def get_files_to_individually_colocate(path):
    """TODO."""

    logger.info(
        "Reading in all files. Note if there are a lot of file to read "
        "this may take a little time."
    )
    # Basically copying logic here from cf-python read globbing,
    # because we need to get a list of files to separately loop through
    # to do colocation on, but once a globbed read is done the fields are
    # all put into one fieldlist so we can't do a globbed read and go from
    # there. But we do need to check the list of files to read are valid
    # up-front, so use the same logic as cf-python (I have taken the liberty
    # of improving the variable names and adding some commenting.)
    files = glob(path)
    for filesystem_item in files:
        if os.path.isdir(filesystem_item):
            # Keep as ptint until address TODO
            # TODO deal with sub-directories under read glob
            logger.info(
                "Warning, read directory includes a sub-directory. "
                "Ignoring sub-directory cases for now."
            )

    logger.info(
        "Globbed list of files to attempt to read with cf is: "
        f"{pformat(files)}")

    return files


@timeit
def read_obs_input_data(obs_data_path):
    """Read in all observational input data.

    TODO: DETAILED DOCS
    """
    logger.info(
        f"Observational data input location is: '{obs_data_path}'\n"
    )
    fl = cf.read(obs_data_path, ignore_read_error=True)
    if not fl:
        return

    logger.info(
        "Read in observational data. For example, its first field is:\n")
    logger.info(fl[0].dump(display=False))

    return fl


@timeit
def read_model_input_data(model_data_path):
    """Read in all model input data.

    TODO: DETAILED DOCS
    """
    logger.info(
        f"Model data input location is: '{model_data_path}'\n"
    )
    fl = cf.read(model_data_path)

    logger.info("Read in model data. For example, its first field is:\n")
    logger.info(fl[0].dump(display=False))

    return fl


@timeit
def get_input_fields_of_interest(fl, chosen_fields):
    """Return the field(s) of interest from the input dataset.

    TODO: DETAILED DOCS
    """
    if chosen_fields is not False:  # distinguish from 0 etc.
        # Take only relevant fields from the list of fields read in
        fl = fl[chosen_fields]

    return fl


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
    index=False,
):
    """Generate plots of the flight track for a pre-colocation preview.

    If index is provided, it is assumed there will be multiple preview plots
    and therefore each should be labelled with the index in the name.

    TODO: DETAILED DOCS
    """
    # First configure general settings for plot
    # Change the viewpoint to be over the UK only, with high-res map outline
    cfp.mapset(**cfp_mapset_config)
    cfp.cscale(cfp_cscale)
    if index is False:  # distinguish it from 0, a possible index
        index = ""  # so the name does not change
    else:
        index = f"_{index}"

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
            # therefore whole track will be red to make it clear it is a block
            # colour without meaning attached
            cfp.cscale("scale28")
            cfp.gopen(
                file=(
                    f"{outputs_dir}/"
                    f"{plotname_start}_obs_track_only{index}.png"
                )
            )
            cfp_input_track_only_config.update(verbose=verbose)
            cfp.traj(equal_data_obs_field, **cfp_input_track_only_config)
            cfp.gclose()
            cfp.cscale(
                cfp_cscale
            )  # reset for normal (default-style) plots after
        if plot_of_input_obs_track_only in (0, 2):
            cfp.gopen(
                file=(
                    f"{outputs_dir}/"
                    f"{plotname_start}_obs_track_with_data_{index}.png"
                )
            )
            cfp_input_general_config.update(verbose=verbose)
            cfp.traj(obs_field, **cfp_input_general_config)
            cfp.gclose()


@timeit
def satellite_plugin(fieldlist, config=None):
    """Pre-processing of a field from a satellite swath.

    Define this is own function so we can apply the timing decorator.
    """
    return satellite_compliance_plugin(fieldlist, config=config)


@timeit
def ensure_cf_compliance(field, plugin, satellite_plugin_config=None):
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
    if plugin == "satellite":
        logger.info("Starting satellite pre-processing plugin.")

        # If no config is provided (None), the plugin will apply defaults
        return satellite_plugin(field, config=satellite_plugin_config)

    elif plugin == "flight":
        raise NotImplementedError(
            "Flight pre-processing plugin yet to be finalised.")

    elif plugin == "UM":
        raise NotImplementedError(
            "UM pre-processing plugin yet to be finalised.")

    elif plugin == "WRF":
        raise NotImplementedError(
            "WRF pre-processing plugin yet to be finalised.")

    else:
        return field


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

    logger.warning(
        f"Applied override to observational times, now have: {obs_times}, "
        f"with data of: {obs_times.data}"
    )
    return obs_times


@timeit
def check_time_coverage(obs_times, model_times):
    """TODO"""

    msg_start = (
        "Model data datetimes must cover the whole of the datetime range "
        "spanned by the observational data, but got"
    )

    # TODO can we replace with first and last value since we are
    # assuming (to document) times are never decreasing in order
    #model_min = model_times[0]
    #obs_min = obs_times[0]
    #model_max = model_times[-1]
    #obs_max = obs_times[-1]
    model_min = model_times.minimum()
    obs_min = obs_times.minimum()
    model_max = model_times.maximum()
    obs_max = obs_times.maximum()

    logger.debug(
        f"Model data has maxima {model_max!r} and minima {model_min!r}"
    )
    logger.debug(f"Obs data has maxima {obs_max!r} and minima {obs_min!r}")

    if model_min > obs_min:
        raise ValueError(
            f"{msg_start} minima of {model_min!r} for the model > {obs_min!r} "
            "for the observations."
        )
    if model_max < obs_max:
        raise ValueError(
            f"{msg_start} maxima of {model_max!r} for the model < {obs_max!r} "
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

    obs_times_units = obs_times.get_property("units", None)
    logger.info(f"Units on obs. time coordinate are: {obs_times_units}")
    model_times_units = model_times.get_property("units", None)
    logger.info(f"Units on model time coordinate are: {model_times_units}")

    # Ensure the units of the obs and model datetimes are consistent - conform
    # them if they differ.
    if obs_times_units and model_times_units:
        same = obs_times.Units.equals(model_times.Units)
        if not same:
            # Change the units on the model (not obs) times since there are
            # fewer data points on those, meaning less converting work.
            # Will raise its own error here if units are not equivalent.
            model_times.Units = obs_times.Units
            logger.info(f"Unit-conformed model time coord. is: {model_times}")

        logger.debug(
            f"Units on observational and model time coords. are the same: "
            f"{same}\n"
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

    obs_calendar = obs_times.get_property("calendar", None)
    logger.info(f"Calendar on obs. time coordinate is: {obs_calendar}")

    model_calendar = model_times.get_property("calendar", None)
    logger.info(f"Calendar on model time coordinate is: {model_calendar}")

    # If both have calendars defined, we need to check for consistency
    # between these, else the datetimes aren't comparable
    if obs_calendar and model_calendar:
        # Some custom calendar consistency logic, necessary for e.g. WRF data
        before_pg_cutoff = cf.gt(cf.dt(1582, 10, 15))
        if (
            obs_calendar == "standard"
            and model_calendar == "proleptic_gregorian"
            and before_pg_cutoff.evaluate(model_times.minimum())
        ):
            # 'A calendar with the Gregorian rules for leap-years extended to
            #  dates before 1582-10-15', see:
            # https://cfconventions.org/Data/cf-conventions/
            # cf-conventions-1.11/cf-conventions.html#calendar
            # so it unless the data is before 1582, e.g. very historical runs,
            # it i equivalent to have 'standard' set (and can match up).
            logger.info(
                f"Changing {model_times} calendar from '{model_calendar}' to "
                "'standard' (equivalent given all times are after 1582-10-15) "
                "to enable the time co-location to work."
            )
            model_times.override_calendar("standard", inplace=True)

        logger.debug(
            f"Calendars on observational and model time coords. are the same?: "
            f"{obs_times.calendar == model_times.calendar}\n"
        )


@timeit
def persist_all_metadata(field):
    """Persist all of the metadata for a field.
    """
    logger.warning(
        f"Persisting data for all metadata constructs of field."
    )
    for construct_name, construct_obj in field.constructs.filter_by_data(
            todict=True).items():
        logger.debug("Construct is", construct_name)
        construct_obj.persist(inplace=True)


def bounding_box_query(
        model_field, model_id, coord_tight_bounds, model_coord):
    """TODO."""
    logger.info(
        f"Starting a bounding box query for {coord_tight_bounds} on "
        f"{model_coord} of {model_field} "
    )

    obs_time_min, obs_time_max = coord_tight_bounds

    # Get an array with truth values representing whether the obs values
    # are inside or outside the region of relevance for the model field
    # TODO use greater/less than or equal to (e.g. 'gt' or 'ge')?
    # TODO could combine into one 'wo' to simplify, probably?
    # Note we can't do 'wo' since for these cases there wouldn't be
    # want zeros.
    min_query_result = cf.lt(obs_time_min) == model_coord
    max_query_result = cf.gt(obs_time_max) == model_coord

    # Get indices of last case of index being outside of the range of the
    # obs times fr below, and the first of it being outside from above in terms
    # of position. +/1 will ensure we take the values immediately around.
    # Method based on the below logic, want 2 and 4 as resulting indices:
    #    >>> a = [1, 1, 1, 0, 0, 0, 0, 0]
    #    >>> b = [0, 0, 0, 0, 1, 1, 1, 1]
    #    >>> np.argmin(a)
    #    3
    #    >>> np.argmax(b)
    #    4
    # Note: originally tried np.where(a)[0][-1] and np.where(b)[0][0][5]
    # instead of argmin/max but that will be less efficient(?)

    lower_index = np.argmin(min_query_result)
    upper_index = np.argmax(max_query_result)

    # Remove 1 *only* if the index is not the first one already, else we
    # get an index of 0-1=-1 which is the last value and will mess things up!
    # And the same for the final index.
    # TODO check for cyclicity considerations.
    if lower_index != 0:
        lower_index -= 1
    if upper_index != model_coord.size:
        upper_index += 1

    slice_on = [lower_index, upper_index]

    logger.info(
        f"Bounding box indices are min {lower_index} and max {upper_index}")
    # Now can do a subspace using these indices
    model_field_after_bb = model_field.subspace(
        "envelope", **{model_id: slice(*tuple(slice_on))})

    logger.info(f"Results from bounding box query is: {model_field_after_bb}")

    return model_field_after_bb


@timeit
def subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field, halo_size, verbose, no_vertical=False,
):
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
    if not no_vertical:
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

    # Note: this requires a 'halo' plugin_config. feature introduced in
    #       cf-python 3.16.2.
    # TODO SLB: need to think about possible compications of cyclicity, etc.,
    #           and account for those.
    # Note: getting some dask arrays out instead of slices, due to Dask
    # laziness. DH to look into.
    x_coord_tight_bounds = obs_X.data.minimum(), obs_X.data.maximum()
    y_coord_tight_bounds = obs_Y.data.minimum(), obs_Y.data.maximum()
    if not no_vertical:
        z_coord_tight_bounds = obs_Z.data.minimum(), obs_Z.data.maximum()
    t_coord_tight_bounds = obs_times.data.minimum(), obs_times.data.maximum()

    bb_kwargs = {
        "X": cf.wi(*x_coord_tight_bounds),
        "Y": cf.wi(*y_coord_tight_bounds),
        # Can't just use 'T' here since we might have a different name
        model_t_id: cf.wi(*t_coord_tight_bounds),
    }
    if not no_vertical:
        bb_kwargs["Z"] = cf.wi(*z_coord_tight_bounds)

    # Attempt to do a full bounding box subspace immediately (if indices call
    # works, the subspace call will work) - if it works, great! But probably it
    # won't work and we deal with that next...
    immediate_subspace_works = False
    try:
        model_field_bb_indices = model_field.subspace(
            "envelope", halo_size, **bb_kwargs
        )
        immediate_subspace_works = True
        if verbose:
            logger.debug(
                "Immediate full indices calculation attempt WORKED, "
                f"proceeding using {model_field_bb_indices}"
            )
    except Exception as exc:
        logger.debug(
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
        logger.info(
            "Set to create 4D bounding box onto model field, based on obs. field "
            f"tight boundaries of (4D: X, Y, Z, T):\n{pformat(bb_kwargs)}\n"
        )

        vertical_sn = None
        # Note: can do the spatial and the temporal subspacing separately, and if
        # want to do this make the call twice for each coordinate arg. Reasons we
        # may want to do this include having separate halo sizes for each
        # coordinate, etc.
        model_field_bb = model_field.subspace(
            "envelope", halo_size, **bb_kwargs
        )
    else:  # more likely case, so be more careful and treat axes separately
        # Time
        logger.info("1. Time subspace step")
        time_kwargs = {model_t_id: cf.wi(*t_coord_tight_bounds)}

        # TODO partial also not working here - clues, clues.
        try:
            # For the time subspace (only), we don't need a halo
            model_field = model_field.subspace(
                "envelope", **time_kwargs
            )
        except ValueError:
            # Both times may sit inside between one model time and another
            # and the time subspace may fail then, and we can't solve this
            # with a halo because the subspace doesn't know what point to
            # 'halo' around. So we need to be more clever.
            # TODO we decided to write this into this module then move it out
            # as a new query to cf eventually.
            model_field = bounding_box_query(
                model_field, model_t_id, t_coord_tight_bounds, model_times)

        logger.info(
            f"Time ('{model_t_id}') bounding box calculated. It is: "
            f"{model_field}"
        )

        # Horizontal
        logger.info("2. Horizontal subspace step")
        # For this case where we do 3 separate subspaces, we reassign to
        # the same field and only at the end create 'model_field_bb' variable.
        # We should be safe to do the horizontal subspacing as one

        # TODO do we need to ensure cyclicity set correctly, or should that
        # be guaranteed by pre-proc or compliance reqs?

        try:
            model_field = model_field.subspace(
                "envelope",
                halo_size,
                X=cf.wi(*x_coord_tight_bounds),
                Y=cf.wi(*y_coord_tight_bounds),
            )
            logger.info(
                "Horizontal ('X' and 'Y') bounding box calculated. It is: "
                f"{model_field}"
            )
        except ValueError:
            # Two possible issues here: it could be that all of the X and/or
            # all of the Y points sit within two model X or Y points, such
            # that we need to do a bounding box query one either or both of
            # these OR it could be that, usually for data defined at either
            # of the poles, the subspace is hitting a bug in cf-python whereby
            # slices which act on cyclic axes which have near-full coverage
            # of the possible axes values, such as cf.wi(-179, 179) for the
            # longitude will fail. In the latter case, nothing (much) would be
            # subspaced out anyway, so it is safe and alomost equivalent to
            # not perform the subpace along that axes anyway.
            #
            # To distinguish these two cases, for now until the latter/bug is
            # fixed, check the extent of outside of the query.

            # X axis case separately
            X = model_field.coordinate("X")
            wo_query_x = cf.wo(*x_coord_tight_bounds) == X
            wo_count_x = np.sum(wo_query_x.array)
            # TODO choose right < value here, should probably be 1 but check
            # how halo effects might influence
            if wo_count_x < 3:  # extend by 1 each side to acount for halo effect
                model_field = bounding_box_query(
                    model_field, "X", x_coord_tight_bounds, X
                )
            # Else it is the latter/bug case so we are good to continue without
            # the x axis subspace.

            # Y axis case separately
            Y = model_field.coordinate("Y")
            wo_query_y = cf.wo(*y_coord_tight_bounds) == Y
            wo_count_y = np.sum(wo_query_y.array)
            # TODO choose right < value here, should probably be 1 but check
            # how halo effects might influence
            if wo_count_y < 3:  # extend by 1 each side to acount for halo effect
                model_field = bounding_box_query(
                    model_field, "Y", y_coord_tight_bounds, X
                )
            # Else it is the latter/bug case so we are good to continue without
            # the x axis subspace.

        # Vertical, if appropriate
        # Now we set model_field -> model_field_bb, as this is our
        # last separate subspace.
        if no_vertical:
            model_field_bb = model_field
            vertical_sn = False
        else:
            logger.info("3. Vertical subspace step")
            # First, need to calculate the vertical coordinates if there are
            # parametric vertical dimension coordinates to handle.
            # TODO cater for case where are > 1 coord refs (ValueError for now)
            coord_ref = model_field.coordinate_reference(default=None)
            if not coord_ref:  # no parametric coords, simple case
                model_field_bb = model_field.subspace(
                    "envelope",
                    halo_size,
                    Z=cf.wi(*z_coord_tight_bounds),
                )
                vertical_sn = False
            else:
                logger.info(
                    "Need to calculate parametric vertical coordinates. "
                    "Attempting..."
                )
                model_field_w_vertical = model_field.compute_vertical_coordinates()

                # TODO: see Issue 802, after closure will have better way to know
                # the vertical coordinate added by the calc, if it added it at all:
                # https://github.com/NCAS-CMS/cf-python/issues/802
                added_vertical = not model_field_w_vertical.equals(model_field)
                if not added_vertical:
                    raise ValueError("Couldn't calculate vertical coordinates.")

                # If a vertical dim coord was added, we need to use that for our
                # z coordinate from now onwards
                # TODO move vertical calc. out of this method more generally for
                # better processing going forward
                # TODO handle lack of, will currently give ValueError
                vertical_sn = model_field_w_vertical.coordinate_reference().coordinate_conversion.get_parameter(
                    "computed_standard_name"
                )
                new_z_coord = model_field_w_vertical.coordinate(vertical_sn)
                logger.info(
                    "Added vertical coordinates from parameters: "
                    f"{new_z_coord.dump(display=False)}."
                )

                # Reset model_field to one with vertical coord now
                # TODO use in-place before so no need to create new one?
                model_field = model_field_w_vertical
                logger.info(
                    "Model field with vertical coords is: "
                    f"{model_field.dump(display=False)}"
                )

                # Unit conforming: convert units on new cal'd Z to obs Z units
                # TODO can deal with further unit conformance using query units
                # for the queries we subspace on!
                new_z_coord.Units = obs_Z.Units
                logger.info(
                    "Units conformed for computed vertical coordinates:"
                    f"{new_z_coord} with same units as {obs_Z}"
                )

                vert_kwargs = {vertical_sn: cf.wi(*z_coord_tight_bounds)}
                # TODO: partial case commented below is breaking things here! WHY!?
                # ## model_field = model_field_bb_subspace(**vert_kwargs)
                model_field_bb = model_field.subspace(
                    "envelope",
                    halo_size,
                    **vert_kwargs,
                )

            logger.info(
                f"Vertical ('Z') bounding box calculated. It is: {model_field_bb}"
            )
            # Note: no need to persist at end like with stages 1-2 of BB for
            # time and horizontal since there is a persist after this method
            # is called.

    logger.info(
        "4D bounding box calculated. Model data with bounding box applied is: "
        f"{model_field_bb}"
    )

    return model_field_bb, vertical_sn


@timeit
def spatial_interpolation(
    obs_field,
    model_field_bb,
    interpolation_method,
    interpolation_z_coord,
    source_axes,
    model_t_identifier,
    vertical_sn,
    no_vertical,
):
    """Interpolate the flight path spatially (3D for X-Y and vertical Z).

    Horizontal X-Y and vertical Z coordinates are interpolated. This is
    done under-the-hood in cf-python with the ESMF LocStream feature, see:
    https://xesmf.readthedocs.io/en/latest/notebooks/Using_LocStream.html

    TODO: DETAILED DOCS
    """
    # TODO: UGRID grids might need some extra steps/work for this.

    logger.info(
        "Starting spatial interpolation (regridding) step..."
    )

    if no_vertical:
        logger.warning(
            f"Doing spatial regridding without using vertical levels.")
        spatially_colocated_field = model_field_bb.regrids(
            obs_field,
            method=interpolation_method,
            src_axes=source_axes,
        )
        logger.info("\nSpatial interpolation (regridding) complete.\n")
        logger.info(f"XY-colocated data is:\n {spatially_colocated_field}")

        return spatially_colocated_field

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
            method=interpolation_method,
            z=interpolation_z_coord,
            # TODO, guess we set ln_z if z is altitude not pressure?
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
            model_t_identifier, item=True
        )

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
            new_z_coord,
            axes=[model_t_identifier, "Z", source_axes["Y"], source_axes["X"]],
        )
        z_coord = model_field_bb.coordinate(new_vertical_id)
        z_coord.set_property("standard_name", value=vertical_sn)

        spatially_colocated_fields = cf.FieldList()

        for mtime in model_bb_t:
            kwargs = {model_t_identifier: mtime}
            # TODO what subspace args might we want here?
            model_field_z_per_time = model_field_bb.subspace(**kwargs)
            z_coord_per_time = model_field_z_per_time.coordinate(vertical_sn)

            # Need to squeeze out the time coordinate, but ONLY from the
            # vertical_sn (computer vertical coords) z coordinate, not the
            # data axes overall.
            model_field_z_per_time.del_construct(vertical_sn)
            fin_z_coord = z_coord_per_time.squeeze(time_da_index)
            model_field_z_per_time.set_construct(
                fin_z_coord,
                axes=["Z", source_axes["Y"], source_axes["X"]],
            )

            logger.info(
                f"Squeezed Z coordinate: {z_coord_per_time},"
                f"{z_coord_per_time.data}"
            )
            logger.info(
                f"Model field per time data is: {model_field_z_per_time}"
            )

            # ALSO NEED TO SQUEEZE X AND Y AUX COORDS! for those 2d aux
            # lat and lons! Then everything is all set up for the 3D Z regrids
            # HACK FIRST USE DIRECT NAMES TO GET WORKIN: ncvar%XLAT, ncvar%XLONG
            for a_name in ("ncvar%XLAT", "ncvar%XLONG"):
                a_coord = model_field_z_per_time.coordinate(a_name)
                model_field_z_per_time.del_construct(a_name)
                fin_a_coord = (
                    a_coord.squeeze()
                )  # safe - can other dim be size 1?
                model_field_z_per_time.set_construct(
                    fin_a_coord,
                    axes=[source_axes["Y"], source_axes["X"]],
                )

            # Do the regrids weighting operation for the 3D Z in each case
            spatially_colocated_field_comp = model_field_z_per_time.regrids(
                obs_field,
                method=interpolation_method,
                z=vertical_sn,
                ln_z=True,  # TODO should we use a log here in this case?
                src_axes=source_axes,
            )
            logger.info(
                f"3D Z colocated field component for {mtime} is "
                f"{spatially_colocated_field_comp} "
            )
            spatially_colocated_fields.append(spatially_colocated_field_comp)
        # Finally, need to concatenate the individually-regridded per-time
        # components
        spatially_colocated_field = cf.Field.concatenate(
            spatially_colocated_fields
        )
        logger.info(
            f"Final concatenated field (from 3D Z colocated fields) is "
            f"{spatially_colocated_field} "
        )

    # TODO: consider whether or not to persist the regridded / spatial interp
    # before the next stage, or to do in a fully lazy way.

    logger.info("\nSpatial interpolation (regridding) complete.\n")
    logger.info(f"XYZ-colocated data is:\n {spatially_colocated_field}")

    return spatially_colocated_field


def time_subspace_per_segment(
    index,
    model_times_len,
    t1,
    t2,
    m,
    obs_time_key,
    model_time_key,
    model_t_identifier,
):
    """TODO."""
    # Define the pairwise segment datetime endpoints
    logger.info(f"Datetime endpoints for this segment are: {t1}, {t2}.\n")

    # Define a query which will find any datetimes within these times
    # to map all observational times to the appropriate segment, later.
    q = cf.wi(
        cf.dt(t1), cf.dt(t2), open_upper=True
    )  # TODO is cf.dt wrapping necessary?
    logger.info(f"Querying with query: {q} on field:\n{m}\n")

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
    logger.info(
        f"\nUsing subspace arguments for i=0 of: {s0_subspace_args}\n"
    )
    s0 = m.subspace(**s0_subspace_args)

    s1_subspace_args = {
        obs_time_key: q,
        model_time_key: [index + 1],
    }
    logger.info(
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
    logger.debug(
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
    split_segments=False,
):
    """Interpolate the flight path temporally (in time T).

    This co-locates between model data time points to match the time
    coordinate sampling of the flight path and is done using a method that
    performs a convolution-based merge of relevant segments of the
    (bouding box subspaced) model field already interpolated spatially onto
    the flight path.

    TODO: DETAILED DOCS
    """
    logger.info("Starting time interpolation step.")
    if split_segments:
        logger.info("Using split segments.\n")

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

    logger.info(
        f"Number of model time data points: {model_times_len}\n"
        f"Number of observational time sample data points: {obs_times_len}\n"
    )
    logger.info(f"Observational (aux) coord. time key is: {obs_time_key}")
    logger.info(f"Model (dim) time key is: {model_time_key}\n")

    # Empty objects ready to populate - TODO make these FieldLists if approp.?
    v_w = []

    # Iterate over pairs of adjacent model datetimes, defining 'segments'.
    # Chop the flight path up into these *segments* and do a weighted merge
    # of data from segments adjacent in the model times to form the final
    # time-interpolated value.
    logger.info(
        "*** Begin iteration over pairwise 'segments'. ***\n"
        f"Segments to loop over are, pairwise: {model_times.datetime_array}"
    )
    # Note the length of (pairwise(model_times.datetime_array) is equal to
    # model_times_len - 1 by its nature, e.g. A, B, C -> (A, B), (B, C)).
    for index, (t1, t2) in enumerate(pairwise(model_times.datetime_array)):
        logger.info(f"\n*** Segment {index} ***\n")
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
        # HACK
        if True:  ####index in (halo_size - 1, model_times_len - 1 - halo_size):
            permit_null_subspace = True
            logger.debug(
                "Allowing potential null-return subspace for segment emerging "
                f"from halo size of {halo_size}, equivalent halo position in "
                f"time segment array of: {index + 1}/{model_times_len - 1}"
            )

        if permit_null_subspace:
            try:
                values_weighted = time_subspace_per_segment(
                    index,
                    model_times_len,
                    t1,
                    t2,
                    m,
                    obs_time_key,
                    model_time_key,
                    model_t_identifier,
                )
                v_w.append(values_weighted)
            except IndexError:
                logger.debug(
                    f"Null-return subspce for segment with: {t1}, {t2}.\n"
                    "This is a result of the halo_size set, so not a cause "
                    "for concern!"
                )
        else:
            values_weighted = time_subspace_per_segment(
                index,
                model_times_len,
                t1,
                t2,
                m,
                obs_time_key,
                model_time_key,
                model_t_identifier,
            )
            v_w.append(values_weighted)

    # NOTE: masked values are mostly/all to do with the pressure being below
    #       when flight lands and takes off etc. on runway and close, cases
    #       relating to the Heaviside function. So it is all good and expected
    #       to have masked values in the data, at the end and/or start.
    #       Eventually we will add an extrapolation option whereby user can
    #       choose to extrapolate as well as interpolate, and therefore assign
    #       values to the masked ones.
    logger.info("Final per-segment weighted value arrays are:")
    logger.info(pformat(v_w))

    if not v_w:
        raise ValueError("Empty weights array, something went wrong!")
    # Concatenate the data values found above from each segment, to finally
    # get the full set of model-to-obs co-located data.
    if len(v_w) > 1:  # TODO is this just a hack?
        concatenated_weighted_values = cf.Data.concatenate(v_w)
        logger.info(
            "\nFinal concatenated weighted value array is: "
            f"{concatenated_weighted_values.array}, with length: "
            f"{len(concatenated_weighted_values)}\n"
        )
    else:
        # HACK, getting all 19 air pressure values for now, take first one as
        # case whilst get working generally
        concatenated_weighted_values = v_w[0]
        # Note that 0th index here gives all 0 values - maybe they are all masked
        # for that and some other indices?
        concatenated_weighted_values = concatenated_weighted_values[
            10, :].squeeze()

    # Report on number of masked and unmasked data points for info/debugging
    masked_value_count = (
        len(concatenated_weighted_values)
        - concatenated_weighted_values.count()
    ).array[0]
    logger.debug(
        f"Masking: {concatenated_weighted_values.count().array[0]} "
        f"non-masked values vs. {masked_value_count} masked."
    )

    # Finally, reattach that data to (a copy of) the obs field to get final
    # values on the right domain, though we still need to adapt the metadata to
    # reflect the new context so that the field with data set is contextually
    # correct.
    final_result_field = obs_field.copy()

    logger.info(
        f"Concatenated weighted values are: {concatenated_weighted_values}"
    )

    try:
        final_result_field.set_data(
            concatenated_weighted_values, inplace=True)
    except:
        final_result_field.set_data(
            concatenated_weighted_values,
            inplace=True, set_axes=False
        )

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
    )  # include divider to previous critical
    final_result_field.set_property("history", history_details)
    logger.info(
        "\nNew history message reads: "
        f"{final_result_field.get_property('history')}\n"
    )

    logger.info("\nFinal result field is:\n" f"\n{final_result_field}\n")
    logger.info("The final result field has data statistics of:\n")
    logger.info(pformat(final_result_field.data.stats()))

    # TODO: consider whether or not to persist the regridded / time interp.
    # before the next stage, or to do in a fully lazy way.

    logger.info("\nTime interpolation complete.")

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

    logger.info("Writing of output file complete.")


@timeit
def make_outputs_plot(
    output,
    obs_t_identifier,
    cfp_output_levs_config,
    outputs_dir,
    plotname_start,
    new_obs_starttime,
    cfp_output_general_config,
    verbose,
    preprocess_model=False,
):
    """Generate a post-colocation result plot of the track(s) or swath(s).

    The plot may optionally be displayed during script execution, else
    saved to disk.

    TODO: DETAILED DOCS
    """
    cfp_output_general_config.update(verbose=verbose)

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

    # WRF ONLY, TODO move underlying logic to pre-processing so as not to
    # clog up main module
    if preprocess_model == "WRF":
        aux_coor_t = output.auxiliary_coordinate(obs_t_identifier)
        dim_coor_t = cf.DimensionCoordinate(source=aux_coor_t)
        output.set_construct(dim_coor_t, axes="ncdim%obs")

    # Make and open the final plot
    # NOTE: can try 'legend_lines=True' for the lines plotted with average
    #       between the two scatter marker points, if preferable?
    cfp.gopen(
        file=f"{outputs_dir}/{plotname_start}_final_colocated_field.png",
    )

    # Set levels for plotting of data in a colourmap
    # Min, max as determined using output.min(), .max():
    if cfp_output_levs_config:
        cfp.levs(**cfp_output_levs_config)

    # Note the set start time of the obs on the plot title as key info.
    if new_obs_starttime:
        update_title = f"assuming starting time of {new_obs_starttime}"
        orig_title = cfp_output_general_config.get("title", None)
        if orig_title:
            cfp_output_general_config.update(
                title=f"{orig_title} {update_title}"
            )
        else:
            cfp_output_general_config["title"] = update_title.title()

    cfp.traj(output, **cfp_output_general_config)

    cfp.gclose()
    logger.info("Plot created.")


@timeit
def colocate_single_file(
    file_to_colocate,
    index,
    args,
    preprocess_obs,
    skip_all_plotting,
    outputs_dir,
    plotname_start,
    verbose,
    model_field,  # TODO pull this out of loop
    halo_size,  # TODO use args instead of names since pass args in
    interpolation_method,
    colocation_z_coord,
):
    """Perform model-to-observational colocation using a single file source."""
    logger.info(
        f"\n_____ Start of colocation iteration with file number {index + 1}: "
        f"{file_to_colocate} _____\n"
    )

    # Process and validate inputs, including optional preview plot
    obs_data = read_obs_input_data(file_to_colocate)
    if obs_data is None:
        return

    obs_field = get_input_fields_of_interest(
        obs_data, args.chosen_obs_fields)
    # Apply any specified pre-processing: use returned fields since the
    # input may be a FieldList which gets reduced to less fields or to one
    if preprocess_obs:
        obs_field = ensure_cf_compliance(
            obs_field, preprocess_obs, args.satellite_plugin_config)

    # Persist obs field - do this as early as possible, but after
    # the pre-processing
    persist_all_metadata(obs_field)

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
            index,
        )

    # Time coordinate considerations, pre-colocation
    times, time_identifiers = get_time_coords(obs_field, model_field)
    obs_times, model_times = times
    obs_t_identifier, model_t_identifier = time_identifiers

    new_obs_starttime = args.start_time_override
    if new_obs_starttime:
        # TODO can just do in-place rather than re-assign, might be best?
        obs_times = set_start_datetime(
            obs_times, obs_t_identifier, new_obs_starttime
        )

    # TODO apply obs_t_identifier, model_t_identifier in further logic
    ensure_unit_calendar_consistency(obs_field, model_field)

    # Ensure the model time axes covers the entire time axes span of the
    # obs track, else we can't go forward - if so inform about this clearly
    check_time_coverage(obs_times, model_times)

    # For the satellite swath cases, ignore vertical height since it is
    # dealt with by the averaging kernel.
    # TODO how do we account for the averging kernel work in this case?
    no_vertical = False
    if preprocess_obs == "satellite":
        no_vertical = True

    # Subspacing to remove irrelavant information, pre-colocation
    # TODO tidy passing through of computed vertical coord identifier
    model_field_bb, vertical_sn = subspace_to_spatiotemporal_bounding_box(
        obs_field, model_field, halo_size, verbose, no_vertical=no_vertical,
    )

    # Perform spatial and then temporal interpolation to colocate
    spatially_colocated_field = spatial_interpolation(
        obs_field,
        model_field_bb,
        interpolation_method,
        colocation_z_coord,
        args.source_axes,
        model_t_identifier,
        vertical_sn,
        no_vertical,
    )

    # For such cases as satellite swaths, the times can straddle model points
    # so we need to chop these up into ones on each side of a model time
    # segmentm as per our approach below.
    split_segments = False
    if preprocess_obs == "satellite":
        split_segments = True

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
        split_segments=split_segments,
    )

    logger.info(f"End of colocation iteration with file: {file_to_colocate}")
    return final_result_field, obs_t_identifier  # TODO remove obs_t from ret


@timeit
def main():
    """Perform end-to-end model-to-observational co-location."""

    # Print the ASCII VISION banner - this must come before any logging!
    print(toolkit_banner())

    # Env print
    get_env_and_diagnostics_report()

    # Prepare inputs and config. ready for possibly-iterative co-location
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
    preprocess_obs = args.preprocess_mode_obs
    preprocess_model = args.preprocess_mode_model
    # TODO: eventually remove the deprecated alternatives, but for now
    # accept both (see cli.py end of process_cli_arguments for the listing
    # of any deprecated options)
    # Note that e.g. "A" or "B" evaluates to "A"
    colocation_z_coord = args.vertical_colocation_coord or args.regrid_z_coord
    interpolation_method = (
        args.spatial_colocation_method or args.regrid_method)

    # Need to do this again here to pick up on this module's logger
    setup_logging(verbose)

    # Read in model outside of a loop
    model_data = read_model_input_data(args.model_data_path)
    model_field = get_input_fields_of_interest(
        model_data, args.chosen_model_fields)
    if preprocess_model:
            model_field = ensure_cf_compliance(model_field, preprocess_model)

    # Persist model field outside of loop
    persist_all_metadata(model_field)

    # Initiate to store colocated fields
    output_fields = cf.FieldList()

    # Start colocating the indivdual files to read (which may just be one
    # file in many cases)
    read_file_list = get_files_to_individually_colocate(args.obs_data_path)
    length_read_file_list = len(read_file_list)
    logger.info(f"Read file list has length: {length_read_file_list}")
    if not read_file_list:
        raise ValueError(
            f"Bad path, nothing readable by cf: {args.obs_data_path}")

    logger.info(
        "\n_____ Starting colocation iteration to cover a total of "
        f"{length_read_file_list} files."
    )
    for index, file_to_colocate in enumerate(read_file_list):
        file_fl_result, obs_t_identifier = colocate_single_file(
            file_to_colocate,
            index,
            args,
            preprocess_obs,
            skip_all_plotting,
            outputs_dir,
            plotname_start,
            verbose,
            model_field,  # TODO pull this out of loop
            halo_size,  # TODO use args instead of names since pass args in
            interpolation_method,
            colocation_z_coord,
        )
        if file_fl_result is None:
            continue
        output_fields.append(file_fl_result)

    # 3. Post-processing of co-located results and prepare outputs
    if not output_fields:
        raise ValueError("Empty resulting FieldList: something went wrong!")

    compound_output = len(output_fields) > 1
    if compound_output:
        # Concatenate the fields now since they should all constitute one
        # DSG feature.
        output = output_fields.concatenate()
        logger.info(
            f"Have compound output, a FieldList of length {len(output_fields)}"
        )
    else:
        output = output_fields[0]  # unpack to field in this case
        logger.info(
            "Have singular output i.e. just one result field."
        )
        logger.info(
        "Final pre-concatenated fieldlist from colocation of all inputs "
        f"from specified observational data path is: {output_fields}"
    )

    logger.info(
        "Final Field(List) from colocation of all inputs from specified "
        f"observational data path is: {output}"
    )

    # Create and process outputs
    create_cra_outputs()  # TODO currently does nothing

    # TODO improve path handling with PathLib library
    output_path_name = f"{outputs_dir}/{args.output_file_name}"
    write_output_data(output, output_path_name)

    if not skip_all_plotting:
        # Plot the output
        make_outputs_plot(
            output,
            obs_t_identifier,
            args.cfp_output_levs_config,
            outputs_dir,
            plotname_start,
            args.start_time_override,
            args.cfp_output_general_config,
            verbose,
            preprocess_model,
        )


if __name__ == "__main__":
    sys.exit(main())
