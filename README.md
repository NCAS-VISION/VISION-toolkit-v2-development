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

2. The **environment** you need will to run it requires a custom version of
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

Please contact Sadie if you need any help running anything here.
