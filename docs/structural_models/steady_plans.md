
    


Categorical list of functions
-------------------------------

### Creating new steady plans ###

Function | Description
----------|------------
[`SteadyPlan`](#steadyplan) | Create new steady plan object


### Exogenizing and endogenizing steady-state values ###

Function | Description
----------|------------


### Fixing steady-state values ###

Function | Description
----------|------------
[`fix`](#fix) | Fix steady-state values
[`unfix`](#unfix) | Unfix steady-state values


### Getting information about steady plans ###

Function | Description
----------|------------
[`print_table`](#print_table) | Print the `SimulationPlan` as a table





Directly accessible properties
------------------------------

Property | Description
----------|------------



&#9744;&#160;`SteadyPlan`
---------------------------

==Create new steady plan object==
        



&#9744;&#160;`fix`
--------------------

==Fix steady-state values==
        



&#9744;&#160;`print_table`
----------------------------

==Print the `SimulationPlan` as a table==

    self.print_table()


### Input arguments ###

???+ input "self"
    `SimulationPlan` to be printed on the screen, with one row showing
    exogenized or endogenized data points grouped by the name and dates.


### Returns ###

Returns no value; the table is printed on the screen.
        



&#9744;&#160;`unfix`
----------------------

==Unfix steady-state values==
        