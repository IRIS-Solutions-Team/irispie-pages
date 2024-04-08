
`Simultaneous` models
======================
    


Categorical list of functions
-------------------------------

### Creating new simultaneous models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;Simultaneous.from_file](#simultaneousfrom_file) | Create `Simultaneous` model object from source file or files
[:octicons-file-24:&nbsp;Simultaneous.from_string](#simultaneousfrom_string) | Create `Simultaneous` model from string


### Applying structural filters on models ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;kalman_filter](#kalman_filter) | Run Kalman filter on a model using time series data





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:&nbsp;is_deterministic](#is_deterministic) | True for models declared as deterministic
[:octicons-package-24:&nbsp;is_flat](#is_flat) | True for models declared as flat
[:octicons-package-24:&nbsp;is_linear](#is_linear) | True for models declared as linear
[:octicons-package-24:&nbsp;max_lag](#max_lag) | Maximul lag in the model (negative or zero)
[:octicons-package-24:&nbsp;max_lead](#max_lead) | Maximul lead in the model (positive or zero)
[:octicons-package-24:&nbsp;num_measurement_equations](#num_measurement_equations) | Number of measurement equations
[:octicons-package-24:&nbsp;num_transition_equations](#num_transition_equations) | Number of transition equations



☐ `Simultaneous.from_file`
----------------------------

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
        



☐ `Simultaneous.from_string`
------------------------------

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
        



☐ `kalman_filter`
-------------------

==Run Kalman filter on a model using time series data==

Executes a Kalman filter on a model, compliant with `KalmanFilterableProtocol`, 
using time series observations from the input Databox. This method enables state 
estimation and uncertainty quantification in line with the model's dynamics and 
the time series data.

    kalman_output, output_info = self.kalman_filter(
        input_db, 
        span, 
        diffuse_factor=None, 
        return_=("predict", "update", "smooth"),
        return_predict=True, 
        return_update=True, 
        return_smooth=True, 
        rescale_variance=False,
        shocks_from_data=False, 
        stds_from_data=False, 
        prepend_initial=False,
        append_terminal=False, 
        unpack_singleton=True
    )


### Input arguments ###


???+ input "self"
    The model, compliant with `KalmanFilterableProtocol`, performing the 
    Kalman filtering.

???+ input "input_db"
    A Databox containing time series data to be used for filtering.

???+ input "span"
    A date span over which the filtering process is executed based on the
    measurement time series.

???+ input "diffuse_factor"
    A real number or `None`, specifying the scale factor for the diffuse
    initialization. If `None`, the default value is used.

???+ input "return_"
    An iterable of strings indicating which steps' results to return: 
    "predict", "update", "smooth".

???+ input "return_predict"
    If `True`, return prediction step results.

???+ input "return_update"
    If `True`, return update step results.

???+ input "return_smooth"
    If `True`, return smoothing step results.

???+ input "rescale_variance"
    If `True`, rescale all variances by the optimal variance scale factor
    estimated using maximum likelihood after the filtering process.

???+ input "shocks_from_data"
    If `True`, use possibly time-varying shock values from the data; these
    values are interpreted as the medians (means) of the shocks. If `False`,
    zeros are used for all shocks.

???+ input "stds_from_data"
    If `True`, use possibly time-varying standard deviation values from the
    data. If `False`, currently assigned constant values are used for the
    standard deviations of all shocks.

???+ input "prepend_initial"
    If `True`, prepend observations to the resulting time series to cover
    initial conditions based on the model's maximum lag. No measurement
    observations are used in these initial time periods (even if some are
    available in the input data).

???+ input "append_terminal"
    If `True`, append observations to the resulting time series to cover
    terminal conditions based on the model's maximum lead. No measurement
    observations are used in these terminal time periods (even if some are
    available in the input data).

???+ input "unpack_singleton"
    If `True`, unpack `output_info` into a plain dictionary for models with a
    single variant.


### Returns ###


???+ returns "kalman_output"
    An object containing the following attributes, each being a Databox:

    | Attribute                  | Description
    |----------------------------|---------------------------------------------------
    | `predict_med`              | Medians from the prediction step.
    | `predict_std`              | Standard deviations from the prediction step.
    | `predict_mse_measurement`  | Mean squared error matrices from the prediction step.
    | `update_med`               | Medians from the update step.
    | `update_std`               | Standard deviations from the update step.
    | `predict_err`              | Prediction errors.
    | `smooth_med`               | Medians from the smoothing step.
    | `smooth_std`               | Standard deviations from the smoothing step.

    Some of these attributes may be `None` if the corresponding step was not
    requested in `return_`.

???+ returns "output_info"
    A dictionary containing additional information about the filtering process,
    such as log likelihood and variance scale. For models with multiple
    variants, `output_info` is a list of such dictionaries. If
    `unpack_singleton=False`, also `output_info` is a one-element list
    containing the dictionary for singleton models, too.
        