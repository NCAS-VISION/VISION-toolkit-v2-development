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

Input data must be:
   
#. CF Compliant, that is abiding by the
   `CF Metadata Conventions <https://cfconventions.org/>`_. Ideally the
   data should abide by the latest version of the CF Conventions (as per the
   document listed against 'latest released version' on the
   `official website 'Conventions' page <https://cfconventions.org/conventions.html>`_),
   though earlier versions are generally sufficient.

#. In a form whereby, when aggregated during reading by ``cf.read`` or otherwise,
   there is precisely one field per physical variable, which could be either
   from:

   * the data already being in a form with one field per physical variable; or

   * the data being aggregatable to that form (see for reference the
     `cf-python aggregate function <https://ncas-cms.github.io/cf-python/function/cf.aggregate.html>`_
     (``cf.aggregate``) which is run during the ``cf.read`` operation
     which the VISION Toolkit uses to read-in datasets, and corresponding
     `aggregation rules outlined here <https://ncas-cms.github.io/cf-python/aggregation_rules.html>`_).

#. TODO

   #. TODO

   #. TODO

#. TODO

   #. TODO

   #. TODO
