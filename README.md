# VISION-toolkit-v2-development

**Version 2 of the VISION project toolkit**

:warning: Note this code is *under development though should be relatively stable now*, though
there may be some changes. For a released earlier version of the toolkit, please see and
use the tool provided in the
[`VISION-toolkit`](https://github.com/NCAS-VISION/VISION-toolkit) repository,
and consult the documentation there. (When this code is ready it will be copied to that
repository as its canonical home and marked as Version 2.0 of the toolkit.) :warning:

## Context

For context on this toolkit and its scientific and technical background, please consult
[these slides](https://github.com/sadielbartholomew/sadielbartholomew/blob/master/talks-and-workshops/VISION_UoR_Met_Dept_lunchtime_seminar.pdf)
from a recent talk given by a VISION team member.

## Instructions for setup and use

### Installing the toolkit

#### Environment

The **environment** needed to install and run VISION v2 toolkit requires the following:

   1. Python version 3.10 or later;
   2. cf-python at a version of minimum of 3.17.0,
     see https://ncas-cms.github.io/cf-python/installation.html for guidance;
   3. ESMPy at version of minimum 8.7.0, see the 'Optional -> Regridding' sub-section in the installation
   guidance for cf-python linked above for means to install this (conda/mamba makes it simplest);

and if you want to do any plotting with the toolkit you will also need:

   4. cf-plot at a version of minimum 3.4.0, see https://ncas-cms.github.io/cf-plot/installation.html
   for guidance.

#### Commands to install

**Install** the toolkit by following these steps:

Note: soon the library will be added to PyPI and will be installable with `pip`. Until then,
follow these steps.

1.  Clone this repository. Use
    `git clone <HTTPS path to this repo>` as below, or you can clone via SSH or the GitHub CLI
    (for help if required see
    https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository):

    ```console
    $ git clone https://github.com/NCAS-VISION/VISION-toolkit-v2-development.git
    ```

2. Install locally by changing into the root directory of the repo and running an 'editable' `pip` command:

    ``` console
    $ cd VISION-toolkit-v2-development
    $ pip install -e .
    ```

:warning: Warning: if you don't use the `pip` install command above and instead try to run the toolkit with
the Python interpreter like a Python script using `python visiontoolkit/visiontoolkit.py` or similar,
there will be errors due to relative imports using `.<module>` syntax. With the `pip` command above
applied successfully, you will be able to call `visiontoolkit` as a command and therefore run VISION v2
as a proper CLI (or alternatively use the VISION v2 Python API).


### Running the toolkit

The script is packaged so it can be run as a command after installation as per the above instructions. See the available command-line interface from running:

```console
$ visiontoolkit --help
```

For example, this repository contains example configuration files for running
with both UM and WRF model inputs, though note both assume pre-processing
has been done on the input data to ensure correct form and CF Compliance
(more information will be added about this here soon):

```console
$ cd visiontoolkit
$ visiontoolkit --config-file="configurations/um-faam-stanco-1.json"
```

or using WRF model input:

```console
$ cd visiontoolkit
$ visiontoolkit --config-file="configurations/wrf-faam-stanco-1.json"
```

The above examples are of flight trajectories. A satellite observation case example is:

```console
$ cd visiontoolkit
$ visiontoolkit --config-file="configurations/um-satellite-1.json"
```

