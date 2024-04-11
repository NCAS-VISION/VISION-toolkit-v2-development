# VISION Project Resources

Scripts and resources related to the VISION project 

## Instructions relating to the resources

### Instructions to run the cf-python end-to-end co-location script

*Note: these instructions are brief given we are quickly updating
the script and relevant libraries, but hopefully enough to go on
for now. Once things stabilise more, we will update them and add
detail.*

1. The **script** is under this repo `vision-project-resources` at
   `cf-scripts/cf-vision-flight-e2e.py`.

2. The **environment** you need will to run it requires a custom version of
   cf-python and of cf-plot, and otherwise you will need all the
   dependencies of those libraries. So, to get the right
   Python environment (conda and/or mamba will make it simplest):

   1. Ensure you are using Python version 3.10 or later
   2. Install the latest cf-python and cf-plot, noting this is mostly
      to ensure you have the right dependencies because we will
      then go on to install the `main` branch of cf-python and apply a
      `diff` to cf-plot, so use different versions of those.
      To do this, see the instructions at:

      * https://ncas-cms.github.io/cf-python/installation.html
      * https://ncas-cms.github.io/cf-plot/build/download.html#to-install-cf-plot

   3. Now we need to get and use the current `main` branch of cf-python
      instead of the latest release, to capture new regridding features
      required by the script that are yet to be released:
      * you can use some approach such as those listed on:
      https://stackoverflow.com/questions/20101834/pip-install-from-git-repo-branch
      if necessary, or:

      * `git clone` the cf-python repo: https://github.com/NCAS-CMS/cf-python
      * run `pip install -e .` in the root of the repository to install
        the state of the repo, which will be the current `main` branch state.

   4. We should use the latest version of cf-plot, but we need to apply a
      patch (note `main` is still called `master` on this repo), so:

      * `git clone` the cf-plot repo: https://github.com/NCAS-CMS/cf-plot
      * re-wind to the commit `fbe1f683297ea38954d1dd4ff92e5b6e85c681b1`
        which was from the release `v3.3.0`.
      * apply the following `diff` to apply the patch via
        `git apply <diff below copied to a file, name>`

        ```diff
        diff --git a/cfplot/cfplot.py b/cfplot/cfplot.py
        index 95a45c7..36c1805 100644
        --- a/cfplot/cfplot.py
        +++ b/cfplot/cfplot.py
        @@ -8379,7 +8379,11 @@ def traj(f=None, title=None, ptype=0, linestyle='-', linewidth=1.0, linecolor='b
             for track in np.arange(ntracks):
                 xpts = lons[track, :]
                 ypts = lats[track, :]
        -        data2 = data[track, :]
        +        ###print("DEBUG", data, track, xpts)
        +        ###try:
        +        data2 = data  #[track, :]
        +        ###except:
        +        ###data2 = data[track]

                 xpts_orig = deepcopy(xpts)
                 xpts = np.mod(xpts + 180, 360) - 180
        @@ -8417,17 +8421,26 @@ def traj(f=None, title=None, ptype=0, linestyle='-', linewidth=1.0, linecolor='b
                     else:
                         line_xpts = xpts.compressed()
                         line_ypts = ypts.compressed()
        -                line_data = data2.compressed()
        +                line_data = data2.compressed()  # TODO SADIE BUG

        -                for i in np.arange(np.size(line_xpts)-1):
        -                    val = (line_data[i] + line_data[i+1])/2.0
        +                for i in np.arange(np.size(line_xpts)-1):  ## CHANGE FROM -1

        -                    col = plotvars.cs[np.max(np.where(val > plotvars.levels))]
        -                    mymap.plot(line_xpts[i:i+2], line_ypts[i:i+2], color=col,
        -                               linewidth=plot_linewidth, linestyle=linestyle,
        -                               zorder=zorder, clip_on=True, transform=ccrs.PlateCarree())
        -
        -        # Plot vectors
        +                    #print("JUPITER'S MOONS", i, np.size(line_xpts)-2)
        +                    #if i != np.size(line_xpts)-2:
        +                    #try:
        +                    try:
        +                        val = (line_data[i] + line_data[i+1])/2.0   # SADIE
        +                        #else:
        +                        #    val = line_data[i]
        +                        # SADIE HERE
        +                        col = plotvars.cs[np.max(np.where(val > plotvars.levels))]
        +                        mymap.plot(line_xpts[i:i+2], line_ypts[i:i+2], color=col,
        +                                   linewidth=plot_linewidth, linestyle=linestyle,
        +                                   zorder=zorder, clip_on=True,
        +                                   transform=ccrs.PlateCarree())
        +                    except:
        +                        pass
        +                        # Plot vectors
                 if vector:
                     if verbose and track == 0:
                         print('plotting vectors')
        @@ -8469,10 +8482,24 @@ def traj(f=None, title=None, ptype=0, linestyle='-', linewidth=1.0, linecolor='b
                 for track in np.arange(ntracks):
                     xpts = lons[track, :]
                     ypts = lats[track, :]
        -            data2 = data[track, :]
        -
        -
        -
        +            ###print("DEBUG", data, track, xpts)
        +            ###try:
        +            data2 = data  ###[track, :]
        +            ###except:
        +            ###data2 = data[track]
        +            ###print("DATA2 IS", data2)
        +
        +            """
        +            col_sadie = plotvars.cs[np.max(np.where(data2 > plotvars.levels))]
        +            mymap.scatter(xpts, ypts,  #xpts[pts], ypts[pts],
        +                                  s=markersize*2,##*15,
        +                                  c=col_sadie,   # SADIE HERE
        +                                  marker=marker,
        +                                  edgecolors=markeredgecolor,
        +                                  transform=ccrs.PlateCarree(),
        +                                  zorder=101
        +            )
        +            """
                     for i in np.arange(np.size(levs)-1):
                         color = plotvars.cs[i]

        @@ -8486,13 +8513,17 @@ def traj(f=None, title=None, ptype=0, linestyle='-', linewidth=1.0, linecolor='b
                         else:
                             plot_zorder = zorder
                         if np.size(pts) > 0:
        -
        -                    mymap.scatter(xpts[pts], ypts[pts],
        -                                  s=markersize*15,
        -                                  c=color,
        +                    ###print("ADDING A SCATTER HERE", xpts, len(xpts))
        +                    ###print("DATA IS FOR COLOURS", data)
        +                    mymap.scatter(xpts[pts], ypts[pts],  #xpts[pts], ypts[pts],
        +                                  linewidth=0.0,
        +                                  s=markersize/2,##*15,
        +                                  c=[plotvars.cs[np.max(np.where(d > plotvars.levels))] for d in data2[pts]],   # SADIE HERE
                                           marker=marker,
                                           edgecolors=markeredgecolor,
        -                                  transform=ccrs.PlateCarree(), zorder=plot_zorder)
        +                                  transform=ccrs.PlateCarree(),
        +                                  zorder=plot_zorder
        +                                  )

             # Axes
             plot_map_axes(axes=axes, xaxis=xaxis, yaxis=yaxis,
        ```

3. As for the script, new features have been added which introduce failures,
   so to get something working end-to-end you should re-wind back to the
   commit `bbb410bbf80ed623acec34d8c70fd3cb9506e1fd` which is known to run
   for us. If things don't work on that, you cna try reverting to older
   commits to explore to get something working, for now.

4. You will need to point to the right data location in the script.
   The input data will need to be made
   CF-compliant to work to run, and there is a script that does that
   for datasets which aren't yet compliant. Please ask Maria for a copy
   of that script, until we can add it to this repo.

   The paths to your data should be specified at the top of the script in:
   https://github.com/NCAS-VISION/vision-project-resources/blob/fa96207705032e1cf7683a3087b2593376043a59/cf-scripts/cf-vision-flight-e2e.py#L25-L29


Please make a note of any issues you experience, and let us know.
