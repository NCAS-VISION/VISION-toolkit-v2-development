# VISION Project Resources

Scripts and resources related to the VISION project 

## Instructions relating to the resources

### Running the script

The script has now been given minimal packaging so it can be
run as a command. Try it out with:

```console
$ visiontoolkit --help
```

and use the CLI inputs to guide as to what to specify as arguments.

Note that for development, I have mostly been using FAAM STANCO campaign
data for which I provide a custom config. as follows to run the script:

```console
$ cd visiontoolkit
$ visiontoolkit --config-file="configurations/faam-stanco-e2e-config.json"
```

(that configuration JSON file is provided in this repository.)

If you want to run using WRF model input data, there is also a configuration script for that at
`visiontoolkit/configurations/wrf-preprocessed-e2e-config.json`, though note
the WRF prcoessing is under active development so values in this configuration file may soon be
tweaked. You will need to point in the script to pre-processed WRF data such as that processed
with code under, with saved outputs stored under, `wrf-vert-coords`.


### Instructions to run the vision toolkit code

*Note: these instructions are brief given we are quickly updating
the script and relevant libraries, but hopefully enough to go on
for now. Once things stabilise more, we will update them and add
detail.*

1. The working toolkit (at this stage, just a lone script) is under this repo at
  `visiontoolkit/visiontoolkit.py`. If you install the toolkit via `pip install -e .`
  or similar, you can run that script simply by calling the command `visiontoolkit`, but
  you could also run it as a script via e.g. `python visiontoolkit/visiontoolkit.py`.
  Note: the code was developed first under `cf-scripts/cf-vision-flight-e2e.py` but
  has since been moved across to `visiontoolkit/visiontoolkit.py` for proper packaging
  requrements and the old directory `cf-scripts` deleted.

2. The **environment** you need will to run it requires a custom branch of
   cf-plot, and otherwise you will need all the
   dependencies of that and of cf-python. So, to get the right
   Python environment (conda and/or mamba will make it simplest):

   1. Ensure you are using Python version 3.10 or later.
   2. Install the latest cf-python and cf-plot, noting in the latter case this
      is mostly to ensure you have the right dependencies because we will
      then go on to apply a patch `diff` to cf-plot, so use different
      versions of those. To do this, see the instructions at:

      * https://ncas-cms.github.io/cf-python/installation.html
      * https://ncas-cms.github.io/cf-plot/build/download.html#to-install-cf-plot

   3. You need the latest version of cf-plot ON A SPECIFIC BRANCH WHERE A
       PATCH HAS BEEN APPLIED, so use the `generalise-traj` branch required
       using the following command:
       pip install git+https://github.com/NCAS-CMS/cf-plot.git@generalise-traj

Please contact Sadie if you need any help running anything here.
