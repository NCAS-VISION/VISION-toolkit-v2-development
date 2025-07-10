.. _Quickstart:

Quickstart
==========

Running the toolkit
-------------------

Via the command line: the `visiontoolkit` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the toolkit as covered in the :ref:`installation guide <Installation>`.
You will then have access to the `visiontoolkit` command which is the means to
run and configure the toolkit. To understand the available options
for configuration, run with the `--help` option for a summary of the
available command-line interface:

.. code-block:: console

   $ visiontoolkit --help

Note that configuration can be made either by:

* specifying valid keywords the command line, or
* through use of a configuration file in YAML format specified using the
  `--config-file` (equivalently `-c`) option followed by a valid path to
  the configuration file provided on the command line.


Examples
%%%%%%%%
  
For example, this repository contains example configuration files for running
with both UM and WRF model inputs, though note both assume pre-processing
has been done on the input data to ensure correct form and CF Compliance
(more information will be added about this here soon):

.. code-block:: console

   $ cd visiontoolkit
   $ visiontoolkit --config-file="configurations/um-faam-stanco-1.json"

or using WRF model input:

.. code-block:: console

   $ cd visiontoolkit
   $ visiontoolkit --config-file="configurations/wrf-faam-stanco-1.json"

The above examples are of flight trajectories. A satellite observation case example is:

.. code-block:: console

   $ cd visiontoolkit
   $ visiontoolkit --config-file="configurations/um-satellite-1.json"


Via the Python API
^^^^^^^^^^^^^^^^^^

You can also use the toolkit through the Python API which is documented
:ref:`here <PythonAPI>`: import `visiontoolkit` and make use of any
applicable objects such as functions and exceptions.

A good place to start might be the `colocate` function, which accepts a
model field and an observational field and colocates the former onto
the latter.
