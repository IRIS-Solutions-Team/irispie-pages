
Time periods
=============

Time periods represent one single calendar period of time of a given
frequency (yearly, half-yearly, quarterly, monthly, daily, or a special
integer frequency). The time `Periods` are used to time stamp individual
observations in [`Series`](series.md) objects.

Time spans represent a range of time periods, from a start period to an end
period.
    


Categorical list of functions
-------------------------------

### Creating new time periods ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;dd](#dd) | Create a daily-frequency time period or time span
[:octicons-file-24:&nbsp;hh](#hh) | Create a half-yearly-frequency time period or time span
[:octicons-file-24:&nbsp;ii](#ii) | Create an integer-frequency time period or time span
[:octicons-file-24:&nbsp;mm](#mm) | Create a monthly-frequency time period or time span
[:octicons-file-24:&nbsp;qq](#qq) | Create a quarterly-frequency time period or time span
[:octicons-file-24:&nbsp;yy](#yy) | Create a yearly-frequency time period or time span





Directly accessible properties
------------------------------

Property | Description
----------|------------



Time period constructors
--------------------------

Overview of time period constructors:

| Constructor | Description
|-------------|-------------
| `yy`        | Yearly period
| `hh`        | Half-yearly period
| `qq`        | Quarterly period
| `mm`        | Monthly period
| `dd`        | Daily period
| `ii`        | Integer period (numbered observations)


### Syntax for creating new time periods ###

    per = yy(year)
    per = hh(year, halfyear)
    per = qq(year, quarter)
    per = mm(year, month)
    per = dd(year, month, day_in_month)
    per = dd(year, None, day_in_year)
    per = ii(number)


### Input arguments ###

???+ input "year"
    Calendar year as integer.

???+ input "halfyear"
    Half-year as integer, 1 or 2.

???+ input "quarter"
    Quarter as integer, 1 to 4.

???+ input "month"
    Month as integer, 1 to 12.

???+ input "day_in_month"
    Day in month as integer, 1 to 31.

???+ input "day_in_year"
    Day in year as integer, 1 to 365 (or 366 in leap years).

???+ input "number"
    Observation number as integer.


### Returns ###


???+ returns "per"
    A `Period` object representing one single time period of a given
    frequency.
        



☐ `dd`
--------

==Create a daily-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).
    



☐ `hh`
--------

==Create a half-yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `ii`
--------

==Create an integer-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `mm`
--------

==Create a monthly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `qq`
--------

==Create a quarterly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `yy`
--------

==Create a yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).
