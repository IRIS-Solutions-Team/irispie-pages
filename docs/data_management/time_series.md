
Time series
============

The `Series` objects represent numerical time series, organized as rows of
observations stored in NumPy arrays and'
[date](dates.md)
stamped. A `Series` object can hold multiple
variants of the data, stored as mutliple columns.
    


Categorical list of functions
-------------------------------

### Creating new time series ###

Function | Description
----------|------------
[:octicons-file-24:`Series`](#series) | Create a new `Series` object





Directly accessible properties
------------------------------

Property | Description
----------|------------
[:octicons-package-24:`num_periods`](#num_periods) | Number of periods from the first to the last observation
[:octicons-package-24:`num_variants`](#num_variants) | Number of variants (columns) within the `Series` object
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
        