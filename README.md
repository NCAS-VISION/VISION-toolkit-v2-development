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

1. **Install** the toolkit by cloning this repository and running `pip install -e .` in the root
   directory of it. Note you do not need to do this to run the script, since you can
   run it with `python visiontoolkit/visiontoolkit.py`, but with that installation
   you can run and use the command `visiontoolkit` instead of having to call the script
   with the Python interpreter.

4. The **environment** you need will to run it requires the following:

   1. Python version 3.10 or later;
   2. cf-python at a version of minimum of 3.17.0,
     see https://ncas-cms.github.io/cf-python/installation.html for guidance;
   3. cf-plot  at a version of minimum 3.4.0, see https://ncas-cms.github.io/cf-plot/installation.html
   for guidance.


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

