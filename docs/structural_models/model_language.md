
# Model source language

The model source language is used for writing and structuring model source
code, which can be in the form of a single text file, multiple files, or a string.

The language comprises a number of keywords, each signifying the beginning of
a specific section, such as a section declaring the model variable names, or a
section defining the model equations. The sections can be arranged in any
order, and the same type of section can be repeated multiple times.


## Declaring model quantities

Keyword | Description | [`Simultaneous`](simultaneous.md) | [`Sequential`](sequential.md)
---|---|:---:|:---:
`!variables` | Declare endogenous/transition variables | :material-check: |
`!unanticipated_shocks` | Declare unanticipated shocks | :material-check: |
`!anticipated_shocks` | Declare anticipated shocks | :material-check: |
`!measurement_variables` | Declare measurement variables | :material-check: |
`!measurement_shocks` | Declare measurement shocks | :material-check: |
`!exogenous_variables` | Declare exogenous variables | :material-check: |
`!parameters` | Declare parameters | :material-check: | :material-check:


## Defining model equations

Keyword | Description | [`Simultaneous`](simultaneous.md) | [`Sequential`](sequential.md)
---|---|:---:|:---:
`!equations` | Define equations | :material-check: | :material-check:
`!measurement_equations` | Define measurement equations | :material-check: |



## Special operators inside equations

Operator | Description | [`Simultaneous`](simultaneous.md) | [`Sequential`](sequential.md)
---|---|:---:|:---:
`{±k}` | Time shift (`-` for lags, `+` for lead)| :material-check: | :material-check:
`!!` | Steady-state form of equation | :material-check: |
`===` | Identity sign | | :material-check:

