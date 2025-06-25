"""Plotting module of the VISION toolkit. All plotting functionality is here."""

import logging

# NOTE: keep this order (cfp then cf imported) to avoid Seg Fault issues
import cfplot as cfp
import cf

import numpy as np


logger = logging.getLogger(__name__)


def preview_plots(
    obs_field,
    plot_mode,
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

    # Determine plotting mode, default is 2 (plot only outputs):
    #   0 i.e. False. Don't plot anything (skip all)
    #   1 i.e. standard True: plot both inputs (data on tracks) and outputs
    #   2 meaning true in that we plot, but we only plot the outputs
    #   3 meaning true in that we plot both inputs and outputs, but inputs
    #     are shown track-only i.e. with no data shown on them
    #
    # Could do e.g. 4 and 5 for inputs only (data on track or just track),
    # but doubt there's motivation/application for that unless asked and
    # if we have 5+ modes it is better to change to use two plus flags

    if cfp_input_levs_config:
        cfp.levs(**cfp_input_levs_config)

    # Plot *input* observational data for a preview, before doing anything
    # Min, max as determined using final_result_field.min(), .max():
    if plot_mode == 1:  # i.e. plot inputs with data on tracks
        ### plot_of_input_obs_track_only in (0, 2):
        cfp.gopen(
            file=(
                f"{outputs_dir}/"
                f"{plotname_start}_obs_track_with_data_{index}.png"
            )
        )
        cfp_input_general_config.update(verbose=verbose)
        cfp.traj(obs_field, **cfp_input_general_config)
        cfp.gclose()
    elif plot_mode == 3:  # i.e. plot inputs as tracks only, without data on
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
        cfp.traj(
            equal_data_obs_field, **cfp_input_track_only_config
        )
        cfp.gclose()
        cfp.cscale(
            cfp_cscale
        )  # reset for normal (default-style) plots after


def output_plots(
    output,
    cfp_output_levs_config,
    outputs_dir,
    plotname_start,
    new_obs_starttime,
    cfp_output_general_config,
    verbose,
):
    """Generate a post-colocation result plot of the track(s) or swath(s).

    The plot may optionally be displayed during script execution, else
    saved to disk.

    TODO: DETAILED DOCS
    """
    cfp_output_general_config.update(verbose=verbose)

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
