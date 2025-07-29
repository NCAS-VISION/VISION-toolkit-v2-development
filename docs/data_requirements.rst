.. _DataRequirements:

Data Requirements
=================

.. _CFConventions: https://cfconventions.org/


Context
-------

To work, the VISION Toolkit requires the input data for the
model and for the observations to be *sufficiently standard with respect
to its metadata and structure*. Specifically, it must be
compliant with the CF Conventions metadata standard (see the official
`CF Conventions website <CFConventions_>`_ for further information) and
have particular CF-compliant coordinates of suitable form
present. They must also be *compatible for co-location with each other*,
notably the extent of the observational data must lie within the
extent of the model data.

Details are provided below in a numbered checklist which should be
consulted to ensure validity.

.. note::

   For selected cases, we have data pre-processing built into the toolkit
   as plugins which will conduct some processing of specific datasets of
   standard format from a given project or model to
   enable them to conform to the requirements where they don't quite
   satisfy them (for historical reasons or to abide by other/internal
   data standards etc.). You can choose to enable these plugins via the
   configuration. For more details, see the ``preprocess-mode-obs`` and
   ``preprocess-mode-model`` configuration options as covered in the
   :ref:`CLI <Command-line Interface (CLI) Reference>`.


.. warning::

   If you attempt to use the VISION Toolkit with model and/or observational
   data which does not abide by the requirements documented here, it cannot
   be guaranteed to work. (However, if you believe your data does in fact
   meet these requirements and the toolkit is erroring or not seeming to
   work correctly some way, please :ref:`contact us <IntroContact>`
   so we can verify whether the data or the toolkit is
   at issue).


Checklist for validity of input data
------------------------------------

Input datasets separately
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   These rules for validity apply whether the data in question is model or
   observational data, unless indicated otherwise.

To work with the VISION toolkit, input data must satisfy the following.
   
1. Be CF Compliant, that is abiding by the
   `CF Metadata Conventions <https://cfconventions.org/>`_.

   * Ideally the data should abide by the latest version of the CF Conventions
     (as per the document listed against 'latest released version' on the
     `official website 'Conventions' page <https://cfconventions.org/conventions.html>`_),
     but earlier versions are generally sufficient.

2. Be in a form whereby, when aggregated during reading by ``cf.read`` or otherwise,
   there is precisely one field per physical variable (e.g. one field only for
   a temperature variable), which could be either from:

   * The data already being in a form with one field per physical variable (preferred); OR

   * The data being immediately aggregatable to that form (see for reference the
     `cf-python aggregate function <https://ncas-cms.github.io/cf-python/function/cf.aggregate.html>`_
     (``cf.aggregate``) which is run during the ``cf.read`` operation
     which the VISION Toolkit uses to read-in datasets, and corresponding
     `aggregation rules outlined here <https://ncas-cms.github.io/cf-python/aggregation_rules.html>`_); OR

   * (Least desirable, but acceptable/supported) configuration being provided
     to support a more relaxed aggregation of the data into that form, which
     requires altering the aggregtion rule logic to be less strict to
     reduce down the read-in fields more than the default aggregation rules
     would, based upon provision of a dictionary of extra
     keywords to provide to the `cf.aggregate` operation ran by the `cf.read`
     used by the toolkit to read the data, see ``[[TODO NEW CONFIG INPUT]]``.

3. Each such field representing a physical variable having suitable coordinates
   (for the model data these must be in the form of *dimension* coordinates),
   defined to cover the context in spatiotemporal space, notably:

   * Model data should be gridded in at least 4D (3D spatially plus time,
     X-Y-Z-T);

   * Whereas observational data may be lower dimensional to account
     for constant levels, for example ship data may be defined without
     vertical (Z) levels (i.e. on X-Y-T).

4. Vertical (Z) coordinates, where required as covered above, should be defined
   either directly or as parametric vertical coordinates, and should have the
   appropriate dimensionality.

   * The vertical (Z) coordinate must be in the form of either an
     altitude/height/depth or a pressure coordinate, with appropriate CF Standard
     Name assigned, taken to be `air_pressure` by default but this should be
     adapted for another such standard name using the
     ``vertical-colocation-coord`` (see the corresponding
     :ref:`Command-line Interface <cli>` option).

   * If an altitude/height/depth, it will need to be either a 1D dimension
     coordinate OR a 3D auxiliary coordinate OR a parametric form which
     would become an auxiliary 4D coordinate).

   * Otherwise, if a form of pressure, it will need to be either a 1D dimension
     coordinate OR a parametric form which
     would become an auxiliary 4D coordinate.

   * If the model data input is in PP format and has vertical coordinates
     defined parametrically in terms of an atmosphere hybrid height
     coordinate, the orography
     `needs to be known <https://cfconventions.org/cf-conventions/cf-conventions.html#atmosphere-hybrid-height-coordinate>`_
     so a suitable orography
     dataset must be supplied via specifying the path to it using the ``orography``
     configuration option
     (see the :ref:`Command-line Interface <cli>`).

   * Otherwise, parametric vertical coordinates are handled by the toolkit
     logic without need for further input.


5. (As specified by the CF Conventions, but for clarity emphasised here)
   for observational data defined as discrete sampling geometries, which
   should be the form for example for trajectories e.g. flight paths,
   the time coordinate must have values in strict monotonically
   increasing order (i.e. always increasing).


.. SLB: TODO ask DH whether we need to say anything else explicitly about being
   in DSG form for paths, given that the CF compliance should ensure this
   anyway.


.. note::

   **Specifically regarding satellite datasets:** the VISION Toolkit has
   only been tested so far on *nadir-viewing* satellites 
   (those that observe the Earth directly beneath them, in a downward direction,
   rather than at some angle) and due to the processing of the vertical coordinates
   through averaging kernel the distinction may be important. Therefore at
   present it isn't clear whether the toolkit works accurately for satellite
   data from those that are not nadir-viewing.
      

Model and observational datasets compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Furthermore, to work with the VISION toolkit, any given input combination of
model and observational datasets together should be *compatible* with each
other for the purposes of co-location, in the sense that:

6. The observational data spatial domain must lie fully inside the model
   data spatial domain for all shared coordinates, for the full datetime range
   on which both are defined. For example, for an observational input
   of ship or buoy data in X-Y-T, for all points across the time
   coordinate T, the ship/buoy data X and Y points must lie within
   the X range and Y range of the model data.

   .. SLB: does halo influence this? If so, clarify in a note.

7. The observational data datetime range must lie inside the datetime range
   of the model, unless a ``start-time-override`` (see the corresponding
   :ref:`Command-line Interface <cli>` option) is applied to override the
   observational datetime range, in which case the observational range with
   the override set must then lie within the model's datetime range
   (so, the ``start-time-override`` must lie inside the model datetime range
   and the datetime corresponding to the duration difference from the
   earliest to latest timepoints in the original observational data, added
   to the ``start-time-override`` datetime, must also).

8. For trajectory observational data, for example flight, ship and buoy
   paths, consecutive points in the path (those one after the other in
   time) must not span more than one grid cell in the model data i.e.
   must always lie in adjacent grid cells. (Otherwise, the operation of
   co-location is deemed too nonsensical to perform.)
