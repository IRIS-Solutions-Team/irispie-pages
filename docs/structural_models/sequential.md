
`Sequential` models
====================

`Sequential` models are models where the equations are simulated sequentially,
one data point at a time. The order of execution in simulations is either
period-by-period and equation-by-equation, or vice versa, equation-by-equation
and period-by-period.
    


Categorical list of functions
-------------------------------

### Creating new `Sequential` models ###

Function | Description
----------|------------
[Sequential.from_file](#sequentialfrom_file) | Create new `Sequential` model object from source file or files
[Sequential.from_string](#sequentialfrom_string) | Create sequential model object from string


### Simulating `Sequential` models ###

Function | Description
----------|------------
[simulate](#simulate) | Simulate sequential model


### Manipulating `Sequential` model parameters ###

Function | Description
----------|------------
[assign](#assign) | Assign model parameters


### Information about `Sequential` models ###

Function | Description
----------|------------
[get_description](#get_description) | Get model description text
[set_description](#set_description) | Set model description text


### Manipulating `Sequential` models ###

Function | Description
----------|------------
[copy](#copy) | Create a deep copy
[reorder_equations](#reorder_equations) | Reorder model equations
[sequentialize](#sequentialize) | Reorder the model equations so that they can be solved sequentially





Directly accessible properties
------------------------------

Property | Description
----------|------------
[all_names](#all_names) | Names of all variables occurring in the model in order of appearance
[equation_strings](#equation_strings) | Equation strings in order of appearance
[identity_index](#identity_index) | Indexes of identity equations
[incidence_matrix](#incidence_matrix) | Incidence matrix with equations in rows and LHS quantities in columns
[is_sequential](#is_sequential) | `True` if the model equations are ordered sequentially
[lhs_names](#lhs_names) | Names of LHS variables in order of their equations
[lhs_quantities](#lhs_quantities) | LHS quantities in order of appearance
[max_lag](#max_lag) | Maximum lag occurring on the RHS of equations
[max_lead](#max_lead) | Maximum lead occurring on the RHS of equations
[nonidentity_index](#nonidentity_index) | Indexes of nonidentity equations
[num_equations](#num_equations) | Number of equations
[parameter_names](#parameter_names) | Names of model parameters
[residual_names](#residual_names) | Names of residuals in order of their equations
[rhs_only_names](#rhs_only_names) | Names of variables appearing only on the RHS of equations



☐ `Sequential.from_file`
--------------------------

==Create new `Sequential` model object from source file or files==

```
self = Sequential.from_file(
    file_names,
    /,
    context=None,
    description="",
)
```

Read and parse one or more source files specified by `file_names` (a string
or a list of strings) with model source code, and create a `Sequential`
model object.


### Input arguments ###


???+ input "file_names"
    The name of the model source file from which the `Sequential` model object
    will be created, or a list of file names; if multiple file names are
    specified, they will all combined together in the given order.

???+ input "context"
    Dictionary supplying the values used in [preparsing](preparser.md) commands, and the
    definition of non-standard functions used in the equations.

???+ input "description"
    Description of the model specified as a text string.


### Returns ###


???+ returns "self"
    A new `Sequential` model object created from the `file_names`.
        



☐ `Sequential.from_string`
----------------------------

==Create sequential model object from string==

```
self = Sequential.from_string(
    string,
    /,
    *,
    context=None,
    description="",
)
```

Read and parse a text `string` with a model source code, and create a
`Sequential` model object. Otherwise, this function behaves the same way as
[`Sequential.from_file`](#sequentialfrom_file).


### Input arguments ###

???+ input "string"

    Text string from which the `Sequential` model object will be created.

See [`Sequential.from_file`](#sequentialfrom_file) for other input arguments.



### Returns ###

See [`Sequential.from_file`](sequentialfrom_file) for return values.
        



☐ `assign`
------------

==Assign model parameters==

Assigns parameters to a `Sequential` model. The method can assign parameters
from individual arguments, from a `Databox`, or from a `dict`.


### Assigning individual parameters ###

```
self.assign(
    name_one=value_one,
    name_two=value_two,
    # etc
)
```


### Assigning parameters from a `Databox` or a `dict` ###

```
self.assign(databox, )
```


### Input arguments ###


???+ input "self"
    `Sequential` model whose parameters will be assigned.


???+ input "name_one, name_two, ..."
    Names of the parameters to assign.


???+ input "value_one, value_two, ..."
    Values to assign to `name_one`, `name_two`, etc.


???+ input "databox"
    `Databox` or `dict` from which the parameters will be extracted and
    assigned. Any names in the `Databox` or `dict` that are not model
    parameters will be ignored.


### Returns ###

Returns no value; the method modifies the model in place.
        



☐ `copy`
----------

==Create a deep copy==

```
other = self.copy()
```


### Input arguments ###


???+ input "self"
    A `Sequential` model object to be copied.


### Returns ###


???+ returns "other"
    A deep copy of `self`.
        



☐ `get_description`
---------------------

==Get model description text==

```
description = self.get_description()
```

### Input arguments ###


???+ input "self"

    `Sequential` model object whose description will be returned.


### Returns ###


???+ returns " "

    Description of `self`.
        



☐ `reorder_equations`
-----------------------

==Reorder model equations==

```
self.reorder_equations(new_order, )
```

Reorder the model equations within `self` according to the `new_order` of
equation indexes.


### Input arguments ###


???+ input "self"

    `Sequential` model object whose equations will be reordered.

???+ input "new_order"

    New order of model equations specified as a list of equation indexes
    (integers starting from 0).
        



☐ `sequentialize`
-------------------

==Reorder the model equations so that they can be solved sequentially==

```
eids_reordered = self.sequentialize()
```

Reorder the model equations within `self` so that they can be solved
sequentially. The reordered equation indexes are returned as a tuple.


### Input arguments ###


???+ input "self"

    `Sequential` model object whose equations will be reordered sequentially.


### Returns ###


???+ returns "eids_reordered"

    Tuple of equation indexes (integers starting from 0) specifying the
    new order of equations.
        



☐ `set_description`
---------------------

==Set model description text==

```
self.set_description(description, )
```

...


### Input arguments ###


???+ input "self"

    `Sequential` model object whose description will be set.


???+ input "description"

    New description of `self`.
        



☐ `simulate`
--------------

==Simulate sequential model==

```
output_db, info = self.simulate(
    input_db,
    simulation_span,
    *,
    plan=None,
    execution_order="dates_equations",
    prepend_input=True,
    target_databox=None,
    when_nonfinite="warning",
    num_variants=None,
    remove_initial=True,
    remove_terminal=True,
)
```

Simulate a `Sequential` model, `self`, on a time `span`, period by period,
equation by equation. The `simulate` function does not reorder the
equations; if needed, this must be done by running `reorder` before
simulating the model.


### Input arguments ###


???+ input "self"
    `Sequential` model that will be simulated.

???+ input "input_db"
    Input databox (a `Databox` object) with all the necessary initial
    conditions (initial lags) for the LHS variables, and all the values for
    the RHS variables needed to simulate `self` on the time `span`.

???+ input "plan"
    `PlanSimulate` object with a simulation plan, i.e. information about
    which LHS variables to exogenize at which dates. If `plan=None`, no
    simulation plan is imposed on the simulation.

???+ input "simulation_span"
    [Time span](../data_management/spans.md) for the simulation; the time
    span needs to go forward and have a one-period step.

???+ input "plan"
    [Simulation plan](plans.md) for the simulation specifying the
    exogenized data points. If `None`, no simulation plan is imposed.

???+ input "prepend_input"
    If `True`, the input time series observations are prepended to the results.

???+ input "target_databox"
    Custom databox to which the simulated time series will be added. If
    `None`, a new databox is created.

???+ input "when_nonfinite"
    Action to take when a simulated data point is non-finite (`nan` or `inf` or `-inf`). The options are

    * `"error"`: raise an error,
    * `"warning"`: log a warning,
    * `"silent"`: do nothing.

???+ input "execution_order"
    Order in which the model equations and simulation periods are executed. The options are

    * `"dates_equations"`: all equations for the first period, all equations for the second period, …
    * `"equations_dates"`: all periods for the first equation, all periods for the second equation, …

???+ input "num_variants"
    Number of variants to simulate. If `None`, the number of variants is
    determined by the number of variants in the `self` model.

???+ input "remove_initial"
    If `True`, remove the initial condition data, i.e. all lags before the
    start of the simulation span.

???+ input "remove_terminal"
    If `True`, remove the terminal condition data, i.e. all leads after the
    end of the simulation span.


### Returns ###


???+ returns "output_db"

    Output databox with the simulated time series for the LHS variables.

???+ returns "info"

    Information about the simulation; `info` is a dict with the following
    items.
        