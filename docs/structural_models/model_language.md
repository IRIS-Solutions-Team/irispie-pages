
# Model source language

The model source language is used for writing and structuring model source
code, which can be in the form of a single text file, multiple files, or a string.

The language comprises a number of keywords, each signifying the beginning of
a specific section, such as a section declaring the model variable names, or a
section defining the model equations. The sections can be arranged in any
order, and the same type of section can be repeated multiple times.


## Declaring model quantities

Keyword | Description | [`Simultaneous`](simultaneous_models) | [`Sequential`](sequential_models)
---|---|:---:|:---:
`!variables` | Declare endogenous/transition variables | &#10003; |
`!unanticipated_shocks` | Declare unanticipated shocks | &#10003; |
`!anticipated_shocks` | Declare anticipated shocks | &#10003; |
`!measurement_variables` | Declare measurement variables | &#10003; |
`!measurement_shocks` | Declare measurement shocks | &#10003; |
`!exogenous_variables` | Declare exogenous variables | &#10003; |
`!parameters` | Declare parameters | &#10003; | &#10003


## Defining model equations

Keyword | Description | [`Simultaneous`](simultaneous_models) | [`Sequential`](sequential_models)
---|---|:---:|:---:
`!equations` | Define equations | &#10003; | &#10003;
`!measurement_equations` | Define measurement equations | &#10003; |

