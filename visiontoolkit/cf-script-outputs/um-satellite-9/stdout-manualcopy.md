╭─░▒▓    ~/g/vision-project-resources/visiont/configurations    satellite-case *3 ?23 
╰─ visiontoolkit --config-file="configurations/um-satellite-9.json" -vvv               ─╯

.______________________________________________.
|   _     _  _   ______  _  _______  _______   |
|  (_)   (_)| | / _____)| |(_______)(_______)  |
|   _     _ | |( (____  | | _     _  _     _   |
|  | |   | || | \____ \ | || |   | || |   | |  |
|   \ \ / / | | _____) )| || |___| || |   | |  |
|    \___/  |_|(______/ |_| \_____/ |_|   |_|  |
|   _______             _   _      _           |
|  (_______)           | | | |    (_)   _      |
|      _   ___    ___  | | | |  _  _  _| |_    |
|     | | / _ \  / _ \ | | | |_/ )| |(_   _)   |
|     | || |_| || |_| || | |  _ ( | |  | |_    |
|     |_| \___/  \___/  \_)|_| \_)|_|   \__)   |
.______________________________________________.
    
Parsed CLI configuration arguments are:
Namespace(verbose=3, config_file='configurations/um-satellite-9.json', preprocess_mode_obs=None, preprocess_mode_model=None, start_time_override=None, obs_data_path=None, model_data_path=None, chosen_obs_fields=None, chosen_model_fields=None, skip_all_plotting=False, outputs_dir=None, output_file_name=None, history_message=None, spatial_colocation_method=None, vertical_colocation_coord=None, source_axes=None, plotname_start=None, show_plot_of_input_obs=False, plot_of_input_obs_track_only=False, cfp_cscale=None, cfp_mapset_config=None, cfp_input_levs_config=None, cfp_input_general_config=None, cfp_input_track_only_config=None, cfp_output_levs_config=None, cfp_output_general_config=None, satellite_plugin_config=None, regrid_z_coord=None, regrid_method=None)

Default configuration is:
{'cfp-cscale': 'plasma',
 'cfp-input-general-config': {'legend': True,
                              'linewidth': 0.4,
                              'markersize': 5,
                              'title': 'Input: observational field (path, to '
                                       'be used for co-location, with its '
                                       'corresponding data, to be ignored)'},
 'cfp-input-levs-config': {},
 'cfp-input-track-only-config': {'colorbar': False,
                                 'legend': True,
                                 'linewidth': 0,
                                 'markersize': 0.5,
                                 'title': 'Input: flight track from '
                                          'observational field to co-locate '
                                          'model field onto'},
 'cfp-mapset-config': {},
 'cfp-output-general-config': {'legend': True,
                               'linewidth': 0.4,
                               'markersize': 5,
                               'title': 'Result: model co-located onto '
                                        'observational path'},
 'cfp-output-levs-config': {},
 'chosen-model-fields': False,
 'chosen-obs-fields': False,
 'halo-size': 1,
 'history-message': 'Processed using the NCAS VISION Toolkit to colocate from '
                    'model data to the observational data spatio-temporal '
                    'location.',
 'model-data-path': '.',
 'obs-data-path': '.',
 'output-file-name': 'vision_toolkit_result_field.nc',
 'outputs-dir': '.',
 'plot-of-input-obs-track-only': True,
 'plotname-start': 'vision_toolkit',
 'preprocess-mode-model': None,
 'preprocess-mode-obs': None,
 'show-plot-of-input-obs': True,
 'skip-all-plotting': False,
 'source-axes': False,
 'spatial-colocation-method': 'linear',
 'start-time-override': False,
 'verbose': 0,
 'vertical-colocation-coord': 'air_pressure'}

Traceback (most recent call last):
  File "/home/slb93/miniconda3/envs/cf-env-312/bin/visiontoolkit", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/visiontoolkit.py", line 35, in wrapper
    output = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/visiontoolkit.py", line 1398, in main
    args = process_config()
           ^^^^^^^^^^^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/cli.py", line 380, in process_config
    config_from_file = process_config_file(config_file)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/slb93/git-repos/vision-project-resources/visiontoolkit/cli.py", line 424, in process_config_file
    with open(config_file) as f:
         ^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'configurations/um-satellite-9.json'
╭─░▒▓    ~/g/vision-project-resources/visiont/configurations    satellite-case *3 ?23 
╰─ cd ..                                                                               ─╯
╭─░▒▓    ~/g/vision-project-resources/visiontoolkit    satellite-case *3 ?23 
╰─ visiontoolkit --config-file="configurations/um-satellite-9.json" -vvv               ─╯

.______________________________________________.
|   _     _  _   ______  _  _______  _______   |
|  (_)   (_)| | / _____)| |(_______)(_______)  |
|   _     _ | |( (____  | | _     _  _     _   |
|  | |   | || | \____ \ | || |   | || |   | |  |
|   \ \ / / | | _____) )| || |___| || |   | |  |
|    \___/  |_|(______/ |_| \_____/ |_|   |_|  |
|   _______             _   _      _           |
|  (_______)           | | | |    (_)   _      |
|      _   ___    ___  | | | |  _  _  _| |_    |
|     | | / _ \  / _ \ | | | |_/ )| |(_   _)   |
|     | || |_| || |_| || | |  _ ( | |  | |_    |
|     |_| \___/  \___/  \_)|_| \_)|_|   \__)   |
.______________________________________________.
    
Parsed CLI configuration arguments are:
Namespace(verbose=3, config_file='configurations/um-satellite-9.json', preprocess_mode_obs=None, preprocess_mode_model=None, start_time_override=None, obs_data_path=None, model_data_path=None, chosen_obs_fields=None, chosen_model_fields=None, skip_all_plotting=False, outputs_dir=None, output_file_name=None, history_message=None, spatial_colocation_method=None, vertical_colocation_coord=None, source_axes=None, plotname_start=None, show_plot_of_input_obs=False, plot_of_input_obs_track_only=False, cfp_cscale=None, cfp_mapset_config=None, cfp_input_levs_config=None, cfp_input_general_config=None, cfp_input_track_only_config=None, cfp_output_levs_config=None, cfp_output_general_config=None, satellite_plugin_config=None, regrid_z_coord=None, regrid_method=None)

Default configuration is:
{'cfp-cscale': 'plasma',
 'cfp-input-general-config': {'legend': True,
                              'linewidth': 0.4,
                              'markersize': 5,
                              'title': 'Input: observational field (path, to '
                                       'be used for co-location, with its '
                                       'corresponding data, to be ignored)'},
 'cfp-input-levs-config': {},
 'cfp-input-track-only-config': {'colorbar': False,
                                 'legend': True,
                                 'linewidth': 0,
                                 'markersize': 0.5,
                                 'title': 'Input: flight track from '
                                          'observational field to co-locate '
                                          'model field onto'},
 'cfp-mapset-config': {},
 'cfp-output-general-config': {'legend': True,
                               'linewidth': 0.4,
                               'markersize': 5,
                               'title': 'Result: model co-located onto '
                                        'observational path'},
 'cfp-output-levs-config': {},
 'chosen-model-fields': False,
 'chosen-obs-fields': False,
 'halo-size': 1,
 'history-message': 'Processed using the NCAS VISION Toolkit to colocate from '
                    'model data to the observational data spatio-temporal '
                    'location.',
 'model-data-path': '.',
 'obs-data-path': '.',
 'output-file-name': 'vision_toolkit_result_field.nc',
 'outputs-dir': '.',
 'plot-of-input-obs-track-only': True,
 'plotname-start': 'vision_toolkit',
 'preprocess-mode-model': None,
 'preprocess-mode-obs': None,
 'show-plot-of-input-obs': True,
 'skip-all-plotting': False,
 'source-axes': False,
 'spatial-colocation-method': 'linear',
 'start-time-override': False,
 'verbose': 0,
 'vertical-colocation-coord': 'air_pressure'}

Succesfully read-in JSON config. file at: configurations/um-satellite-9.json
Configuration from file is:
{'cfp-cscale': 'plasma',
 'cfp-input-levs-config': {'max': 55, 'min': -5, 'step': 5},
 'cfp-mapset-config': {'proj': 'robin', 'resolution': '10m'},
 'cfp-output-levs-config': {'max': 1.6e-07, 'min': 2e-08, 'step': 2e-08},
 'chosen-model-fields': -2,
 'chosen-obs-fields': False,
 'model-data-path': '../data/main-workwith-test-ISO-simulator/Model_Input',
 'obs-data-path': '../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-201707032*',
 'output-file-name': 'um_satellite_9_vision_result.nc',
 'outputs-dir': 'cf-script-outputs/um-satellite-9',
 'preprocess-mode-obs': 'satellite',
 'skip-all-plotting': False,
 'start-time-override': '2017-07-21 00:00:00'}

Final input configuration, considering CLI and file inputs (with CLI overriding the file values) is:
Namespace(verbose=3, config_file='configurations/um-satellite-9.json', preprocess_mode_obs='satellite', preprocess_mode_model=None, start_time_override='2017-07-21 00:00:00', obs_data_path='../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-201707032*', model_data_path='../data/main-workwith-test-ISO-simulator/Model_Input', chosen_obs_fields=False, chosen_model_fields=-2, skip_all_plotting=False, outputs_dir='cf-script-outputs/um-satellite-9', output_file_name='um_satellite_9_vision_result.nc', history_message='Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.', spatial_colocation_method='linear', vertical_colocation_coord='air_pressure', source_axes=False, plotname_start='vision_toolkit', show_plot_of_input_obs=True, plot_of_input_obs_track_only=True, cfp_cscale='plasma', cfp_mapset_config={'resolution': '10m', 'proj': 'robin'}, cfp_input_levs_config={'min': -5, 'max': 55, 'step': 5}, cfp_input_general_config={'legend': True, 'markersize': 5, 'linewidth': 0.4, 'title': 'Input: observational field (path, to be used for co-location, with its corresponding data, to be ignored)'}, cfp_input_track_only_config={'legend': True, 'colorbar': False, 'markersize': 0.5, 'linewidth': 0, 'title': 'Input: flight track from observational field to co-locate model field onto'}, cfp_output_levs_config={'min': 2e-08, 'max': 1.6e-07, 'step': 2e-08}, cfp_output_general_config={'legend': True, 'markersize': 5, 'linewidth': 0.4, 'title': 'Result: model co-located onto observational path'}, satellite_plugin_config=None, regrid_z_coord=None, regrid_method=None, halo_size=1)

Found file name from glob: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_750_799-v1000.nc

_____ Time taken (in s) for 'get_files_to_individually_colocate' to run: 5.8228 _____

Read file list has length: 47

_____ Start of colocation iteration with file number 1 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_750_799-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1379 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.7573 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(4560)) K
Auxiliary coords: latitude(ncdim%npres(4560)) = [72.25733947753906, ..., 74.6573257446289] degree_north
                : longitude(ncdim%npres(4560)) = [-139.09249877929688, ..., 120.14857482910156] degree_east
                : time(ncdim%npres(4560)) = [2017-07-04 01:12:54, ..., 2017-07-04 01:17:56]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4632 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4633 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 8.7243 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(4560) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:05:02]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1187 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2852 _____

Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6916 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1806 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 4560

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(4560)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(4560)) = [72.25733947753906, ..., 74.6573257446289] degree_north
                : longitude(ncdim%npres(4560)) = [-139.09249877929688, ..., 120.14857482910156] degree_east
                : time(ncdim%npres(4560)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:02]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(4560)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(4560)) = [72.25733947753906, ..., 74.6573257446289] degree_north
                : longitude(ncdim%npres(4560)) = [-139.09249877929688, ..., 120.14857482910156] degree_east
                : time(ncdim%npres(4560)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:02]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 4560): [[5.892879096811857e-08, ..., 1.4293488020311155e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(4560)) 1
Auxiliary coords: latitude(ncdim%npres(4560)) = [72.25733947753906, ..., 74.6573257446289] degree_north
                : longitude(ncdim%npres(4560)) = [-139.09249877929688, ..., 120.14857482910156] degree_east
                : time(ncdim%npres(4560)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:02]

The final result field has data statistics of:

{'maximum': 1.0178290122635623e-07,
 'mean': 6.95406086922826e-08,
 'median': 6.741093267263625e-08,
 'mid_range': 7.839052197667256e-08,
 'minimum': 5.499814272698889e-08,
 'range': 4.678475849936734e-08,
 'root_mean_square': 7.018509202238268e-08,
 'sample_size': 4560,
 'standard_deviation': 9.489514471096779e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2999 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_750_799-v1000.nc

_____ Start of colocation iteration with file number 2 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_100_149-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1183 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5313 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [38.912376403808594, ..., 20.1785831451416] degree_north
                : longitude(ncdim%npres(6000)) = [-170.03509521484375, ..., 163.07650756835938] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:04:14, ..., 2017-07-03 22:10:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4827 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4828 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3163 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1086 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2194 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7807 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1599 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [38.912376403808594, ..., 20.1785831451416] degree_north
                : longitude(ncdim%npres(6000)) = [-170.03509521484375, ..., 163.07650756835938] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [38.912376403808594, ..., 20.1785831451416] degree_north
                : longitude(ncdim%npres(6000)) = [-170.03509521484375, ..., 163.07650756835938] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[6.127818644187892e-08, ..., 2.5244605896895456e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [38.912376403808594, ..., 20.1785831451416] degree_north
                : longitude(ncdim%npres(6000)) = [-170.03509521484375, ..., 163.07650756835938] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.227557351314553e-08,
 'mean': 6.36405301130096e-08,
 'median': 6.257331099483421e-08,
 'mid_range': 6.773742090279774e-08,
 'minimum': 5.319926829244995e-08,
 'range': 2.9076305220695582e-08,
 'root_mean_square': 6.394340847193153e-08,
 'sample_size': 6000,
 'standard_deviation': 6.216302272525354e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2666 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_100_149-v1000.nc

_____ Start of colocation iteration with file number 3 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_250_299-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1195 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5859 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-38.8714485168457, ..., -55.99214553833008] degree_north
                : longitude(ncdim%npres(6000)) = [-164.52804565429688, ..., 158.3148193359375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:45:18, ..., 2017-07-03 20:51:56]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4984 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4984 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3055 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1195 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2076 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7461 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1891 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-38.8714485168457, ..., -55.99214553833008] degree_north
                : longitude(ncdim%npres(6000)) = [-164.52804565429688, ..., 158.3148193359375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-38.8714485168457, ..., -55.99214553833008] degree_north
                : longitude(ncdim%npres(6000)) = [-164.52804565429688, ..., 158.3148193359375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.769598996286158e-08, ..., 1.3004967738672385e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-38.8714485168457, ..., -55.99214553833008] degree_north
                : longitude(ncdim%npres(6000)) = [-164.52804565429688, ..., 158.3148193359375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.900258697308401e-08,
 'mean': 6.060928808167699e-08,
 'median': 5.870779510160866e-08,
 'mid_range': 6.704724760948633e-08,
 'minimum': 5.5091908245888654e-08,
 'range': 2.391067872719536e-08,
 'root_mean_square': 6.081911769456416e-08,
 'sample_size': 6000,
 'standard_deviation': 5.047700008670725e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2178 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_250_299-v1000.nc

_____ Start of colocation iteration with file number 4 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_000_049-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1231 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.584 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.18312072753906, ..., 64.40560913085938] degree_north
                : longitude(ncdim%npres(6000)) = [-129.86781311035156, ..., 144.50819396972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:32:54, ..., 2017-07-03 23:39:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4862 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4862 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3581 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1148 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2376 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.759 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1742 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.18312072753906, ..., 64.40560913085938] degree_north
                : longitude(ncdim%npres(6000)) = [-129.86781311035156, ..., 144.50819396972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.18312072753906, ..., 64.40560913085938] degree_north
                : longitude(ncdim%npres(6000)) = [-129.86781311035156, ..., 144.50819396972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.696505653464524e-08, ..., 1.6104416476494192e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.18312072753906, ..., 64.40560913085938] degree_north
                : longitude(ncdim%npres(6000)) = [-129.86781311035156, ..., 144.50819396972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.1482824732312389e-07,
 'mean': 7.7216360398164e-08,
 'median': 7.428098891150302e-08,
 'mid_range': 8.49320525602674e-08,
 'minimum': 5.5035857797410906e-08,
 'range': 5.979238952571298e-08,
 'root_mean_square': 7.846520265423902e-08,
 'sample_size': 6000,
 'standard_deviation': 1.3943518724900475e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2541 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_000_049-v1000.nc

_____ Start of colocation iteration with file number 5 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_500_549-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1216 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5706 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-25.879701614379883, ..., 1.220100998878479] degree_north
                : longitude(ncdim%npres(6000)) = [-3.3370931148529053, ..., 9.663345336914062] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:18:38, ..., 2017-07-03 21:25:16]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4914 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4915 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2008 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1137 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2258 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6946 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1128 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-25.879701614379883, ..., 1.220100998878479] degree_north
                : longitude(ncdim%npres(6000)) = [-3.3370931148529053, ..., 9.663345336914062] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-25.879701614379883, ..., 1.220100998878479] degree_north
                : longitude(ncdim%npres(6000)) = [-3.3370931148529053, ..., 9.663345336914062] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[6.219072689377505e-08, ..., 2.999162775196408e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-25.879701614379883, ..., 1.220100998878479] degree_north
                : longitude(ncdim%npres(6000)) = [-3.3370931148529053, ..., 9.663345336914062] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.8994141461721066e-07,
 'mean': 8.293029226113996e-08,
 'median': 7.35841281823247e-08,
 'mid_range': 1.2296460045095295e-07,
 'minimum': 5.5987786284695234e-08,
 'range': 1.3395362833251542e-07,
 'root_mean_square': 8.74897994767891e-08,
 'sample_size': 6000,
 'standard_deviation': 2.7875287226693706e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2414 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_500_549-v1000.nc

_____ Start of colocation iteration with file number 6 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_700_749-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.2981 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.4589 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [56.76377487182617, ..., 85.5788803100586] degree_north
                : longitude(ncdim%npres(6000)) = [-60.164161682128906, ..., -25.483671188354492] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:24:14, ..., 2017-07-03 23:30:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5419 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.542 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2692 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1272 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0012 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2137 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6715 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1206 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [56.76377487182617, ..., 85.5788803100586] degree_north
                : longitude(ncdim%npres(6000)) = [-60.164161682128906, ..., -25.483671188354492] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [56.76377487182617, ..., 85.5788803100586] degree_north
                : longitude(ncdim%npres(6000)) = [-60.164161682128906, ..., -25.483671188354492] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[2.6330071141225186e-08, ..., 1.4387264910224282e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [56.76377487182617, ..., 85.5788803100586] degree_north
                : longitude(ncdim%npres(6000)) = [-60.164161682128906, ..., -25.483671188354492] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.2000370648654527e-07,
 'mean': 7.562390001165611e-08,
 'median': 7.111640456523408e-08,
 'mid_range': 8.659239902279152e-08,
 'minimum': 5.318109155903778e-08,
 'range': 6.682261492750749e-08,
 'root_mean_square': 7.672580888418172e-08,
 'sample_size': 6000,
 'standard_deviation': 1.2956677658991763e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1199 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_700_749-v1000.nc

_____ Start of colocation iteration with file number 7 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_000_049-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1291 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6737 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [70.2000732421875, ..., 58.221038818359375] degree_north
                : longitude(ncdim%npres(6000)) = [-98.28284454345703, ..., -165.58937072753906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:11:58, ..., 2017-07-03 20:18:36]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4778 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4778 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2287 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1114 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2192 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6682 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1087 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [70.2000732421875, ..., 58.221038818359375] degree_north
                : longitude(ncdim%npres(6000)) = [-98.28284454345703, ..., -165.58937072753906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [70.2000732421875, ..., 58.221038818359375] degree_north
                : longitude(ncdim%npres(6000)) = [-98.28284454345703, ..., -165.58937072753906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.0156028405509094e-08, ..., 1.482241278505548e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [70.2000732421875, ..., 58.221038818359375] degree_north
                : longitude(ncdim%npres(6000)) = [-98.28284454345703, ..., -165.58937072753906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.1434357265089642e-07,
 'mean': 8.245478860534829e-08,
 'median': 8.007435281949024e-08,
 'mid_range': 8.622176516531609e-08,
 'minimum': 5.809995767973576e-08,
 'range': 5.624361497116066e-08,
 'root_mean_square': 8.343441549523808e-08,
 'sample_size': 6000,
 'standard_deviation': 1.274792238285704e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1732 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_000_049-v1000.nc

_____ Start of colocation iteration with file number 8 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_400_449-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1332 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.493 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-80.44025421142578, ..., -52.14552307128906] degree_north
                : longitude(ncdim%npres(6000)) = [-22.938282012939453, ..., 6.639440059661865] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:44:14, ..., 2017-07-03 22:50:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4716 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4716 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2144 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1112 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0011 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2153 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6809 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1146 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-80.44025421142578, ..., -52.14552307128906] degree_north
                : longitude(ncdim%npres(6000)) = [-22.938282012939453, ..., 6.639440059661865] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-80.44025421142578, ..., -52.14552307128906] degree_north
                : longitude(ncdim%npres(6000)) = [-22.938282012939453, ..., 6.639440059661865] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 2.2617254564429078e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-80.44025421142578, ..., -52.14552307128906] degree_north
                : longitude(ncdim%npres(6000)) = [-22.938282012939453, ..., 6.639440059661865] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.214528739801456e-08,
 'mean': 5.9307007187488376e-08,
 'median': 5.9298057196885345e-08,
 'mid_range': 5.9499926772064403e-08,
 'minimum': 5.6854566146114245e-08,
 'range': 5.290721251900317e-09,
 'root_mean_square': 5.93153503905834e-08,
 'sample_size': 6000,
 'standard_deviation': 9.948318555838475e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2338 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_400_449-v1000.nc

_____ Start of colocation iteration with file number 9 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_150_199-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1355 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.7127 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [16.101226806640625, ..., -3.117630958557129] degree_north
                : longitude(ncdim%npres(6000)) = [-178.69688415527344, ..., 158.25538635253906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:10:54, ..., 2017-07-03 22:17:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4987 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4987 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3338 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1035 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2254 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.8827 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1596 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [16.101226806640625, ..., -3.117630958557129] degree_north
                : longitude(ncdim%npres(6000)) = [-178.69688415527344, ..., 158.25538635253906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [16.101226806640625, ..., -3.117630958557129] degree_north
                : longitude(ncdim%npres(6000)) = [-178.69688415527344, ..., 158.25538635253906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.4225687695725746e-08, ..., 4.479795601744815e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [16.101226806640625, ..., -3.117630958557129] degree_north
                : longitude(ncdim%npres(6000)) = [-178.69688415527344, ..., 158.25538635253906] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.40411098018912e-08,
 'mean': 5.656718163091382e-08,
 'median': 5.674024130146791e-08,
 'mid_range': 5.759438522572952e-08,
 'minimum': 5.114766064956785e-08,
 'range': 1.2893449152323347e-08,
 'root_mean_square': 5.664456750973382e-08,
 'sample_size': 6000,
 'standard_deviation': 2.9598970759130754e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.4281 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_150_199-v1000.nc

_____ Start of colocation iteration with file number 10 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_000_049-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1335 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5657 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.38213348388672, ..., 66.63133239746094] degree_north
                : longitude(ncdim%npres(6000)) = [-96.92585754394531, ..., 170.10670471191406] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:50:54, ..., 2017-07-03 21:57:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5242 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5242 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3556 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1116 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.223 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9295 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1685 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.38213348388672, ..., 66.63133239746094] degree_north
                : longitude(ncdim%npres(6000)) = [-96.92585754394531, ..., 170.10670471191406] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.38213348388672, ..., 66.63133239746094] degree_north
                : longitude(ncdim%npres(6000)) = [-96.92585754394531, ..., 170.10670471191406] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.6545631030562103e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [72.38213348388672, ..., 66.63133239746094] degree_north
                : longitude(ncdim%npres(6000)) = [-96.92585754394531, ..., 170.10670471191406] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.1232315652747503e-07,
 'mean': 7.723071566768657e-08,
 'median': 7.4048417083636e-08,
 'mid_range': 8.519183969670454e-08,
 'minimum': 5.8060522865934044e-08,
 'range': 5.4262633661540983e-08,
 'root_mean_square': 7.842424311740774e-08,
 'sample_size': 6000,
 'standard_deviation': 1.3630057446512288e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2663 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_000_049-v1000.nc

_____ Start of colocation iteration with file number 11 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_200_249-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1346 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5626 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-15.6161527633667, ..., -34.411888122558594] degree_north
                : longitude(ncdim%npres(6000)) = [-160.61048889160156, ..., 173.57003784179688] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:38:38, ..., 2017-07-03 20:45:16]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5117 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5118 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3241 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1223 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2192 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7791 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1624 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-15.6161527633667, ..., -34.411888122558594] degree_north
                : longitude(ncdim%npres(6000)) = [-160.61048889160156, ..., 173.57003784179688] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-15.6161527633667, ..., -34.411888122558594] degree_north
                : longitude(ncdim%npres(6000)) = [-160.61048889160156, ..., 173.57003784179688] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.3859397372679624e-08, ..., 1.9168102616842383e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-15.6161527633667, ..., -34.411888122558594] degree_north
                : longitude(ncdim%npres(6000)) = [-160.61048889160156, ..., 173.57003784179688] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.239370559764006e-08,
 'mean': 5.970310820110239e-08,
 'median': 5.868733560827711e-08,
 'mid_range': 6.689006584600299e-08,
 'minimum': 5.138642609436591e-08,
 'range': 3.1007279503274155e-08,
 'root_mean_square': 6.006613919934254e-08,
 'sample_size': 6000,
 'standard_deviation': 6.593932775078654e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2496 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_200_249-v1000.nc

_____ Start of colocation iteration with file number 12 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_650_699-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.145 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5842 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [37.286678314208984, ..., 64.73428344726562] degree_north
                : longitude(ncdim%npres(6000)) = [-70.94972229003906, ..., -51.64992141723633] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:59:34, ..., 2017-07-04 01:06:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5259 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5259 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2882 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1439 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2724 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7369 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1181 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [37.286678314208984, ..., 64.73428344726562] degree_north
                : longitude(ncdim%npres(6000)) = [-70.94972229003906, ..., -51.64992141723633] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [37.286678314208984, ..., 64.73428344726562] degree_north
                : longitude(ncdim%npres(6000)) = [-70.94972229003906, ..., -51.64992141723633] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[7.848906362651274e-08, ..., 1.3297881855993258e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [37.286678314208984, ..., 64.73428344726562] degree_north
                : longitude(ncdim%npres(6000)) = [-70.94972229003906, ..., -51.64992141723633] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.1195670055897998e-07,
 'mean': 7.782567208442266e-08,
 'median': 7.649847830674912e-08,
 'mid_range': 8.273487877405943e-08,
 'minimum': 5.351305698913887e-08,
 'range': 5.8443643569841103e-08,
 'root_mean_square': 7.869704856901971e-08,
 'sample_size': 6000,
 'standard_deviation': 1.1678622268168524e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2034 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_650_699-v1000.nc

_____ Start of colocation iteration with file number 13 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_550_599-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1335 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6293 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-8.816637992858887, ..., 18.283443450927734] degree_north
                : longitude(ncdim%npres(6000)) = [-57.163978576660156, ..., -44.49198913574219] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:46:14, ..., 2017-07-04 00:52:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5275 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5275 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2088 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1129 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2356 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7505 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1176 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-8.816637992858887, ..., 18.283443450927734] degree_north
                : longitude(ncdim%npres(6000)) = [-57.163978576660156, ..., -44.49198913574219] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-8.816637992858887, ..., 18.283443450927734] degree_north
                : longitude(ncdim%npres(6000)) = [-57.163978576660156, ..., -44.49198913574219] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 3.86630114218396e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-8.816637992858887, ..., 18.283443450927734] degree_north
                : longitude(ncdim%npres(6000)) = [-57.163978576660156, ..., -44.49198913574219] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.744823131658038e-08,
 'mean': 6.873125560779703e-08,
 'median': 6.898690356976685e-08,
 'mid_range': 7.167946488439675e-08,
 'minimum': 5.591069845221313e-08,
 'range': 3.1537532864367255e-08,
 'root_mean_square': 6.893944134800471e-08,
 'sample_size': 6000,
 'standard_deviation': 5.3536040151145715e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2106 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_550_599-v1000.nc

_____ Start of colocation iteration with file number 14 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_150_199-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1314 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.553 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [13.872132301330566, ..., -5.35856294631958] degree_north
                : longitude(ncdim%npres(6000)) = [155.33441162109375, ..., 132.37576293945312] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:52:54, ..., 2017-07-03 23:59:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5423 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5423 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2193 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1068 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.4519 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7081 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1201 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [13.872132301330566, ..., -5.35856294631958] degree_north
                : longitude(ncdim%npres(6000)) = [155.33441162109375, ..., 132.37576293945312] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [13.872132301330566, ..., -5.35856294631958] degree_north
                : longitude(ncdim%npres(6000)) = [155.33441162109375, ..., 132.37576293945312] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.440969739654095e-08, ..., 2.481509734167973e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [13.872132301330566, ..., -5.35856294631958] degree_north
                : longitude(ncdim%npres(6000)) = [155.33441162109375, ..., 132.37576293945312] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.03356296345125e-08,
 'mean': 5.475627654999056e-08,
 'median': 5.461821611159361e-08,
 'mid_range': 5.5857906132636604e-08,
 'minimum': 5.138018263076071e-08,
 'range': 8.955447003751784e-09,
 'root_mean_square': 5.478870831971483e-08,
 'sample_size': 6000,
 'standard_deviation': 1.884870744571522e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1958 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_150_199-v1000.nc

_____ Start of colocation iteration with file number 15 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.127 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.5615 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-84.9181137084961, ..., -64.42240142822266] degree_north
                : longitude(ncdim%npres(6000)) = [-165.8921356201172, ..., 49.57024002075195] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:58:38, ..., 2017-07-03 21:05:16]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4948 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4948 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2415 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1259 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2204 _____

Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7603 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1595 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-84.9181137084961, ..., -64.42240142822266] degree_north
                : longitude(ncdim%npres(6000)) = [-165.8921356201172, ..., 49.57024002075195] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-84.9181137084961, ..., -64.42240142822266] degree_north
                : longitude(ncdim%npres(6000)) = [-165.8921356201172, ..., 49.57024002075195] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.6101411358239507e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-84.9181137084961, ..., -64.42240142822266] degree_north
                : longitude(ncdim%npres(6000)) = [-165.8921356201172, ..., 49.57024002075195] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.063088040089106e-08,
 'mean': 5.8307160203725015e-08,
 'median': 5.8268446522821504e-08,
 'mid_range': 5.892337268541214e-08,
 'minimum': 5.721586496993323e-08,
 'range': 3.415015430957826e-09,
 'root_mean_square': 5.831147681791156e-08,
 'sample_size': 6000,
 'standard_deviation': 7.095052240706408e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2996 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc

_____ Start of colocation iteration with file number 16 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_300_349-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1301 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6027 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-61.97477722167969, ..., -71.37745666503906] degree_north
                : longitude(ncdim%npres(6000)) = [-167.63230895996094, ..., 114.1983642578125] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:51:58, ..., 2017-07-03 20:58:36]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5613 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5613 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3079 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1272 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.247 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7987 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.165 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-61.97477722167969, ..., -71.37745666503906] degree_north
                : longitude(ncdim%npres(6000)) = [-167.63230895996094, ..., 114.1983642578125] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-61.97477722167969, ..., -71.37745666503906] degree_north
                : longitude(ncdim%npres(6000)) = [-167.63230895996094, ..., 114.1983642578125] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.5317342828203038e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-61.97477722167969, ..., -71.37745666503906] degree_north
                : longitude(ncdim%npres(6000)) = [-167.63230895996094, ..., 114.1983642578125] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.246257094753359e-08,
 'mean': 5.8903347977036235e-08,
 'median': 5.8720556109881115e-08,
 'mid_range': 5.976375671419035e-08,
 'minimum': 5.706494248084711e-08,
 'range': 5.397628466686481e-09,
 'root_mean_square': 5.8910080737196374e-08,
 'sample_size': 6000,
 'standard_deviation': 8.906231297115389e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2887 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_300_349-v1000.nc

_____ Start of colocation iteration with file number 17 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_100_149-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1355 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6239 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [30.707611083984375, ..., 11.695836067199707] degree_north
                : longitude(ncdim%npres(6000)) = [-148.41339111328125, ..., -173.19769287109375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:25:18, ..., 2017-07-03 20:31:56]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4857 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4857 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.215 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1164 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0015 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2429 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.675 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1306 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [30.707611083984375, ..., 11.695836067199707] degree_north
                : longitude(ncdim%npres(6000)) = [-148.41339111328125, ..., -173.19769287109375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [30.707611083984375, ..., 11.695836067199707] degree_north
                : longitude(ncdim%npres(6000)) = [-148.41339111328125, ..., -173.19769287109375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[6.253910289881578e-08, ..., 5.273239134772398e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [30.707611083984375, ..., 11.695836067199707] degree_north
                : longitude(ncdim%npres(6000)) = [-148.41339111328125, ..., -173.19769287109375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.644548148679343e-08,
 'mean': 5.73374219741582e-08,
 'median': 5.651037063719364e-08,
 'mid_range': 6.446205739570766e-08,
 'minimum': 5.2478633304621895e-08,
 'range': 2.396684818217153e-08,
 'root_mean_square': 5.748005769045158e-08,
 'sample_size': 6000,
 'standard_deviation': 4.0468597029009014e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1296 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_100_149-v1000.nc

_____ Start of colocation iteration with file number 18 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_400_449-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.147 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6159 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.23518371582031, ..., -50.12211227416992] degree_north
                : longitude(ncdim%npres(6000)) = [-47.98834228515625, ..., -20.469276428222656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:26:14, ..., 2017-07-04 00:32:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5274 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5274 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2268 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1272 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2338 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7829 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.124 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.23518371582031, ..., -50.12211227416992] degree_north
                : longitude(ncdim%npres(6000)) = [-47.98834228515625, ..., -20.469276428222656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.23518371582031, ..., -50.12211227416992] degree_north
                : longitude(ncdim%npres(6000)) = [-47.98834228515625, ..., -20.469276428222656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[4.771321994306838e-08, ..., 2.0494876553700888e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.23518371582031, ..., -50.12211227416992] degree_north
                : longitude(ncdim%npres(6000)) = [-47.98834228515625, ..., -20.469276428222656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.167382406157208e-08,
 'mean': 5.907536103995304e-08,
 'median': 5.927325549441316e-08,
 'mid_range': 5.913568340016591e-08,
 'minimum': 5.659754273875974e-08,
 'range': 5.0762813228123416e-09,
 'root_mean_square': 5.908259998366351e-08,
 'sample_size': 6000,
 'standard_deviation': 9.248452999252472e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2305 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_400_449-v1000.nc

_____ Start of colocation iteration with file number 19 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_250_299-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1394 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6575 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-30.430103302001953, ..., -48.417823791503906] degree_north
                : longitude(ncdim%npres(6000)) = [171.46310424804688, ..., 140.05967712402344] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:24:14, ..., 2017-07-03 22:30:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5095 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5095 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2194 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1222 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2706 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.704 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1355 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-30.430103302001953, ..., -48.417823791503906] degree_north
                : longitude(ncdim%npres(6000)) = [171.46310424804688, ..., 140.05967712402344] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-30.430103302001953, ..., -48.417823791503906] degree_north
                : longitude(ncdim%npres(6000)) = [171.46310424804688, ..., 140.05967712402344] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.8448827030083795e-08, ..., 1.505883994650545e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-30.430103302001953, ..., -48.417823791503906] degree_north
                : longitude(ncdim%npres(6000)) = [171.46310424804688, ..., 140.05967712402344] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.903356900717228e-08,
 'mean': 6.111161361682719e-08,
 'median': 5.984804072373e-08,
 'mid_range': 6.580808678026491e-08,
 'minimum': 5.258260455335753e-08,
 'range': 2.6450964453814754e-08,
 'root_mean_square': 6.128491537061067e-08,
 'sample_size': 6000,
 'standard_deviation': 4.6055980209450685e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2025 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_250_299-v1000.nc

_____ Start of colocation iteration with file number 20 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_550_599-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1348 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6542 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-2.5868430137634277, ..., 24.517383575439453] degree_north
                : longitude(ncdim%npres(6000)) = [-7.780371189117432, ..., 5.0582661628723145] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:25:18, ..., 2017-07-03 21:31:56]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5164 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5164 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2045 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1086 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2229 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7612 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1026 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-2.5868430137634277, ..., 24.517383575439453] degree_north
                : longitude(ncdim%npres(6000)) = [-7.780371189117432, ..., 5.0582661628723145] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-2.5868430137634277, ..., 24.517383575439453] degree_north
                : longitude(ncdim%npres(6000)) = [-7.780371189117432, ..., 5.0582661628723145] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[9.4601248017648e-08, ..., 4.6633532096935194e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-2.5868430137634277, ..., 24.517383575439453] degree_north
                : longitude(ncdim%npres(6000)) = [-7.780371189117432, ..., 5.0582661628723145] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.8014948205814999e-07,
 'mean': 8.918714028389354e-08,
 'median': 8.835453781578332e-08,
 'mid_range': 1.1748748940494396e-07,
 'minimum': 5.4825496751737944e-08,
 'range': 1.2532398530641204e-07,
 'root_mean_square': 9.308127973621674e-08,
 'sample_size': 6000,
 'standard_deviation': 2.6641671218467666e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.3008 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_550_599-v1000.nc

_____ Start of colocation iteration with file number 21 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_100_149-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1336 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6724 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [36.75355911254883, ..., 17.92775535583496] degree_north
                : longitude(ncdim%npres(6000)) = [163.55218505859375, ..., 137.3218231201172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:46:14, ..., 2017-07-03 23:52:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5336 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5336 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2393 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1324 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2412 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7944 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1256 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [36.75355911254883, ..., 17.92775535583496] degree_north
                : longitude(ncdim%npres(6000)) = [163.55218505859375, ..., 137.3218231201172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [36.75355911254883, ..., 17.92775535583496] degree_north
                : longitude(ncdim%npres(6000)) = [163.55218505859375, ..., 137.3218231201172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.315752078602467e-08, ..., 3.220133214586457e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [36.75355911254883, ..., 17.92775535583496] degree_north
                : longitude(ncdim%npres(6000)) = [163.55218505859375, ..., 137.3218231201172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.730705459892127e-08,
 'mean': 6.2294437364195e-08,
 'median': 5.7959902885284663e-08,
 'mid_range': 7.380677270485128e-08,
 'minimum': 5.03064908107813e-08,
 'range': 4.700056378813997e-08,
 'root_mean_square': 6.31532159837182e-08,
 'sample_size': 6000,
 'standard_deviation': 1.037939124248361e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2343 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_100_149-v1000.nc

_____ Start of colocation iteration with file number 22 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_450_499-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.134 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.6909 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-49.07011413574219, ..., -21.90143585205078] degree_north
                : longitude(ncdim%npres(6000)) = [0.23472200334072113, ..., 15.874102592468262] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:11:58, ..., 2017-07-03 21:18:36]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5004 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5005 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.1972 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1258 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2191 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.805 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1297 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-49.07011413574219, ..., -21.90143585205078] degree_north
                : longitude(ncdim%npres(6000)) = [0.23472200334072113, ..., 15.874102592468262] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-49.07011413574219, ..., -21.90143585205078] degree_north
                : longitude(ncdim%npres(6000)) = [0.23472200334072113, ..., 15.874102592468262] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.879045446130872e-08, ..., 3.857172127483246e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-49.07011413574219, ..., -21.90143585205078] degree_north
                : longitude(ncdim%npres(6000)) = [0.23472200334072113, ..., 15.874102592468262] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.211853537113156e-08,
 'mean': 6.621399509125193e-08,
 'median': 6.656758344436705e-08,
 'mid_range': 7.36917001600458e-08,
 'minimum': 5.526486494896003e-08,
 'range': 3.685367042217153e-08,
 'root_mean_square': 6.68828462208023e-08,
 'sample_size': 6000,
 'standard_deviation': 9.435145608370591e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.3505 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_450_499-v1000.nc

_____ Start of colocation iteration with file number 23 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_050_099-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1488 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.9294 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [60.09725570678711, ..., 43.46177291870117] degree_north
                : longitude(ncdim%npres(6000)) = [-151.82008361816406, ..., 166.9567108154297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:57:34, ..., 2017-07-03 22:04:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7299 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.73 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.5121 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1792 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0015 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.348 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0264 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.2322 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [60.09725570678711, ..., 43.46177291870117] degree_north
                : longitude(ncdim%npres(6000)) = [-151.82008361816406, ..., 166.9567108154297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [60.09725570678711, ..., 43.46177291870117] degree_north
                : longitude(ncdim%npres(6000)) = [-151.82008361816406, ..., 166.9567108154297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 2.2460577175811736e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [60.09725570678711, ..., 43.46177291870117] degree_north
                : longitude(ncdim%npres(6000)) = [-151.82008361816406, ..., 166.9567108154297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.230600647806064e-07,
 'mean': 8.277894345088516e-08,
 'median': 8.177359168445812e-08,
 'mid_range': 8.809588420514834e-08,
 'minimum': 5.313170362969026e-08,
 'range': 6.992836115091615e-08,
 'root_mean_square': 8.456551124309617e-08,
 'sample_size': 6000,
 'standard_deviation': 1.7290812964154696e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.8325 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_050_099-v1000.nc

_____ Start of colocation iteration with file number 24 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_750_799-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1963 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.4313 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(1800)) K
Auxiliary coords: latitude(ncdim%npres(1800)) = [71.84090423583984, ..., 87.46150207519531] degree_north
                : longitude(ncdim%npres(1800)) = [-106.36113739013672, ..., 140.45420837402344] degree_east
                : time(ncdim%npres(1800)) = [2017-07-03 23:30:54, ..., 2017-07-03 23:32:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7302 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7303 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.4054 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(1800) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:01:58]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.2112 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0015 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3427 _____

Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.055 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1349 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 1800

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(1800)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(1800)) = [71.84090423583984, ..., 87.46150207519531] degree_north
                : longitude(ncdim%npres(1800)) = [-106.36113739013672, ..., 140.45420837402344] degree_east
                : time(ncdim%npres(1800)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:01:58]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(1800)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(1800)) = [71.84090423583984, ..., 87.46150207519531] degree_north
                : longitude(ncdim%npres(1800)) = [-106.36113739013672, ..., 140.45420837402344] degree_east
                : time(ncdim%npres(1800)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:01:58]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 1800): [[0.0, ..., 1.4139272967058068e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(1800)) 1
Auxiliary coords: latitude(ncdim%npres(1800)) = [71.84090423583984, ..., 87.46150207519531] degree_north
                : longitude(ncdim%npres(1800)) = [-106.36113739013672, ..., 140.45420837402344] degree_east
                : time(ncdim%npres(1800)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:01:58]

The final result field has data statistics of:

{'maximum': 9.735075177484693e-08,
 'mean': 7.531498700065713e-08,
 'median': 7.233000660856605e-08,
 'mid_range': 7.889682646451403e-08,
 'minimum': 6.044290115418114e-08,
 'range': 3.690785062066579e-08,
 'root_mean_square': 7.602696530295289e-08,
 'sample_size': 1800,
 'standard_deviation': 1.0380375054267085e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.7349 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_750_799-v1000.nc

_____ Start of colocation iteration with file number 25 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_600_649-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1937 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.3635 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [14.431976318359375, ..., 41.56182861328125] degree_north
                : longitude(ncdim%npres(6000)) = [-62.62815475463867, ..., -48.427913665771484] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:52:54, ..., 2017-07-04 00:59:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.688 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.688 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3227 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1534 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0017 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.333 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9254 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1802 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [14.431976318359375, ..., 41.56182861328125] degree_north
                : longitude(ncdim%npres(6000)) = [-62.62815475463867, ..., -48.427913665771484] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [14.431976318359375, ..., 41.56182861328125] degree_north
                : longitude(ncdim%npres(6000)) = [-62.62815475463867, ..., -48.427913665771484] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[6.490270136538549e-08, ..., 1.7614749380473474e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [14.431976318359375, ..., 41.56182861328125] degree_north
                : longitude(ncdim%npres(6000)) = [-62.62815475463867, ..., -48.427913665771484] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.25100103774558e-08,
 'mean': 5.603903459548297e-08,
 'median': 5.43998786710295e-08,
 'mid_range': 6.220413863761062e-08,
 'minimum': 5.1898266897765434e-08,
 'range': 2.061174347969037e-08,
 'root_mean_square': 5.618663339135211e-08,
 'sample_size': 6000,
 'standard_deviation': 4.069935314039492e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.7066 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_600_649-v1000.nc

_____ Start of colocation iteration with file number 26 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_650_699-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.217 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.4589 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [35.12025451660156, ..., 62.50778579711914] degree_north
                : longitude(ncdim%npres(6000)) = [-44.58864212036133, ..., -26.046480178833008] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:17:34, ..., 2017-07-03 23:24:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.6586 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.6587 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.311 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1777 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0015 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3423 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.8961 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.2253 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [35.12025451660156, ..., 62.50778579711914] degree_north
                : longitude(ncdim%npres(6000)) = [-44.58864212036133, ..., -26.046480178833008] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [35.12025451660156, ..., 62.50778579711914] degree_north
                : longitude(ncdim%npres(6000)) = [-44.58864212036133, ..., -26.046480178833008] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.329437621326368e-08, ..., 1.5176692873125333e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [35.12025451660156, ..., 62.50778579711914] degree_north
                : longitude(ncdim%npres(6000)) = [-44.58864212036133, ..., -26.046480178833008] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.634729209130414e-08,
 'mean': 7.027169351656918e-08,
 'median': 6.926244706457703e-08,
 'mid_range': 7.447607792759409e-08,
 'minimum': 5.2604863763884044e-08,
 'range': 4.3742428327420096e-08,
 'root_mean_square': 7.103479211121388e-08,
 'sample_size': 6000,
 'standard_deviation': 1.0384160081428977e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6574 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_650_699-v1000.nc

_____ Start of colocation iteration with file number 27 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_600_649-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1929 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.0802 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [12.201823234558105, ..., 39.32752990722656] degree_north
                : longitude(ncdim%npres(6000)) = [-36.675350189208984, ..., -22.745515823364258] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:10:54, ..., 2017-07-03 23:17:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.8358 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.8358 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3377 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1632 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0016 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3124 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0097 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1776 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [12.201823234558105, ..., 39.32752990722656] degree_north
                : longitude(ncdim%npres(6000)) = [-36.675350189208984, ..., -22.745515823364258] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [12.201823234558105, ..., 39.32752990722656] degree_north
                : longitude(ncdim%npres(6000)) = [-36.675350189208984, ..., -22.745515823364258] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[6.036046328855005e-08, ..., 1.770823096982479e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [12.201823234558105, ..., 39.32752990722656] degree_north
                : longitude(ncdim%npres(6000)) = [-36.675350189208984, ..., -22.745515823364258] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.979872375910496e-08,
 'mean': 6.316034778082159e-08,
 'median': 6.12104439568376e-08,
 'mid_range': 6.650122275022618e-08,
 'minimum': 5.3203721741347394e-08,
 'range': 2.6595002017757564e-08,
 'root_mean_square': 6.34397141987811e-08,
 'sample_size': 6000,
 'standard_deviation': 5.947083808783168e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6125 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_600_649-v1000.nc

_____ Start of colocation iteration with file number 28 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_500_549-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1836 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.3576 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-34.33134078979492, ..., -7.225325107574463] degree_north
                : longitude(ncdim%npres(6000)) = [-27.291372299194336, ..., -13.67333984375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:57:34, ..., 2017-07-03 23:04:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7001 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7001 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3208 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1516 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0015 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3317 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9995 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1554 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-34.33134078979492, ..., -7.225325107574463] degree_north
                : longitude(ncdim%npres(6000)) = [-27.291372299194336, ..., -13.67333984375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-34.33134078979492, ..., -7.225325107574463] degree_north
                : longitude(ncdim%npres(6000)) = [-27.291372299194336, ..., -13.67333984375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.6677811366124025e-08, ..., 3.866707195611432e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-34.33134078979492, ..., -7.225325107574463] degree_north
                : longitude(ncdim%npres(6000)) = [-27.291372299194336, ..., -13.67333984375] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.429337760005499e-08,
 'mean': 6.949485483511971e-08,
 'median': 7.036406885158749e-08,
 'mid_range': 7.482713900204666e-08,
 'minimum': 5.536090040403834e-08,
 'range': 3.893247719601665e-08,
 'root_mean_square': 7.003828760040945e-08,
 'sample_size': 6000,
 'standard_deviation': 8.70786319617536e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6584 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_500_549-v1000.nc

_____ Start of colocation iteration with file number 29 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_450_499-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.197 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.3937 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.240726470947266, ..., -28.00251007080078] degree_north
                : longitude(ncdim%npres(6000)) = [-49.63764572143555, ..., -32.64811325073242] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:32:54, ..., 2017-07-04 00:39:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.6867 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.6868 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3012 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.154 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0016 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3316 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9611 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1586 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.240726470947266, ..., -28.00251007080078] degree_north
                : longitude(ncdim%npres(6000)) = [-49.63764572143555, ..., -32.64811325073242] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.240726470947266, ..., -28.00251007080078] degree_north
                : longitude(ncdim%npres(6000)) = [-49.63764572143555, ..., -32.64811325073242] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.788502897339115e-08, ..., 2.957845095667811e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.240726470947266, ..., -28.00251007080078] degree_north
                : longitude(ncdim%npres(6000)) = [-49.63764572143555, ..., -32.64811325073242] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.106189815569425e-08,
 'mean': 5.65997774044664e-08,
 'median': 5.6777524162272733e-08,
 'mid_range': 5.708383317016724e-08,
 'minimum': 5.310576818464023e-08,
 'range': 7.956129971054016e-09,
 'root_mean_square': 5.6617221177193606e-08,
 'sample_size': 6000,
 'standard_deviation': 1.4053225936114836e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6325 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_450_499-v1000.nc

_____ Start of colocation iteration with file number 30 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_200_249-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.184 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.2595 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-9.386215209960938, ..., -28.371044158935547] degree_north
                : longitude(ncdim%npres(6000)) = [149.91012573242188, ..., 125.40457916259766] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:59:34, ..., 2017-07-04 00:06:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5325 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5326 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2257 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1329 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2323 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6748 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1076 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-9.386215209960938, ..., -28.371044158935547] degree_north
                : longitude(ncdim%npres(6000)) = [149.91012573242188, ..., 125.40457916259766] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-9.386215209960938, ..., -28.371044158935547] degree_north
                : longitude(ncdim%npres(6000)) = [149.91012573242188, ..., 125.40457916259766] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[2.4298869713833723e-08, ..., 3.5266321252996604e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-9.386215209960938, ..., -28.371044158935547] degree_north
                : longitude(ncdim%npres(6000)) = [149.91012573242188, ..., 125.40457916259766] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 7.987780031445694e-08,
 'mean': 6.160696137880381e-08,
 'median': 6.055658016419126e-08,
 'mid_range': 6.498972154833269e-08,
 'minimum': 5.010164278220843e-08,
 'range': 2.9776157532248513e-08,
 'root_mean_square': 6.211991470494469e-08,
 'sample_size': 6000,
 'standard_deviation': 7.966562158182126e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1512 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_200_249-v1000.nc

_____ Start of colocation iteration with file number 31 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_550_599-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.135 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.3229 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-11.059074401855469, ..., 16.039691925048828] degree_north
                : longitude(ncdim%npres(6000)) = [-31.377643585205078, ..., -18.72844886779785] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:04:14, ..., 2017-07-03 23:10:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5262 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5262 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2375 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1293 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2376 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6572 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1466 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-11.059074401855469, ..., 16.039691925048828] degree_north
                : longitude(ncdim%npres(6000)) = [-31.377643585205078, ..., -18.72844886779785] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-11.059074401855469, ..., 16.039691925048828] degree_north
                : longitude(ncdim%npres(6000)) = [-31.377643585205078, ..., -18.72844886779785] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.988833355126922e-08, ..., 3.319502759334317e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-11.059074401855469, ..., 16.039691925048828] degree_north
                : longitude(ncdim%npres(6000)) = [-31.377643585205078, ..., -18.72844886779785] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.0298404261385988e-07,
 'mean': 8.441722169753187e-08,
 'median': 8.596708674503391e-08,
 'mid_range': 8.052906523077919e-08,
 'minimum': 5.8074087847698496e-08,
 'range': 4.490995476616138e-08,
 'root_mean_square': 8.497109023910703e-08,
 'sample_size': 6000,
 'standard_deviation': 9.686013488129368e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2492 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_550_599-v1000.nc

_____ Start of colocation iteration with file number 32 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_300_349-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1386 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.7676 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.81584930419922, ..., -68.70222473144531] degree_north
                : longitude(ncdim%npres(6000)) = [142.42311096191406, ..., 80.64900207519531] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:12:54, ..., 2017-07-04 00:19:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5192 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5192 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2029 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1336 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2427 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6983 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1134 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.81584930419922, ..., -68.70222473144531] degree_north
                : longitude(ncdim%npres(6000)) = [142.42311096191406, ..., 80.64900207519531] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.81584930419922, ..., -68.70222473144531] degree_north
                : longitude(ncdim%npres(6000)) = [142.42311096191406, ..., 80.64900207519531] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.888892925523195e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-55.81584930419922, ..., -68.70222473144531] degree_north
                : longitude(ncdim%npres(6000)) = [142.42311096191406, ..., 80.64900207519531] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.520015342975148e-08,
 'mean': 5.863550470740746e-08,
 'median': 5.853984568520953e-08,
 'mid_range': 6.074331085317967e-08,
 'minimum': 5.628646827660784e-08,
 'range': 8.913685153143641e-09,
 'root_mean_square': 5.864279888853115e-08,
 'sample_size': 6000,
 'standard_deviation': 9.249049617706738e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1758 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_300_349-v1000.nc

_____ Start of colocation iteration with file number 33 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_500_549-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1334 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.8307 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.09333419799805, ..., -4.991189956665039] degree_north
                : longitude(ncdim%npres(6000)) = [-52.989681243896484, ..., -39.56920623779297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:39:34, ..., 2017-07-04 00:46:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5042 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5042 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2033 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.12 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2285 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.6763 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1062 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.09333419799805, ..., -4.991189956665039] degree_north
                : longitude(ncdim%npres(6000)) = [-52.989681243896484, ..., -39.56920623779297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.09333419799805, ..., -4.991189956665039] degree_north
                : longitude(ncdim%npres(6000)) = [-52.989681243896484, ..., -39.56920623779297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[7.136271528850622e-08, ..., 3.8968912001357994e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.09333419799805, ..., -4.991189956665039] degree_north
                : longitude(ncdim%npres(6000)) = [-52.989681243896484, ..., -39.56920623779297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.070720867221622e-08,
 'mean': 6.266191844606657e-08,
 'median': 5.67249477570235e-08,
 'mid_range': 6.585328542936047e-08,
 'minimum': 5.0999362186504726e-08,
 'range': 2.9707846485711497e-08,
 'root_mean_square': 6.32899571013739e-08,
 'sample_size': 6000,
 'standard_deviation': 8.89396686255642e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1895 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_500_549-v1000.nc

_____ Start of colocation iteration with file number 34 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_400_449-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1345 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.3309 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-72.1034927368164, ..., -44.370853424072266] degree_north
                : longitude(ncdim%npres(6000)) = [2.72760009765625, ..., 26.026796340942383] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:05:18, ..., 2017-07-03 21:11:56]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.512 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5121 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.1998 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1238 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2733 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.1931 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1423 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-72.1034927368164, ..., -44.370853424072266] degree_north
                : longitude(ncdim%npres(6000)) = [2.72760009765625, ..., 26.026796340942383] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-72.1034927368164, ..., -44.370853424072266] degree_north
                : longitude(ncdim%npres(6000)) = [2.72760009765625, ..., 26.026796340942383] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 2.033541788730244e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-72.1034927368164, ..., -44.370853424072266] degree_north
                : longitude(ncdim%npres(6000)) = [2.72760009765625, ..., 26.026796340942383] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.368420288073195e-08,
 'mean': 5.9351963036286156e-08,
 'median': 5.9304784985305204e-08,
 'mid_range': 5.990797260288344e-08,
 'minimum': 5.613174232503494e-08,
 'range': 7.552460555697012e-09,
 'root_mean_square': 5.93644153690726e-08,
 'sample_size': 6000,
 'standard_deviation': 1.2158519034427117e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2985 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_400_449-v1000.nc

_____ Start of colocation iteration with file number 35 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_050_099-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1435 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.3624 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.218753814697266, ..., 41.222015380859375] degree_north
                : longitude(ncdim%npres(6000)) = [-179.8167266845703, ..., 141.27391052246094] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 23:39:34, ..., 2017-07-03 23:46:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5204 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5205 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3523 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1295 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0017 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2278 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7958 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1577 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.218753814697266, ..., 41.222015380859375] degree_north
                : longitude(ncdim%npres(6000)) = [-179.8167266845703, ..., 141.27391052246094] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.218753814697266, ..., 41.222015380859375] degree_north
                : longitude(ncdim%npres(6000)) = [-179.8167266845703, ..., 141.27391052246094] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[9.020776332920032e-08, ..., 2.7585863645598036e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.218753814697266, ..., 41.222015380859375] degree_north
                : longitude(ncdim%npres(6000)) = [-179.8167266845703, ..., 141.27391052246094] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.5168333876186831e-07,
 'mean': 8.915261782453842e-08,
 'median': 8.622282549809568e-08,
 'mid_range': 1.0289815163410165e-07,
 'minimum': 5.411296450633499e-08,
 'range': 9.757037425553332e-08,
 'root_mean_square': 9.128383667284414e-08,
 'sample_size': 6000,
 'standard_deviation': 1.960993556201245e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.3278 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_050_099-v1000.nc

_____ Start of colocation iteration with file number 36 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_700_749-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1446 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.7983 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.68095016479492, ..., 87.7805404663086] degree_north
                : longitude(ncdim%npres(6000)) = [-87.94585418701172, ..., -46.36087417602539] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 01:06:14, ..., 2017-07-04 01:12:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5152 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5153 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2477 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.105 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.001 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2417 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.659 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1371 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.68095016479492, ..., 87.7805404663086] degree_north
                : longitude(ncdim%npres(6000)) = [-87.94585418701172, ..., -46.36087417602539] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.68095016479492, ..., 87.7805404663086] degree_north
                : longitude(ncdim%npres(6000)) = [-87.94585418701172, ..., -46.36087417602539] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.027190639505601e-08, ..., 1.4132289474291063e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [58.68095016479492, ..., 87.7805404663086] degree_north
                : longitude(ncdim%npres(6000)) = [-87.94585418701172, ..., -46.36087417602539] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 1.2045876970225407e-07,
 'mean': 7.967667687194012e-08,
 'median': 7.876993261647323e-08,
 'mid_range': 8.672286143713406e-08,
 'minimum': 5.298695317201405e-08,
 'range': 6.747181653024001e-08,
 'root_mean_square': 8.070673619855116e-08,
 'sample_size': 6000,
 'standard_deviation': 1.2853187560561396e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.1282 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_700_749-v1000.nc

_____ Start of colocation iteration with file number 37 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_450_499-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1354 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.8669 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-57.464630126953125, ..., -30.18920135498047] degree_north
                : longitude(ncdim%npres(6000)) = [-24.008747100830078, ..., -6.455443859100342] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:50:54, ..., 2017-07-03 22:57:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5552 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5553 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2026 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.118 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0012 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2497 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7024 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1143 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-57.464630126953125, ..., -30.18920135498047] degree_north
                : longitude(ncdim%npres(6000)) = [-24.008747100830078, ..., -6.455443859100342] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-57.464630126953125, ..., -30.18920135498047] degree_north
                : longitude(ncdim%npres(6000)) = [-24.008747100830078, ..., -6.455443859100342] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 3.4498854157250346e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-57.464630126953125, ..., -30.18920135498047] degree_north
                : longitude(ncdim%npres(6000)) = [-24.008747100830078, ..., -6.455443859100342] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.805955128339833e-08,
 'mean': 5.712422194183792e-08,
 'median': 5.691491563768558e-08,
 'mid_range': 6.175467385665919e-08,
 'minimum': 5.5449796429920054e-08,
 'range': 1.2609754853478272e-08,
 'root_mean_square': 5.713771657176465e-08,
 'sample_size': 6000,
 'standard_deviation': 1.241741750507002e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.3638 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_450_499-v1000.nc

_____ Start of colocation iteration with file number 38 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_350_399-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.142 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.3359 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.80592346191406, ..., -68.4852066040039] degree_north
                : longitude(ncdim%npres(6000)) = [140.90611267089844, ..., 11.343539237976074] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:19:34, ..., 2017-07-04 00:26:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.5153 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.5153 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2504 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1075 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2416 _____

Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.2667 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1721 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.80592346191406, ..., -68.4852066040039] degree_north
                : longitude(ncdim%npres(6000)) = [140.90611267089844, ..., 11.343539237976074] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.80592346191406, ..., -68.4852066040039] degree_north
                : longitude(ncdim%npres(6000)) = [140.90611267089844, ..., 11.343539237976074] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.3366755533617057e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-78.80592346191406, ..., -68.4852066040039] degree_north
                : longitude(ncdim%npres(6000)) = [140.90611267089844, ..., 11.343539237976074] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.064958923945817e-08,
 'mean': 5.845268871083069e-08,
 'median': 5.840152484118461e-08,
 'mid_range': 5.893446951927159e-08,
 'minimum': 5.721934979908501e-08,
 'range': 3.4302394403731556e-09,
 'root_mean_square': 5.845731912661016e-08,
 'sample_size': 6000,
 'standard_deviation': 7.357594342359572e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.2786 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_350_399-v1000.nc

_____ Start of colocation iteration with file number 39 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_600_649-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1353 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 1.3413 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [20.60399627685547, ..., 47.770606994628906] degree_north
                : longitude(ncdim%npres(6000)) = [-13.781310081481934, ..., 1.3079309463500977] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:31:58, ..., 2017-07-03 21:38:36]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.4995 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.4995 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2224 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1329 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0009 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.2217 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.7628 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1429 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [20.60399627685547, ..., 47.770606994628906] degree_north
                : longitude(ncdim%npres(6000)) = [-13.781310081481934, ..., 1.3079309463500977] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [20.60399627685547, ..., 47.770606994628906] degree_north
                : longitude(ncdim%npres(6000)) = [-13.781310081481934, ..., 1.3079309463500977] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.4506366005247262e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [20.60399627685547, ..., 47.770606994628906] degree_north
                : longitude(ncdim%npres(6000)) = [-13.781310081481934, ..., 1.3079309463500977] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.978165342396613e-08,
 'mean': 6.466863192227881e-08,
 'median': 6.160954375651955e-08,
 'mid_range': 7.195224473105669e-08,
 'minimum': 5.412283603814724e-08,
 'range': 3.565881738581889e-08,
 'root_mean_square': 6.510967630338167e-08,
 'sample_size': 6000,
 'standard_deviation': 7.565579530476227e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.3449 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_600_649-v1000.nc

_____ Start of colocation iteration with file number 40 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_250_299-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1249 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.445 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.6698112487793, ..., -50.466548919677734] degree_north
                : longitude(ncdim%npres(6000)) = [145.7615203857422, ..., 113.07560729980469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-04 00:06:14, ..., 2017-07-04 00:12:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7227 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7227 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3196 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1763 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3505 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0185 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1565 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.6698112487793, ..., -50.466548919677734] degree_north
                : longitude(ncdim%npres(6000)) = [145.7615203857422, ..., 113.07560729980469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.6698112487793, ..., -50.466548919677734] degree_north
                : longitude(ncdim%npres(6000)) = [145.7615203857422, ..., 113.07560729980469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[4.4466212914875374e-08, ..., 1.2401599621560399e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-32.6698112487793, ..., -50.466548919677734] degree_north
                : longitude(ncdim%npres(6000)) = [145.7615203857422, ..., 113.07560729980469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.61816178220815e-08,
 'mean': 6.457795985437485e-08,
 'median': 5.942859192223874e-08,
 'mid_range': 6.990862431389946e-08,
 'minimum': 5.3635630805717425e-08,
 'range': 3.254598701636407e-08,
 'root_mean_square': 6.522968489543114e-08,
 'sample_size': 6000,
 'standard_deviation': 9.197765631064264e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.5956 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703233254z_20170704011758z_250_299-v1000.nc

_____ Start of colocation iteration with file number 41 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_350_399-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1882 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.0309 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-76.59542846679688, ..., -69.6657485961914] degree_north
                : longitude(ncdim%npres(6000)) = [166.09689331054688, ..., 42.236366271972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:37:34, ..., 2017-07-03 22:44:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7288 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7289 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3642 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1583 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3455 _____

Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0838 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.2154 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-76.59542846679688, ..., -69.6657485961914] degree_north
                : longitude(ncdim%npres(6000)) = [166.09689331054688, ..., 42.236366271972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-76.59542846679688, ..., -69.6657485961914] degree_north
                : longitude(ncdim%npres(6000)) = [166.09689331054688, ..., 42.236366271972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[0.0, ..., 1.3584075769608562e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-76.59542846679688, ..., -69.6657485961914] degree_north
                : longitude(ncdim%npres(6000)) = [166.09689331054688, ..., 42.236366271972656] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.107046983346479e-08,
 'mean': 5.834868693737884e-08,
 'median': 5.829752544561345e-08,
 'mid_range': 5.90954081096504e-08,
 'minimum': 5.7120346385836004e-08,
 'range': 3.950123447628784e-09,
 'root_mean_square': 5.8353242777973296e-08,
 'sample_size': 6000,
 'standard_deviation': 7.291607428060222e-10}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 2.2624 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_350_399-v1000.nc

_____ Start of colocation iteration with file number 42 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_650_699-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1981 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.0933 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [43.23649597167969, ..., 70.91064453125] degree_north
                : longitude(ncdim%npres(6000)) = [-23.489736557006836, ..., -1.6323620080947876] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 21:38:38, ..., 2017-07-03 21:45:16]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7348 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7348 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3371 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1726 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3486 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0542 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.153 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [43.23649597167969, ..., 70.91064453125] degree_north
                : longitude(ncdim%npres(6000)) = [-23.489736557006836, ..., -1.6323620080947876] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [43.23649597167969, ..., 70.91064453125] degree_north
                : longitude(ncdim%npres(6000)) = [-23.489736557006836, ..., -1.6323620080947876] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[9.384959253587547e-08, ..., 1.4744838363128162e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [43.23649597167969, ..., 70.91064453125] degree_north
                : longitude(ncdim%npres(6000)) = [-23.489736557006836, ..., -1.6323620080947876] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.116660104683303e-08,
 'mean': 7.378125643553588e-08,
 'median': 7.361039191165976e-08,
 'mid_range': 7.467777282518251e-08,
 'minimum': 5.8188944603532006e-08,
 'range': 3.297765644330102e-08,
 'root_mean_square': 7.402504604231565e-08,
 'sample_size': 6000,
 'standard_deviation': 6.002802708789028e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.7046 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_650_699-v1000.nc

_____ Start of colocation iteration with file number 43 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_300_349-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1995 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.6603 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-53.59278869628906, ..., -67.37742614746094] degree_north
                : longitude(ncdim%npres(6000)) = [168.04571533203125, ..., 111.05509948730469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:30:54, ..., 2017-07-03 22:37:32]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7148 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7148 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.2841 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1661 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.33 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9332 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1597 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-53.59278869628906, ..., -67.37742614746094] degree_north
                : longitude(ncdim%npres(6000)) = [168.04571533203125, ..., 111.05509948730469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-53.59278869628906, ..., -67.37742614746094] degree_north
                : longitude(ncdim%npres(6000)) = [168.04571533203125, ..., 111.05509948730469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[3.595777169145134e-08, ..., 1.7460728622102064e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-53.59278869628906, ..., -67.37742614746094] degree_north
                : longitude(ncdim%npres(6000)) = [168.04571533203125, ..., 111.05509948730469] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.955371655997247e-08,
 'mean': 5.8829830627597704e-08,
 'median': 5.866013560033619e-08,
 'mid_range': 6.322063914020388e-08,
 'minimum': 5.6887561720435286e-08,
 'range': 1.266615483953718e-08,
 'root_mean_square': 5.88413486219457e-08,
 'sample_size': 6000,
 'standard_deviation': 1.1641889784390352e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.5667 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_300_349-v1000.nc

_____ Start of colocation iteration with file number 44 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_200_249-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1871 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.0169 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [-7.141152858734131, ..., -26.17736053466797] degree_north
                : longitude(ncdim%npres(6000)) = [175.70501708984375, ..., 151.5620574951172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 22:17:34, ..., 2017-07-03 22:24:12]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.705 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.705 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3255 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.147 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0014 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.4045 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0504 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1433 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-7.141152858734131, ..., -26.17736053466797] degree_north
                : longitude(ncdim%npres(6000)) = [175.70501708984375, ..., 151.5620574951172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [-7.141152858734131, ..., -26.17736053466797] degree_north
                : longitude(ncdim%npres(6000)) = [175.70501708984375, ..., 151.5620574951172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.318142380784202e-08, ..., 3.432661717942742e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [-7.141152858734131, ..., -26.17736053466797] degree_north
                : longitude(ncdim%npres(6000)) = [175.70501708984375, ..., 151.5620574951172] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 6.806763799152084e-08,
 'mean': 5.8160495167439496e-08,
 'median': 5.6879931695056335e-08,
 'mid_range': 5.9604200774322666e-08,
 'minimum': 5.1140763557124494e-08,
 'range': 1.6926874434396343e-08,
 'root_mean_square': 5.846826617201458e-08,
 'sample_size': 6000,
 'standard_deviation': 5.991239524488429e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6785 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703215054z_20170703233254z_200_249-v1000.nc

_____ Start of colocation iteration with file number 45 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_700_749-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1884 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.6139 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(5040)) K
Auxiliary coords: latitude(ncdim%npres(5040)) = [63.69267272949219, ..., 89.53279876708984] degree_north
                : longitude(ncdim%npres(5040)) = [-45.68848419189453, ..., 122.72491455078125] degree_east
                : time(ncdim%npres(5040)) = [2017-07-03 21:45:18, ..., 2017-07-03 21:50:52]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.765 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7651 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3909 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(5040) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:05:34]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1809 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.002 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.4119 _____

Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Halo reduced to keep subspace within axis limits
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.1618 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1769 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 5040

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(5040)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(5040)) = [63.69267272949219, ..., 89.53279876708984] degree_north
                : longitude(ncdim%npres(5040)) = [-45.68848419189453, ..., 122.72491455078125] degree_east
                : time(ncdim%npres(5040)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:34]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(5040)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(5040)) = [63.69267272949219, ..., 89.53279876708984] degree_north
                : longitude(ncdim%npres(5040)) = [-45.68848419189453, ..., 122.72491455078125] degree_east
                : time(ncdim%npres(5040)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:34]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 5040): [[0.0, ..., --]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(5040)) 1
Auxiliary coords: latitude(ncdim%npres(5040)) = [63.69267272949219, ..., 89.53279876708984] degree_north
                : longitude(ncdim%npres(5040)) = [-45.68848419189453, ..., 122.72491455078125] degree_east
                : time(ncdim%npres(5040)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:05:34]

The final result field has data statistics of:

{'maximum': 1.196347565830073e-07,
 'mean': 7.704603662601549e-08,
 'median': 7.251148044493921e-08,
 'mid_range': 8.64147670496119e-08,
 'minimum': 5.3194777516216473e-08,
 'range': 6.643997906679083e-08,
 'root_mean_square': 7.825958386724114e-08,
 'sample_size': 5032,
 'standard_deviation': 1.372846339895445e-08}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 2.3931 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_700_749-v1000.nc

_____ Start of colocation iteration with file number 46 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_050_099-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.2238 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 2.4488 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [52.759822845458984, ..., 35.00285339355469] degree_north
                : longitude(ncdim%npres(6000)) = [-135.17489624023438, ..., -169.03524780273438] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:18:38, ..., 2017-07-03 20:25:16]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.7648 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.7649 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.3231 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.1649 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0013 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.3021 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 0.9971 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1921 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [52.759822845458984, ..., 35.00285339355469] degree_north
                : longitude(ncdim%npres(6000)) = [-135.17489624023438, ..., -169.03524780273438] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [52.759822845458984, ..., 35.00285339355469] degree_north
                : longitude(ncdim%npres(6000)) = [-135.17489624023438, ..., -169.03524780273438] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.858132802300655e-08, ..., 1.6150585848956235e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [52.759822845458984, ..., 35.00285339355469] degree_north
                : longitude(ncdim%npres(6000)) = [-135.17489624023438, ..., -169.03524780273438] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 9.622931058982183e-08,
 'mean': 6.716525303193244e-08,
 'median': 6.799972570143363e-08,
 'mid_range': 7.297311507860598e-08,
 'minimum': 4.9716919567390133e-08,
 'range': 4.65123910224317e-08,
 'root_mean_square': 6.770708625583094e-08,
 'sample_size': 6000,
 'standard_deviation': 8.548585521068472e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.5922 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_050_099-v1000.nc

_____ Start of colocation iteration with file number 47 of total 47: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_150_199-v1000.nc _____


_____ Time taken (in s) for 'read_obs_input_data' to run: 0.1719 _____


_____ Time taken (in s) for 'read_model_input_data' to run: 3.3561 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'get_input_fields_of_interest' to run: 0.0 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final pre-processed field from satellite plugin is Field: air_temperature (ncvar%t)
--------------------------------
Data            : air_temperature(ncdim%npres(6000)) K
Auxiliary coords: latitude(ncdim%npres(6000)) = [7.672985076904297, ..., -11.548052787780762] degree_north
                : longitude(ncdim%npres(6000)) = [-155.6153564453125, ..., -178.5377655029297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-03 20:31:58, ..., 2017-07-03 20:38:36]

_____ Time taken (in s) for 'satellite_plugin' to run: 0.8662 _____


_____ Time taken (in s) for 'ensure_cf_compliance' to run: 0.8663 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels

_____ Time taken (in s) for 'make_preview_plots' to run: 0.4575 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Applied override to observational times, now have: time(6000) day since 2000-01-01 , with data of: [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'set_start_datetime' to run: 0.2579 _____


_____ Time taken (in s) for 'ensure_unit_calendar_consistency' to run: 0.0035 _____


_____ Time taken (in s) for 'check_time_coverage' to run: 0.4604 _____

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'subspace_to_spatiotemporal_bounding_box' to run: 1.0893 _____

Doing spatial regridding without using vertical levels.
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

_____ Time taken (in s) for 'spatial_interpolation' to run: 0.1531 _____

Starting time interpolation step.
Using split segments.

Number of model time data points: 3
Number of observational time sample data points: 6000

Observational (aux) coord. time key is: auxiliarycoordinate2
Model (dim) time key is: dimensioncoordinate0

*** Begin iteration over pairwise 'segments'. ***
Segments to loop over are, pairwise: [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)
 cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)]

*** Segment 0 ***

Datetime endpoints for this segment are: 2017-07-20 23:00:00, 2017-07-21 00:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [7.672985076904297, ..., -11.548052787780762] degree_north
                : longitude(ncdim%npres(6000)) = [-155.6153564453125, ..., -178.5377655029297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 20, 23, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [0]}


*** Segment 1 ***

Datetime endpoints for this segment are: 2017-07-21 00:00:00, 2017-07-31 01:00:00.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Querying with query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False))) on field:
Field: id%UM_m01s51i010_vn1105 (ncvar%UM_m01s51i010_vn1105)
-----------------------------------------------------------
Data            : id%UM_m01s51i010_vn1105(time(3), air_pressure(19), ncdim%npres(6000)) 1
Cell methods    : time(3): point
Dimension coords: time(3) = [2017-07-20 23:00:00, 2017-07-21 00:00:00, 2017-07-31 01:00:00]
                : air_pressure(19) = [1000.0, ..., 100.0] hPa
Auxiliary coords: latitude(ncdim%npres(6000)) = [7.672985076904297, ..., -11.548052787780762] degree_north
                : longitude(ncdim%npres(6000)) = [-155.6153564453125, ..., -178.5377655029297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]


Using subspace arguments for i=0 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [1]}

Using subspace arguments for i=1 of: {'auxiliarycoordinate2': <CF Query: (wi [cftime.DatetimeGregorian(2017, 7, 21, 0, 0, 0, 0, has_year_zero=False), cftime.DatetimeGregorian(2017, 7, 31, 1, 0, 0, 0, has_year_zero=False)))>, 'dimensioncoordinate0': [2]}

Final per-segment weighted value arrays are:
[<CF Data(19, 6000): [[5.8245453093477225e-08, ..., 5.080873678026486e-08]] 1>]

New history message reads: Converted from UM/PP by cf-python v3.17.0 ~ Processed using the NCAS VISION Toolkit to colocate from model data to the observational data spatio-temporal location.

/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)

Final result field is:

Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(ncdim%npres(6000)) 1
Auxiliary coords: latitude(ncdim%npres(6000)) = [7.672985076904297, ..., -11.548052787780762] degree_north
                : longitude(ncdim%npres(6000)) = [-155.6153564453125, ..., -178.5377655029297] degree_east
                : time(ncdim%npres(6000)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

The final result field has data statistics of:

{'maximum': 8.034833880932188e-08,
 'mean': 5.517965506021436e-08,
 'median': 5.3571959015214004e-08,
 'mid_range': 6.478297552508518e-08,
 'minimum': 4.921761224084848e-08,
 'range': 3.1130726568473405e-08,
 'root_mean_square': 5.532036247569286e-08,
 'sample_size': 6000,
 'standard_deviation': 3.943117025629124e-09}

Time interpolation complete.

_____ Time taken (in s) for 'time_interpolation' to run: 1.6365 _____

End of colocation iteration with file: ../data/marias-satellite-example-data/satellite-data/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_150_199-v1000.nc
Have compound output, a FieldList of length 47
/home/slb93/miniconda3/envs/cf-env-312/lib/python3.12/site-packages/numpy/ma/core.py:467: RuntimeWarning: invalid value encountered in cast
  fill_value = np.array(fill_value, copy=False, dtype=ndtype)
Final Field(List) from colocation of all inputs from specified observational data path is: Field: long_name=CO MASS MIX RATIO ON PRESS LEVS (ncvar%t)
----------------------------------------------------------
Data            : long_name=CO MASS MIX RATIO ON PRESS LEVS(key%domainaxis0(275400)) 1
Auxiliary coords: latitude(key%domainaxis0(275400)) = [72.25733947753906, ..., -11.548052787780762] degree_north
                : longitude(key%domainaxis0(275400)) = [-139.09249877929688, ..., -178.5377655029297] degree_east
                : time(key%domainaxis0(275400)) = [2017-07-21 00:00:00, ..., 2017-07-21 00:06:38]

_____ Time taken (in s) for 'create_cra_outputs' to run: 0.0 _____


_____ Time taken (in s) for 'write_output_data' to run: 12.265 _____

traj - making a trajectory plot
traj - plotting different colour markers based on a user set of levels
plotting lines
plotting markers
con - adding a colour bar

_____ Time taken (in s) for 'make_outputs_plot' to run: 8.3316 _____


_____ Time taken (in s) for 'main' to run: 310.9363 _____
