"""Converter for CF compliance pre-processing of a satellite swath field."""

import logging

from pprint import pformat

import cf


logger = logging.getLogger(__name__)


# Configuration based on variable names etc. These defaults are used unless
# the user specifies any config. to override this
PLUGIN_CONFIG_DEFAULTS = {
    "latitude": "latitude",
    "longitude": "longitude",
    "sensingtime": "sensingtime",
    "do_retrieval": "do_retrieval",
    "sensingtime_msec": "sensingtime_msec",
    "sensingtime_day": "sensingtime_day",
    "sensingtime": "sensingtime",
    "npres": "npres",
    "npi": "npi",
}


def satellite_compliance_plugin(fieldlist, config=None):
    """The converter.

    Configuration may be provided to override the defaults.
    """
    logging.info(
        f"Before pre-processing, fieldlist to satellite plugin is {fieldlist}"
    )

    plugin_config = PLUGIN_CONFIG_DEFAULTS
    if config:
        # Basic validation of input as dict of keys
        try:
            dict(config)
        except TypeError:
            raise TypeError(
                f"Bad configuration, require dictionary but got: {config}")

        # Only update keys which will do something, else warn of irrelevance
        for config_key, config_value in config.items():
            if config_key in plugin_config:
                plugin_config[config_key] = config_value
            else:
                logging.warning(
                    f"Unrecognised satellite plugin config. item: {config_key}"
                )

    logging.info(
        f"Final configuration for satellite plugin is {pformat(plugin_config)}"
    )

    s0 = fieldlist.select_by_identity("air_temperature")[0]

    # Remove the vertical axis
    index = []
    for i, key in enumerate(s0.get_data_axes()):
        if s0.domain_axis(key).nc_get_dimension() == plugin_config["npres"]:
            index.append(slice(None))
            npres_position = i
        else:
            index.append(0)

    if len(index) != s0.ndim:
        raise ValueError("Unexpected dimensions. TODO EXPAND")

    s = s0[tuple(index)].squeeze()

    # Satellite time - applying standard units
    time_of_day =  fieldlist.select_field(
        f"ncvar%{plugin_config['sensingtime_msec']}")
    time_of_day.override_units("ms", inplace=True)
    time_of_day.dtype = float

    day = fieldlist.select_field(f"ncvar%{plugin_config['sensingtime_day']}")
    day.override_units("day since 2000-01-01", inplace=True)
    day.dtype = float

    time = day.copy()
    time.data += time_of_day.data

    time.clear_properties()
    time.set_property("standard_name", "time")

    # Satelite latitude and longitude
    lat = fieldlist.select_field(f"ncvar%{plugin_config['latitude']}")
    lon = fieldlist.select_field(f"ncvar%{plugin_config['longitude']}")

    # Check for spatial subsetting
    if lat.size == s.size:
        do_retrival = fieldlist.select_field("ncvar%do_retrieval")
        mask = do_retrival.data.where(1, None, cf.masked).mask.persist()

        for f in (time, lat, lon):
            f.where(mask, cf.masked, inplace=True)
            data = f.del_data()
            data.compressed(inplace=True)
            if data.size != s.size:
                raise ValueError("Incompatible sizes. TODO EXPAND")

            f.domain_axis().set_size(s.size)
            f.set_data(data.compressed())

        del mask

    # Create satelite "trajectory"
    s.set_construct(cf.AuxiliaryCoordinate(source=lat))
    s.set_construct(cf.AuxiliaryCoordinate(source=lon))
    s.set_construct(cf.AuxiliaryCoordinate(source=time))
    s.set_property("featureType", "trajectory")

    logging.critical(
        f"Final pre-processed field from satellite plugin is {s}")

    return s
