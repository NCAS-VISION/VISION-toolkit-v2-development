# VISION-toolkit-v2-development

**Development towards Version 2 of the VISION project toolkit**

:warning: Note this code is *actively under development* and no guarantees about
functionality or about documentation or testing can be made. For a released
earlier version of the toolkit, please see and use the tool provided in the
[`VISION-toolkit`](https://github.com/NCAS-VISION/VISION-toolkit) repository,
and consult the documentation there. (When this code is ready it will be copied to that
repository as its canonical home and marked as Version 2.0 of the toolkit.) :warning:

## Instructions for setup and use

### Installing the toolkit

1. **Install** the toolkit by cloning this repository and running `pip install -e .` in the root
   directory of it. Note you do not need to do this to run the script, since you can
   run it with `python visiontoolkit/visiontoolkit.py`, but with that installation
   you can run and use the command `visiontoolkit` instead of having to call the script
   with the Python interpreter.

4. The **environment** you need will to run it requires a custom branch of
   cf-plot, and otherwise you will need all the
   dependencies of that and of cf-python. So, to get the right
   Python environment (`conda` and/or `mamba` will make it simplest):

   1. Ensure you are using Python version 3.10 or later.
   2. Install the latest cf-python and cf-plot (noting in the latter case this
      is mostly to ensure you have the right dependencies because we will
      then go on to install a specific branch from cf-plot as below).
      To do this, see the instructions at:

      * https://ncas-cms.github.io/cf-python/installation.html
      * https://ncas-cms.github.io/cf-plot/build/download.html#to-install-cf-plot

   3. You need the latest version of cf-plot on a specific branch where a special
      bug-fix patch has bene applied, so use the `generalise-traj` branch required
      using the following command:
      `pip install git+https://github.com/NCAS-CMS/cf-plot.git@generalise-traj`


### Running the toolkit

The script has now been given minimal packaging so it can be
run as a command after installation as per the abov instructions. See the available
CLI from running:

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

