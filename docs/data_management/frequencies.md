
Time frequencies
=================

Time frequencies are simple integer values that represent the number of time
periods within a year, plus two special frequencies: a so-called "integer"
frequency (for simple numbered observations without relation to calendar time),
and a representation for unknown or unspecified frequencies. For convenience,
the `Frequency` enum provides a set of predefined names for all the time
frequencies available.

The `Frequencies` are classified into regular and
irregular frequencies. Regular frequencies are those that are evenly spaced
within a year no matter the year, while irregular frequencies are those that
vary in the number of periods within a year due to human calendar conventions
and irregularities.


| Integer value | `Frequency` enum       | Regular           | Description
|--------------:|------------------------|:-----------------:|-------------
| 1             | `irispie.YEARLY`       | :material-check:  | Yearly frequency
| 2             | `irispie.HALFYEARLY`   | :material-check:  | Half-yearly frequency
| 4             | `irispie.QUARTERLY`    | :material-check:  | Quarterly frequency
| 12            | `irispie.MONTHLY`      | :material-check:  | Monthly frequency
| 52            | `irispie.WEEKLY`       |                   | Weekly frequency
| 365           | `irispie.DAILY`        |                   | Daily frequency
| 0             | `irispie.INTEGER`      |                   | Integer frequency (numbered observations)
| -1            | `irispie.UNKNOWN`      |                   | Unknown or unspecified frequency


The most often direct use of `Frequencies` in frequency conversion methods, such
as `aggregate` and `disaggregate` for time [`Series`](series.md) and whenever a
custom check of time period or time series properties is needed.
    