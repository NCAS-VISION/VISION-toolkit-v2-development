

Application Programming Interface (API) Reference
=================================================

.. currentmodule:: visiontoolkit
.. default-role:: obj


Full program as executed from CLI:
----------------------------------

.. autosummary::
   :toctree: generated

   main


Core functions:
---------------

.. autosummary::
   :toctree: generated

   timeit
   get_env_and_diagnostics_report
   get_files_to_individually_colocate
   read_obs_input_data
   read_model_input_data
   get_input_fields_of_interest
   vertical_parametric_computation
   vertical_parametric_computation_ahhc
   vertical_parametric_computation_ahspc
   ensure_cf_compliance
   set_start_datetime
   check_time_coverage
   get_time_coords
   ensure_unit_calendar_consistency
   persist_all_metadata
   bounding_box_query
   subspace_to_spatiotemporal_bounding_box
   spatial_interpolation
   time_subspace_per_segment
   time_interpolation
   create_contiguous_ragged_array_output
   write_output_data
   colocate_single_file


Custom exceptions:
------------------

.. autosummary::
   :toctree: generated

   CFComplianceIssue
   IncompatibleDataInputsIssue
   DataReadingIssue
   ConfigurationIssue
   InternalsIssue


Plotting:
---------

.. autosummary::
   :toctree: generated

   make_preview_plots
   make_output_plots


Command-line parsing:
---------------------

TODO


Default values:
---------------

TODO


Plugins:
--------

TODO

.. autosummary::
   :toctree: generated

   satellite_plugin
