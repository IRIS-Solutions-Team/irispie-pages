
Simulation meta plans
======================

`SimulationPlan` objects are used to set up meta information about
conditioning assumptions for simulations of
[`Simultaneous`](simultaneous_modelsd) or [`Sequential`](sequential_models)
models. The simulation plans specify

* what variables to exogenize in what periods
* what shocks to endogenized in what periods (`Simultaneous` models only)
* what anticipation status to assign (`Simultaneous` models only)

The plans only contain meta information, not the actual data points for the
exogenized variables. The actual data points are expected to be included in
the input databox when the simulation is run.
    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`end` | End date of the simulation span
`frequency` | Date frequency of the simulation span
`num_periods` | Number of periods in the simulation span
`start` | Start date of the simulation span





Categorical list of functions
-------------------------------

### Creating new simulation plans ###

Function | Description
----------|------------
[`SimulationPlan`](#simulationplan) | Create new simulation plan object


### Defining exogenized and endogenized data points in [`Simultaneous` simulations](simultaneous.md#simulate) ###

Function | Description
----------|------------
[`endogenize_anticipated`](#endogenize_anticipated) | Endogenize certain quantities at certain dates
[`endogenize_unanticipated`](#endogenize_unanticipated) | Endogenize certain quantities at certain dates
[`exogenize_anticipated`](#exogenize_anticipated) | Exogenize certain quantities at certain dates
[`exogenize_unanticipated`](#exogenize_unanticipated) | Exogenize certain quantities at certain dates as unanticipated


### Defining exogenized and endogenized data points in [`Sequential` simulations](sequential.md#simulate) ###

Function | Description
----------|------------
[`exogenize`](#exogenize) | Exogenize certain LHS quantities at certain dates


### Getting information about simulation plans ###

Function | Description
----------|------------
[`print_table`](#print_table) | Print the `SimulationPlan` as a table


### Getting information about simulation plans for [`Simultaneous` models](simultaneous.md) ###

Function | Description
----------|------------
[`get_endogenized_anticipated_in_period`](#get_endogenized_anticipated_in_period) | Get names endogenized as anticipated in a certain period
[`get_endogenized_unanticipated_in_period`](#get_endogenized_unanticipated_in_period) | Get names endogenized as unanticipated in a certain period
[`get_exogenized_anticipated_in_period`](#get_exogenized_anticipated_in_period) | Get names exogenized as anticipated in a certain period
[`get_exogenized_unanticipated_in_period`](#get_exogenized_unanticipated_in_period) | Get names exogenized as unanticipated in a certain period


### Getting information about simulation plans for [`Sequential` models](sequential.md) ###

Function | Description
----------|------------
[`get_exogenized_in_period`](#get_exogenized_in_period) | Get names exogenized in a certain period



&#9744;&#160;`SimulationPlan`
-------------------------------

==Create new simulation plan object==

    self = SimulationPlan(
        model,
        time_span,
    )


Create a new simulation plan object for a
[`Simultaneous`](sequential_models) or
[`Sequential`](sequential_models) model.

### Input arguments ###

???+ input "model"

    A [`Simultaneous`](sequential_models) or
    [`Sequential`](sequential_models) model that will be simulated.

???+ input "time_span"

    A date range on which the `model` will be simulated.


### Returns ###

???+ returns "self"

    A new empty simulation plan object.
        



&#9744;&#160;`endogenize_anticipated`
---------------------------------------

==Endogenize certain quantities at certain dates==
        



&#9744;&#160;`endogenize_unanticipated`
-----------------------------------------

==Endogenize certain quantities at certain dates==
        



&#9744;&#160;`exogenize`
--------------------------

==Exogenize certain LHS quantities at certain dates==

Exogenize certain LHS quantities at specified dates, setting them as
predetermined values within the simulation of
a [`Sequential` model](sequential.md). This method is used to control how
the model behaves during simulations by fixing certain variables to known
values.

    self.exogenize(
        dates,
        names,
        *,
        transform=None,
        when_data=False,
    )

### Input arguments ###

???+ input "self"
    The simulation plan in which data points will be exogenized.

???+ input "dates"
    A list of dates or `...` to apply to all dates at which the quantities 
    will be exogenized.

???+ input "names"
    A list of names or a single name, or `...` to apply to all names that 
    specifies which quantities to set as predetermined at the specified dates.

???+ input "transform"
    Specifies the transformation to apply to the exogenized quantities. If not
    specified, no transformation is applied. Available transformations include:

    * `None`: Exogenize the LHS variables as they are with no
    transformation.

    * `"log"`: Exogenize the natural logarithm of the LHS variables. Input
    time series needs to be prefixed with `log_`.

    * `"diff"`: Exogenize the first difference of the LHS variables. Input
    time series needs to be prefixed with `diff_`.

    * `"diff_log"`: Exogenize the first difference of the natural logarithm
    of the LHS variables. Input time series needs to be prefixed with
    `diff_log_`.

    * `"roc"`: The gross rate of change of the LHS variables from one
    period to the next. Input time series needs to be prefixed with `roc_`.

    * `"pct"`: The percentage change of the LHS variables from one period
    to the next. Input time series needs to be prefixed with `pct_`.

???+ input "when_data"
    Specifies whether the exogenization should only occur if a valid 
    value exists in the input data.


### Returns ###


???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



&#9744;&#160;`exogenize_anticipated`
--------------------------------------

==Exogenize certain quantities at certain dates==

    self.exogenize_anticipated(
        dates,
        names,
    )


### Input arguments ###


???+ input "dates"

    Dates at which the `names` will be exogenized; use `...` for all simulation dates.

???+ input "names"

    Names of quantities to exogenize at the `dates`; use `...` for all exogenizable quantities.
        



&#9744;&#160;`exogenize_unanticipated`
----------------------------------------

==Exogenize certain quantities at certain dates as unanticipated==

```
self.exogenize_unanticipated(
    dates, names,
    /,
    transform=None,
    when_data=False,
)
```

### Input arguments ###


???+ input "dates"

    Dates at which the `names` will be exogenized; use `...` for all simulation dates.

???+ input "names"

    Names of quantities to exogenize at the `dates`; use `...` for all exogenizable quantities.


### Input arguments available only for `Sequential` models ###

???+ input "transform"

    Transformation (specified as a string) to be applied to the exogenized
    quantities; if `None`, no tranformation is applied.

???+ input "when_data"

    If `True`, the data point will be exogenized only if a proper value
    exists in the input data.
        



&#9744;&#160;`get_endogenized_anticipated_in_period`
------------------------------------------------------

==Get names endogenized as anticipated in a certain period==
        



&#9744;&#160;`get_endogenized_unanticipated_in_period`
--------------------------------------------------------

==Get names endogenized as unanticipated in a certain period==
        



&#9744;&#160;`get_exogenized_anticipated_in_period`
-----------------------------------------------------

==Get names exogenized as anticipated in a certain period==
        



&#9744;&#160;`get_exogenized_in_period`
-----------------------------------------

==Get names exogenized in a certain period==
        



&#9744;&#160;`get_exogenized_unanticipated_in_period`
-------------------------------------------------------

==Get names exogenized as unanticipated in a certain period==
        



&#9744;&#160;`print_table`
----------------------------

==Print the `SimulationPlan` as a table==

    self.print_table()


### Input arguments ###

???+ input "self"
    `SimulationPlan` to be printed on the screen, with one row showing
    exogenized or endogenized data points grouped by the name and dates.


### Returns ###

Returns no value; the table is printed on the screen.
        