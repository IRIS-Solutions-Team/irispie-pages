
Time series
============

The `Series` objects represent numerical time series, organized as rows of
observations stored in NumPy arrays and [date](dates.md)
stamped. A `Series` object can hold multiple
variants of the data, stored as mutliple columns.
    


Categorical list of functions
-------------------------------

### Creating new time series ###

Function | Description
----------|------------
[:octicons-file-24:`Series`](#series) | Create a new `Series` object


### Converting time series frequency ###

Function | Description
----------|------------
[:octicons-file-24:`aggregate`](#aggregate) | Aggregate  time series to a lower frequency
[:octicons-file-24:`disaggregate`](#disaggregate) | Disaggregate  time series to a higher frequency


### Calculating univariate time series filters ###

Function | Description
----------|------------
[:octicons-file-24:`hpf`](#hpf) | Constrained Hodrick-Prescott filter
[:octicons-file-24:`mov_*`](#mov_*) | Moving functions
[:octicons-file-24:`x13`](#x13) | Interface to X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:`start_date`](#start_date) | Start date of the time series
[:octicons-package-24:`dates`](#dates) | N-tuple with the dates from the start date to the end date of the time series
[:octicons-package-24:`end_date`](#end_date) | End date of the time series
[:octicons-package-24:`frequency`](#frequency) | Date frequency of the time series
[:octicons-package-24:`from_to`](#from_to) | Two-tuple with the start date and end date of the time series
[:octicons-package-24:`num_periods`](#num_periods) | Number of periods from the first to the last observation
[:octicons-package-24:`num_variants`](#num_variants) | Number of variants (columns) within the `Series` object
[:octicons-package-24:`span`](#span) | Time span of the time series
[:octicons-package-24:`shape`](#shape) | Shape of time series data




---

&#9744;&nbsp;`Series`
----------------------------------


==Create a new `Series` object==

```
self = Series(
    start_date=start_date,
    values=values,
)
```

```
self = Series(
    dates=dates,
    values=values,
)
```

### Input arguments ###


???+ input "start_date"

    The date of the first value in the `values`.

???+ input "values"

    Time series observations, supplied either as a tuple of values, or a
    NumPy array.

### Returns ###

???+ returns "self"

    The newly created `Series` object.
        




---

&#9744;&nbsp;`aggregate`
----------------------------------


==Aggregate  time series to a lower frequency==


### Changing time series in-place ###

    self.aggregate(
        target_freq,
        /,
        method="mean",
        remove_missing=False,
        select=None,
        )


### Creating new time series ###

    new_series = aggregate(self, ...)


### Input arguments ###


???+ input "target_freq"
    The new frequency to which the original time series will be diaggregated.

???+ input "method"
    Aggregation method, i.e. a function applied to the high-frequency
    values within each low-frequency period:

    * "mean" - the arithmetic average of high-frequency values
    * "sum" - the sum of high-frequency values
    * "first" - the value in the first high-frequency period
    * "last" - the value in the last high-frequency period
    * "min" - the minimum of high-frequency values
    * "max" - the maximum of high-frequency values

???+ input "remove_missing"
    Remove missing values from the high-frequency data before
    applying the aggregation `method`.

???+ input "select"
    Select only the high-frequency values at the specified indexes;
    `select=None` means all values are used.
        




---

&#9744;&nbsp;`disaggregate`
----------------------------------


==Disaggregate  time series to a higher frequency==


### Changing time series in-place ###

    self.disaggregate(
        target_freq,
        /,
        method="flat",
        model=
        )


### Creating new time series ###

    new_series = disaggregate(self, ...)


### Input arguments ###


???+ input "target_freq"
    The new frequency to which the original time series will be aggregated.

???+ input "method"
    Aggregation method, i.e. a function applied to the high-frequency
    values within each low-frequency period:

    * "mean" - the arithmetic average of high-frequency values
    * "sum" - the sum of high-frequency values
    * "first" - the value in the first high-frequency period
    * "last" - the value in the last high-frequency period
    * "min" - the minimum of high-frequency values
    * "max" - the maximum of high-frequency values

???+ input "remove_missing"
    Remove missing values from the high-frequency data before
    applying the aggregation `method`.

???+ input "select"
    Select only the high-frequency values at the specified indexes;
    `select=None` means all values are used.
        




---

&#9744;&nbsp;`hpf`
----------------------------------


==Constrained Hodrick-Prescott filter==


### Function for creating new Series objects ###


```
trend, gap = irispie.hpf(
    self,
    span=None,
    smooth=None,
    log=False,
    level=None,
    change=None,
)
```


### Methods for changing the existing Series object in-place ###


```
self.hpf_trend(
    span=None,
    smooth=None,
    log=False,
    level=None,
    change=None,
)
```

```
self.hpf_gap(
    span=None,
    smooth=None,
    log=False,
    level=None,
    change=None,
)
```


### Input arguments ###


???+ input "self"
    A `Series` object with the time series data to be filtered. All the
    observations contained in the input time series are used in the
    Hodrick-Prescott filter calculations no matter the time `span`
    specified; the time `span` only determines the time span of the output
    series.

???+ input "span"
    Time span on which the trend component of the Hodrick-Prescott filter
    is calculated. If `span=None`, the results are calculated on
    the time span of the original series, `self`.

???+ input "smooth"
    Smoothing parameter (aka $\lambda$) for the Hodrick-Prescott filter. If `smooth=None`,
    a default value is used based on the frequency of the input series `self`:

    | Date frequency | Default $\lambda$ |
    |----------------|------------------:|
    | Yearly         |               100 |
    | Half-yearly    |               400 |
    | Quarterly      |             1,600 |
    | Monthly        |           144,000 |
    | Otherwise      |             1,600 |

???+ input "log"
    If `log=True`, the Hodrick-Prescott filter is calculated on the logarithm
    of the input data, and the results are delogarithmized back to the original
    scale.

???+ input "level"
    A `Series` object with the level constraints for the Hodrick-Prescott
    filter (aka judgmental adjustments). If `level=None`, no level
    constraints are imposed. If `log=True`, the level constraints are
    logarithmized first before entering the calculations.

???+ input "change"
    A `Series` object with the change constraints for the Hodrick-Prescott
    filter (aka judgmental adjustments). If `change=None`, no change
    constraints are imposed. If `log=True`, the change constraints are
    logarithmized first before entering the calculations; this effectively
    means that for `log=True`, the `change` constraints need to be
    expressed as gross rates of change (period on period).


### Returns ###


???+ returns "trend"
    A new `Series` object with the trend component of the Hodrick-Prescott
    filter. The trend component is always returned on the time `span`
    specified.

???+ returns "gap"
    A new `Series` object with the trend component of the Hodrick-Prescott
    filter. The gap component is calculated on the time `span` as the
    difference between the actual observations and the trend component.

???+ returns "self"
    The existing `Series` object with its values replaced in-place by the trend
    component of the Hodrick-Prescott filter.


### Details ###

??? abstract "Math description"
    The constrained Hodrick-Prescott filter is a method for separating a time series into a
    lower-frequency (trend) component and a higher-frequency (cyclical)
    component subject to level and/or change constraints. The filter is
    implemented as the following constrained dynamic optimization problem

    $$
    \begin{gathered}
    \min\nolimits_{\{\overline{y}_t\}} \sum_{t\in\Omega}
        \lambda \, \left( y_t - \overline{y}_t \right)^2
        + \sum_{t=3}^{T} \left( \Delta \overline{y}_t - \Delta \overline{y}_{t-1} \right)^2 \\[10pt]
    \text{subject to} \\[10pt]
    \overline{y}_t = L_t \qquad \forall t \in \Omega_L \\[10pt]
    \Delta \overline{y}_t = C_t \qquad \forall t \in \Omega_C
    \end{gathered}
    $$

    where

    * $y_t$ is the original time series data,
    * $\overline{y}_t$ is the calculated trend component,
    * $L_t$ is the level constraint data,
    * $C_t$ is the change constraint data,
    * $\lambda$ is the smoothing parameter,
    * $1, \dots, T$ is the time span,
    * $\Omega$ is the time periods within the time span where the original data are available,
    * $\Omega_L$ is the time periods within the time span where the level constraint data are specified,
    * $\Omega_C$ is the time periods within the time span where the change constraint data are specified.

    The gap component, $\widehat{y}_t$, is then calculated as the difference between the
    original data and the trend component,

    $$
    \widehat{y}_t \equiv y_t - \overline{y}_t
    $$
        




---

&#9744;&nbsp;`mov_*`
----------------------------------


==Moving functions==


### Function for creating new Series objects ###

```
output = irispie.mov_sum(self, window=None, )
output = irispie.mov_avg(self, window=None, )
output = irispie.mov_mean(self, window=None, )
output = irispie.mov_prod(self, window=None, )
```


### Methods for changing the existing Series object in-place ###


```
self.mov_sum(window=None, )
self.mov_avg(window=None, )
self.mov_mean(window=None, )
self.mov_prod(window=None, )
```

Note that `mov_avg` and `mov_mean` are identical functions and the names
can be used interchangeably.


### Input arguments ###


???+ input "self"
    Time series on whose data a moving function is applied:

    - `mov_sum`: moving sum
    - `mov_avg` or `mov_mean`: moving average
    - `mov_prod`: moving product

???+ input "window"
    Number of observations (a negative integer) to include in the moving
    function (counting from the current time period backwards). If
    `window=None`, the default window is derived from the time series
    frequency:

    | Date frequency | Default window |
    |----------------|---------------:|
    | Yearly         |             –1 |
    | Quarterly      |             –4 |
    | Monthly        |            –12 |
    | Weekly         |            –52 |
    | Daily          |           –365 |
    | Otherwise      |             –4 |

    Note that the default windows for daily and weekly frequencies are
    fixed number and do not depend on the actual number of days in a
    calendar year or the actual number of weeks in a calendar year.


### Returns ###


???+ returns "output"
    New time series with data calculated as the moving function of the
    original data.

???+ returns "self"
    Time series with data replaced by the moving function of the original
    data.
        




---

&#9744;&nbsp;`x13`
----------------------------------


==Interface to X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure==


### Function for creating new Series objects ###


```
output = irispie.x13(
)
```


### Methods for changing the existing Series object in-place ###


```
self.x13(
)
```


### Input arguments ###


???+ input "self"


### Returns ###


???+ returns "self"


???+ returns "output"


### Details ###

        