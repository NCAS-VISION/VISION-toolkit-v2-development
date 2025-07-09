.. _PythonAPI:

Application Programming Interface (API) Reference
=================================================

.. currentmodule:: visiontoolkit
.. default-role:: obj


Full program as executed from CLI
---------------------------------

.. autosummary::
   :toctree: generated

   main


Core functions
--------------

Data input and compliance
+++++++++++++++++++++++++

.. autosummary::
   :toctree: generated

   get_files_to_individually_colocate
   read_obs_input_data
   read_model_input_data
   get_input_fields_of_interest
   vertical_parametric_computation
   vertical_parametric_computation_ahhc
   vertical_parametric_computation_ahspc
   ensure_cf_compliance
   check_time_coverage
   ensure_unit_calendar_consistency
   set_start_datetime
   get_time_coords


Co-location and bounding
++++++++++++++++++++++++

.. autosummary::
   :toctree: generated

   colocate
   colocate_single_file
   bounding_box_query
   subspace_to_spatiotemporal_bounding_box
   spatial_interpolation
   time_subspace_per_segment
   time_interpolation


Data output
+++++++++++

.. autosummary::
   :toctree: generated

   create_contiguous_ragged_array_output
   write_output_data


Helper
++++++

.. autosummary::
   :toctree: generated

   logger
   timeit
   get_env_and_diagnostics_report


Performance
+++++++++++

.. autosummary::
   :toctree: generated

   persist_all_metadata


Custom exceptions
-----------------

.. autosummary::
   :toctree: generated

   CFComplianceIssue
   IncompatibleDataInputsIssue
   DataReadingIssue
   ConfigurationIssue
   InternalsIssue


Plotting
--------

.. autosummary::
   :toctree: generated

   plotting.preview_plots
   plotting.output_plots
   make_preview_plots
   make_output_plots


Command-line parsing
--------------------

.. autosummary::
   :toctree: generated

   cli.setup_logging
   cli.process_cli_arguments
   cli.process_config
   cli.validate_config
   cli.process_config_file


Default values
--------------

.. autosummary::
   :toctree: generated

   constants.CONFIG_DEFAULTS


Plugins
-------

For Satellite observational data
++++++++++++++++++++++++++++++++

.. autosummary::
   :toctree: generated

   satellite_plugin
   plugins.satellite_compliance_converter.satellite_compliance_plugin


For WRF Data
++++++++++++

.. autosummary::
   :toctree: generated

   plugins.wrf_data_compliance_fixes.wrf_extra_compliance_fixes
   plugins.wrf_data_compliance_fixes.wrf_further_compliance_fixes
