

UM: 
WRF:


Examples
========

Examples available in this documentation demonstrate use of data
from two different models as input to the VISION tool, namely:

* the `Unified Model (UM) <https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model>`_;
* the `Weather Research and Forecasting (WRF) Model <https://www.mmm.ucar.edu/models/wrf>`_;

as well as two formats of observational data:

* flights paths;
* satellite swaths.

Note this only showcases a subset of possibilities for
supported models and observational inputs. For rules on input
data which the VISION toolkit is capable of handling, indicating
further possibilities, please see the :ref:`DataRequirements`
section.


Examples using the UM
---------------------

.. _UMFlightExamples:

Examples using the UM and flight paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``[UF1]``: UM model data co-located onto FAAM STANCO campaign flight path

  * Configuration file:
    `um-faam-stanco-1.json <https://github.com/NCAS-VISION/VISION-toolkit-v2-development/blob/main/visiontoolkit/configurations/um-faam-stanco-1.json>`_
  * Input datasets available from: TODO

* ``[UF2]``: UM model data co-located onto FAAM STANCO campaign flight path (overriding start time)

  * Configuration file:
    `um-faam-stanco-2.json <https://github.com/NCAS-VISION/VISION-toolkit-v2-development/blob/main/visiontoolkit/configurations/um-faam-stanco-2.json>`_
  * Input datasets available from: TODO

* ``[UF3]``: UM model data co-located onto FAAM STANCO campaign flight path (different overriding start time)

  * Configuration file:
    `um-faam-stanco-3.json <https://github.com/NCAS-VISION/VISION-toolkit-v2-development/blob/main/visiontoolkit/configurations/um-faam-stanco-3.json>`_
  * Input datasets available from: TODO


.. _UMSatelliteExamples:

Examples using the UM and satellite swaths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``[US1]``: UM model data co-located onto a satellite swath
* ``[US2]``: UM model data co-located onto a (different) satellite swath
* ``[US3]``: UM model data co-located onto a (different) satellite swath
* ``[US4]``: UM model data co-located onto a (different) satellite swath
* ``[US5]``: UM model data co-located onto a full satellite orbit of swaths
* ``[US6]``: UM model data co-located onto three consecutive full satellite orbits of swaths
* ``[US7]``: UM model data co-located onto a full revolution of consecutive full satellite orbits of swaths
* ``[US8]``: Particular satellite swath (from observational input) discrete sampling geometry preview only (no data)
* ``[US9]``: Particular satellite swath (from observational input) discrete sampling geometry preview only (no data)


Examples using the WRF Model
----------------------------

.. _WRFFlightExamples:

Examples using WRF and flight paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``[WF1]``: WRF model data co-located onto FAAM STANCO campaign flight path
* ``[WF2]``: WRF model data co-located onto FAAM STANCO campaign flight path (overriding start time)
* ``[WF3]``: WRF model data co-located onto FAAM STANCO campaign flight path (different overriding start time)
* ``[WF4]``: WRF model data co-located onto FAAM STANCO campaign flight path (different overriding start time)
* ``[WF5]``: WRF model data co-located onto a minimal two-point flight test case

