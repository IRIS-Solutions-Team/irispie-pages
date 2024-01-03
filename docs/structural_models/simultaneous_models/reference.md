
`Simultaneous` model objects
==============================
    


Categorical list of functions
-------------------------------

### Creating new simultaneous models ###

Function | Description
----------|------------
[:octicons-file-24:`Simultaneous.from_file`](#simultaneousfrom_file) | Create `Simultaneous` model object from source file or files
[:octicons-file-24:`Simultaneous.from_string`](#simultaneousfrom_string) | Create `Simultaneous` model from string





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:`is_deterministic`](#is_deterministic) | True for models declared as deterministic
[:octicons-package-24:`is_flat`](#is_flat) | True for models declared as flat
[:octicons-package-24:`is_linear`](#is_linear) | True for models declared as linear
[:octicons-package-24:`num_measurement_equations`](#num_measurement_equations) | Number of measurement equations
[:octicons-package-24:`num_transition_equations`](#num_transition_equations) | Number of transition equations




---

&#9744;&nbsp;`Simultaneous.from_file`
----------------------------------


==Create `Simultaneous` model object from source file or files==

```
self = Simultaneous.from_file(
    file_names,
    /,
    context=None,
    description="",
)
```

Read and parse one or more source files specified by `file_names` (a string
or a list of strings) with model source code, and create a `Simultaneous`
model object.


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
        




---

&#9744;&nbsp;`Simultaneous.from_string`
----------------------------------


==Create `Simultaneous` model from string==

```
self = Simultaneous.from_string(
    string,
    /,
    context=None,
    description="",
)
```

Read and parse a text `string` with a model source code, and create a
`Simultaneous` model object. Otherwise, this function behaves the same way as
[`Simultaneous.from_file`](#simultaneousfrom_file).


### Input arguments ###


???+ input "string"

    Text string from which the `Simultaneous` model object will be created.

See [`Simultaneous.from_file`](#simultaneousfrom_file) for other input arguments.


### Returns ###

See [`Simultaneous.from_file`](simultaneousfrom_file) for return values.
        