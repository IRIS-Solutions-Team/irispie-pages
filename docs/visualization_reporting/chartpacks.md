
Chartpacks
===========
    


Categorical list of functions
-------------------------------

### Creating new chartpacks ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;Chartpack](#chartpack) | Create a new chartpack


### Plotting chartpacks ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;plot](#plot) | Plot the chartpack


### Adding figures and charts to chartpacks ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;add_chart](#add_chart) | Add a new chart to an existing figure in the chartpack
[:octicons-file-24:&nbsp;add_figure](#add_figure) | Add a new figure to the chartpack





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:&nbsp;num_figures](#num_figures) | Total number of figures in the chartpack



☐ `Chartpack`
---------------

==Create a new chartpack==

```
self = Chartpack(
    title="",
    span=...,
    tiles=None,
    transforms=None,
    highlight=None,
    legend=None,
    reverse_plot_order=False,
)
```

### Input arguments ###

???+ input "title"

    The title of the chartpack, used as a basis for creating a caption
    shown at the top of each figure.

???+ input "span"

    The date span on which the time series will be plotted.

???+ input "tiles"

    The number of rows and columns of the figure grid. If input "None", the number of
    rows and columns will be determined automatically.

???+ input "transforms"

    A dictionary of functions that will be applied to the input data before
    plotting.

???+ input "highlight"

    A date span that will be highlighted in the charts.

???+ input "legend"

    A list of strings that will be used as the legend of the charts.

???+ input "reverse_plot_order"

    If `True`, the order of plotting the individual time series within each
    chart will be reversed.

### Returns

???+ returns "self"

    A new empty `Chartpack` object.
        



☐ `add_chart`
---------------

==Add a new chart to an existing figure in the chartpack==
        



☐ `add_figure`
----------------

==Add a new figure to the chartpack==
        



☐ `plot`
----------

==Plot the chartpack==
        