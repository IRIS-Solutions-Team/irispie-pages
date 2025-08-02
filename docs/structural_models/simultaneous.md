
`Simultaneous` models
======================

    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`is_deterministic` | True for models declared as deterministic
`is_flat` | True for models declared as flat
`is_linear` | True for models declared as linear
`max_lag` | Maximul lag in the model (negative or zero)
`max_lead` | Maximul lead in the model (positive or zero)
`num_measurement_equations` | Number of measurement equations
`num_transition_equations` | Number of transition equations





Categorical list of functions
-------------------------------

### Creating new Simultaneous models ###

Function | Description
----------|------------
[`from_portable`](#from_portable) | Create `Simultaneous` model from portable dictionary
[`from_portable_file`](#from_portable_file) | Read a `Simultaneous` object from a portable JSON file
[`Simultaneous.from_file`](#simultaneousfrom_file) | Create `Simultaneous` model object from source file or files
[`Simultaneous.from_string`](#simultaneousfrom_string) | Create `Simultaneous` model from string


### Getting information about Simultaneous models ###

Function | Description
----------|------------
[`get_equations`](#get_equations) | Get the model equations
[`get_steady_changes`](#get_steady_changes) | Get steady-state changes of variables
[`get_steady_levels`](#get_steady_levels) | Get steady-state levels of variables


### Applying structural filters on Simultaneous models ###

Function | Description
----------|------------
[`kalman_filter`](#kalman_filter) | 
[`neg_log_likelihood`](#neg_log_likelihood) | 


### Manipulating Simultaneous model parameters ###

Function | Description
----------|------------
[`rescale_stds`](#rescale_stds) | Rescale the standard deviations of model shocks


### Serializing, saving and loading Simultaneous models ###

Function | Description
----------|------------
[`to_portable`](#to_portable) | Serialize `Simultaneous` model to portable dictionary
[`to_portable_file`](#to_portable_file) | Write a `Simultaneous` object to a portable JSON file



&#9744;&#160;`from_portable`
------------------------------

==Create `Simultaneous` model from portable dictionary==

Create a `Simultaneous` model object from a portable dictionary. See
`Simultaneous.to_portable` for details on the structure of the portable
dictionary.

```
self = Simultaneous.from_portable(portable)
```


### Input arguments ###

???+ input "portable"
    A dictionary with the structure described in the documentation of
    `Simultaneous.to_portable`.


### Returns ###

???+ returns "self"
    A new `Simultaneous` model object created from the portable dictionary.
        



&#9744;&#160;`from_portable_file`
-----------------------------------

==Read a `Simultaneous` object from a portable JSON file==

Read a JSON file and convert the contents to a `Simultaneous` object. See
[`Simultaneous.from_portable`](#from_portable) for details on the conversion
from a portable dictionary.

```
self = Simultaneous.from_portable_file(
    file_name,
    json_settings=None,
)
```


### Input arguments ###

???+ input "file_name"
    Filename from which to read the JSON file.

???+ input "json_settings"
    Optional settings to pass to `json.load`.


### Returns ###

???+ returns "self"
    A new `Simultaneous` object created from the contents of the JSON file.

        



&#9744;&#160;`Simultaneous.from_file`
---------------------------------------

==Create `Simultaneous` model object from source file or files==

Read and parse one or more source files specified by `file_names` (a string
or a list of strings) with model source code, and create a `Simultaneous`
model object.

```
self = Simultaneous.from_file(
    file_names,
    #
    context=None,
    description="",
)
```


### Input arguments ###

???+ input "file_names"
    The name of the model source file from which the `Simultaneous` model object
    will be created, or a list of file names; if multiple file names are
    specified, they will all combined together in the given order.

???+ input "context"
    Dictionary supplying the values used in preparsing commands, and the
    definition of non-standard functions used in the equations.

???+ input "description"
    Desscription of the model specified as a text string.


### Returns ###

???+ returns "self"
    `Simultaneous` model object created from the `file_names`.
        



&#9744;&#160;`Simultaneous.from_string`
-----------------------------------------

==Create `Simultaneous` model from string==

Read and parse a text `string` with a model source code, and create a
`Simultaneous` model object. Otherwise, this function behaves the same way as
[`Simultaneous.from_file`](#simultaneousfrom_file).

```
self = Simultaneous.from_string(
    string,
    #
    context=None,
    description="",
)
```


### Input arguments ###


???+ input "string"

    Text string from which the `Simultaneous` model object will be created.

See [`Simultaneous.from_file`](#simultaneousfrom_file) for other input arguments.


### Returns ###

See [`Simultaneous.from_file`](simultaneousfrom_file) for return values.
        



&#9744;&#160;`get_equations`
------------------------------

==Get the model equations==

    equations = self.get_equations(
        kind=None,
    )


### Input arguments ###

???+ input "self"
    A `Simultaneous` model object.

???+ input "kind"
    The kind of equations to retrieve. If `None`, all equations are returned.


### Returns ###

???+ returns "equations"
    A tuple of strings representing the equations of the model, with dynamic
    and steady equations concatenated using "!!" if they differ.
        



&#9744;&#160;`get_steady_changes`
-----------------------------------

==Get steady-state changes of variables==

    steady_changes = self.get_steady_changes(
        *,
        round: int = None,
        unpack_singleton: bool = True,
        output_typ: type = Databox,
    )


### Input arguments ###


???+ input "self"
    `Simultaneous` model object with a valid first-order solution.

???+ input "round"
    Number of decimal places to round the output values.

???+ input "unpack_singleton"
    If `True`, unpack singleton lists and return the single element. If
    `False`, return the list as is.

???+ input "output_type"
    Cast output as this type; the constructor for this type must accept a
    dictionary.


### Returns ###


???+ returns "steady_changes"
    Databox with the steady-state changes for each variable, i.e. first
    differences or gross rates of change depending on the log status of
    each variable.
        



&#9744;&#160;`get_steady_levels`
----------------------------------

==Get steady-state levels of variables==

    steady_levels = self.get_steady_levels(
        *,
        round: int = None,
        unpack_singleton: bool = True,
        output_typ: type = Databox,
    )


### Input arguments ###


???+ input "self"
    `Simultaneous` model object with a valid first-order solution.

???+ input "round"
    Number of decimal places to round the output values.

???+ input "unpack_singleton"
    If `True`, unpack singleton lists and return the single element. If
    `False`, return the list as is.

???+ input "output_type"
    Cast output as this type; the constructor for this type must accept a
    dictionary.


### Returns ###


???+ returns "steady_levels"
    Databox with the steady-state levels for each variable.
        



&#9744;&#160;`kalman_filter`
------------------------------

        



&#9744;&#160;`neg_log_likelihood`
-----------------------------------

        



&#9744;&#160;`rescale_stds`
-----------------------------

==Rescale the standard deviations of model shocks==

Adjust the standard deviations of the model shocks by a specified factor. 
This method allows scaling the standard deviations for the shocks in the 
model based on the provided factor.

    self.rescale_stds(
        factor,
        kind=None,
    )


### Input arguments ###


???+ input "factor"
    A real non-negative number by which to scale the standard deviations of the
    model shocks. This value is used to multiply the existing standard
    deviations.

???+ input "kind"
    An optional parameter to narrow down the types of shocks to rescale. It
    can be one, or a combination, of the following:

    * `ir.UNANTICIPATED_STD`
    * `ir.ANTICIPATED_STD`
    * `ir.MEASUREMENT_STD`

    If `None`, the standard deviations of all shocks will be rescaled.


### Returns ###


???+ returns "None"
    This method does not return any value but modifies the standard deviations 
    of model shocks in-place, rescaling them.
        



&#9744;&#160;`to_portable`
----------------------------

==Serialize `Simultaneous` model to portable dictionary==

Convert a `Simultaneous` model object to a dictionary of primitive values that
can be saved to a JSON file or transmitted over the network. The structure of
the portable dictionary is described below.

```
portable = self.to_portable()
```


### Input arguments ###

???+ input "self"
    `Simultaneous` model object to be serialized.


### Returns ###

???+ returns "portable"
    A JSON-serializable dictionary with the structure described below.


### Details ###


???+ abstract "Structure of the portable dictionary, format 0.3.0:"

    The portable dictionary has the following structure:

    ```
        {
            "portable_format": "0.3.0",
            "source": {
                "description": <str>,
                "flags": {
                    "is_linear: <bool>,
                    "is_flat": <bool>,
                    "is_deterministic": <bool>
                },
                "quantities": [ <QUANTITY>, ... ],
                "equations": [ <EQUATION>, ... ],
                "context": {},
            "variants": [ <VARIANT>, ... ],
        }
    ```

    The meaning of the `flags` is as follows:

    * `is_linear` is `True` if the model has been created with the
    `linear=True`, and the calculation of first-order solution matrices is
    expected to be independent of the model steady state. * `is_flat` is `True`

    * `is_flat` is `True` if the model has been created with the `flat=True`,
    and the calculation of the model steady state is done assuming that no model
    variable is growing over time in steady state.

    * `is_deterministic` is `True` if the model has been created with the
    `deterministic=True`, and the model is expected to have no stochastic
    shocks; all shocks are assumed to be deterministic add-factors, and there
    are no `std` parameter created.

    The `quantities` is a list of quantities, with each `<QUANTITY>` described
    as a five-element tuple:

    ```
    [ <KIND>, <NAME>, <LOGLY>, <DESCRIPTION>, <ATTRIBUTES> ]
    ```

    where

    * `<KIND>` is a string representing the kind of the quantity,

    * `<NAME>` is a string with the name of the quantity,

    * `<LOGLY>` is a boolean or `None` indicating whether the quantity is
    declared as a log variable `None` if irrelevant for the respective kind of variables),

    * `<DESCRIPTION>` is a string with the description of the quantity,

    * `<ATTRIBUTES>` is a string containing all attributes separated by a white space.


    The kinds of variables are coded as follows:

    | Kind of variable | Code |
    |-------------------|------|
    | Transition variable | `#x` |
    | Measurement variable | `#y` |
    | Unanticipated shock | `#u` |
    | Anticipated shock | `#v` |
    | Measurement shock | `#w` |
    | Parameter | `#p` |
    | Exogenous variable | `#z` |


    The `equations` is a list of equations, with each `<EQUATION>` described as
    a five-tuple:

    ```
    [ <KIND>, <DYNAMIC>, <STEADY>, <DESCRIPTION>, <ATTRIBUTES> ]
    ```

    where
    * `<KIND>` is a string representing the kind of the equation,

    * `<DYNAMIC>` is a string with the dynamic variant of the equation,

    * `<STEADY>` is a string with the steady-state variant of the equation,

    * `<DESCRIPTION>` is a string with the description of the equation,

    * `<ATTRIBUTES>` is a string containing all attributes separated by a white space.


    The kinds of equations are coded as follows:

    | Kind of equation | Code |
    |-------------------|------|
    | Transition equation | `#T` |
    | Measurement equation | `#M` |
    | Steady autovalues | `#A` |


    The `variants` is a list of parameter (and steady-state) variants, with each
    `<VARIANT>` being a dictionary with its keys corresponding to the names of
    the model quantities (including `std_` names for the standard deviations of
    shocks), and the values being two-tuples consisting of the level and the
    changes of the respective quantity; the change is `None` whenever irrelevant
    for the respective kind of quantity.
        



&#9744;&#160;`to_portable_file`
---------------------------------

==Write a `Simultaneous` object to a portable JSON file==

Convert the `Simultaneous` object to a portable dictionary and write it to a
JSON file. See [`Simultaneous.to_portable`](#to_portable) for details on the
conversion to a portable dictionary.


```
self.to_portable_file(
    file_name,
    json_settings=None,
)
```


### Input arguments ###

???+ input "file_name"
    Filename under which to save the JSON file.

???+ input "json_settings"
    Optional settings to pass to `json.dump`.


### Returns ###

The method returns `None`.
        