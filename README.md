# VISION Project Resources

Scripts and resources related to the VISION project 

## Instructions relating to the resources

### Running the script

The script has now been given minimal packaging so it can be
run as a command. Try it out with:

```console
$ visiontoolkit --help
```

and use the CLI inputs to guide as to what to specify.

Note that for development, I have mostly been using FAAM STANCO campaign
data for which I provide a custom config. as follows to run the script:

```console
$ visiontoolkit --config-file="configurations/faam-stanco-e2e-config.json"
```

(that configuration JSON file is provided in this repository.)


### Instructions to run the cf-python end-to-end co-location script

*Note: these instructions are brief given we are quickly updating
the script and relevant libraries, but hopefully enough to go on
for now. Once things stabilise more, we will update them and add
detail.*

1. The **script** is under this repo `vision-project-resources` at
   `cf-scripts/cf-vision-flight-e2e.py`.

2. The **environment** you need will to run it requires a custom version of
   cf-plot, and otherwise you will need all the
   dependencies of that and of cf-python. So, to get the right
   Python environment (conda and/or mamba will make it simplest):

   1. Ensure you are using Python version 3.10 or later
   2. Install the latest cf-python and cf-plot, noting in the latter case this
      is mostly to ensure you have the right dependencies because we will
      then go on to apply a patch `diff` to cf-plot, so use different
      versions of those. To do this, see the instructions at:

      * https://ncas-cms.github.io/cf-python/installation.html
      * https://ncas-cms.github.io/cf-plot/build/download.html#to-install-cf-plot

   3. You need the latest version of cf-plot, but also have to apply a
      patch (note `main` is still called `master` on this repo) on top
      of that to tweak some functionality, so:

      * `git clone` the cf-plot repo: https://github.com/NCAS-CMS/cf-plot
      * apply the following `diff` to apply the patch via
        `git apply <diff below copied to a file, name>`

        ```diff
        diff --git a/cfplot/cfplot.py b/cfplot/cfplot.py
        index 1ecc474..f45533e 100644
        --- a/cfplot/cfplot.py
        +++ b/cfplot/cfplot.py
        @@ -10398,7 +10398,7 @@ def traj(
             for track in np.arange(ntracks):
                 xpts = lons[track, :]
                 ypts = lats[track, :]
        -        data2 = data[track, :]
        +        data2 = data

                 xpts_orig = deepcopy(xpts)
                 xpts = np.mod(xpts + 180, 360) - 180
        @@ -10427,6 +10427,7 @@ def traj(
                         print("plotting markers")

                     if legend_lines is False:
        +                """
                         mymap.plot(
                             xpts,
                             ypts,
        @@ -10443,6 +10444,7 @@ def traj(
                             clip_on=True,
                             transform=ccrs.PlateCarree(),
                         )
        +                """
                     else:
                         line_xpts = xpts.compressed()
                         line_ypts = ypts.compressed()
        @@ -10451,6 +10453,7 @@ def traj(
                         for i in np.arange(np.size(line_xpts) - 1):
                             val = (line_data[i] + line_data[i + 1]) / 2.0

        +                    """
                             col = plotvars.cs[np.max(np.where(val > plotvars.levels))]
                             mymap.plot(
                                 line_xpts[i: i + 2],
        @@ -10462,6 +10465,7 @@ def traj(
                                 clip_on=True,
                                 transform=ccrs.PlateCarree(),
                             )
        +                    """

                 # Plot vectors
                 if vector:
        @@ -10478,6 +10482,7 @@ def traj(
                             pts = xpts.size

                         for pt in np.arange(pts - 1):
        +                    """
                             mymap.arrow(
                                 xpts[pt],
                                 ypts[pt],
        @@ -10492,6 +10497,8 @@ def traj(
                                 clip_on=True,
                                 transform=ccrs.PlateCarree(),
                             )
        +                    """
        +                    pass

             # Plot different colour markers based on a user set of levels
             if legend:
        @@ -10511,7 +10518,7 @@ def traj(
                 for track in np.arange(ntracks):
                     xpts = lons[track, :]
                     ypts = lats[track, :]
        -            data2 = data[track, :]
        +            data2 = data

                     for i in np.arange(np.size(levs) - 1):
                         color = plotvars.cs[i]
        @@ -10535,9 +10542,10 @@ def traj(
                                 xpts[pts],
                                 ypts[pts],
                                 s=markersize * 15,
        -                        c=color,
        +                        c=[plotvars.cs[np.max(np.where(d > plotvars.levels))] for d in data2[pts]],
                                 marker=marker,
        -                        edgecolors=markeredgecolor,
        +                        linewidth=plot_linewidth,
        +                        ###edgecolors=markeredgecolor,  # SLB BUG HERE
                                 transform=ccrs.PlateCarree(),
                                 zorder=plot_zorder,
                             )

        ```

See below for instructions on specifying data inputs.

Please make a note of any issues you experience, and let us know.


### Inputs to the cf-python end-to-end co-location script

You will need to point to the right data location in the script.

The input data will need to be made
CF-compliant to work to run, and there is a script that does that
for datasets which aren't yet compliant. Please see the `twine-vision`
Slack channel for details of such a script, provided by Maria.

The paths to your data should be specified at the top of the script in:
https://github.com/NCAS-VISION/vision-project-resources/blob/a40bdbf4c9162c883efdeaa20061e162e7ff3141/cf-scripts/cf-vision-flight-e2e.py#L31-L39


### Outputs from the cf-python end-to-end co-location script

Outputs are generated from the script (if it runs successfully), to
the directory set in the `OUTPUTS_DIR` variable:

* XY plots of the flight track (across any Z) for:
  * the input obervational field and/or only its track, if the relevant
    flags are set to `True`, namely
    namely `SHOW_PLOT_OF_INPUT_OBS` and `PLOT_OF_INPUT_OBS_TRACK_ONLY`);
  * the output co-located field.
* the final output co-located field netCDF file, written-out at the
  end of the script, in `cf-script-outputs/cf_vision_result_field.nc`.

Furthermore, when the `VERBOSE` flag is `True`, lots of information is
output to STDOUT and this can be saved and stored with the following
command from a script run:

```console
$ python cf-vision-flight-e2e.py >out 2>&1
```

with the STDOUT captured for the runs which generated the plots
added to this repo also stored in this way, in the text file
`cf-script-outputs/cf-vision-flight-e2e-stdout.txt`, for illustration.
