
Time spans
============

Time spans represent a range of time periods of the same date frequency,
from a start period to an end period (possibly with a step size other than
1), going either forward or backward.
    


Categorical list of functions
-------------------------------

### Creating new time spans ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;Span](#span) | Create a time span


### Time span manipulation ###

Function | Description
----------|------------
[:octicons-file-24:&nbsp;reverse](#reverse) | Reverse the time span





Directly accessible properties
------------------------------

Property | Description
----------|------------



☐ `Span`
----------

==Create a time span==


### Using the `Span` constructor ###

    span = Span(start_per, end_per, step=1)


### Shorthand using the `>>` and `<<` operators ###

    span = start_per >> end_per #[^1]
    span = end_per << start_per #[^2]

1. Equivalent to `Span(start_per, end_per, step=1)`
2. Equivalent to `Span(end_per, start_per, step=-1)`
        



☐ `reverse`
-------------

==Reverse the time span==

Reverses the direction of the time span, so that the start period becomes
the end period and vice versa.


    self.reverse()


### Input arguments ###

???+ input "self"
    The time span to be reversed.


### Returns ###

The time span is reversed in place.
        