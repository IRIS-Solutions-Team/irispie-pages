
Time series
============

Time `Series` objects represent numerical time series, organized as rows of
observations stored in [`numpy`](https://numpy.org) arrays and time stamped
using [time `Periods`](periods.md). A `Series` object can hold multiple
variants of the data, stored as mutliple columns.
    


Categorical list of functions
-------------------------------

### Constructing new time series ###

Function | Description
----------|------------
[Series](#series) | Create a new `Series` object


### Converting time series frequency ###

Function | Description
----------|------------
[aggregate](#aggregate) | Aggregate time series to a lower frequency
[disaggregate](#disaggregate) | Disaggregate time series to a higher frequency


### Homogenizing time series ###

Function | Description
----------|------------
[clip](#clip) | Clip time series to a new start and end period
[fill_missing](#fill_missing) | Fill missing observations


### Filtering time series ###

Function | Description
----------|------------
[hpf](#hpf) | Constrained Hodrick-Prescott filter
[x13](#x13) | X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure


### Applying moving window functions ###

Function | Description
----------|------------
[mov_avg](#mov_avg) | Moving average
[mov_mean](#mov_mean) | Moving average
[mov_prod](#mov_prod) | Moving product
[mov_sum](#mov_sum) | Moving sum


### Calculating temporal change ###

Function | Description
----------|------------
[adiff](#adiff) | Annualized first difference
[adiff_log](#adiff_log) | Annualized first difference of logs
[apct](#apct) | Annualized percent change
[aroc](#aroc) | Annualized gross rate of change
[diff](#diff) | First difference
[diff_log](#diff_log) | First difference of logs
[pct](#pct) | Percent change
[roc](#roc) | Gross rate of change


### Calculating temporal cumulation ###

Function | Description
----------|------------
[cum_diff](#cum_diff) | Cumulation of first differences
[cum_diff_log](#cum_diff_log) | Cumulation of first differences of logs
[cum_pct](#cum_pct) | Cumulation of percent changes
[cum_roc](#cum_roc) | Cumulation of gross rates of change





Directly accessible properties
------------------------------

Property | Description
----------|------------
[start](#start) | Start date of the time series
[periods](#periods) | N-tuple with the periods from the start period to the end period of the time series
[end](#end) | End period of the time series
[frequency](#frequency) | Date frequency of the time series
[from_to](#from_to) | Two-tuple with the start date and end date of the time series
[num_periods](#num_periods) | Number of periods from the first to the last observation
[num_variants](#num_variants) | Number of variants (columns) within the `Series` object
[span](#span) | Time span of the time series
[shape](#shape) | Shape of time series data



Time series indexing
----------------------

Time `Series` objects can be indexed in four ways (note the square versus round
brackets):

| Indexing                                           | Description
|----------------------------------------------------|-------------
| `self[shift]`                                      | Time shift
| `self[dates]`, `self[dates, variants]`             | Data extraction
| `self[dates] = ...`, `self[dates, variants] = ...` | Data assignment
| `self(dates)`, `self(dates, variants)`             | Time `Series` recreation


### Time shift ###

```
self[shift]
```

Time shift is done by passing an integer to the `self[shift]` or
`self[shift]` indexing. The time shift syntax returns a new copy of the
original series, with the time periods shifted by `shift`.


### Data extractation ###

```
self[dates]
self[dates, variants]
```

The `dates` is a `Dater` or a tuple of `Daters` or a time `Span` object,
and `variants` is an integer or a tuple of integers or a `slice` object
specifying the variants. The data extraction syntax returns a
two-dimensional `numpy` array, with the time dimension running along the
rows and the variant dimension running along the columns.


### Data assignment ###

```
self[dates] = ...
self[dates, variants] = ...
```

The `dates` is a `Dater` or a tuple of `Daters` or a time `Span` object,
and `variants` is an integer or a tuple of integers or a `slice` object
specifying the variants. The data assignment syntax sets the data in the
time series.


### Time `Series` recreation ###

```
self(dates)
self(dates, variants)
```

The `dates` is a `Dater` or a tuple of `Daters` or a time `Span` object,
and `variants` is an integer or a tuple of integers or a `slice` object
specifying the variants. The time `Series` recreation syntax returns a new
time `Series` object based on the data selected by the `dates` and
`variants`.
        



Moving window calculations
----------------------------


Overview of moving window functions:

| Function | Description
|----------|-------------
| `mov_sum` | Moving sum, $y_t = \sum_{i=0}^{k-1} x_{t-i}$
| `mov_avg` | Moving average, $y_t = \frac{1}{k} \sum_{i=0}^{k-1} x_{t-i}$
| `mov_mean` | Same as `mov_avg`
| `mov_prod` | Moving product, $y_t = \prod_{i=0}^{k-1} x_{t-i}$

where

* $k$ is the window length determined by the `window` input argument
(note that $k$ above is a positive integer while `window` needs to be
entered as a negative integer).



### Function for creating new Series objects ###

```
new = irispie.mov_sum(self, window=None, )
new = irispie.mov_avg(self, window=None, )
new = irispie.mov_mean(self, window=None, )
new = irispie.mov_prod(self, window=None, )
```


### Methods for changing existing Series objects in-place ###


```
self.mov_sum(window=None, )
self.mov_avg(window=None, )
self.mov_mean(window=None, )
self.mov_prod(window=None, )
```


### Input arguments ###


???+ input "self"
    Time series on whose data a moving function is calculated (see the
    overview table above).

???+ input "window"
    A negative interger determining the number of observations to include
    in the moving window, counting from the current time period backwards
    (the minus sign is a convention to indicate that the window goes
    backwards in time). If `window=None` (or not specified), the default
    window is derived from the time series frequency:

    | Date frequency | Default window |
    |----------------|---------------:|
    | `YEARLY`       |             –1 |
    | `QUARTERLY`    |             –4 |
    | `MONTHLY`      |            –12 |
    | `WEEKLY`       |            –52 |
    | `DAILY`        |           –365 |
    | Otherwise      |             –4 |

    Note that the default windows for `DAILY` and `WEEKLY` frequencies are
    fixed numbers and do not depend on the actual number of days in a
    calendar year or the actual number of weeks in a calendar year.


### Returns ###


???+ returns "new"
    New time series with data calculated as a moving window function of the
    original data.

???+ returns "self"
    Time series with data replaced by the moving window function of the
    original data.
        



Temporal change calculations
------------------------------


Overview of temporal change functions:

| Function      | Description
|---------------|-------------
| `diff`        | First difference, $y_t = x_t - x_{t-k}$ 
| `diff_log`    | First difference of logs, $y_t = \log x_t - \log x_{t-k}$ 
| `pct`         | Percent change, $y_t = 100 (x_t/x_{t-k} - 1)$ 
| `roc`         | Gross rate of change, $y_t = x_t/x_{t-k}$ 
| `adiff`       | Annualized first difference, $y_t = a \cdot (x_t - x_{t-1})$ 
| `adiff_log`   | Annualized first difference of logs, $y_t = a \cdot (\log x_t - \log x_{t-1})$ 
| `apct`        | Annualized percent change, $y_t = 100 [(x_t/x_{t-1})^a - 1]$ 
| `aroc`        | Annualized gross rate of change, $y_t = (x_t/x_{t-1})^a$ 

where

* $k$ is the time shift (time lag) with which the temporal change is
calculated, determined by the negative value of the `shift` input argument;

* $a$ is the annualization factor, determined by the frequency of the time
series (i.e. the number of calendar periods within a year).


### Functional forms creating a new Series object ###


```
new = irispie.diff(self, /, shift=-1)
new = irispie.diff_log(self, /, shift=-1)
new = irispie.pct(self, /, shift=-1)
new = irispie.roc(self, /, shift=-1)
new = irispie.adiff(self)
new = irispie.adiff_log(self)
new = irispie.apct(self)
new = irispie.aroc(self)
```


### Class methods changing an existing Series object in-place ###


```
self.diff(shift=-1)
self.difflog(shift=-1)
self.pct(shift=-1)
self.roc(shift=-1)
self.adiff()
self.adifflog()
self.apct()
self.aroc()
```



### Input arguments ###


???+ input "self"
    Time series on whose data a temporal change function is calculated (see
    the overview table above).

???+ input "shift"
    A negative integer determining a time lag at which the temporal change
    function is calculated. If `shift=None` (or not specified), `shift` is
    set to `-1`.


### Returns ###


???+ returns "new"
    New time series with data calculated as a temporal change function of
    the original data.

???+ returns "self"
    Time series with data replaced by a temporal change function of the
    original data.
        



Temporal cumulation calculations
----------------------------------

Overview of temporal cumulation calculations:

| Function      | Description
|---------------|-------------
| `cum_diff`    | Cumulative difference, $y_t = \sum_{i=0}^{t} (x_i - x_{i-k})$
| `cum_diff_log`| Cumulative difference of logs, $y_t = \sum_{i=0}^{t} (\log x_i - \log x_{i-k})$
| `cum_pct`     | Cumulative percent change, $y_t = 100 \sum_{i=0}^{t} (x_i/x_{i-k} - 1)$
| `cum_roc`     | Cumulative gross rate of change, $y_t = \prod_{i=0}^{t} (x_i/x_{i-k})$

where

* $k$ is the time shift (time lag) with which the temporal change is
calculated, determined by the negative value of the `shift` input argument.

* $t$ is the end date of the time series.


### Functional forms creating new Series objects ###


```
new = irispie.cum_diff(self, /, shift=-1, initial=None, span=None)
new = irispie.cum_diff_log(self, /, shift=-1, initial=None, span=None)
new = irispie.cum_pct(self, /, shift=-1, initial=None, span=None)
new = irispie.cum_roc(self, /, shift=-1, initial=None, span=None)
```


### Class methods changing existing Series objects in-place ###


```
self.cum_diff(/, shift=-1, initial=None, span=None)
self.cum_diff_log(/, shift=-1, initial=None, span=None)
self.cum_pct(/, shift=-1, initial=None, span=None)
self.cum_roc(/, shift=-1, initial=None, span=None)
```


### Input arguments ###


???+ input "self"
    Time series on whose data a temporal cumulation is calculated (see the
    overview table above).

???+ input "shift"
    A negative integer determining a time lag at which the temporal
    cumulation is calculated. If `shift=None` (or not specified), `shift`
    is set to `-1`.

???+ input "initial"
    Initial value of the cumulative series. If `initial=None` (or not specified),
    the initial value is set to `0` for `diff` and `diff_log`, and to
    `1` for `pct` and `roc`.

???+ input "span"
    Time span on which the values from the original series are cumulated.
    If `span=None` (or not specified), the time span is set to the entire
    time series.


### Returns ###


???+ returns "new"
    New time series with data calculated as temporal cumulation of the
    original data.

???+ returns "self"
    Time series with data replaced by temporal cumulation of the original
    data.

        



☐ `Series`
------------

==Create a new `Series` object==

```
self = Series(
    start=start,
    values=values,
)
```

```
self = Series(
    periods=periods,
    values=values,
)
```


### Input arguments ###


???+ input "start"

    The time [`Period`](periods.md) of the first value in the `values`.

???+ input "periods"

    An iterable of time [`Periods`](periods.md) that will be used to time stamp
    the `values`. The iterable can be e.g. a tuple, a list, a time
    [`Span`](spans.md), or a single time [`Period`](periods.md).

???+ input "values"

    Time series values, supplied either as a single values, a tuple of values,
    or a NumPy array.


### Returns ###


???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



☐ `adiff`
-----------

==Annualized first difference==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `adiff_log`
---------------

==Annualized first difference of logs==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `aggregate`
---------------

==Aggregate time series to a lower frequency==


### Function form for creating new time `Series` objects ###

    new = irispie.aggregate(
        self,
        target_freq,
        /,
        method="mean",
        remove_missing=False,
        select=None,
    )


### Class method form for creating new time `Series` objects ###

    self.aggregate(
        target_freq,
        /,
        method="mean",
        remove_missing=False,
        select=None,
    )


### Input arguments ###


???+ input "target_freq"
    The new frequency to which the original time series will be diaggregated.

???+ input "method"
    Aggregation method, i.e. a function applied to the high-frequency
    values within each low-frequency period:

    | Method    | Description
    |-----------|-------------
    | "mean"    | Arithmetic average of high-frequency values
    | "sum"     | Sum of high-frequency values
    | "first"   | Value in the first high-frequency period
    | "last"    | Value in the last high-frequency period
    | "min"     | Minimum of high-frequency values
    | "max"     | Maximum of high-frequency values

???+ input "remove_missing"
    Remove missing values from the high-frequency data before
    applying the aggregation `method`.

???+ input "select"
    Select only the high-frequency values at the specified indexes;
    `select=None` means all values are used.


### Returns ###

???+ returns "self"
    The original time `Series` object with the aggregated data.

???+ returns "new"
    A new time `Series` object with the aggregated data.
        



☐ `apct`
----------

==Annualized percent change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `aroc`
----------

==Annualized gross rate of change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `clip`
----------

==Clip time series to a new start and end period==

    self.clip(new_start, new_end)


### Input arguments ###


???+ input "new_start"
    The new start period for the `self` time series; if `None`, the current
    start period is kept.

???+ input "new_end"
    The new end period for the `self` time series; if `None`, the current
    end period is kept.


### Returns ###


???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



☐ `cum_diff`
--------------

==Cumulation of first differences==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



☐ `cum_diff_log`
------------------

==Cumulation of first differences of logs==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



☐ `cum_pct`
-------------

==Cumulation of percent changes==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



☐ `cum_roc`
-------------

==Cumulation of gross rates of change==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



☐ `diff`
----------

==First difference==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `diff_log`
--------------

==First difference of logs==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `disaggregate`
------------------

==Disaggregate time series to a higher frequency==


### Function form for creating new time `Series` objects ###

    new = irispie.disaggregate(
        self,
        target_freq,
        /,
        method="flat",
    )


### Class method form for changing existing time `Series` objects in-place ###

    self.disaggregate(
        target_freq,
        /,
        method="flat",
        model=None,
    )


### Input arguments ###


???+ input "target_freq"
    The new frequency to which the original time series will be aggregated.

???+ input "method"
    Aggregation method, i.e. a function applied to the high-frequency
    values within each low-frequency period:

    | Method    | Description
    |-----------|-------------
    | "flat"    | Repeat the high-frequency values
    | "first"   | Place the low-frequency value in the first high-frequency period
    | "last"    | Place the low-frequency value in the last high-frequency period
    | "arip"    | Interpolate using a smooth autoregressive process


### Returns ###


???+ returns "new"
    A new time `Series` object with the disaggregated data.



### Details ###

???+ details "ARIP algorithm"

    The `method="arip" setting invokes an interpolation method that assumes the
    underlying high-frequency process to be an autoregression. The method can be
    described in its state-space recursive form, although the numerical
    implementation is stacked-time.

    The `"rate"` model:

    $$
    \begin{gathered}
    x_t = \rho \, x_{t-1} + \epsilon_t \\[10pt]
    y_t = Z \, x_t \\[10pt]
    \epsilon_t \sim N(0, \sigma_t^2)
    \end{gathered}
    $$

    The `"diff"` model:

    $$
    \begin{gathered}
    x_t = x_{t-1} + c + \epsilon_t \\[10pt]
    y_t = Z \, x_t \\[10pt]
    \epsilon_t \sim N(0, 1)
    \end{gathered}
    $$

    where

    * $x_t$ is the underlying high-frequency process;

    * $y_t$ is the observed low-frequency time series;

    * $Z$ is an aggregation vector depending on the `aggregation` specification,

    | Aggregation | $Z$ vector
    |-------------|-----------
    | "sum"       | $(1, 1, \ldots, 1)$
    | "mean"      | $\tfrac{1}{n}\,(1, 1, \ldots, 1)$
    | "first"     | $(1, 0, \ldots, 0)$
    | "last"      | $(0, 0, \ldots, 1)$

    * $\rho$ is a gross rate of change estimated as the average rate of change
    in the observed series, $y_t$, and converted to high frequency;

    * $c$ is a constant estimated as the average difference in the observed
    series, $y_t$, and converted to high frequency;

    * $\sigma_t$ is a time-varying standard deviation of the high-frequency process, set to $\sigma_0 = 1$, and $\sigma_t = \rho \, \sigma_{t-1}$.
        



☐ `fill_missing`
------------------

==Fill missing observations==


### Function form for creating new time `Series` objects ###

    new = irispie.fill_missing(
        self,
        method,
        span=None,
        *args,
    )


### Class method form for changing existing time `Series` objects in-place ###

    self.fill_missing(
        method,
        span=None,
        *args,
    )


### Input arguments ###


???+ input "self"
    The time `Series` object to be filled.

???+ input "method"
    The method to be used for filling missing observations. The following methods are available:

    | Method        | Description
    |---------------|-------------
    | "next"        | Next available observation
    | "previous"    | Previous available observation
    | "nearest"     | Nearest available observation
    | "linear"      | Linear interpolation or extrapolation
    | "log_linear"  | Log-linear interpolation or extrapolation

???+ input "span"
    The time span to be filled. If `None`, the time span of the input time `Series` is filled.


### Returns ###


???+ returns "self"
    The time `Series` object with missing observations filled.

???+ returns "new"
    A new time `Series` object with missing observations filled.
        



☐ `hpf`
---------

==Constrained Hodrick-Prescott filter==


### Functional forms creating a new time `Series` object ###

    trend, gap = irispie.hpf(
        self,
        /,
        span=None,
        smooth=None,
        log=False,
        level=None,
        change=None,
    )


### Class methods changing an existing time `Series` object in-place ###

    self.hpf_trend(
        /,
        span=None,
        smooth=None,
        log=False,
        level=None,
        change=None,
    )

    self.hpf_gap(
        /,
        span=None,
        smooth=None,
        log=False,
        level=None,
        change=None,
    )


### Input arguments ###


???+ input "self"
    A time `Series` object whose data are filtered. All the
    observations contained in the input time series are used in the
    Hodrick-Prescott filter calculations no matter the time `span`
    specified; the time `span` only determines the time span of the output
    series.

???+ input "span"
    Time span on which the trend component of the Hodrick-Prescott filter
    is calculated. If `span=None`, the results are returned on
    the time span of the original series, `self`.

???+ input "smooth"
    Smoothing parameter (also known as $\lambda$) for the Hodrick-Prescott filter. If `smooth=None`,
    a default value is used based on the frequency of the input series `self`:

    | Date frequency | Default `smooth` ($\lambda$)
    |----------------|-----------------------------:
    | `YEARLY`       |                         100
    | `HALF-YEARLY`  |                         400
    | `QUARTERLY`    |                       1,600
    | `MONTHLY`      |                     144,000
    | Otherwise      |                       1,600

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
    filter. The trend component is always returned on the entier time `span`
    specified regardless of the actual time span of the original series.

???+ returns "gap"
    A new `Series` object with the trend component of the Hodrick-Prescott
    filter. The gap component is calculated on the time `span` as the
    difference between the actual observations and the trend component;
    therefore, unline the `trend` series, the `gap` series is defined only
    in time periods where the actual observations are available in the
    original series.

???+ returns "self"
    The existing `Series` object with its values replaced in-place by the trend
    component of the Hodrick-Prescott filter.


### Details ###


???+ abstract "Time span of HP filter calculations"

    The Hodrick-Prescott filter is calculated on a time span starting in
    the period that is the first common period of

    * the input data,
    * the `span` argument,
    * the level constraints, and
    * the change constraints.

    and ending in the period that is the last common period of the same
    four data sources.

    The actual time series returned is then clipped to comply with the
    `span` argument if necessary.


???+ abstract "Algorighm"

    The constrained Hodrick-Prescott filter is a method for decomposing a
    time series into a lower-frequency (trend) component and a
    higher-frequency (cyclical) component subject to level and/or change
    constraints. The filter is implemented as the following constrained
    dynamic optimization problem

    $$
    \begin{gathered}
    \min\nolimits_{\{\overline{y}_t\}}
        \left[
            \lambda \sum_{t\in\Omega}
            \left( y_t - \overline{y}_t \right)^2
            + \sum_{t=3}^{T}
            \left( \Delta \overline{y}_t - \Delta \overline{y}_{t-1} \right)^2
        \right]
        \\[10pt]
    \text{subject to} \\[10pt]
    \overline{y}_t = L_t \ \forall t \in \Omega_L \\[10pt]
    \Delta \overline{y}_t = C_t \ \forall t \in \Omega_C
    \end{gathered}
    $$

    where

    * $y_t$ is the original time series data,
    * $\overline{y}_t$ is the calculated trend component,
    * $L_t$ is the level constraint data,
    * $C_t$ is the change constraint data,
    * $\lambda$ is the smoothing parameter,
    * $1, \dots, T$ is the HP filter time span (see above),
    * $\Omega$ is the time periods within the filter time span where the original data are available,
    * $\Omega_L$ is the time periods within the filter time span where the level constraint data are specified,
    * $\Omega_C$ is the time periods within the filter time span where the change constraint data are specified.

    The gap component, $\widehat{y}_t$, is then calculated as the difference between the
    original data and the trend component,

    $$
    \widehat{y}_t \equiv y_t - \overline{y}_t
    $$
        



☐ `mov_avg`
-------------

==Moving average==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



☐ `mov_mean`
--------------

==Moving average==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



☐ `mov_prod`
--------------

==Moving product==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



☐ `mov_sum`
-------------

==Moving sum==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



☐ `pct`
---------

==Percent change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `roc`
---------

==Gross rate of change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



☐ `x13`
---------

==X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure==


### Function for creating new Series objects ###


```
new, out_info = irispie.x13(
    self,
    /,
    span=None,
    output="sa",
    mode=None,
    when_error="warning",
    clean_up=True,
    unpack_singleton=True,
    return_info=False,
)
```


### Class methods for changing existing Series objects in-place ###


```
out_info = self.x13(
    span=None,
    output="sa",
    mode=None,
    when_error="warning",
    clean_up=True,
    unpack_singleton=True,
    return_info=False,
)
```


### Input arguments ###


???+ input "self"
    A time `Series` object whose data will be run through the
    X13-ARIMA-TRAMO-SEATS procedure.

???+ input "span"
    A time span be specified as a `Span` object. If `span=None` or `span=...`,
    the time span goes from the first observed period to the last observed
    period in the input time series.

???+ input "output"
    The type of output to be returned by X13. The following options are
    available:

    | Output    | Description
    |-----------|-------------
    | `"sf"`    | Seasonal factors
    | `"sa"`    | Seasonally adjusted series
    | `"tc"`    | Trend-cycle
    | `"irr"`   | Irregular component

???+ input "mode"
    The mode to be used for the X13 run. The following options are available (see the
    [X13 documentation](https://www.census.gov/srd/www/x13as/)):

    | Mode          | Description
    |---------------|-------------
    | `None`        | Automatically selected
    | `"mult"`      | Multiplicative
    | `"add"`       | Additive
    | `"pseudoadd"` | Pseudo-additive
    | `"logadd"`    | Log-additive

    If `mode=None`, the mode is automatically selected based on the data. If the data is
    strictly positive or strictly negative, the multiplicative mode is used, otherwise
    the additive mode is used.

???+ input "when_error"
    The action to be taken when an error occurs. The following options are
    available:

    | Action      | Description
    |-------------|-------------
    | `"warning"` | Issue a warning
    | `"error"`   | Raise an error

???+ input "unpack_singleton"
    If `True`, unpack `out_info` into a plain dictionary for models with a
    single variant.

???+ input "return_info"
    If `True`, return a dictionary with information about the X13 run as the
    second output argument.


### Returns ###


???+ returns "self"
    The `Series` object with the output data.

???+ returns "new"
    A new `Series` object with the output data.

???+ returns "out_info"
    A dictionary with information about the X13 run. The dictionary
    contains the following keys:

    | Key | Description
    |-----|-------------
    | `mode` | The mode used for the X13 run
    | `log` | The log file from the X13 run
    | `out` | The output file from the X13 run
    | `err` | The error file from the X13 run
    | `success` | A boolean indicating whether the X13 run was successful


### Details ###

        