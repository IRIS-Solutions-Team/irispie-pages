
Writing `Sequential` models
============================

`Sequential` model objects are created from model source code (either a
text file, a collection of multiple text files, or a text string) written
in [`the model source language`](../model_language.md).


Structure of `Sequential` model source code
--------------------------------------------

Each `Sequential` model source code must consist of at least one
[`!equations`](../model_language.md#declaring-model-quantities)
section, and any number of
[`!parameters`](../model_language.md#declaring-model-quantities)
sections.


`Sequential` equations
-----------------------

Each equation of a `Sequential` model must be written in one of the
following forms:

1. Nonidentity equation with a plain LHS name

```
lhs_name = rhs_expression;
```

1. Nonidentity equation with a LHS transformation

```
transform(lhs_name) = rhs_expression;
```

where `transform` is one of the transformations listed below.


1. Identity with a plain LHS name

```
lhs_name === rhs_expression;
```

1. Identity with an LHA transformation
```
transform(lhs_name) === rhs_expression;
```

where `transform` is one of the transformations listed below.


LHS transformations
--------------------

Transformation | Description
---|---
`log` | Natural logarithm
`diff` | First difference (period on period)
`diff_log` | First difference of logs (period on period)
`pct` | Percent change (period on period)
`roc` | Gross rate of change (period on period)

