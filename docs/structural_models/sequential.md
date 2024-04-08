
`Sequential` models
====================
    


Categorical list of functions
-------------------------------

### Creating new `Sequential` models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;Sequential.from_file](#sequentialfrom_file) | Create new `Sequential` model object from source file or files
[:octicons-file-24:&nbsp;Sequential.from_string](#sequentialfrom_string) | Create sequential model object from string


### Simulating `Sequential` models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;simulate](#simulate) | Simulate sequential model


### Manipulating `Sequential` model parameters ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;assign](#assign) | Assign model parameters


### Information about `Sequential` models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;get_description](#get_description) | Get model description text
[:octicons-file-24:&nbsp;set_description](#set_description) | Set model description text


### Manipulating `Sequential` models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;copy](#copy) | Create a deep copy
[:octicons-file-24:&nbsp;reorder_equations](#reorder_equations) | Reorder model equations
[:octicons-file-24:&nbsp;sequentialize](#sequentialize) | Reorder the model equations so that they can be solved sequentially





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:&nbsp;all_names](#all_names) | Names of all variables occurring in the model in order of appearance
[:octicons-package-24:&nbsp;equation_strings](#equation_strings) | Equation strings in order of appearance
[:octicons-package-24:&nbsp;identity_index](#identity_index) | Indexes of identity equations
[:octicons-package-24:&nbsp;incidence_matrix](#incidence_matrix) | Incidence matrix with equations in rows and LHS quantities in columns
[:octicons-package-24:&nbsp;is_sequential](#is_sequential) | `True` if the model equations are ordered sequentially
[:octicons-package-24:&nbsp;lhs_names](#lhs_names) | Names of LHS variables in order of their equations
[:octicons-package-24:&nbsp;lhs_quantities](#lhs_quantities) | LHS quantities in order of appearance
[:octicons-package-24:&nbsp;max_lag](#max_lag) | Maximum lag occurring on the RHS of equations
[:octicons-package-24:&nbsp;max_lead](#max_lead) | Maximum lead occurring on the RHS of equations
[:octicons-package-24:&nbsp;nonidentity_index](#nonidentity_index) | Indexes of nonidentity equations
[:octicons-package-24:&nbsp;num_equations](#num_equations) | Number of equations
[:octicons-package-24:&nbsp;parameter_names](#parameter_names) | Names of model parameters
[:octicons-package-24:&nbsp;residual_names](#residual_names) | Names of residuals in order of their equations
[:octicons-package-24:&nbsp;rhs_only_names](#rhs_only_names) | Names of variables appearing only on the RHS of equations



☐ `Sequential.from_file`
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
    Dictionary supplying the values used in preparsing commands, and the
    definition of non-standard functions used in the equations.

???+ input "description"
    Description of the model specified as a text string.


### Returns ###


???+ returns "self"
    A new `Sequential` model object created from the `file_names`.
        



☐ `Sequential.from_string`
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
        



☐ `assign`
------------

==Assign model parameters==

```
self.assign(
    name_one=value_one,
    name_two=value_two,
    # etc
)
```

```
self.assign(databox, )
```

...


### Input arguments ###


???+ input "self"

    `Sequential` model whose parameters will be assigned.


???+ input "name_one"

    Name of a parameter to assign.


???+ input "value_one"

    Value to assign to `name_one`.

etc...

???+ input "databox"

    `Databox` or `dict` from which the parameters will be extracted and
    assigned.
        



☐ `copy`
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
        



☐ `get_description`
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
        



☐ `reorder_equations`
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
        



☐ `sequentialize`
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
        



☐ `set_description`
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
        



☐ `simulate`
--------------

==Simulate sequential model==

```
output_db, info = self.simulate(
    input_db, span,
    /,
    prepend_input=True,
    plan=None,
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


### Returns ###

???+ returns "output_db"

    Output databox with the simulated time series for the LHS variables.

???+ returns "info"

    Information about the simulation; `info` is a dict with the following
    items.
        