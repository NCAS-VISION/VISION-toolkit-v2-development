"""Test suite for the VISION Toolkit."""

import sys

import pytest
from unittest.mock import patch  # Only using patch, not unittest

import visiontoolkit


@pytest.fixture
def provide_data():
    pass  # TODO


@pytest.fixture
def setup_test():
    pass  # TODO


@pytest.fixture
def teardown_test():
    pass  # TODO


class TestGeneral:
    """Test the VISION Toolkit application in general.

    This includes minimal command-line specification and in
    particular checking for sensible error messages upon lack of
    adequate configuration provision. Testing here covers anything
    general or that which does not run the main co-location code.

    """

    def test_help(self, capsys):
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
            "Networks (VISION) toolkit flight simulator"
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

    def test_verbosity(self, capsys):
        """Test the `$ visiontoolkit -` command."""
        pass  # TODO


class TestFlightObservationsUMModel:
    """Test toolkit for case of flight path observations and UM model input.
    """
    c1_flight_um = {}
    pass


class TestFlightObservationsWRFModel:
    """Test toolkit for case of flight path observations and WRF model input.
    """
    c1_fight_wrf = {}
    pass


class TestSatelliteObservationsUMModel:
    """Test toolkit for case of satellite observations and UM model input.
    """
    # Define configurations to use
    # TODO consolidate these to build up from base one with shared settings
    c1_satellite_um = {
        'cfp-cscale': 'inferno',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'boundinglat': -60,
                              'lon_0': 0,
                              'proj': 'spstere',
                              'resolution': '10m'},
        'cfp-output-levs-config': {'max': 6.5e-08, 'min': 5.5e-08, 'step': 5e-10},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc',
        'output-file-name': 'um_satellite_1_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-1',
        'preprocess-mode-obs': 'satellite',
        'show-plot-of-input-obs': False,
        'skip-all-plotting': False,
        'start-time-override': '2017-07-17 03:14:15'
    }
    c2_satellite_um = {
        'cfp-cscale': 'inferno',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'resolution': '10m'},
        'cfp-output-levs-config': {'max': 6.5e-08, 'min': 5.5e-08, 'step': 5e-10},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc',
        'output-file-name': 'um_satellite_2_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-2',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-13 05:00:00'
    }
    c3_satellite_um = {
        'cfp-cscale': 'inferno',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'boundinglat': -60,
                              'lon_0': 0,
                              'proj': 'spstere',
                              'resolution': '10m'},
        'cfp-output-levs-config': {'max': 6.5e-08, 'min': 5.5e-08, 'step': 5e-10},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703013854z_20170703032054z_350_399-v1000.nc',
        'output-file-name': 'um_satellite_3_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-3',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-17 03:14:15'
    }
    c4_satellite_um = {
        'cfp-cscale': 'plasma',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'proj': 'robin', 'resolution': '10m'},
        'cfp-output-levs-config': {'max': 1.2e-07, 'min': 5e-08, 'step': 5e-09},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_000_049-v1000.nc',
        'output-file-name': 'um_satellite_4_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-4',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-21 06:15:00'
    }
    c5_satellite_um = {
        'cfp-cscale': 'plasma',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'proj': 'robin', 'resolution': '10m'},
        'cfp-output-levs-config': {'max': 1e-07, 'min': 5e-08, 'step': 5e-09},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'air_temperature',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_050_099-v1000.nc',
        'output-file-name': 'um_satellite_5_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-5',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-12 10:45:00'
    }
    c6_satellite_um = {
        'cfp-cscale': 'inferno',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'latmax': 45,
                              'latmin': 10,
                              'lonmax': 165,
                              'lonmin': 125,
                              'resolution': '10m'},
        'cfp-output-levs-config': {'max': 6.5e-08, 'min': 5.5e-08, 'step': 5e-10},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=Retrieved emissivity',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data-leap-second/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20161231234157z_20170101012357z_100_149-v1000.nc',
        'output-file-name': 'um_satellite_6_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-6',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-17 12:00:00'
    }
    c7_satellite_um = {
        'cfp-cscale': 'inferno',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'boundinglat': -65,
                              'lon_0': 0,
                              'proj': 'spstere',
                              'resolution': '10m'},
        'cfp-output-levs-config': {'max': 6.5e-08, 'min': 5.5e-08, 'step': 5e-10},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc',
        'output-file-name': 'um_satellite_7_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-7',
        'preprocess-mode-obs': 'satellite',
        'satellite-plugin-config': {'npres': 'npres'},
        'skip-all-plotting': False,
        'start-time-override': '2017-07-13 05:00:00'
    }
    c8_satellite_um = {
        'cfp-cscale': 'plasma',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'resolution': '10m'},
        'cfp-output-levs-config': {'max': 1.6e-07, 'min': 2e-08, 'step': 2e-08},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=Land fraction',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_*.nc',
        'output-file-name': 'um_satellite_8_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-8',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': False,
        'start-time-override': '2017-07-21 00:00:00'
    }
    c9_satellite_um = {
        'cfp-cscale': 'plasma',
        'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
        'cfp-mapset-config': {'proj': 'robin', 'resolution': '10m'},
        'cfp-output-levs-config': {'max': 1.6e-07, 'min': 2e-08, 'step': 2e-08},
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-201707032*',
        'output-file-name': 'um_satellite_9_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-9',
        'preprocess-mode-obs': 'satellite',
        'show-plot-of-input-obs': False,
        'skip-all-plotting': False,
        'start-time-override': '2017-07-21 00:00:00'
    }
    c10_satellite_um = {
        'chosen-model-field': 'id%UM_m01s51i010_vn1105',
        'chosen-obs-field': 'long_name=State vector for atmospheric temperature in '
        'terms of principal component weights.',
        'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
        'obs-data-path': '../data/marias-satellite-example-data/satellite-data/*',
        'output-file-name': 'um_satellite_10_vision_result.nc',
        'outputs-dir': 'toolkit-outputs/um-satellite-10',
        'preprocess-mode-obs': 'satellite',
        'skip-all-plotting': True,
        'start-time-override': '2017-07-21 00:00:00'
    }
    pass


class TestSatelliteObservationsWRFModel:
    """Test toolkit for case of satellite observations and WRF model input.
    """
    pass


if __name__ == "__main__":
    pytest.main()
