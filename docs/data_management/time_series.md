
Time series
============

Time `Series` objects represent numerical time series, organized as rows of
observations stored in [`numpy`](https://numpy.org) arrays and time stamped
using [time `Periods`](periods.md). A `Series` object can hold multiple
variants of the data, stored as mutliple columns.
    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`start` | Start date of the time series
`periods` | N-tuple with the periods from the start period to the end period of the time series
`end` | End period of the time series
`frequency` | Date frequency of the time series
`from_until` | Two-tuple with the start date and end date of the time series
`has_missing` | True if the time series is non-empty and contains in-sample missing values
`is_empty` | True if the time series is empty
`num_periods` | Number of periods from the first to the last observation
`num_variants` | Number of variants (columns) within the `Series` object
`span` | Time span of the time series
`shape` | Shape of time series data





Categorical list of functions
-------------------------------

### Constructing new time series ###

Function | Description
----------|------------
[`Series`](#series) | Create a new `Series` object
[`Series.from_start_and_array`](#seriesfrom_start_and_array) | Create a new `Series` object from a start period and a numpy array


### Converting time series frequency ###

Function | Description
----------|------------
[`aggregate`](#aggregate) | Aggregate time series to a lower frequency
[`disaggregate`](#disaggregate) | Disaggregate time series to a higher frequency


### Getting information about time series ###

Function | Description
----------|------------
[`get_description`](#get_description) | Get description attached to an object
[`set_description`](#set_description) | Set the description for an object


### Manipulating time series values ###

Function | Description
----------|------------
[`replace_where`](#replace_where) | Replace time series values that pass a test
[`trim`](#trim) | Trim time series data


### Combining multiple time series ###

Function | Description
----------|------------
[`overlay`](#overlay) | Overlay another time series values onto the current time series
[`underlay`](#underlay) | Underlay another time series values beneath the current time series


### Homogenizing and extrapolating time series ###

Function | Description
----------|------------
[`clip`](#clip) | Clip time series to a new start and end period
[`extrapolate`](#extrapolate) | Extrapolate time series using autoregressive process
[`fill_missing`](#fill_missing) | Fill missing observations


### Filtering time series ###

Function | Description
----------|------------
[`hpf`](#hpf) | Constrained Hodrick-Prescott filter
[`x13`](#x13) | X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure


### Applying moving window functions ###

Function | Description
----------|------------
[`mov_avg`](#mov_avg) | Moving average
[`mov_mean`](#mov_mean) | Moving average
[`mov_prod`](#mov_prod) | Moving product
[`mov_sum`](#mov_sum) | Moving sum


### Calculating temporal change ###

Function | Description
----------|------------
[`adiff`](#adiff) | Annualized first difference
[`adiff_log`](#adiff_log) | Annualized first difference of logs
[`apct`](#apct) | Annualized percent change
[`aroc`](#aroc) | Annualized gross rate of change
[`diff`](#diff) | First difference
[`diff_log`](#diff_log) | First difference of logs
[`pct`](#pct) | Percent change
[`roc`](#roc) | Gross rate of change


### Converting measures of temporal change ###

Function | Description
----------|------------
[`pct_from_apct`](#pct_from_apct) | Percent change from annualized percent change
[`pct_from_roc`](#pct_from_roc) | Percent change from gross rate of change
[`roc_from_apct`](#roc_from_apct) | Gross rate of change from annualized percent change
[`roc_from_aroc`](#roc_from_aroc) | Gross rate of change from annualized gross rate of change
[`roc_from_pct`](#roc_from_pct) | Gross rate of change from percent change


### Calculating temporal cumulation ###

Function | Description
----------|------------
[`cum_diff`](#cum_diff) | Cumulation of first differences
[`cum_diff_log`](#cum_diff_log) | Cumulation of first differences of logs
[`cum_pct`](#cum_pct) | Cumulation of percent changes
[`cum_roc`](#cum_roc) | Cumulation of gross rates of change


### Indexing time series ###

Function | Description
----------|------------



Indexing time series
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
        



Calculating temporal change
-----------------------------

Overview of temporal change functions with flexible time shifts:


| Function      | Description
|---------------|-------------
| `diff`        | First difference, $y_t = x_t - x_s$ 
| `diff_log`    | First difference of logs, $y_t = \log x_t - \log x_s$ 
| `pct`         | Percent change, $y_t = 100 \cdot (x_t/x_s - 1)$ 
| `roc`         | Gross rate of change, $y_t = x_t/x_s$ 


Overview of temporal change functions with fixed time shifts:

| Function      | Description
|---------------|-------------
| `adiff`       | Annualized first difference, $y_t = a \cdot (x_t - x_{t-1})$ 
| `adiff_log`   | Annualized first difference of logs, $y_t = a \cdot (\log x_t - \log x_{t-1})$ 
| `apct`        | Annualized percent change, $y_t = 100 \cdot \left[ (x_t/x_{t-1})^a - 1 \right]$ 
| `aroc`        | Annualized gross rate of change, $y_t = (x_t/x_{t-1})^a$ 

where

* $x_t$ is the value of the time series at $t$;

* $x_s$ is the reference value of the time series in some preceding period $s$;
the value of $s$ depends on the (optional) input argument `shift` (whose default
value is `shift=-1`); see the explanation below;

* $a$ is an annualization factor, determined by the frequency of the time
series (i.e. the number of segments of a give frequency within a year: 1 for
yearly frequency, 2 for semi-annual frequency, 4 for quarterly frequency, 12 for
monthly frequency, 365 for daily frequency).

The `shift` input argument can be either a negative integer or a string to cover
some specific temporal change calculations:

* If `shift` is a negative integer, the reference period is $s := t-k$ where $k$ is
the negative value of `shift`; positive values (leads) of `shift` are not allowed.

* `shift="yoy"` means a year-on-year change, whereby the time shift is set to
the negative of the frequency of the time series, $s := t-a$ with $a$ being
defined above (the annualization factor).

* `shift="soy"` means a change over the start of the current year; in this case,
the reference period $s$ is set to the first segment of the current year (i.e.
the 1st half-year, the 1st quarter, the 1st month, etc.)

* `shift="eopy"` means a change over the end of the previous year; in this case,
the reference period $s$ is set to the last segment of the previous year (i.e.
the 2nd half-year, the 4th quarter, the 12th month, etc.).

* `shift="tty"` means a change throughout the year; this is equivalent to
`shift=-1` except for any start-of-year periods; in start-of-year periods, the
value of the resulting series is unchanged; for instance, `diff` applied to a
quarterly series with `shift="tty"` will return a series in which the Q1 value
will be unchanged, the Q2 value will be the difference between Q2 and Q1, the Q3
value will be the difference between Q3 and Q2, and the Q4 value will be the
difference between Q4 and Q3.


### Functional forms creating a new Series object ###

```
new = irispie.diff(self, shift=-1)
new = irispie.diff_log(self, shift=-1)
new = irispie.pct(self, shift=-1)
new = irispie.roc(self, shift=-1)
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
    A negative integer or a string determining a time lag at which the temporal change
    function is calculated. If `shift=None` (or not specified), `shift` is
    set to `-1`. If `shift` is a string, it must be one of the following:

    * `"yoy"`: year-on-year change
    * `"soy"`: change over the start of the current year
    * `"eopy"`: change over the end of the previous year
    * `"tty"`: change throughout the year


### Returns ###

???+ returns "new"
    New time series with data calculated as a temporal change function of
    the original data.

???+ returns "self"
    Time series with data replaced by a temporal change function of the
    original data.
        



Calculating temporal cumulation
---------------------------------

Overview of temporal cumulation calculations:

| Function      | Description
|---------------|-------------
| `cum_diff`    | Cumulative difference, $y_t = \sum_{i=0}^{t} (x_i - x_{i-k})$
| `cum_diff_log`| Cumulative difference of logs, $y_t = \sum_{i=0}^{t} (\log x_i - \log x_{i-k})$
| `cum_pct`     | Cumulative percent change, $y_t = 100 \sum_{i=0}^{t} (x_i/x_{i-k} - 1)$
| `cum_roc`     | Cumulative gross rate of change, $y_t = \prod_{i=0}^{t} (x_i/x_{i-k})$

where

* $k$ is a time shift (time lag) with which the temporal change is
calculated, determined by the negative value of the `shift` input argument.

* $t$ is the end date of the time series.


### Functional forms creating new Series objects ###

```
new = irispie.cum_diff(self, shift=-1, initial=None, span=None)
new = irispie.cum_diff_log(self, shift=-1, initial=None, span=None)
new = irispie.cum_pct(self, shift=-1, initial=None, span=None)
new = irispie.cum_roc(self, shift=-1, initial=None, span=None)
```


### Class methods changing existing Series objects in-place ###

```
self.cum_diff(shift=-1, initial=None, span=None)
self.cum_diff_log(shift=-1, initial=None, span=None)
self.cum_pct(shift=-1, initial=None, span=None)
self.cum_roc(shift=-1, initial=None, span=None)
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
        



Converting measures of temporal change
----------------------------------------

Overview of temporal change conversions:

| Function          | Description
|-------------------|-------------
| `roc_from_pct`    | Convert percent change to gross rate of change
| `pct_from_roc`    | Convert gross rate of change to percent change
| `pct_from_apct`   | Convert annualized percent change to percent change
| `roc_from_apct`   | Convert annualized percent change to gross rate of change
| `roc_from_aroc`   | Convert annualized gross rate of change to gross rate of change

### Functional forms changing an existing Series object in-place ###

```
new = irispie.roc_from_pct(self)
new = irispie.pct_from_roc(self)
new = irispie.pct_from_apct(self)
new = irispie.roc_from_apct(self)
new = irispie.roc_from_aroc(self)
```

### Class methods changing an existing Series object in-place ###

```
self.roc_from_pct()
self.pct_from_roc()
self.pct_from_apct()
self.roc_from_apct()
self.roc_from_aroc()
```
        



&#9744;&#160;`Series`
-----------------------

==Create a new `Series` object==

    self = Series(
        start=start,
        values=values,
    )


    self = Series(
        periods=periods,
        values=values,
    )


    self = Series(
        periods=periods,
        func=func,
    )


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

???+ input "func"
    A function that will be used to populate the time series; the function
    should not take any input arguments, and should return a single (scalar)
    numerical value; the function will called once for each period and each
    variant.


### Returns ###

???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



&#9744;&#160;`Series.from_start_and_array`
--------------------------------------------

==Create a new `Series` object from a start period and a numpy array==

    self = Series.from_start_and_array(
        start,
        array,
        description="",
        trim=True,
    )


### Input arguments ###

???+ input "start"
    The time [`Period`](periods.md) of the first value in the `array`.

???+ input "array"
    A numpy array containing the time series values. The array is reshaped to a
    two-dimensional array if needed. The individual rows are expected to
    correspond to a continuous sequence of time periods starting from `start`.

???+ input "description"
    A string description of the time series.

???+ input "trim"
    If `True`, the time series date will be trimmed to remove any leading
    or trailing periods that contain only `nan` values.


### Returns ###

???+ returns "self"
    A new `Series` object initialized with the provided start period and
    numpy array.
        



&#9744;&#160;`adiff`
----------------------

==Annualized first difference==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`adiff_log`
--------------------------

==Annualized first difference of logs==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`aggregate`
--------------------------

==Aggregate time series to a lower frequency==


### Function form for creating new time `Series` objects ###

    new = irispie.aggregate(
        self,
        target_freq,

        method="mean",
        discard_missing=False,
        select=None,
    )


### Class method changing an existing Series object in-place ###

    self.aggregate(
        target_freq,

        method="mean",
        discard_missing=False,
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
    | "prod"    | Product of high-frequency values
    | "first"   | Value in the first high-frequency period
    | "last"    | Value in the last high-frequency period
    | "min"     | Minimum of high-frequency values
    | "max"     | Maximum of high-frequency values

???+ input "discard_missing"
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
        



&#9744;&#160;`apct`
---------------------

==Annualized percent change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`aroc`
---------------------

==Annualized gross rate of change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`clip`
---------------------

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

        



&#9744;&#160;`cum_diff`
-------------------------

==Cumulation of first differences==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



&#9744;&#160;`cum_diff_log`
-----------------------------

==Cumulation of first differences of logs==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



&#9744;&#160;`cum_pct`
------------------------

==Cumulation of percent changes==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



&#9744;&#160;`cum_roc`
------------------------

==Cumulation of gross rates of change==

See documentation for [temporal cumulation calculations](#temporal-cumulation-calculations) or
`help(irispie.Series.temporal_cumulation)`.
        



&#9744;&#160;`diff`
---------------------

==First difference==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`diff_log`
-------------------------

==First difference of logs==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`disaggregate`
-----------------------------

==Disaggregate time series to a higher frequency==


### Function form for creating new time `Series` objects ###

    new = irispie.disaggregate(
        self,
        target_freq,

        method="flat",
    )


### Class method form for changing existing time `Series` objects in-place ###

    self.disaggregate(
        target_freq,

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
    | "middle"  | Place the low-frequency value in the middle high-frequency period
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
        



&#9744;&#160;`extrapolate`
----------------------------

==Extrapolate time series using autoregressive process==


### Functional forms creating a new time `Series` object ###


    new = extrapolate(
        self,
        ar_coeffs,
        span,
        *,
        intercept=0,
        log=False,
    )


### Class method changing an existing time `Series` object in-place ###


    self.extrapolate(
        ar_coeffs,
        span,
        *,
        intercept=0,
        log=False,
    )


### Input arguments ###


???+ input "self"
    The time `Series` object to be extrapolated by an autoregressive process.

???+ input "ar_coeffs"
    The autoregressive coefficients to be used in the extrapolation, entered as
    a tuple of AR_1, AR_2, ..., AR_p coefficients as if on the RHS of the AR
    process definition; see Details below.

???+ input "span"
    The time span on which the time series will be extrapolated.

???+ input "intercept"
    The intercept in the autorergressive process.

???+ input "log"
    If `log=True`, the time series will be logarithmized before the
    extrapolation and then delogarithmized back.


### Returns ###


???+ returns "self"
    The existing time `Series` object with its values replaced in-place.

???+ returns "new"
    A new time `Series` object.


### Details ###


The new extrapolated observations are created using this $p$-th order
autoregressive process defined recursively as:

$$
x_t = \rho_1 \, x_{t-1} + \cdots + \rho_p \, x_{t-p} + c, \qquad t = 1, \dots, T
$$

where

* the initial condion $x_{0},\ x_{-1}, \, \dots,\ x_{-p+1}$ are taken from
the existing observations in the input series `self`;

* the autoregressive coefficents
$\rho_1,\ \rho_2,\ \dots,\ \rho_p$ given by the input argument `ar_coeff`

* $c$ is the `intercept`.
        



&#9744;&#160;`fill_missing`
-----------------------------

==Fill missing observations==


### Function form for creating new time `Series` objects ###

    new = irispie.fill_missing(
        self,
        method,
        *args,
        span=None,
    )


### Class method form changing existing `Series` objects in-place ###

    self.fill_missing(
        method,
        *args,
        span=None,
    )


### Input arguments ###


???+ input "self"
    The time `Series` object to be filled.

???+ input "method"
    The method to be used for filling missing observations. The following methods are available:

    | Method         | Description
    |----------------|-------------
    | "constant"     | Fill with a constant value
    | "next"         | Next available observation
    | "previous"     | Previous available observation
    | "nearest"      | Nearest available observation
    | "linear"       | Linear interpolation or extrapolation
    | "log_linear"   | Log-linear interpolation or extrapolation
    | "from_series"  | Fill with values from another time series object

???+ input "*args"
    Additional arguments to be passed to the filling method. The following methods require additional arguments:

    | Method         | Additional argument(s)
    |----------------|-----------------------
    | "constant"     | A single constant value
    | "from_series"  | A time `Series` object


???+ input "span"
    The time span to be filled. If `None`, the time span of the input time `Series` is filled.


### Returns ###


???+ returns "self"
    The time `Series` object with missing observations filled.

???+ returns "new"
    A new time `Series` object with missing observations filled.
        



&#9744;&#160;`get_description`
--------------------------------


==Get description attached to an object==

    description = self.get_description()


### Input arguments ###

???+ input "self"
    An object from which to get the description.


### Returns ###

???+ returns "description"
    The description attached to the object.

        



&#9744;&#160;`hpf`
--------------------

==Constrained Hodrick-Prescott filter==


### Functional form creating a new time `Series` object ###


    trend, gap = irispie.hpf(
        self,
        /,
        span=None,
        smooth=None,
        log=False,
        level=None,
        change=None,
    )


### Class method changing an existing time `Series` objects in-place ###


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


???+ abstract "Algorithm"

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
        



&#9744;&#160;`mov_avg`
------------------------

==Moving average==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



&#9744;&#160;`mov_mean`
-------------------------

==Moving average==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



&#9744;&#160;`mov_prod`
-------------------------

==Moving product==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



&#9744;&#160;`mov_sum`
------------------------

==Moving sum==


See documentation of [moving window calculations](#moving-window-calculations) or
`help(irispie.Series.moving_window)`.
        



&#9744;&#160;`overlay`
------------------------

==Overlay another time series values onto the current time series==

Overlay the values of another time series onto the current time series on the
entire span of the other time series, i.e. from the start to the end period
regardless of missing in-sample values.

    self.overlay(
        other,
        method="by_span",
    )

### Input arguments ###

???+ input "self"
    The current time series object.

???+ input "other"
    The time series object whose values will be overlaid onto the current time
    series.

???+ input "method"
    The method to use for overlaying the values. The default (and currently the
    only available) method is `"by_span"`.

### Returns ###

This method modifies `self` in place and returns `None`.

### Details ###

???+ abstract "Algorithm"

    The resulting time series is determined the following way:

    1. The span of the resulting series starts at the earliest start period of the two
    series and ends at the latest end period of the two series.

    2. The observations from the `self` (current) time series used to fill the
    resulting time span.

    3. Within the span of the `other` time series (from the first available
    observation to the last available observation), the observations from this
    `other` time series are superimposed on the resulting time series, including any
    in-sample missing observations.




&#9744;&#160;`pct`
--------------------

==Percent change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`pct_from_apct`
------------------------------

==Percent change from annualized percent change==

See documentation for [converting measures of temporal
change](#temporal-change-conversion).
        



&#9744;&#160;`pct_from_roc`
-----------------------------

==Percent change from gross rate of change==

See documentation for [converting measures of temporal
change](#temporal-change-conversion).
        



&#9744;&#160;`replace_where`
------------------------------

==Replace time series values that pass a test==

    self.replace_where(
        test,
        new_value,
    )


### Input arguments ###


???+ input "self"
    Time series whose observations will be tested and those passing the test
    replaced.

???+ input "test"
    A function (or a Callable) that takes a numpy array and returns `True` or
    `False` for each individual value.

???+ input "new_value"
    The value to replace the observations that pass the test.


### Returns ###


???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



&#9744;&#160;`roc`
--------------------

==Gross rate of change==

See documentation for [temporal change calculations](#temporal-change-calculations) or
`help(irispie.Series.temporal_change)`.
        



&#9744;&#160;`roc_from_apct`
------------------------------

==Gross rate of change from annualized percent change==

See documentation for [converting measures of temporal
change](#temporal-change-conversion).
        



&#9744;&#160;`roc_from_aroc`
------------------------------

==Gross rate of change from annualized gross rate of change==

See documentation for [converting measures of temporal
change](#temporal-change-conversion).
        



&#9744;&#160;`roc_from_pct`
-----------------------------

==Gross rate of change from percent change==

See documentation for [converting measures of temporal
change](#temporal-change-conversion).
        



&#9744;&#160;`set_description`
--------------------------------


==Set the description for an object==

    self.set_description(
        description,
    )


### Input arguments ###

???+ input "self"
    An Iris Pie object to which to attach the description.


???+ input "description"
    The description to attach to the Iris Pie object.


### Returns ###

This method modifies the Iris Pie object in place and returns `None`.

        



&#9744;&#160;`trim`
---------------------

==Trim time series data==

Trim leading and trailing missing values from the time series data.

    self.trim()

### Input arguments ###

???+ input "self"
    The time series object to trim.

### Returns ###

This method modifies `self` in place and returns `None`.
        



&#9744;&#160;`underlay`
-------------------------

==Underlay another time series values beneath the current time series==

Underlay the values of another time series beneath the current time series on
the entire span of the other time series, i.e. from the start to the end period
regardless of missing in-sample values.

    self.underlay(
        other,
        method="by_span",
    )

### Input arguments ###

???+ input "self"
    The current time series object.

???+ input "other"
    The time series object whose values will be underlaid beneath the current
    time series.

???+ input "method"
    The method to use for underlaying the values. The default (and currently the
    only available) method is `"by_span"`.

### Returns ###

This method modifies `self` in place and returns `None`.

### Details ###

???+ abstract "Algorithm"

    The resulting time series is determined the following way:

    1. The span of the resulting series starts at the earliest start period of the two
    series and ends at the latest end period of the two series.

    2. The observations from the `other` time series used to fill the
    resulting time span.

    3. Within the span of the `self` time series (from the first available
    observation to the last available observation), the observations from this
    `self` time series are superimposed on the resulting time series, including any
    in-sample missing observations.
        



&#9744;&#160;`x13`
--------------------

==X13-ARIMA-TRAMO-SEATS seasonal adjustment procedure==


### Function for creating new Series objects ###


```
new = irispie.x13(
    self,

    span=None,
    output="seasonally_adjusted",
    mode=None,
    when_error="warning",
    clean_up=True,

    specs_template=None,
    add_to_specs=None,
    allow_missing=False,
    mode=None,

    unpack_singleton=True,
    return_info=False,
)
```

```
new, info = irispie.x13(
    ...,
    return_info=True,
    ...,
)
```


### Class method for changing existing time `Series` objects in-place ###


```
self.x13(
    self,

    span=None,
    output="seasonally_adjusted",
    mode=None,
    when_error="warning",
    clean_up=True,

    specs_template=None,
    add_to_specs=None,
    allow_missing=False,
    mode=None,

    unpack_singleton=True,
    return_info=False,
)
```

```
info = self.x13(
    ...,
    return_info=True,
    ...,
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
    available at the moment:

    | Output                  | X13 table | Description
    |-------------------------|-----------|-------------
    | `"seasonal"`            | `d10`     | Seasonal factors
    | `"seasonally_adjusted"` | `d11`     | Seasonally adjusted series
    | `"trend_cycle"`         | `d12`     | Trend-cycle component
    | `"irregular"`           | `d13`     | Irregular component
    | `"seasonal_and_td"`     | `d16`     | Combined seasonal and trading day factors
    | `"holiday_and_td"`      | `d18`     | Combined holiday and trading day factors

???+ input "specs_template"
    A dictionary with a specs template for the X13 run; if `None`, a default
    specs template is used (see below for the structure of the default template).

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

???+ input "allow_missing"
    If `True`, allow missing values in the input time series and automatically
    add an empty `automdl` spec if no ARIMA model is specified.

???+ input "add_to_specs"
    A dictionary with additional settings to be added to the `specs_template` (or
    the default templated).

???+ input "when_error"
    The action to be taken when an error occurs. The following options are
    available:

    | Action      | Description
    |-------------|-------------
    | `"warning"` | Issue a warning
    | `"error"`   | Raise an error

???+ input "unpack_singleton"
    If `True`, unpack `info` into a plain dictionary for models with a
    single variant.

???+ input "return_info"
    If `True`, return a dictionary with information about the X13 run as another
    output argument.


### Returns ###


???+ returns "self"
    The `Series` object with the output data.

???+ returns "new"
    A new `Series` object with the output data.

???+ returns "info"
    (Only returned if `return_info=True` which is not the default behavior)
    Dictionary with information about the X13 run; `info` contains the
    following items:

    | Key | Description
    |-----|-------------
    | `success` | True if the X13 run was successful
    | `specs_template` | The specs template used for the X13 run
    | `mode` | The mode used for the X13 run
    | `spc` | The spc file from the X13 run
    | `log` | The log file from the X13 run
    | `out` | The output file from the X13 run
    | `err` | The error file from the X13 run
    | `*` | Any other output file written by X13


### Details ###


???+ abstract "Default SPC template structure"

    The default specs template is a dictionary equivalent to the following SPC
    file:

    ```
    series{
        start=$(series_start)
        data=(
    $(series_data)
        )
        period=$(series_period)
        decimals=5
        precision=5
    }

    transform{
        function=$(transform_function)
    }

    x11{
        mode=$(x11_mode)
        save=$(x11_save)
    }

    ```
        