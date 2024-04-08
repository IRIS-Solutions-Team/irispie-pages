
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





Directly accessible properties
------------------------------

Property | Description
----------|------------



☐ `Span`
----------

==Create a time span==


    span = Span(start_per, end_per, step=1)
    span = start_per >> end_per
    span = end_per << start_per

        