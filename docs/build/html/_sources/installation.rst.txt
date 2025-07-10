.. _Installation:

Installation
============

Dependencies
------------

The **environment** needed to install and run VISION v2 toolkit requires the following:

   1. Python version ``3.10`` or later;
   2. cf-python at a version of minimum of ``3.17.0``,
      see https://ncas-cms.github.io/cf-python/installation.html for guidance;
   3. ESMPy at version of minimum ``8.7.0``, see the 'Optional -> Regridding' sub-section in the installation
      guidance for cf-python linked above for means to install this (conda/mamba makes it simplest);

and if you want to do any plotting with the toolkit you will also need:

   4. cf-plot at a version of minimum ``3.4.0``, see https://ncas-cms.github.io/cf-plot/installation.html
      for guidance.


Commands to install
-------------------

**Install** the toolkit by following these steps:

Note: soon the library will be added to PyPI and will be installable with ``pip``. Until then,
follow these steps.

1. Clone the code repository. Use
   ``git clone <toolkit path>`` as below, or you can clone via SSH or the GitHub CLI
   (for help if required see
   https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository):

   .. code-block:: console

      $ git clone https://github.com/NCAS-VISION/VISION-toolkit-v2-development.git


2. Install locally by changing into the root directory of the repo and running an 'editable' ``pip`` command:

   .. code-block:: console

      $ cd VISION-toolkit-v2-development
      $ pip install -e .


.. warning::

   If you don't use the ``pip`` install command above and instead try to run the toolkit with
   the Python interpreter like a Python script using ``python visiontoolkit/visiontoolkit.py`` or similar,
   there will be errors due to relative imports using ``.<module>`` syntax. With the ``pip`` command above
   applied successfully, you will be able to call ``visiontoolkit`` as a command and therefore run VISION v2
   as a proper CLI (or alternatively use the VISION v2 Python API).

