"""Converter for certain WRF datasets to ensure CF Compliant ZT coordinates."""

import logging

import cf


logger = logging.getLogger(__name__)


def wrf_extra_compliance_fixes(
        model_field_bb, z_coord, z_axes_spec, z_id,
        model_t_identifier
):
    """Extra CF compliance fixes for WRF data.

    TODO: DETAILED DOCS
    """
    # TODO possible bug in WRF pre-proc or in cf whereby aux coord axes
    # are not in compatible order with the data axes. For now, swap
    # them over but this should be rectified with WRF experts.
    new_z_coord = z_coord.swapaxes(1, 0)
    z_name = model_field_bb.construct(z_id).standard_name
    model_field_bb.del_construct(z_id)
    txyz_axes = [model_t_identifier,] + z_axes_spec
    new_z_id = model_field_bb.set_construct(
        new_z_coord,
        axes=txyz_axes,
    )
    z_coord = model_field_bb.coordinate(new_z_id)

    # Must take care to set standard name not key as the value! To aid this
    # could do with renaming variables to make them clearer (TODO)
    z_coord.set_property("standard_name", value=z_name)

    return z_coord


def wrf_further_compliance_fixes(
        model_field_z_per_time, vertical_sn, time_da_index, z_axes_spec,
        source_axes, lat_id="ncvar%XLAT", lon_id="ncvar%XLONG",
):
    """More CF compliance fixes for WRF data.

    TODO: DETAILED DOCS
    """
    z_coord_per_time = model_field_z_per_time.coordinate(vertical_sn)

    # Need to squeeze out the time coordinate, but ONLY from the
    # vertical_sn (computer vertical coords) z coordinate, not the
    # data axes overall.
    model_field_z_per_time.del_construct(vertical_sn)
    z_coord_per_time.squeeze(time_da_index, inplace=True)
    fin_z_coord = z_coord_per_time

    new_z_id = model_field_z_per_time.set_construct(
        fin_z_coord,
        axes=z_axes_spec,
    )
    z_coord = model_field_z_per_time.coordinate(new_z_id)
    z_coord.set_property("standard_name", value=vertical_sn)

    logger.info(
        f"Squeezed Z coordinate: {z_coord_per_time},"
        f"{z_coord_per_time.data}"
    )
    logger.info(
        f"Model field per time data is: {model_field_z_per_time}"
    )

    # Also need to squeeze x and y aux coords! for those 2D aux
    # lat and lons! Then everything is all set up for the 3D Z regrids.
    # Need to do this so we have lat and lon coords which are usable
    # for the regrids later, else get the error:
    # ValueError: Could not find 1-d nor 2-d latitude and longitude coordinates
    for a_name in (lat_id, lon_id) and source_axes:
        # These keys are safe to get, since raise error if they
        # weren't present above
        x_y_axes_spec = [source_axes["Y"], source_axes["X"]]

        a_coord = model_field_z_per_time.coordinate(a_name)
        model_field_z_per_time.del_construct(a_name)

        # Is this safe - can other dim be size 1 that we don't want to squeeze?
        fin_a_coord = (
            a_coord.squeeze()
        )
        new_a_id = model_field_z_per_time.set_construct(
            fin_a_coord,
            axes=x_y_axes_spec,
        )
        a_coord = model_field_z_per_time.coordinate(new_a_id)