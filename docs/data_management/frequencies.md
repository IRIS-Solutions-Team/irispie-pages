
Time frequencies
=================

Time frequencies are simple integer values that represent the number of
time periods within a year. For convenience, the `Frequency` enum provides
a set of predefined names for all the time frequencies available. The
`Frequencies` are furthermore classified into regular and irregular
frequencies. Regular frequencies are those that are evenly spaced within a
year.

| Integer value | `Frequency` enum       | Regular           | Description
|--------------:|------------------------|:-----------------:|-------------
| 1             | `irispie.YEARLY`       | :material-check:  | Yearly period
| 2             | `irispie.HALFYEARLY`   | :material-check:  | Half-yearly period
| 4             | `irispie.QUARTERLY`    | :material-check:  | Quarterly period
| 12            | `irispie.MONTHLY`      | :material-check:  | Monthly period
| 52            | `irispie.WEEKLY`       |                   | Weekly period
| 365           | `irispie.DAILY`        |                   | Daily period
| 0             | `irispie.INTEGER`      |                   | Integer period (numbered observations)

The time `Frequencies` are most often used in frequency
conversion methods, such as `convert_to_new_freq` for time
[`Periods`](periods.md), or `aggregate` and `disaggregate` for time
[`Series`](series.md).
    