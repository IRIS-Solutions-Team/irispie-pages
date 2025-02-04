
Time spans
============

Time spans represent a range of time periods of the same time frequency,
from a start period to an end period (possibly with a step size other than
1), going either forward or backward.
    


Categorical list of functions
-------------------------------

### Creating new time spans ###

Function | Description
----------|------------
[`Span`](#span) | Create a new time span


### Arithmetic operations on time spans ###

Function | Description
----------|------------
[`+`](#+) | Add an offset to the time span
[`-`](#-) | Subtract an offset or a Period from the time span


### Manipulating time spans ###

Function | Description
----------|------------
[`reverse`](#reverse) | Reverse the time span
[`shift`](#shift) | Shift the entire time span
[`shift_end`](#shift_end) | Shift the end of the time span
[`shift_start`](#shift_start) | Shift the start period of the time span


### Converting time spans to strings ###

Function | Description
----------|------------
[`to_iso_strings`](#to_iso_strings) | Convert time span periods to ISO-8601 representations
[`to_sdmx_strings`](#to_sdmx_strings) | Convert time span periods to SDMX representations





Directly accessible properties
------------------------------

Property | Description
----------|------------
`direction` | Direction of the time span
`end` | End period of the time span
`frequency` | Frequency of the time span
`start` | Start period of the time span
`step` | Step size of the time span



&#9744;&#160;`Span`
---------------------

==Create a new time span==


### Using the `Span` constructor ###

    span = Span(start_per, end_per, step=1)


### Shorthand using the `>>` and `<<` operators ###

    span = start_per >> end_per #[^1]
    span = end_per << start_per #[^2]

1. Equivalent to `Span(start_per, end_per, step=1)`
2. Equivalent to `Span(end_per, start_per, step=-1)`
        



&#9744;&#160;`+`
------------------

==Add an offset to the time span==

Shifts both the start and end of the time span by a specified number of periods.
This method is used to adjust the entire span forward or backward in time. It can be 
used either by adding the offset to the span (`span + offset`) or the offset to the 
span (`offset + span`), effectively creating a new time span that begins and ends
earlier or later than the original.

    new_span = self + offset
    new_span = offset + self

### Input arguments ###

???+ input "self"
    The time span to be adjusted.

???+ input "offset"
    The number of periods by which to shift the time span. This must be an integer,
    where positive values indicate a forward shift and negative values indicate a 
    backward shift.

### Returns ###

???+ returns "new_span"
    A new `Span` object representing the time span shifted by the specified number of
    periods.
        



&#9744;&#160;`-`
------------------

==Subtract an offset or a Period from the time span==

Adjusts the time span by shifting it backward by a specified number of periods or 
computes a range of integers when a `Period` is subtracted. This method can be used 
to shift the entire span backward in time by an integer offset or to calculate the 
distance between each period in the span and a given `Period`.

    new_span = self - offset
    range_result = self - period


### Input arguments ###


???+ input "self"
    The time span from which the offset or a `Period` is to be subtracted.

???+ input "other"
    If an integer, the number of periods by which to shift the time span backward.
    If a `Period`, a specific period used to calculate the difference in periods 
    between this `Period` and each period within the time span.


### Returns ###


???+ returns "new_span" if `other` is an integer
    A new `Span` object representing the time span shifted backward by the specified 
    number of periods.

???+ returns "range_result" if `other` is a `Period`
    A standard range object containing the distances in periods from each period within
    the span to the specified `Period`.
        



&#9744;&#160;`reverse`
------------------------

==Reverse the time span==

Reverses the direction of the time span, so that the start period becomes
the end period and vice versa.

    self.reverse()


### Input arguments ###

???+ input "self"
    The time span to be reversed.


### Returns ###

The time span is reversed in place.
        



&#9744;&#160;`shift`
----------------------

==Shift the entire time span==

Shifts the entire time span forward or backward by a specified number of
periods. This method adjusts both the start and end of the span simultaneously,
keeping the length of the span unchanged but moving it entirely to a new
position in the timeline.

    self.shift(by)

### Input arguments ###

???+ input "self"
    The time span that will be shifted along the timeline.

???+ input "by"
    The number of periods to shift the time span. Positive values shift the span 
    forward, while negative values shift it backward.

### Returns ###

???+ returns "None"
    This method modifies `self` in-place and does not return a value.

        



&#9744;&#160;`shift_end`
--------------------------

==Shift the end of the time span==

Shifts the end of the time span by a specified number of periods. This
operation modifies the end boundary of the time span, effectively changing its
length. Adjusting the end allows for extension or reduction of the span
depending on the direction and magnitude of the shift.

    self.shift_end(by)

### Input arguments ###

???+ input "self"
    The time span within which the end will be shifted.

???+ input "by"
    The number of periods by which the end will be shifted. This can be
    positive (to extend the span by moving the end forward) or negative
    (to reduce the span by moving the end backward).

### Returns ###

???+ returns "None"
    This method modifies `self` in-place and does not return a value.
        



&#9744;&#160;`shift_start`
----------------------------

==Shift the start period of the time span==

Shifts the start period of the time span by a specified number of periods. This
operation adjusts the start boundary of the time span, effectively changing its
length depending on the direction and magnitude of the shift.

    self.shift_start(by)

### Input arguments ###

???+ input "self"
    The time span within which the start period will be shifted.

???+ input "by"
    The number of periods by which the start period will be shifted. This can be
    positive (to move the start period forward, reducing the span length) or
    negative (to move it backward, increasing the span length).

### Returns ###

This method modifies the object in place and does not return a value.
        



&#9744;&#160;`to_iso_strings`
-------------------------------

==Convert time span periods to ISO-8601 representations==

Converts each period within the time span to an ISO-8601 string format. 

    iso_strings = self.to_iso_strings(*, position="start", )


### Input arguments ###


???+ input "self"
    The time span whose periods are to be converted to ISO-8601 strings.

???+ input "position"
    The position within each period to use when converting to an ISO-8601
    date string. See the documentation for the
    [`to_ymd`](periods.md#to_ymd) method of time [`Periods`](periods.md).


### Returns ###


???+ returns "iso_strings"
    A tuple of ISO-8601 date strings representing each period in the time
    span.
        



&#9744;&#160;`to_sdmx_strings`
--------------------------------

==Convert time span periods to SDMX representations==

Converts each period within the time span to a SDMX string format. 

    sdmx_strings = self.to_sdmx_strings()


### Input arguments ###


???+ input "self"
    The time span whose periods are to be converted to SDMX strings.


### Returns ###


???+ returns "sdmx_strings"
    A tuple of SDMX strings representing each period in the time span.


### See also ###

* [`to_sdmx_string`](periods.md#to_sdmx_string) method of time [`Periods`](periods.md)
        