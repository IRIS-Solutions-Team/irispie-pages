
Time periods
=============

A time `Period` represents one single calendar period of time of a certain
frequency (and hence also a certain duration); the time period
[`Frequencies`](frequencies.md) are identified by an integer value.

Time `Periods` are used to timestamp data observations in time
[`Series`](time_series.md) objects, for basic calenadar time arithmetics, and for
creating time [`Spans`](spans.md).
    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`frequency` | Time frequency of the time period
`segment` | Segment within the calendar year
`year` | Calendar year of the time period





Categorical list of functions
-------------------------------

### Creating new time periods ###

Function | Description
----------|------------
[`irispie.dd`](#irispiedd) | Create a daily-frequency time period or time span
[`irispie.hh`](#irispiehh) | Create a half-yearly-frequency time period or time span
[`irispie.ii`](#irispieii) | Create an integer-frequency time period or time span
[`irispie.mm`](#irispiemm) | Create a monthly-frequency time period or time span
[`irispie.qq`](#irispieqq) | Create a quarterly-frequency time period or time span
[`irispie.yy`](#irispieyy) | Create a yearly-frequency time period or time span
[`Period.from_iso_string`](#periodfrom_iso_string) | Create time period from ISO-8601 string
[`Period.from_python_date`](#periodfrom_python_date) | Create time period from Python datetime
[`Period.from_sdmx_string`](#periodfrom_sdmx_string) | Create time period from SDMX string
[`Period.from_year_segment`](#periodfrom_year_segment) | Create time period from year and segment
[`Period.from_ymd`](#periodfrom_ymd) | Create time period from year, month, and day
[`Period.today`](#periodtoday) | Create time period for today


### Adding, subtracting, and comparing time periods ###

Function | Description
----------|------------
[`shift`](#shift) | Shift time period by a number of periods


### Converting time periods to different frequencies ###

Function | Description
----------|------------
[`refrequent`](#refrequent) | Convert time period to a new frequency


### Converting time periods to different representations ###

Function | Description
----------|------------
[`to_python_date`](#to_python_date) | Convert time period to Python date object
[`to_ymd`](#to_ymd) | Get year, month, and day of time period


### Converting time periods to strings ###

Function | Description
----------|------------
[`to_compact_string`](#to_compact_string) | Compact representation of time period
[`to_iso_string`](#to_iso_string) | ISO-8601 representation of time period
[`to_sdmx_string`](#to_sdmx_string) | SDMX representation of time period



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
        



&#9744;&#160;`irispie.dd`
---------------------------

==Create a daily-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).
    



&#9744;&#160;`irispie.hh`
---------------------------

==Create a half-yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




&#9744;&#160;`irispie.ii`
---------------------------

==Create an integer-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




&#9744;&#160;`irispie.mm`
---------------------------

==Create a monthly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




&#9744;&#160;`irispie.qq`
---------------------------

==Create a quarterly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




&#9744;&#160;`irispie.yy`
---------------------------

==Create a yearly-frequency time period or time span==

See documentation for the [`Period` constructors](#time-period-constructors)
and the [`Span` constructors](spans.md).




&#9744;&#160;`Period.from_iso_string`
---------------------------------------

==Create time period from ISO-8601 string==

Create a time period from an ISO-8601 string representation. The ISO-8601
string format is `yyyy-mm-dd` where `yyyy` is the calendar year, `mm` is
the month of the year, and `dd` is the day of the month, all represented as
integers.

    period = Period.from_iso_string(
        iso_string,
        *,
        frequency=Frequency.DAILY,
    )


### Input arguments ###


???+ input "iso_string"
    ISO-8601 string representation of the time period.

???+ input "frequency"
    Time frequency of the time period; if `None`, a time period of daily
    frequency will be created.


### Returns ###


???+ returns "period"
    Time period object created from the ISO-8601 string.
        



&#9744;&#160;`Period.from_python_date`
----------------------------------------

==Create time period from Python datetime==

Create a time period from a Python `datetime` object. The time period is
created based on the time frequency specified.

    period = Period.from_python_date(
        python_date,
        *,
        frequency=Frequency.DAILY,
    )


### Input arguments ###


???+ input "python_date"
    Python `datetime.datetime` or `datetime.date` object representing the time
    period.

???+ input "frequency"
    Time frequency of the time period; if `None`, a time period of daily
    frequency will be created.


### Returns ###


???+ returns "period"
    Time period object created from the provided Python `datetime` object.
        



&#9744;&#160;`Period.from_sdmx_string`
----------------------------------------

==Create time period from SDMX string==

Create a time period from an SDMX string representation. The SDMX string
format is frequency specific and represents the time period as a string
literal.

    period = Period.from_sdmx_string(
        sdmx_string,
        frequency=Frequency.DAILY,
    )

### Input arguments ###

???+ input "sdmx_string"
    SDMX string representation of the time period.

???+ input "frequency"
    Time frequency of the time period. If `None`, the frequency is inferred
    from the SDMX string itself; supplying the frequency is more efficient
    if it is known in advance.

### Returns ###

???+ returns "period"
    Time period object created from the SDMX string.
        



&#9744;&#160;`Period.from_year_segment`
-----------------------------------------

==Create time period from year and segment==

Create a time period from the calendar year and a segment of the year. The
interpretation of the segment as well as the type of the time period created
depends on the time frequency specified.

    period = Period.from_year_segment(
        freq,
        year,
        segment,
    )

### Input arguments ###

???+ input "freq"
    Time frequency of the time period.

???+ input "year"
    Calendar year as integer.

???+ input "segment"
    Segment of the year as integer; the segment can be a half-year, quarter,
    month, or day, depending on the time frequency, `freq`.

### Returns ###

???+ returns "period"
    Time period object created from the year and segment.
        



&#9744;&#160;`Period.from_ymd`
--------------------------------

==Create time period from year, month, and day==

Create a time period from the calendar year, month, and day. The time period
is created based on the time frequency specified.

    period = Period.from_ymd(
        freq,
        year,
        month=1,
        day=1,
    )

### Input arguments ###

???+ input "freq"
    Time frequency of the time period.

???+ input "year"
    Calendar year as integer.

???+ input "month"
    Month of the year as integer.

???+ input "day"
    Day of the month as integer.

### Returns ###

???+ returns "period"
    Time period object created from the year, month, and day.
        



&#9744;&#160;`Period.today`
-----------------------------

==Create time period for today==

Create a time period for the current date. The time period is created based
on the time frequency specified.

    period = Period.today(freq)

### Input arguments ###

???+ input "freq"
    Time frequency of the time period.

### Returns ###

???+ returns "period"
    Time period object for the current date.
        



&#9744;&#160;`get_distance_from_origin`
-----------------------------------------

==Get distance from origin time period==

Get the distance of the time period from the origin time period. The origin time
period is currently set to the beginning of year 2020 for all calendar periods,
and to 0 for integer periods.

    distance = self.get_distance_from_origin()

### Returns ###

???+ returns "distance"
    Distance of the `self` time period from the origin time period.
        



&#9744;&#160;`refrequent`
---------------------------

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
        



&#9744;&#160;`shift`
----------------------

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
        



&#9744;&#160;`to_compact_string`
----------------------------------

==Compact representation of time period==

The compact string format is frequency specific:

Time frequency | Compact format   | Example
---------------|------------------|--------
Yearly         | `yyY`            | `30Y`
Half-yearly    | `yyHh`           | `30H1`
Quarterly      | `yyQq`           | `30Q1`
Monthly        | `yyMmm`          | `30M01`
Weekly         | `yyWww`          | `30W01`
Daily          | `yymmmdd`        | `30Jan01`
Integer        | `(n)`            | `(1)`

where lowercase letters represent the respective time period components
(integer values) and uppercase letters are literals.


    compact_string = self.to_compact_string()


### Input arguments ###


???+ input "self"
    Time period to convert to a compact string.


### Returns ###


???+ returns "compact_string"
    Compact string representation of the time period.
        



&#9744;&#160;`to_iso_string`
------------------------------

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
        



&#9744;&#160;`to_python_date`
-------------------------------


==Convert time period to Python date object==


Convert a time period to a Python date object. The date object is created based
on the year, month, and day of the time period.


    date = self.to_python_date(
        position="middle",
    )


### Input arguments ###


???+ input "self"
    Time period to convert to a Python date object.

???+ input "position"
    Position that determines the day of the month and the month of the year
    of time periods with time frequency lower than daily. The position can
    be one of the following:

    * `"start"`: Start of the time period (placed on the 1st day of the
    first month within the original period).

    * `"middle"`: Middle of the time period (placed on the 15th day of the
    middle month within the original period).

    * `"end"`: End of the time period (placed on the last day of the last
    month within the original period).


### Returns ###


???+ returns "date"
    Python date object representing the time period.

        



&#9744;&#160;`to_sdmx_string`
-------------------------------

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
        



&#9744;&#160;`to_ymd`
-----------------------

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
        