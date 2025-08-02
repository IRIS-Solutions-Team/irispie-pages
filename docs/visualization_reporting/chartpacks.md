
Chartpacks
===========
    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`num_figures` | Total number of figures in the chartpack





Categorical list of functions
-------------------------------

### Creating new chartpacks ###

Function | Description
----------|------------
[`Chartpack`](#chartpack) | Create a new chartpack


### Getting information about chartpacks ###

Function | Description
----------|------------
[`get_description`](#get_description) | Get description attached to an object
[`set_description`](#set_description) | Set the description for an object


### Plotting chartpacks ###

Function | Description
----------|------------
[`plot`](#plot) | Plot the chartpack


### Adding figures and charts to chartpacks ###

Function | Description
----------|------------
[`add_chart`](#add_chart) | Add a new chart to an existing figure in the chartpack
[`add_figure`](#add_figure) | Add a new figure to the chartpack



&#9744;&#160;`Chartpack`
--------------------------

==Create a new chartpack==

```
self = Chartpack(
    title="",
    span=...,
    tiles=None,
    transforms=None,
    highlight=None,
    legend=None,
    show_legend=None,
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
    A list of strings that will be used as the legend for the charts.

???+ input "show_legend"
    Show the legend in the figure. If `None`, the legend will be shown if `legend` is
    not `None` and non-empty.

???+ input "reverse_plot_order"
    If `True`, the order of plotting the individual time series within each
    chart will be reversed.


### Returns


???+ returns "self"

    A new empty `Chartpack` object.
        



&#9744;&#160;`add_chart`
--------------------------

==Add a new chart to an existing figure in the chartpack==
        



&#9744;&#160;`add_figure`
---------------------------

==Add a new figure to the chartpack==
        



&#9744;&#160;`get_description`
--------------------------------


==Get description attached to an object==

    description = self.get_description()


### Input arguments ###

???+ input "self"
    An object from which to get the description.


### Returns ###

???+ returns "description"
    The description attached to the object.

        



&#9744;&#160;`plot`
---------------------

==Plot the chartpack==
        



&#9744;&#160;`set_description`
--------------------------------


==Set the description for an object==

    self.set_description(
        description,
    )


### Input arguments ###

???+ input "self"
    An Iris Pie object to which to attach the description.


???+ input "description"
    The description to attach to the Iris Pie object.


### Returns ###

This method modifies the Iris Pie object in place and returns `None`.

        