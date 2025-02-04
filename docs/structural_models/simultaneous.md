
`Simultaneous` models
======================
    


Categorical list of functions
-------------------------------

### Creating new Simultaneous models ###

Function | Description
----------|------------
[`Simultaneous.from_file`](#simultaneousfrom_file) | Create `Simultaneous` model object from source file or files
[`Simultaneous.from_string`](#simultaneousfrom_string) | Create `Simultaneous` model from string


### Getting information about Simultaneous models ###

Function | Description
----------|------------


### Applying structural filters on Simultaneous models ###

Function | Description
----------|------------
[`kalman_filter`](#kalman_filter) | Run Kalman filter on a model using time series data
[`neg_log_likelihood`](#neg_log_likelihood) | 


### Manipulating Simultaneous model parameters ###

Function | Description
----------|------------
[`rescale_stds`](#rescale_stds) | Rescale the standard deviations of model shocks





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



&#9744;&#160;`Simultaneous.from_file`
---------------------------------------

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
        



&#9744;&#160;`Simultaneous.from_string`
-----------------------------------------

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
        



&#9744;&#160;`kalman_filter`
------------------------------

==Run Kalman filter on a model using time series data==

Executes a Kalman filter on a model, compliant with `KalmanFilterableProtocol`,
using time series observations from the input Databox. This method enables state
estimation and uncertainty quantification in line with the model's dynamics and
the time series data.

    kalman_output = self.kalman_filter(
        input_db,
        span,
        diffuse_scale=None,
        return_=("predict", "update", "smooth", "predict_err", "predict_mse_obs", ),
        return_predict=True,
        return_update=True,
        return_smooth=True,
        return_predict_err=True,
        return_predict_mse_obs=True,
        rescale_variance=False,
        likelihood_contributions=True,
        shocks_from_data=False,
        stds_from_data=False,
        prepend_initial=False,
        append_terminal=False,
        deviation=False,
        check_singularity=False,
        unpack_singleton=True,
        return_info=False,
    )

    kalman_output, info = self.kalman_filter(
        ...
        return_info=True,
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

???+ input "diffuse_scale"
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

???+ input "likelihood_contributions"
    If `True`, return the contributions of individual periods to the overall
    (negative) log likelihood.

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

???+ input "deviation"
    If `True`, the constant vectors in transition and measurement equations are
    set to zeros, effectively running the Kalman filter as deviations from
    steady state (a balanced-growth path)

???+ input "check_singularity"
    If `True`, check the one-step ahead MSE matrix for the measurement variables
    for singularity, and throw a `SingularMatrixError` exception if the matrix
    is singular.

???+ input "unpack_singleton"
    If `True`, unpack `out_info` into a plain dictionary for models with a
    single variant.

???+ input "return_info"
    If `True`, return additional information about the Kalman filtering process.


### Returns ###


???+ returns "kalman_output"
    A Databox containing some of the following items (depending on the user requests):

    | Attribute         | Type       | Description
    |-------------------|---------------------------------------------------
    | `predict_med`     | `Databox`  | Medians from the prediction step
    | `predict_std`     | `Databox`  | Standard deviations from the prediction step
    | `predict_mse_obs` | `list`     | Mean squared error matrices for the prediction step of the available observations of measurement variables
    | `update_med`      | `Databox`  | Medians from the update step
    | `update_std`      | `Databox`  | Standard deviations from the update step
    | `predict_err`     | `Databox`  | Prediction errors
    | `smooth_med`      | `Databox`  | Medians from the smoothing step
    | `smooth_std`      | `Databox`  | Standard deviations from the smoothing step


???+ returns "out_info"
    A dictionary containing additional information about the filtering process,
    such as log likelihood and variance scale. For models with multiple
    variants, `out_info` is a list of such dictionaries. If
    `unpack_singleton=False`, also `out_info` is a one-element list
    containing the dictionary for singleton models, too.
        



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
        