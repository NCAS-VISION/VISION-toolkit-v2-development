"""Converter for certain WRF datasets to ensure CF Compliant ZT coordinates."""

import logging

import cf


logger = logging.getLogger(__name__)


def wrf_extra_compliance_fixes(
        model_field_bb, z_coord, z_axes_spec, vertical_sn,
        model_t_identifier
):
    """Extra CF compliance fixes for WRF data. TODO move this out of toolkit!

    TODO: DETAILED DOCS
    """
    # TODO possible bug in WRF pre-proc or in cf whereby aux coord axes
    # are not in compatible order with the data axes, so do a HACKY SWAP:
    # WRF pre-proc
    new_z_coord = z_coord.swapaxes(1, 0)  # TODO NOT WORKING?
    model_field_bb.del_construct(vertical_sn)
    txyz_axes = [model_t_identifier,] + z_axes_spec
    # TODO rename vertical_sn to z_id or z_key or similar
    new_vertical_id = model_field_bb.set_construct(
        new_z_coord,
        axes=txyz_axes,
    )
    z_coord = model_field_bb.coordinate(new_vertical_id)
    z_coord.set_property("standard_name", value=vertical_sn)

    return z_coord


def wrf_further_compliance_fixes(
        model_field_z_per_time, vertical_sn, time_da_index, z_axes_spec):
    """More CF compliance fixes for WRF data. TODO move this out of toolkit!

    TODO: DETAILED DOCS
    """
    z_coord_per_time = model_field_z_per_time.coordinate(vertical_sn)

    # Need to squeeze out the time coordinate, but ONLY from the
    # vertical_sn (computer vertical coords) z coordinate, not the
    # data axes overall.
    model_field_z_per_time.del_construct(vertical_sn)
    fin_z_coord = z_coord_per_time.squeeze(time_da_index)
    model_field_z_per_time.set_construct(
        fin_z_coord,
        axes=z_axes_spec,
    )

    logger.info(
        f"Squeezed Z coordinate: {z_coord_per_time},"
        f"{z_coord_per_time.data}"
    )
    logger.info(
        f"Model field per time data is: {model_field_z_per_time}"
    )

    # Also need to squeeze x and y aux coords! for those 2D aux
    # lat and lons! Then everything is all set up for the 3D Z regrids
    # HACK FIRST USE DIRECT NAMES TO GET WORKIN: ncvar%XLAT, ncvar%XLONG
    for a_name in ("ncvar%XLAT", "ncvar%XLONG") and source_axes:
        # These keys are safe to get, since raised error if they
        # werne't present above.
        x_y_axes_spec = [source_axes["Y"], source_axes["X"]]

        a_coord = model_field_z_per_time.coordinate(a_name)
        model_field_z_per_time.del_construct(a_name)
        fin_a_coord = (
            a_coord.squeeze()
        )  # safe - can other dim be size 1?
        model_field_z_per_time.set_construct(
            fin_a_coord,
            axes=x_y_axes_spec,
        )
