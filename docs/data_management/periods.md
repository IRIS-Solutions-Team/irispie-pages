
Time periods
=============

A time `Period` represents one single calendar period of time of a certain
frequency (and hence also a certain duration); the time period
[`Frequencies`](frequencies.md) are identified by an integer value.

Time `Periods` are used to timestamp data observations in time
[`Series`](series.md) objects, for basic calenadar time arithmetics, and for
creating time [`Spans`](spans.md).
    


Categorical list of functions
-------------------------------

### Creating new time periods ###

Function | Description
----------|------------
[irispie.dd](#irispiedd) | Create a daily-frequency time period or time span
[irispie.hh](#irispiehh) | Create a half-yearly-frequency time period or time span
[irispie.ii](#irispieii) | Create an integer-frequency time period or time span
[irispie.mm](#irispiemm) | Create a monthly-frequency time period or time span
[irispie.qq](#irispieqq) | Create a quarterly-frequency time period or time span
[irispie.yy](#irispieyy) | Create a yearly-frequency time period or time span


### Adding, subtracting, and comparing time periods ###

Function | Description
----------|------------
[!=](#!=) | True if time period is not equal to another time period
[+](#+) | Add integer to time period
[-](#-) | Subtract time period or integer from time period
[<](#<) | True if time period is earlier than another time period
[<=](#<=) | True if time period is earlier than or equal to another time period
[==](#==) | True if time period is equal to another time period
[>](#>) | True if time period is later than another time period
[>=](#>=) | True if time period is later than or equal to another time period
[shift](#shift) | Shift time period by a number of periods


### Converting time periods to different frequencies ###

Function | Description
----------|------------
[refrequent](#refrequent) | Convert time period to a new frequency
[to_ymd](#to_ymd) | Get year, month, and day of time period


### Converting time periods to strings ###

Function | Description
----------|------------
[to_iso_string](#to_iso_string) | ISO-8601 representation of time period
[to_sdmx_string](#to_sdmx_string) | SDMX representation of time period





Directly accessible properties
------------------------------

Property | Description
----------|------------
[frequency](#frequency) | Time frequency of the time period
[period](#period) | Period number within the calendar year
[year](#year) | Calendar year of the time period



Time period arithmetics
-------------------------

Time period arithmetics involve operations that can be performed either
between two time periods or between a time period and an integer.
The arithmetic operations include

* **Adding an integer**: Move a time period forward or backward by the
specified number of periods. The integer specifies how many periods of the
respective time frequency to move forward or backward.

* **Subtracting a time period**: Calculate the number of periods between
two time periods. Both periods must be of the same frequency.

* **Subtracting an integer**: Move a time period backward or forward by the
specified number of periods. The integer specifies how many periods of the
respective frequency to move backward or forward.

When performing arithmetic operations involving two time periods, it is necessary 
that both are of the same time frequency. Additionally, some operations involve a 
time period and an integer, such as adding or subtracting a certain number of 
periods represented by an integer.

These operations enable effective management of time period spans and
time-based calculations necessary for scheduling, forecasting, and
historical data analysis in various applications.
        



Time period comparison
------------------------

Time period comparison involves comparing two time periods to determine
their relative position in time. The comparison operations include the
following:

| Operation             | Description
|-----------------------|-------------
| `==`                  | Determine whether two time periods are equal.
| `!=`                  | Determine whether two time periods are not equal.
| `<`                   | Determine whether one time period is earlier than another.
| `<=`                  | Determine whether one time period is earlier than or equal to another.
| `>`                   | Determine whether one time period is later than another.
| `>=`                  | Determine whether one time period is later than or equal to another.

The comparison operations require that both time periods are of the same
time [Frequency](frequencies.md).
        



Time period constructors
--------------------------

Overview of time period constructors:

| Constructor         | Description
|---------------------|-------------
| `irispie.yy`        | Yearly period
| `irispie.hh`        | Half-yearly period
| `irispie.qq`        | Quarterly period
| `irispie.mm`        | Monthly period
| `irispie.dd`        | Daily period
| `irispie.ii`        | Integer period (numbered observations)


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
        



☐ `irispie.dd`
----------------

==Create a daily-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).
    



☐ `irispie.hh`
----------------

==Create a half-yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `irispie.ii`
----------------

==Create an integer-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `irispie.mm`
----------------

==Create a monthly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `irispie.qq`
----------------

==Create a quarterly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `irispie.yy`
----------------

==Create a yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




☐ `!=`
--------

==True if time period is not equal to another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `+`
-------

==Add integer to time period==

Add an integer value to a time period, moving it forward by the number of
periods (if positive) or backward (if negative).

    new_period = period + k
    new_period = k + period


### Input arguments ###


???+ input "period"
    Time period to which the integer is added.

???+ input "k"
    Integer value to add to the time period. Positive values move the
    period forward, while negative values move it backward. The addition is
    frequency specific.


### Returns ###


???+ returns "new_period"
    New time period resulting from the addition of the integer value.


### See also ###

* [Time period arithmetics](#time-period-arithmetics)
        



☐ `-`
-------

==Subtract time period or integer from time period==

Subtraction operations can be performed between two time periods or between a 
time period and an integer. These operations are crucial for calculating the 
distance between periods or adjusting a period's position in time.

* **Subtracting a time period**: Calculate the number of periods between
two time periods. Both periods must be of the same frequency.

* **Subtracting an integer**: Move a time period backward or forward by the
specified number of periods. The integer specifies how many periods of the
respective frequency to move backward or forward.


    result = self - other
    new_period = self - k


### Input arguments ###


???+ input "self"
    The reference time period from which `other` or `k` is subtracted.

???+ input "other"
    The time period to subtract from `self`. The `result` is the number of
    periods between `self` and `other`. The subtraction is frequency specific.

???+ input "k"
    Integer value to subtract from `self`. Positive values move the period
    backward, while negative values move it forward. The subtraction is
    frequency specific.


### Returns ###


???+ returns "result"
    The number of periods between two time periods if `other` is a `Period`.

???+ returns "new_period"
    A new `Period` object representing the time period shifted backward by the 
    specified number of periods if `other` is an integer.
    



☐ `<`
-------

==True if time period is earlier than another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `<=`
--------

==True if time period is earlier than or equal to another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `==`
--------

==True if time period is equal to another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `>`
-------

==True if time period is later than another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `>=`
--------

==True if time period is later than or equal to another time period==

See documentation for [time period comparison](#time-period-comparison).
        



☐ `refrequent`
----------------

==Convert time period to a new frequency==

Convert a time period to a new time frequency by specifying the new
frequency and, optionally, the position of the new time period within the
original time period. The conversion is frequency specific and may require
additional arguments.

    new_period = self.refrequent(
        new_freq,
        *,
        position="start",
    )


### Input arguments ###


???+ input "self"
    Time period to convert to a new time frequency.

???+ input "new_freq"
    New time frequency to which the time period is converted.

???+ input "position"
    Position of the new time period within the original time period. This option
    is effective when the conversion is ambiguous, i.e. from a lower frequency
    period to a higher frequency period. See the position options in
    [`to_ymd`](#to_ymd).


### Returns ###


???+ returns "new_period"
    New time period resulting from the conversion to the new time frequency.
        



☐ `shift`
-----------

==Shift time period by a number of periods==

Shift a time period forward or backward by the specified number of periods. 

    self.shift(k)


### Input arguments ###


???+ input "self"
    Time period to shift forward or backward.

???+ input "k"
    Integer value specifying the number of periods to move the time period.
    Positive values move the period forward, while negative values move it
    backward. The shift is frequency specific.


### Returns ###


Returns no value; the time period is modified in place.
        



☐ `to_iso_string`
-------------------

==ISO-8601 representation of time period==

Get the ISO-8601 string representation of the time period. The ISO-8601
string format is `yyyy-mm-dd` where `yyyy` is the calendar year, `mm` is
the month of the year, and `dd` is the day of the month, all represented as
integers.

    iso_string = self.to_iso_string(*, position="start", )


### Input arguments ###


???+ input "self"
    Time period to convert to an ISO string.

???+ input "position"
    Position that determines the day of the month and the month of the year
    of time periods with time frequency lower than daily. See the position
    options in [`to_ymd`](#to_ymd).


### Returns ###


???+ returns "iso_string"
    ISO-8601 string representation of the time period.
        



☐ `to_sdmx_string`
--------------------

==SDMX representation of time period==

The SDMX string representation of the time periods is a standardized format
used in statistical data exchange. The SDMX string format is frequency
specific:

Time frequency | SDMX format   | Example
---------------|---------------|--------
Yearly         | `yyyy`        | `2030`
Half-yearly    | `yyyy-Hh`     | `2030-H1`
Quarterly      | `yyyy-Qq`     | `2030-Q1`
Monthly        | `yyyy-mm`     | `2030-01`
Weekly         | `yyyy-Www`    | `2030-W01`
Daily          | `yyyy-mm-dd`  | `2030-01-01`
Integer        | `(n)`         | `(1)`

where lowercase letters represent the respective time period components
(integer values) and uppercase letters are literals.


    sdmx_string = self.to_sdmx_string()


### Input arguments ###


???+ input "self"
    Time period to convert to an SDMX string.


### Returns ###


???+ returns "sdmx_string"
    SDMX string representation of the time period.
        



☐ `to_ymd`
------------

==Get year, month, and day of time period==

Get the calendar year, month, and day of the time period as a tuple of
integers.

    year, month, day = self.to_ymd(*, position="start", )


### Input arguments ###


???+ input "self"
    Time period to extract the year, month, and day from.

???+ input "position"
    Position that determins the day of the month and the month of the year
    of time periods with time frequency lower than daily. The position can
    be one of the following:

    * `"start"`: Start of the time period (placed on the 1st day of the
    first month within the original period).

    * `"middle"`: Middle of the time period (placed on the 15th day of the
    middle month within the original period).

    * `"end"`: End of the time period (placed on the last day of the last
    month within the original period).


### Returns ###


???+ returns "year"
    Calendar year of the time period.

???+ returns "month"
    Month of the year of the time period.

???+ returns "day"
    Day of the month of the time period.
        