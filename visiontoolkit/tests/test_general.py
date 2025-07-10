"""Functional/end-to-end tests for the VISION Toolkit."""

import json
import sys

import pytest
from unittest.mock import patch, mock_open

import visiontoolkit


def run_toolkit_with_config(config_dict, capsys, tmp_path):
    """Test command `$ visiontoolkit --config-file=<config as temp json>`.

    Helper function for testing visiontookit on a given config. via the
    capsys fixture.
    """
    # NOTE: seems like we can't simply mock open to simulate reading the JSON
    # file via mock_open because of internal cf-python file existence checks,
    # so we need to write out a temporary file to test a real JSON config. file
    # from the equivalent config. dict of keys and values. Also this matches
    # real-world behaviour preoperly so is safer as a testing approach.
    config_file = tmp_path / "config_file.json"
    config_file.write_text(json.dumps(config_dict))

    with patch.object(
        sys, "argv", ["visiontoolkit.py", "--config-file", str(config_file)]
    ):
        visiontoolkit.main()

    captured = capsys.readouterr()
    return captured


class TestGeneral:
    """Test the VISION Toolkit application in general.

    This includes minimal command-line specification and in
    particular checking for sensible error messages upon lack of
    adequate configuration provision. Testing here covers anything
    general or that which does not run the main co-location code.

    """

    def test_help(self, capsys, tmp_path):
        """Test the `$ visiontoolkit --help` command."""
        # Setup to run command
        with patch.object(sys, "argv", ["visiontoolkit.py", "--help"]):
            with pytest.raises(SystemExit) as excinfo:
                visiontoolkit.main()  # Run command

        cmd_stdout = capsys.readouterr().out
        cmd_stdout_ignore_newlines = cmd_stdout.replace("\n", " ")

        # Actual testing statements
        # 1. Assert something emerges to STDOUT
        assert cmd_stdout != ""

        # 2. Assert basic text including summary appears
        assert "usage: VISION TOOLKIT" in cmd_stdout
        assert (
            "Virtual Integration of Satellite and In-Situ Observation "
            "Networks (VISION) Toolkit Version 2"
        ) in cmd_stdout_ignore_newlines

        # 3. Assert ASCII project symbol appears
        # Just test this via first line to avoid having to wrestle against
        # newlines and whitespace line splitting
        assert ".______________________________________________." in cmd_stdout

        # 4. Assert some CLI argument help descriptions appear.
        # Don't want to test on any specific option since thes might change
        # with a CLI change, but this 'help' command is guaranteed to be there
        # so check the description of that appears.
        assert "options:" in cmd_stdout
        assert (
            "-h, --help            show this help message and exit"
        ) in cmd_stdout_ignore_newlines


class TestFlightObservationsUMModelConstantPressure:
    """Test toolkit for case of flight path observations and UM model input.

    These cases have constant pressure levels.
    """

    # Base configurations, which the specific configurations tend to build on
    # so use these as a base to override with edited values for the final
    # specific configurations
    obs_data_root = "../data/compliant-data/"
    base_config_constant_vert_levs = {
        # Data paths and chosen fields
        "model-data-path": "../data/main-workwith-test-ISO-simulator/Model_Input",
        "obs-data-path": f"{obs_data_root}core_faam_20170703_c016_STANCO_CF.nc",
        "chosen-model-field": "id%UM_m01s51i010_vn1105",
        "chosen-obs-field": False,
        # cf-plot config.
        "cfp-cscale": "WhiteBlueGreenYellowRed",
        "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
        "cfp-mapset-config": {
            "latmax": 54,
            "latmin": 50,
            "lonmax": 2,
            "lonmin": -2,
            "resolution": "10m",
        },
        "cfp-output-levs-config": {
            "max": 1e-07,
            "min": 5e-08,
            "step": 2.5e-09,
        },
        "plot-mode": 2,
    }

    def test_config_c1_flight_um(self, capsys, tmp_path):
        """TODO c1: TODO describe main reasons for config."""
        c1_flight_um = {
            **self.base_config_constant_vert_levs,
            **{
                # Changes relative to base configuration choice, if any
                "plot-mode": 3,
                # Not relevant to testing: names outputs
                "output-file-name": "um_faam_stanco_1_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-faam-stanco-1",
            },
        }
        run_toolkit_with_config(c1_flight_um, capsys, tmp_path)

    def test_config_c2_flight_um(self, capsys, tmp_path):
        """TODO c2: TODO describe main reasons for config."""
        c2_flight_um = {
            **self.base_config_constant_vert_levs,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2017-07-13 05:00:00",
                "chosen-obs-field": "mole_fraction_of_ozone_in_air",
                "plot-of-input-obs-track-only": 0,
                "show-plot-of-input-obs": False,
                # Not relevant to testing: names outputs
                "output-file-name": "um_faam_stanco_2_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-faam-stanco-2",
            },
        }
        run_toolkit_with_config(c2_flight_um, capsys, tmp_path)

    def test_config_c3_flight_um(self, capsys, tmp_path):
        """TODO c3: TODO describe main reasons for config."""
        c3_flight_um = {
            **self.base_config_constant_vert_levs,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2017-07-17 03:14:15",
                "chosen-obs-field": "mole_fraction_of_ozone_in_air",
                "plot-of-input-obs-track-only": 0,
                "show-plot-of-input-obs": False,
                # Not relevant to testing: names outputs
                "output-file-name": "um_faam_stanco_3_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-faam-stanco-3",
            },
        }
        run_toolkit_with_config(c3_flight_um, capsys, tmp_path)

    def test_config_c4_flight_um(self, capsys, tmp_path):
        """TODO c4: TODO describe main reasons for config."""
        c4_flight_um = {
            **self.base_config_constant_vert_levs,
            **{
                # Changes relative to base configuration choice, if any
                "obs-data-path": f"{self.obs_data_root}core_faam_20170703_c016_STANCO_CF-two-point-1.nc",
                "chosen-obs-field": "mole_fraction_of_ozone_in_air",
                "plot-mode": 3,
                # Not relevant to testing: names outputs
                "output-file-name": "um_faam_stanco_4_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-faam-stanco-4",
            },
        }
        run_toolkit_with_config(c4_flight_um, capsys, tmp_path)

    def test_config_c5_flight_um(self, capsys, tmp_path):
        """TODO c5: TODO describe main reasons for config."""
        c5_flight_um = {
            **self.base_config_constant_vert_levs,
            **{
                # Changes relative to base configuration choice, if any
                "obs-data-path": f"{self.obs_data_root}core_faam_20170703_c016_STANCO_CF-two-point-2.nc",
                "chosen-obs-field": "mole_fraction_of_ozone_in_air",
                "halo-size": 0,
                "plot-of-input-obs-track-only": 2,
                "plot-mode": 3,
                # Not relevant to testing: names outputs
                "output-file-name": "um_faam_stanco_5_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-faam-stanco-5",
            },
        }
        run_toolkit_with_config(c5_flight_um, capsys, tmp_path)


class TestFlightObservationsUMModelHybridHeight:
    """Test toolkit for case of flight path observations and UM model input.

    These cases have hybrid height vertical levels.
    """

    # TODO in these cases, plotting issue from cf-plot apparent bug, so
    # turn all plotting off - see commented out lines.

    # Base configurations, which the specific configurations tend to build on
    # so use these as a base to override with edited values for the final
    # specific configurations
    obs_data_root = "../data/compliant-data/"
    base_config_hybid_height = {
        # Data paths and chosen fields
        "model-data-path": "../data/2025-maria-um-hybrid/*.pp",
        "obs-data-path": (
            f"{obs_data_root}core_faam_20170703_c016_STANCO_CF.nc"
        ),
        "orography": "../data/2025-maria-um-hybrid/orography.pp",
        # cf-plot config.
        "cfp-cscale": "WhiteBlueGreenYellowRed",
        "cfp-mapset-config": {
            "latmax": 54,
            "latmin": 50,
            "lonmax": 2,
            "lonmin": -2,
            "resolution": "10m",
        },
        # NOTE for now need both of these levels (input and output cases)
        # set for any plotting, else hit a cf-plot
        # bug that hasn't been fixed for 3.4.0
        # "cfp-input-levs-config": {
        #     "max": 1e-07,
        #     "min": 5e-08,
        #     "step": 2.5e-09,
        # },
        # "cfp-output-levs-config": {
        #     "max": 9.0e-08,
        #     "min": 4.5e-08,
        #     "step": 0.5e-08,
        # },
        "plot-mode": 0,
        # Other
        "start-time-override": "1998-02-21 11:50:00",
    }

    def test_config_c6_flight_um(self, capsys, tmp_path):
        """TODO c6: TODO describe main reasons for config."""
        c6_flight_um = {
            **self.base_config_hybid_height,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-model-field": "air_temperature",
                "chosen-obs-field": False,
                # Not relevant to testing: names outputs
                "output-file-name": "um_hh_faam_stanco_1_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-hybrid-height-faam-stanco-1",
            },
        }
        run_toolkit_with_config(c6_flight_um, capsys, tmp_path)

    def test_config_c7_flight_um(self, capsys, tmp_path):
        """TODO c7: TODO describe main reasons for config."""
        c7_flight_um = {
            **self.base_config_hybid_height,
            **{
                # Changes relative to base configuration choice, if any
                "model-data-path": "../data/2025-maria-um-hybrid/*[!orography].pp",
                "chosen-model-field": "id%UM_m01s34i104_vn1105",
                "chosen-obs-field": "mole_fraction_of_ozone_in_air",
                # Not relevant to testing: names outputs
                "output-file-name": "um_hh_faam_stanco_2_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-hybrid-height-faam-stanco-2",
            },
        }
        run_toolkit_with_config(c7_flight_um, capsys, tmp_path)

    def test_config_c8_flight_um(self, capsys, tmp_path):
        """TODO c8: TODO describe main reasons for config."""
        c8_flight_um = {
            **self.base_config_hybid_height,
            **{
                # Changes relative to base configuration choice, if any
                "model-data-path": "../data/2025-maria-um-hybrid/*[!orography].pp",
                "chosen-model-field": "id%UM_m01s34i117_vn1105",
                "chosen-obs-field": False,
                # Not relevant to testing: names outputs
                "output-file-name": "um_hh_faam_stanco_3_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-hybrid-height-faam-stanco-3",
            },
        }
        run_toolkit_with_config(c8_flight_um, capsys, tmp_path)


class TestFlightObservationsWRFModel:
    """Test toolkit for case of flight path observations and WRF model input."""

    # Base configuration, which the specific configurations tend to build on
    # so use these as a base to override with edited values for the final
    # specific configurations
    base_config_flight_wrf = {
        "model-data-path": (
            "../pre-processing/wrf-model-data-preprocessing/"
            "wrf-data-from-proc-stages/e2e-ready-wrf-update1.nc"
        ),
        "obs-data-path": "../data/compliant-data/core_faam_20170703_c016_STANCO_CF.nc",
        "preprocess-mode-obs":"wrf",
        "chosen-obs-field": "mole_fraction_of_ozone_in_air",
        "chosen-model-field": "ncvar%T",
        "source-axes": {"X": "ncdim%west_east", "Y": "ncdim%south_north"},
        "vertical-colocation-coord": "atmosphere_hybrid_sigma_pressure_coordinate",
        "plot-mode": 2,
        "cfp-mapset-config": {
            "latmax": 54,
            "latmin": 50,
            "lonmax": 2,
            "lonmin": -2,
            "resolution": "10m",
        },
        "cfp-input-levs-config": {"max": 60, "min": 0, "step": 5},
        "cfp-output-levs-config": {"max": -1, "min": -11, "step": 1},
    }

    def test_config_c1_flight_wrf(self, capsys, tmp_path):
        """TODO c1: TODO describe main reasons for config."""
        c1_flight_wrf = {
            **self.base_config_flight_wrf,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2023-07-10 12:00:00",
                "plot-mode": 0,
                # Not relevant to testing: names outputs
                "output-file-name": "wrf_faam_stanco_1_vision_result.nc",
                "outputs-dir": "toolkit-outputs/wrf-faam-stanco-1",
            },
        }
        run_toolkit_with_config(c1_flight_wrf, capsys, tmp_path)

    def test_config_c2_flight_wrf(self, capsys, tmp_path):
        """TODO c2: TODO describe main reasons for config."""
        c2_flight_wrf = {
            **self.base_config_flight_wrf,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2023-07-11 18:00:00",
                # Not relevant to testing: names outputs
                "output-file-name": "wrf_faam_stanco_2_vision_result.nc",
                "outputs-dir": "toolkit-outputs/wrf-faam-stanco-2",
            },
        }
        run_toolkit_with_config(c2_flight_wrf, capsys, tmp_path)

    def test_config_c3_flight_wrf(self, capsys, tmp_path):
        """TODO c3: TODO describe main reasons for config."""
        c3_flight_wrf = {
            **self.base_config_flight_wrf,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2023-07-11 03:14:15",
                # Not relevant to testing: names outputs
                "output-file-name": "wrf_faam_stanco_3_vision_result.nc",
                "outputs-dir": "toolkit-outputs/wrf-faam-stanco-3",
            },
        }
        run_toolkit_with_config(c3_flight_wrf, capsys, tmp_path)

    def test_config_c4_flight_wrf(self, capsys, tmp_path):
        """TODO c4: TODO describe main reasons for config."""
        c4_flight_wrf = {
            **self.base_config_flight_wrf,
            **{
                # Changes relative to base configuration choice, if any
                "start-time-override": "2023-07-12 03:14:15",
                # Not relevant to testing: names outputs
                "output-file-name": "wrf_faam_stanco_4_vision_result.nc",
                "outputs-dir": "toolkit-outputs/wrf-faam-stanco-4",
            },
        }
        run_toolkit_with_config(c4_flight_wrf, capsys, tmp_path)

    @pytest.mark.skip(
        # TODO
        reason=(
            "points too far apart in cell space, we've agreed this shouldn't "
            "be supported as a case but need to add better error to explain"
        )
    )
    def test_config_c5_flight_wrf(self, capsys, tmp_path):
        """TODO c5: TODO describe main reasons for config."""
        c5_flight_wrf = {
            **self.base_config_flight_wrf,
            **{
                # Changes relative to base configuration choice, if any
                "obs-data-path": "../data/2025-laurents-twopoint-flight/field.nc",
                "chosen-obs-field": "ncvar%tc",
                "start-time-override": "2023-07-10 12:00:00",
                "plot-mode": 0,
                # Not relevant to testing: names outputs
                "output-file-name": "wrf_faam_stanco_5_vision_result.nc",
                "outputs-dir": "toolkit-outputs/wrf-faam-stanco-5",
            },
        }
        run_toolkit_with_config(c5_flight_wrf, capsys, tmp_path)


class TestSatelliteObservationsUMModel:
    """Test toolkit for case of satellite observations and UM model input."""

    # Base configuration, which the specific configurations tend to build on
    # so use these as a base to override with edited values for the final
    # specific configurations
    obs_data_dir = "../data/marias-satellite-example-data/satellite-data/"
    obs_data_dir_for_leap_second = (
        "../data/marias-satellite-example-data/satellite-data-leap-second/"
    )
    obs_data_root = f"{obs_data_dir}ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw"
    obs_data_root_ls = f"{obs_data_dir_for_leap_second}ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw"
    base_config_satellite_um = {
        "model-data-path": "../data/main-workwith-test-ISO-simulator/Model_Input",
        "preprocess-mode-obs": "satellite",
        "chosen-model-field": "id%UM_m01s51i010_vn1105",
        "plot-mode": 3,
    }

    def test_config_c1_satellite_um(self, capsys, tmp_path):
        """TODO c1: TODO describe main reasons for config."""
        c1_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=State vector for atmospheric temperature in "
                "terms of principal component weights.",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_350_399-v1000.nc",
                "start-time-override": "2017-07-17 03:14:15",
                "cfp-cscale": "inferno",
                "plot-mode": 2,
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {
                    "boundinglat": -60,
                    "lon_0": 0,
                    "proj": "spstere",
                    "resolution": "10m",
                },
                "cfp-output-levs-config": {
                    "max": 6.5e-08,
                    "min": 5.5e-08,
                    "step": 5e-10,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_1_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-1",
            },
        }
        run_toolkit_with_config(c1_satellite_um, capsys, tmp_path)

    def test_config_c2_satellite_um(self, capsys, tmp_path):
        """TODO c2: TODO describe main reasons for config."""
        c2_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=State vector for atmospheric temperature in "
                "terms of principal component weights.",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_350_399-v1000.nc",
                "preprocess-mode-obs": "satellite",
                "start-time-override": "2017-07-13 05:00:00",
                "cfp-cscale": "inferno",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {"resolution": "10m"},
                "cfp-output-levs-config": {
                    "max": 6.5e-08,
                    "min": 5.5e-08,
                    "step": 5e-10,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_2_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-2",
            },
        }
        run_toolkit_with_config(c2_satellite_um, capsys, tmp_path)

    def test_config_c3_satellite_um(self, capsys, tmp_path):
        """TODO c3: TODO describe main reasons for config."""
        c3_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=State vector for atmospheric temperature in "
                "terms of principal component weights.",
                "obs-data-path": f"{self.obs_data_root}-20170703013854z_20170703032054z_350_399-v1000.nc",
                "start-time-override": "2017-07-17 03:14:15",
                "cfp-cscale": "inferno",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {
                    "boundinglat": -60,
                    "lon_0": 0,
                    "proj": "spstere",
                    "resolution": "10m",
                },
                "cfp-output-levs-config": {
                    "max": 6.5e-08,
                    "min": 5.5e-08,
                    "step": 5e-10,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_3_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-3",
            },
        }
        run_toolkit_with_config(c3_satellite_um, capsys, tmp_path)

    def test_config_c4_satellite_um(self, capsys, tmp_path):
        """TODO c4: TODO describe main reasons for config."""
        c4_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=State vector for atmospheric temperature in "
                "terms of principal component weights.",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_000_049-v1000.nc",
                "start-time-override": "2017-07-21 06:15:00",
                "cfp-cscale": "plasma",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {"proj": "robin", "resolution": "10m"},
                "cfp-output-levs-config": {
                    "max": 1.2e-07,
                    "min": 5e-08,
                    "step": 5e-09,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_4_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-4",
            },
        }
        run_toolkit_with_config(c4_satellite_um, capsys, tmp_path)

    def test_config_c5_satellite_um(self, capsys, tmp_path):
        """TODO c5: TODO describe main reasons for config."""
        c5_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "air_temperature",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_050_099-v1000.nc",
                "start-time-override": "2017-07-12 10:45:00",
                "cfp-cscale": "plasma",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {"proj": "robin", "resolution": "10m"},
                "cfp-output-levs-config": {
                    "max": 1e-07,
                    "min": 5e-08,
                    "step": 5e-09,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_5_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-5",
            },
        }
        run_toolkit_with_config(c5_satellite_um, capsys, tmp_path)

    def test_config_c6_satellite_um(self, capsys, tmp_path):
        """TODO c6: TODO describe main reasons for config."""
        c6_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=Retrieved emissivity",
                "obs-data-path": f"{self.obs_data_root_ls}-20161231234157z_20170101012357z_100_149-v1000.nc",
                "start-time-override": "2017-07-17 12:00:00",
                "cfp-cscale": "inferno",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {
                    "latmax": 45,
                    "latmin": 10,
                    "lonmax": 165,
                    "lonmin": 125,
                    "resolution": "10m",
                },
                "cfp-output-levs-config": {
                    "max": 6.5e-08,
                    "min": 5.5e-08,
                    "step": 5e-10,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_6_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-6",
            },
        }
        run_toolkit_with_config(c6_satellite_um, capsys, tmp_path)

    def test_config_c7_satellite_um(self, capsys, tmp_path):
        """TODO c7: TODO describe main reasons for config."""
        c7_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=State vector for atmospheric temperature in "
                "terms of principal component weights.",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_350_399-v1000.nc",
                "satellite-plugin-config": {"npres": "npres"},
                "start-time-override": "2017-07-13 05:00:00",
                "cfp-cscale": "inferno",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {
                    "boundinglat": -65,
                    "lon_0": 0,
                    "proj": "spstere",
                    "resolution": "10m",
                },
                "cfp-output-levs-config": {
                    "max": 6.5e-08,
                    "min": 5.5e-08,
                    "step": 5e-10,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_7_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-7",
            },
        }
        run_toolkit_with_config(c7_satellite_um, capsys, tmp_path)

    def test_config_c8_satellite_um(self, capsys, tmp_path):
        """TODO c8: TODO describe main reasons for config."""
        c8_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": "long_name=Land fraction",
                "obs-data-path": f"{self.obs_data_root}-20170703201158z_20170703215054z_*.nc",
                "start-time-override": "2017-07-21 00:00:00",
                "cfp-cscale": "plasma",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {"resolution": "10m"},
                "cfp-output-levs-config": {
                    "max": 1.6e-07,
                    "min": 2e-08,
                    "step": 2e-08,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_8_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-8",
            },
        }
        run_toolkit_with_config(c8_satellite_um, capsys, tmp_path)

    def test_config_c9_satellite_um(self, capsys, tmp_path):
        """TODO c9: TODO describe main reasons for config."""
        c9_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": (
                    "long_name=State vector for atmospheric temperature in "
                    "terms of principal component weights."
                ),
                "obs-data-path": f"{self.obs_data_root}-201707032*",
                "start-time-override": "2017-07-21 00:00:00",
                "plot-mode": 2,
                "cfp-cscale": "plasma",
                "cfp-input-levs-config": {"max": 55, "min": -5, "step": 5},
                "cfp-mapset-config": {"proj": "robin", "resolution": "10m"},
                "cfp-output-levs-config": {
                    "max": 1.6e-07,
                    "min": 2e-08,
                    "step": 2e-08,
                },
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_9_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-9",
            },
        }
        run_toolkit_with_config(c9_satellite_um, capsys, tmp_path)

    def test_config_c10_satellite_um(self, capsys, tmp_path):
        """TODO c10: TODO describe main reasons for config."""
        # Note tests default plot mode as no / skip all plotting
        c10_satellite_um = {
            **self.base_config_satellite_um,
            **{
                # Changes relative to base configuration choice, if any
                "chosen-obs-field": (
                    "long_name=State vector for atmospheric temperature in "
                    "terms of principal component weights."
                ),
                "obs-data-path": f"{self.obs_data_dir}/*",
                "start-time-override": "2017-07-21 00:00:00",
                # Not relevant to testing: names outputs
                "output-file-name": "um_satellite_10_vision_result.nc",
                "outputs-dir": "toolkit-outputs/um-satellite-10",
            },
        }
        run_toolkit_with_config(c10_satellite_um, capsys, tmp_path)


class TestSatelliteObservationsWRFModel:
    """Test toolkit for case of satellite observations and WRF model input."""

    # All testing for this case is still TODO, so add at once as both JSON
    # and converted Python dict here.
    pass


if __name__ == "__main__":
    pytest.main()
