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
   observational data.

#. TODO

   #. TODO

   #. TODO

#. TODO

   #. TODO

   #. TODO

#. TODO

   #. TODO

   #. TODO

#. TODO

   #. TODO

   #. TODO
