
Simulation plans
=================

`PlanSimulate` objects are used to set up conditioning assumptions
for simulating [`Simultaneous`](simultaneous_modelsd) or
[`Sequential`](sequential_models) models. The simulation plans specify

* what variables to exogenize in what periods
* what shocks to endogenized in what periods (`Simultaneous` models only)

The plans only contain meta information, not the actual data points for the
exogenized variables. The actual data points are included in the input databox.
    


Categorical list of functions
-------------------------------

### Creating new simulation plans ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;PlanSimulate](#plansimulate) | Create new simulation plan object


### Defining exogenized and endogenized data points ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;endogenize](#endogenize) | Endogenize certain quantities at certain dates
[:octicons-file-24:&nbsp;exogenize](#exogenize) | Exogenize certain quantities at certain dates


### Getting information about simulation plans ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;get_names_endogenized_in_period](#get_names_endogenized_in_period) | Get names endogenized at a certain date
[:octicons-file-24:&nbsp;get_names_exogenized_in_period](#get_names_exogenized_in_period) | Get names exogenized at a certain date





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:&nbsp;end_date](#end_date) | End date of the simulation span
[:octicons-package-24:&nbsp;frequency](#frequency) | Date frequency of the simulation span
[:octicons-package-24:&nbsp;num_periods](#num_periods) | Number of periods in the simulation span
[:octicons-package-24:&nbsp;start_date](#start_date) | Start date of the simulation span



☐ `PlanSimulate`
------------------

==Create new simulation plan object==

```
self = PlanSimulate(model, time_span, )
```

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
        



☐ `endogenize`
----------------

==Endogenize certain quantities at certain dates==
        



☐ `exogenize`
---------------

==Exogenize certain quantities at certain dates==

```
self.exogenize(
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
        



☐ `get_names_endogenized_in_period`
-------------------------------------

==Get names endogenized at a certain date==
        



☐ `get_names_exogenized_in_period`
------------------------------------

==Get names exogenized at a certain date==
        