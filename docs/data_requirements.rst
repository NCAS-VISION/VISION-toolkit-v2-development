.. _DataRequirements:

Data Requirements
=================

.. _CFConventions: https://cfconventions.org/


Context
-------

To work, the VISION Toolkit requires the input data for the
model and for the observations to be *sufficiently standard* with respect
to its metadata and structure. Specifically, it must be
*compliant with the CF Conventions metadata standard* (see the official
`CF Conventions website <CFConventions_>`_ for further information) and
*have particular CF-compliant coordinates of suitable form
present*. Details are provided below in a checklist which should be
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

.. note::

   These rules for validity apply whether the data in question is model or
   observational data, unless indicated otherwise.

To work with the VISION toolkit, input data must satisfy the following.
   
#. Be CF Compliant, that is abiding by the
   `CF Metadata Conventions <https://cfconventions.org/>`_.

   * Ideally the data should abide by the latest version of the CF Conventions
     (as per the document listed against 'latest released version' on the
     `official website 'Conventions' page <https://cfconventions.org/conventions.html>`_),
     but earlier versions are generally sufficient.

#. Be in a form whereby, when aggregated during reading by ``cf.read`` or otherwise,
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
     used by the toolkit to read the data, see TODO NEW CONFIG INPUT.

#. Each such field representing a physical variable having suitable coordinates
   defined to cover the context in spatiotemporal space, notably:

   #. Model data should be gridded in at least 4D (3D spatially plus time,
      X-Y-Z-T);

   #. Whereas observational data may be lower dimensional to account
      for constant levels, for example ship data may be defined without
      vertical (Z) levels (i.e. on X-Y-T).

Furthermore, the model and observational data when considered together should
should be *compatible* with each other for the purposes of co-location,
in the sense that:

#. The observational data spatial domain must lie fully inside the model
   data domain for all shared coordinates, for the full datetime range
   on which both are defined. For example, for an observational input
   of ship or buoy data in X-Y-T, for all points across the time
   coordinate T, the ship/buoy data X and Y points must lie within
   the X range and Y range of the model data.

#. The observational data datetime range must lie inside the datetime range
   of the model, unless a ``start-time-override`` is applied to override
   the observational range, in which case the observational range with
   the override set must then lie within the model's datetime range
   (so, the ``start-time-override`` must lie inside the model datetime range
   and the datetime corresponding to the duration difference from the
   earliest to latest timepoints in the original observational data, added
   to the ``start-time-override`` datetime, must also).

#. For trajectory observational data, for example flight, ship and buoy
   paths, consecutive points in the path (those one after the other in
   time) must not span more than one grid cell in the model data i.e.
   must always lie in adjacent grid cells. (Otherwise, the operation of
   co-location is deemed too non-sensical to perform.)


Specifically regarding satellite datasets:

* The VISION Toolkit has only been tested thus far on *nadir-viewing* satellites 
  (those that observe the Earth directly beneath them, in a downward direction,
  rather than at some angle) and due to the processing of the vertical coordinates
  through averaging kernel the distinction may be important. Therefore at
  present it isn't clear whether the toolkit works accurately for satellite
  data from those that are not nadir-viewing.
