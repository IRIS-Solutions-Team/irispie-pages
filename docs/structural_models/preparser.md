
# Preparser and pseudofunctions

The preparser provides a variety of convenience commands that simplify the
process of writing model source code. Pseudofunctions provide a compact notation
for frequently used temporal transformations. The preparser commands and
pseudofunctions are processed before the model source code is parsed. The
preparser commands and pseudofunctions can be used in both
[`Simultaneous`](simultaneous.md) and [`Sequential`](sequential.md) models.


# List of preparser commands

Command | Description
--------|-------------
`!for ... !do ... !end` | For loops
`!if ... !then ... !else ... !end` | If-then-else branches
`!list(...)` | Lists
`# ...` | Line comments
`#{ ... #}` | Block comments


## For loops

A for loop can be used to parameterize and repeat certain parts of the model
source code. For loops can be nested. The loop body is delimited by the `!do` and
`!end` keywords. The loop iterates over a list of tokens, assigning each token in
turn to a control name. The control name can be implicit (the literal `?`) or
explicit (a name starting with a `?` sign). If the control name is explicit, it
can be parenthesized (the name is enclosed in parentheses) or not. The loop body
can contain occurrences of the control name, which are replaced by the currently
assigned token from the list.


### Abbreviated syntax with implicit control name

    !for a, b, c !do
        ...
    !end

Any occurrence of the literal `?` in the loop body is replaced by the currently
assigned token from the list `a`, `b`, `c`.


### Full syntax with explicit control name

    !for ?name = a, b, c !do
        ...
    !end

Any occurrence of the literal `?name` in the loop body is replaced by the currently
assigned token from the list `a`, `b`, `c`.


### Full syntax with parenthesized explicit control name

    !for ?(name) = a, b, c !do
        ...
    !end

Any occurrence of the literal `?(name)` in the loop body is replaced by the
currently assigned token from the list `a`, `b`, `c`.

Any occurrence of `?{name}` in the loop body is replaced by the uppercased token
currently assigned to `?(name)`.

Any occurrence of `?{name}` in the loop body is replaced by the lowercased token
currently assigned to `?(name)`.


## If-then-else branches

The if-then-else command can be used to conditionally include or exclude parts
of the model source code.

    !if condition !then
        ...
    !else
        ...
    !end



## Lists

    abc`n
    def`n
    ghi`x

    ...

    !list(`n)
    !list(`x)


The list command expands to the comma-separated list of all tokens (names) that were
tagged a backtick followed by the name of the list. In the example above, the
command `!list(`n)` expands to `abc, def`, and the command `!list(`x)` expands
to `ghi`.


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


