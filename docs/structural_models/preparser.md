
# Preparser

The preparser provides a variety of convenience commands that simplify the
process of writing model source code.


List of preparser commands
---------------------------


## For loops

A for loop can be used to parameterize and repeat certain parts of the model
source code.

### Abbreviated syntax with implicit control name

    !for a, b, c !do
        ...
    !end

### Full syntax with explicit control name

    !for ?name = a, b, c !do
        ...
    !end


## If-then branches


    !if condition !then
        ...
    !else
        ...
    !end



## Comments

Comments can be either line comments (from a line comment sign, `#`, until the end of
the line) or block comments (from an opening sign, `#{`, until the closing sign,
`#}`)

### Line comments

    # This is a line comment


### Block comments

    #{ This is a block ...
    ...comment
    #}



## Pseudofunctions

Pseudofunctions offer a compact notation for frequently used temporal
transformations. The pseudofunctions are replaced by a literal text
representation of the corresponding expression, for instance

```
diff(x + y)
```

is replaced by

```
((x + y) - (x[-1] + y[-1]))
```


Pseudofunction | Description | [`Simultaneous`](simultaneous.md) | [`Sequential`](sequential.md)
---------------|-------------|:---------------------------------:|:-----------------------------:
`diff` | Expands to first difference | :material-check: | :material-check:
`diff_log` | Expands to first difference of logarithms | :material-check: | :material-check:
`roc` | Expands to gross rate of change | :material-check: | :material-check:
`pct` | Expands to percent change | :material-check: | :material-check:
`mov_sum` | Expands to moving sum | :material-check: | :material-check:
`mov_avg` | Expands to moving average | :material-check: | :material-check:
`mov_prod`| Expands to moving product | :material-check: | :material-check:


Each pseudofunction can take one optional parameter, a time lag with a
specific meaning. These parameters must be non-zero negative values.


Pseudofunction | Default parameter | Meaning
---------------|------------------:|---------
`diff` | `-1 `       | Number of periods over which the first difference is calculated
`diff_log` | `-1`    | Number of periods over which the first difference of logarithms is calculated
`roc` | `-1`         | Number of periods over which the rate of change is calculated
`pct` | `-1`         | Number of periods over which the percent change is calculated
`mov_sum` | `-4`     | Number of periods in the moving window, including the current period
`mov_avg` | `-4`     | Number of periods in the moving window, including the current period
`mov_prod` | `-4`    | Number of periods in the moving window, including the current period


## Substitutions


    !substitutions

        name1 := expression1;
        name2 := expression2;
        ...



