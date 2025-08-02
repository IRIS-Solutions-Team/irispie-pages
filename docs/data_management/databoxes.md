
Databoxes
==========

`Databoxes` extend the standard `dict` class (technically, they are a
subclass), serving as a universal tool for storing and manipulating
unstructured data organized as key-value pairs. The values stored within
`Databoxes` can be of any type.

`Databoxes` can use any methods implemented for the standard `dict`
objects, and have additional functionalities for data item manipulation,
batch processing, importing and exporting data, and more.
    


Directly accessible properties
------------------------------

Property | Description
----------|------------
`num_items` | Number of items in the databox





Categorical list of functions
-------------------------------

### Creating a new Databox ###

Function | Description
----------|------------
[`Databox.empty`](#databoxempty) | Create an empty Databox
[`Databox.from_array`](#databoxfrom_array) | Create a new `Databox` from a numpy array
[`Databox.from_csv_file`](#databoxfrom_csv_file) | Create a new Databox by reading time series from a CSV file
[`Databox.from_dict`](#databoxfrom_dict) | Create a new `Databox` from a `dict`
[`steady`](#steady) | Create a steady-state Databox for a model
[`zero`](#zero) | Create a zero-state Databox for a model


### Copying and converting a Databox ###

Function | Description
----------|------------
[`shallow`](#shallow) | Create a shallow copy of the Databox
[`to_dict`](#to_dict) | Convert a Databox to a plain dictionary


### Acquiring data via third-party APIs ###

Function | Description
----------|------------
[`_from_fred`](#_from_fred) | Download time series from FRED (St Louis Fed Database)


### Getting information about a Databox ###

Function | Description
----------|------------
[`filter`](#filter) | Filter items in a Databox
[`get_description`](#get_description) | Get description attached to an object
[`get_missing_names`](#get_missing_names) | Identify names not present in a Databox
[`get_names`](#get_names) | Get item names from a Databox
[`get_series_names_by_frequency`](#get_series_names_by_frequency) | Retrieve time series names by frequency
[`get_span_by_frequency`](#get_span_by_frequency) | Retrieve the date span for time series by frequency
[`set_description`](#set_description) | Set the description for an object


### Manipulating a Databox ###

Function | Description
----------|------------
[`apply`](#apply) | Apply a function to items in a Databox
[`clip`](#clip) | Clip the span of time series in a Databox
[`copy`](#copy) | Create a copy of the Databox
[`keep`](#keep) | Keep specified items in a Databox
[`minus_control`](#minus_control) | Subtract control values from a Databox
[`remove`](#remove) | Remove specified items from a Databox
[`rename`](#rename) | Rename items in a Databox


### Evaluating a Databox ###

Function | Description
----------|------------
[`evaluate_expression`](#evaluate_expression) | Evaluate an expression within a Databox context


### Manipulating multiple Databoxes ###

Function | Description
----------|------------
[`_merge`](#_merge) | Merge Databoxes
[`overlay`](#overlay) | Overlay another Databox time series onto the ones in the current Databox
[`prepend`](#prepend) | Prepend time series data to a Databox
[`underlay`](#underlay) | Underlay another Databox time series beneath those in the current Databox


### Extracting data from a Databox ###

Function | Description
----------|------------
[`array_from_series`](#array_from_series) | Retrieve time series data into a numpy array


### Importing and exporting a Databox ###

Function | Description
----------|------------
[`from_pickle_file`](#from_pickle_file) | Read a Databox from a pickled file
[`to_csv_file`](#to_csv_file) | Write Databox time series to a CSV file
[`to_json`](#to_json) | Save a Databox to a JSON file
[`to_pickle_file`](#to_pickle_file) | Write Databox to a pickle file



&#9744;&#160;`Databox.empty`
------------------------------

==Create an empty Databox==

Generate a new, empty Databox instance. This class method is useful for 
initializing a Databox without any pre-existing data.

    Databox.empty()


### Input arguments ###

No input arguments are required for this method.


### Returns ###


???+ returns "Databox"
    Returns a new instance of an empty Databox.
        



&#9744;&#160;`Databox.from_array`
-----------------------------------

==Create a new `Databox` from a numpy array==

Convert a two-dimensional [numpy](https://numpy.org) array data into a
Databox, with the individual time series created from the rows or columns
of the numeric array.

    self = Databox.from_array(
        array,
        names,
        *,
        descriptions=None,
        periods=None,
        start=None,
        target_db=None,
        orientation="vertical",
    )


### Input arguments ###


???+ input "array"
    A numpy array containing the data to be included in the Databox.

???+ input "names"
    A sequence of names corresponding to the series in the array.

???+ input "descriptions"
    Descriptions for each series in the array.

???+ input "periods"
    An iterable of time periods corresponding to the rows of the array. Used if the data
    represents time series.

???+ input "start"
    The start period for the time series data. Used if 'periods' is not provided.

???+ input "target_db"
    An existing Databox to which the array data will be added. If `None`, a new 
    Databox is created.

???+ input "orientation"
    The orientation of the array, indicating how time series are arranged: 

    * `"horizontal"` means each row is a time series;

    * `"vertical"` means each column is a time series.


### Returns ###


???+ returns "self"
    Returns a new Databox populated with the data from the numpy array.
        



&#9744;&#160;`Databox.from_csv_file`
--------------------------------------


==Create a new Databox by reading time series from a CSV file==


    self = Databox.from_csv_file(
        file_name,
        *,
        period_from_string=None,
        start_period_only=False,
        description_row=False,
        delimiter=",",
        csv_reader_settings={},
        numpy_reader_settings={},
        name_row_transform=None,
    )


### Input arguments ###


???+ input "file_name"
    Path to the CSV file to be read.

???+ input "period_from_string"
    A callable for creating date objects from string representations. If `None`,
    a default method expecting the SDMX string format is used.

???+ input "start_period_only"
    If `True`, only the start date of each time series is parsed from the CSV;
    subsequent periods are inferred based on frequency.

???+ input "description_row"
    Indicates if the CSV contains a row for descriptions of the time series.
    Defaults to `False`.

???+ input "delimiter"
    Character used to separate values in the CSV file.

???+ input "name_row_transform"
    A function to transform names in the name row of the CSV.

???+ input "csv_reader_settings"
    Additional settings for the CSV reader.

???+ input "numpy_reader_settings"
    Settings for reading data into numpy arrays.

???+ input "databox_settings"
    Settings for the Databox constructor.


### Returns ###


???+ returns "self"
    An `Databox` populated with time series from the CSV file.
        



&#9744;&#160;`Databox.from_dict`
----------------------------------

==Create a new `Databox` from a `dict`==

Create a new Databox instance populated with data from a provided dictionary. 
This class method can be used to convert a standard Python dictionary into a 
Databox, incorporating all its functionalities.

    self = Databox.from_dict(_dict)


### Input arguments ###


???+ input "_dict"
    A dictionary containing the data to populate the new Databox. Each
    key-value pair in the dictionary will be an item in the Databox.


### Returns ###


???+ returns "self"
    Returns a new Databox populated with the contents of the provided
    dictionary.
        



&#9744;&#160;`steady`
-----------------------


==Create a steady-state Databox for a model==


Create a Databox with steady-state values for a model, based on the provided
model object and the time span. This method generates steady-state time series
data for each item in the model. This constructor can be used for models that
have well-defined steady state, i.e. Simultaneous models and
VectorAutoregression models.


    steady_databox = self.steady(
        model,
        span,
        deviation=False,
    )


### Input arguments ###


???+ input "model"
    The model object for which to generate steady-state time series data.


???+ input "span"
    The time span for which to generate steady-state time series data.

???+ input "deviation"
    If `True`, the steady-state values are generated as deviations from the
    steady state in the form depending on the log status of each variable. If
    `False`, the steady-state values are generated in their original level form.


### Returns ###

???+ returns "steady_databox"
    A Databox containing steady-state time series for the `model`.

        



&#9744;&#160;`zero`
---------------------


==Create a zero-state Databox for a model==

This constructor is equivalent to calling

    zero_databox = Databox.steady(model, span, deviation=True, ...)


See the [`Databox.steady`](#steady) method for details.

        



&#9744;&#160;`_from_fred`
---------------------------

==Download time series from FRED (St Louis Fed Database)==

This method downloads time series data from the FRED database. The data is
downloaded using the FRED API. The method requires an API key, which is provided
by the FRED website. The API key is stored in the `_API_KEY` variable in the
`_fred.py` module. The method downloads the data for the specified series IDs
and returns a `Databox` object with the downloaded series.

db = Databox.from_fred(
    request,
)

### Input arguments ###

???+ input "request"
A dictionary or list of series IDs to download from FRED. If a dictionary is
provided, the keys are used as the FRED codes and the values are used for
the names of the time series in the Databox. If list of strings is provided,
the series IDs are used as the names of the series in the `Databox` object.

### Returns ###

???+ returns "db"
A `Databox` object containing the downloaded time series data.
    



&#9744;&#160;`_merge`
-----------------------

==Merge Databoxes==

Combine one or more databoxes into a single databox using a specified merge
strategy to handle potential conflicts between duplicate keys.

self.merge(
    other,
    merge_strategy="stack",
)


### Input arguments ###

???+ input "other"
The databox or iterable of databoxes to merge into the current databox. If
merging a single databox, it should be passed directly; for multiple
databoxes, pass an iterable containing all.

???+ input "merge_strategy"
Determines how to process keys that exist in more than one databox. The
default strategy is `"stack"`.

* `"stack"`: Stack values; this means combine time series into multiple
columns, or combine lists, or convert non-lists to lists for stacking.

* `"replace"`: Replace existing values with new values.

* `"discard"` and `"silent"`: Retain original values and ignore new values.

* `"warning"`: Behave like `"discard"` but issue a warning for each conflict.

* `"error"`: Raise an error on encountering the first duplicate key.

* `"critical"`: Raise a critical error on encountering the first duplicate key.


### Returns ###

This method modifies the databox in place and returns `None`.
    



&#9744;&#160;`apply`
----------------------


==Apply a function to items in a Databox==

Apply a function to selected Databox items, either in place or by reassigning 
the results.

    self.apply(
        func,
        source_names=None,
        in_place=True,
        when_fails="critical",
        strict_names=False,
    )


### Input arguments ###


???+ input "func"
    The function to apply to each selected item in the Databox.

???+ input "source_names"
    Names of the items to which the function will be applied. Can be a list of 
    names, a single name, a callable returning `True’ for names to include, or 
    `None` to apply to all items.

???+ input "in_place"
    Determines if the results of the function should be assigned back to the 
    items in-place. If `True`, items are updated in-place; if `False`, the
    results are reassigned to the items.

???+ input "when_fails"
    Specifies the action to take if applying the function fails. Options are 
    "critical", "error", "warning", or "silent".

???+ input "strict_names"
    If set to `True`, strictly adheres to the provided names, raising an error 
    if any source name is not found in the Databox.


### Returns ###


???+ returns "None"
    Modifies items in the Databox in-place (note that the `in_place` input
    argument only applies to the Databox items, and not the Databox itself)
    and does not return a value. Errors are handled based on the
    `when_fails’ setting.

        



&#9744;&#160;`array_from_series`
----------------------------------

==Retrieve time series data into a numpy array==

Retrieve the values of specified time series in the Databox into a numpy array.
The values are extracted for the specified periods and variant. This method is
useful for transforming time series data into a format suitable for numerical
analysis.

```
    array = self.array_from_series(
        names,
        periods,


        variant=0,
    )
```


### Input arguments ###

???+ input "names"
    A list of names of the time series to be converted to a numpy array.
    Each name should correspond to a time series item in the Databox.

???+ input "periods"
    A list of periods for which the values of the time series will be
    extracted.

???+ input "variant"
    The variant (column) of the time series to be extracted. This is typically an
    integer representing a specific variant of the time series data.


### Returns ###

???+ returns "array"
    A numpy array containing the values of the specified time series for the
    specified periods and variant. The array is structured such that each row
    corresponds to a time series, and each column corresponds to a period. The
    values are extracted in the order specified by the `names` and `periods`
    arguments. The array is of shape `(len(names), len(periods))`.
        



&#9744;&#160;`clip`
---------------------


==Clip the span of time series in a Databox==

Adjust the time series in a Databox by clipping them to a new specified start
and/or end date. This allows for refining the data span within which the series
operate, based on given periods.

    self.clip(
        new_start_date=None,
        new_end_date=None,
    )


### Input arguments ###


???+ input "new_start_date"
    The new start date for clipping the series. If `None`, only `new_end_date`
    is considered.

???+ input "new_end_date"
    The new end date for clipping the series. If `None`, only `new_start_date`
    is considered.


### Returns ###

This method modifies the databox in place and returns `None`.


### Details ###

The `clip` method adjusts only those time series in the Databox that match the
time frequency of the `new_start_date` and/or `new_end_date`. All other series
are left unchanged.
        



&#9744;&#160;`copy`
---------------------

==Create a copy of the Databox==

Produce a deep copy of the Databox, with options to filter and rename items 
during the duplication process.

    new_databox = self.copy(
        source_names=None,
        target_names=None,
        strict_names=False,
    )


### Input arguments ###


???+ input "source_names"
    Names of the items to include in the copy. Can be a list of names, a single 
    name, a callable returning `True` for names to include, or `None` to copy 
    all items.

???+ input "target_names"
    New names for the copied items, corresponding to 'source_names'. Can be a 
    list of names, a single name, or a callable function taking a source name 
    and returning the new target name.

???+ input "strict_names"
    If set to `True’, strictly adheres to the provided names, raising an error 
    if any source name is not found in the Databox.


### Returns ###


???+ returns "new_databox"
    A new Databox instance that is a deep copy of the current one, containing 
    either all items or only those specified.
        



&#9744;&#160;`evaluate_expression`
------------------------------------


==Evaluate an expression within a Databox context==

Evaluate a given string expression using the entries in the Databox as 
contextual variables. This method first checks if the expression directly 
matches an entry name within the Databox; if not, it attempts to evaluate the 
expression using Python's `eval()` with the current entries as the variable 
context.

    result = self.evaluate_expression(
        expression,
        context=None,
    )

Shortcut syntax:

    result = self(expression, context=None)


### Input arguments ###


???+ input "expression"
    The string expression to evaluate. If the expression matches an item name 
    in the Databox, the corresponding item is returned without further 
    evaluation.

???+ input "context"
    An optional dictionary providing additional context for evaluation. Can 
    include variables that are not present directly in the Databox.


### Returns ###


???+ returns "result"
    The result of the evaluated expression, which can be any valid Python data 
    type based on the content of the expression and available context.

        



&#9744;&#160;`filter`
-----------------------


==Filter items in a Databox==

Select Databox items based on custom name or value test functions.

    filtered_names = self.filter(
        name_test=None,
        value_test=None,
    )


### Input arguments ###


???+ input "name_test"
    A callable function to test each item's name. Returns `True` for names that 
    meet the specified condition.

???+ input "value_test"
    A callable function to test each item's value. Returns `True` for values that 
    meet the specified condition.


### Returns ###


???+ returns "filtered_names"
    A tuple of item names that meet the specified conditions.

        



&#9744;&#160;`from_pickle_file`
---------------------------------

==Read a Databox from a pickled file==

    self = Databox.from_pickle(
        file_name,
        **kwargs,
    )

### Input arguments ###

???+ input "file_name"
    Path to the pickled file to be read.

???+ input "kwargs"
    Additional keyword arguments to pass to the `pickle.load` function.

### Returns ###

???+ returns "self"
    A `Databox` object read from the pickled file.
        



&#9744;&#160;`get_description`
--------------------------------


==Get description attached to an object==

    description = self.get_description()


### Input arguments ###

???+ input "self"
    An object from which to get the description.


### Returns ###

???+ returns "description"
    The description attached to the object.

        



&#9744;&#160;`get_missing_names`
----------------------------------

==Identify names not present in a Databox==

Find and return the names from a provided list that are not present in the 
Databox. This method is helpful for checking which items are missing or have 
yet to be added to the Databox.

    missing_names = self.get_missing_names(names)


### Input arguments ###


???+ input "names"
    An iterable of names to check against the Databox's items.


### Returns ###


???+ returns "missing_names"
    A tuple of names that are not found in the Databox.
        



&#9744;&#160;`get_names`
--------------------------

==Get item names from a Databox==


    names = self.get_names(filter=None, )


### Input arguments ###

???+ input "filter"
    A function that takes a name and returns `True` to include the name in the
    output list, or `False` to keep the name out. If `None`, all names are
    included.


### Returns ###

???+ returns "names"
    A tuple containing all the names of items in the Databox.
        



&#9744;&#160;`get_series_names_by_frequency`
----------------------------------------------

==Retrieve time series names by frequency==

Obtain a list of time series names that match a specified frequency.

    time_series_names = self.get_series_names_by_frequency(frequency)


### Input arguments ###


???+ input "self"
    The Databox object from which to retrieve time series names.

???+ input "frequency"
    The frequency to filter the time series names by. It should be a valid 
    frequency from the `irispie.Frequency` enumeration.


### Returns ###


???+ returns "time_series_names"
    A list of time series names in the Databox that match the specified frequency.
        



&#9744;&#160;`get_span_by_frequency`
--------------------------------------

==Retrieve the date span for time series by frequency==

Get the encompassing date span for all time series with a specified frequency.

    date_span = self.get_span_by_frequency(frequency)


### Input arguments ###


???+ input "self"
    The Databox object from which to retrieve the date span.

???+ input "frequency"
    The frequency for which to determine the date span. Can be an instance of 
    `irispie.Frequency` or a plain integer representing the frequency.


### Returns ###


???+ returns "date_span"
    The date span, as a `Span` object, encompassing all time series in the 
    Databox that match the specified frequency.
        



&#9744;&#160;`keep`
---------------------

==Keep specified items in a Databox==

Retain selected items in a Databox, removing all others. Specify the items to 
keep using `keep_names`, which can be a list of names, a single name, or a 
callable function determining which items to retain.

    self.keep(
        keep_names=None,
        strict_names=False,
    )


### Input arguments ###


???+ input "keep_names"
    The names of the items to be retained in the Databox. Can be a list of names, 
    a single name, or a callable function determining the items to keep.

???+ input "strict_names"
    If set to `True`, enforces strict adherence to the provided names, with an 
    error raised for any name not found in the Databox.


### Returns ###


???+ returns "None"
    Modifies the Databox in-place, keeping only the specified items, and does not 
    return a value.
        



&#9744;&#160;`minus_control`
------------------------------

==Subtract control values from a Databox==

Subtract control values (usually steady-state values or control simulation
values) from the corresponding time series in the Databox.

    self.minus_control(
        model,
        control_databox,
    )

### Input arguments ###

???+ input "model"
    The underlying model object based on which the `self` and `control_databox`
    were created.

???+ input "control_databox"
    The Databox containing control values to subtract from the corresponding
    time series in `self`.

### Returns ###

This method modifies the Databox in place and returns `None`.
        



&#9744;&#160;`overlay`
------------------------


==Overlay another Databox time series onto the ones in the current Databox==

Overlay another Databox's time series onto the corresponding time series in the
current Databox, aligning and incorporating data series using the `overlay`
method defined in the Series class. This operation modifies the current Databox
in-place by applying the overlay technique to each individual series that exists
in both Databoxes.

    self.overlay(
        other,
        names=None,
        strict_names=False,
    )


### Input arguments ###

???+ input "self"
    The Databox onto which the overlay will be applied. It contains the original
    time series data.

???+ input "other"
    The Databox that provides the time series to overlay onto `self`. Only
    series present in both Databoxes will be affected.

???+ input "names"
    An optional iterable of names to overlay. If `None`, the overlay operation
    is attempted on all time series present in both Databoxes.

???+ input "strict_names"
    If `True`, the names provided in `names` are strictly adhered to, and an
    error is raised if any name is not found in both Databoxes.


### Returns ###

This method modifies the Databox in place and returns `None`.


### Details ###

The `overlay` method ensures that corresponding time series in both the source
Databox and the other Databox are merged based on the overlay logic determined
by the Series class.





&#9744;&#160;`prepend`
------------------------

==Prepend time series data to a Databox==

Add time series data from another Databox to the beginning of the current
Databox, up to a specified end date.

    self.prepend(
        other,
        end_prepending,
    )

### Input arguments ###

???+ input "self"
    The Databox to which the time series data will be added.

???+ input "other"
    The Databox containing the time series data to prepend to `self`.

???+ input "end_prepending"
    The end date up to which the time series data from the `other` Databox will
    be added to `self`.

### Returns ###

This method modifies the Databox in place and returns `None`.

### Details ###

This method uses the `underlay` method to add the time series data from the
`other` Databox to the beginning of the `self` Databox.
        



&#9744;&#160;`remove`
-----------------------

==Remove specified items from a Databox==

Remove specified items from the Databox based on the provided names or a 
filtering function. Items to be removed can be specified as a list of names, a 
single name, a callable that returns `True` for names to be removed, or `None`.

    self.remove(
        remove_names=None,
        *,
        strict_names=False,
    )


### Input arguments ###


???+ input "remove_names"
    Names of the items to be removed from the Databox. Can be a list of names, a 
    single name, a callable that returns `True` for names to be removed, or 
    `None`. If `None`, no items are removed.

???+ input "strict_names"
    If `True`, strictly adheres to the provided names, raising an error if any 
    name is not found in the Databox.


### Returns ###

Returns `None`; `self` is modified in place.

        



&#9744;&#160;`rename`
-----------------------

==Rename items in a Databox==

Rename existing items in a Databox by specifying `source_names` and 
`target_names`. The `source_names` can be a list of names, a single name, or a 
callable function returning `True` for names to be renamed. Define `target_names`
as the new names for these items, either as a corresponding list, a single name,
or a callable function taking a source name and returning the new target name.

    self.rename(
        source_names=None,
        target_names=None,
        strict_names=False,
    )


### Input arguments ###


???+ input "source_names"
    The current names of the items to be renamed. Accepts a list of names, a 
    single name, or a callable that generates new names based on the given ones.

???+ input "target_names"
    The new names for the items. Should align with 'source_names'. Can be a list 
    of names, a single name, or a callable function taking each source name and 
    returning the corresponding target name.

???+ input "strict_names"
    If set to `True`, enforces strict adherence to the provided names, with an 
    error raised for any source name not found in the Databox.


### Returns ###

Returns `None`; `self` is modified in place.

        



&#9744;&#160;`set_description`
--------------------------------


==Set the description for an object==

    self.set_description(
        description,
    )


### Input arguments ###

???+ input "self"
    An Iris Pie object to which to attach the description.


???+ input "description"
    The description to attach to the Iris Pie object.


### Returns ###

This method modifies the Iris Pie object in place and returns `None`.

        



&#9744;&#160;`shallow`
------------------------

==Create a shallow copy of the Databox==

Generate a shallow copy of the Databox, with options to filter and rename items
during the duplication process. A shallow copy retains the original items and
references, but does not copy the items themselves.

    shallow_databox = self.shallow(
        source_names=None,
        target_names=None,
        strict_names=False,
    )

### Input arguments ###

???+ input "self"
    The Databox object to copy.

???+ input "source_names"
    Names of the items to include in the copy. Can be a list of names, a single
    name, a callable returning `True` for names to include, or `None` to copy
    all items.

???+ input "target_names"
    New names for the copied items, corresponding to 'source_names'. Can be a
    list of names, a single name, or a callable function taking a source name
    and returning the new target name.

???+ input "strict_names"
    If set to `True`, strictly adheres to the provided names, raising an error
    if any source name is not found in the Databox.

### Returns ###

???+ returns "shallow_databox"
    A new Databox instance that is a shallow copy of the current one, containing
    either all items or only those specified.
        



&#9744;&#160;`to_csv_file`
----------------------------

==Write Databox time series to a CSV file==


    self.to_csv_file(
        file_name,
        *,
        frequency_span=None,
        names=None,
        description_row=False,
        frequency=None,
        numeric_format="g",
        nan_str="",
        delimiter=",",
        round=None,
        date_formatter=None,
        csv_writer_settings={},
        when_empty="warning",
    )


### Input arguments ###


???+ input "file_name"
    Name of the CSV file where the data will be written.

???+ input "frequency_span"
    Specifies the frequencies and their corresponding date ranges for exporting
    data. If `None`, exports data for all available frequencies and their full
    date ranges in the databox.

???+ input "names"
    A list of series names to export. If `None`, exports all series for the 
    specified frequencies.

???+ input "description_row"
    If `True`, include a row of series descriptions in the CSV.

???+ input "frequency"
    Frequency of the data to export.

???+ input "numeric_format"
    The numeric format for data values, e.g., 'g', 'f', etc.

???+ input "nan_str"
    String representation for NaN values in the output.

???+ input "delimiter"
    Character to separate columns in the CSV file.

???+ input "round"
    Number of decimal places to round numeric values.

???+ input "date_formatter"
    Function to format date values. If `None`, SDMX string formatter is used.

???+ input "csv_writer_settings"
    Additional settings for the CSV writer.

???+ input "when_empty"
    Behavior when no data is available for export. Can be "error", "warning", or
    "silent".


### Returns ###


???+ returns "info"
    A dictionary with details about the export:

    * `names_exported`: Names of the series exported to the CSV file.

        



&#9744;&#160;`to_dict`
------------------------

==Convert a Databox to a plain dictionary==

Convert a Databox to a standard Python dictionary, with the keys and values
retained. This method is useful for converting a Databox to a format that can be
used with other Python libraries or functions.

    diction = self.to_dict()

### Input arguments ###

???+ input "self"
    The Databox object to convert to a dictionary.

### Returns ###

???+ returns "diction"
    A dictionary containing the items from the Databox.
        



&#9744;&#160;`to_json`
------------------------

==Save a Databox to a JSON file==

Save a Databox to a JSON file, preserving the structure and data of the Databox
object. This method is useful for storing Databoxes in a format that can be
easily shared or imported into other applications.

    self.to_json(
        file_name,
        **kwargs,
    )

### Input arguments ###

???+ input "self"
    The Databox object to save to a JSON file.

???+ input "file_name"
    Path to the JSON file where the Databox will be saved.

???+ input "**kwargs"
    Additional keyword arguments to pass to the JSON encoder.

### Returns ###

Returns `None`; the Databox is saved to the specified JSON file.
        



&#9744;&#160;`to_pickle_file`
-------------------------------

==Write Databox to a pickle file==

    self.to_pickle(
        file_name,
        **kwargs, 
    )

### Input arguments ###

???+ input "file_name"
    Path to the pickle file where the data will be written.

???+ input "kwargs"
    Additional keyword arguments for the pickle writer.

### Returns ###

This method returns `None`.
        



&#9744;&#160;`underlay`
-------------------------


==Underlay another Databox time series beneath those in the current Databox==

Underlay another Databox's time series beneath the corresponding times series in
the current Databox, aligning and incorporating data series using the `underlay`
method defined in the Series class. This operation modifies the current Databox
in-place by applying the underlay technique to each individual series that
exists in both Databoxes.

    self.underlay(
        other,
        names=None,
        strict_names=False,
    )


### Input arguments ###

???+ input "self"
    The Databox beneath which the underlay will be applied. It contains the original
    time series data.

???+ input "other"
    The Databox that provides the time series to underlay beneta `self`. Only
    series present in both Databoxes will be affected.

???+ input "names"
    An optional iterable of names to underlay. If `None`, the underlay operation
    is attempted on all time series present in both Databoxes.

???+ input "strict_names"
    If `True`, the names provided in `names` are strictly adhered to, and an
    error is raised if any name is not found in both Databoxes.


### Returns ###

This method modifies the Databox in place and returns `None`.


### Details ###

The `underlay` method ensures that corresponding time series in both the source
Databox and the other Databox are merged based on the underlay logic determined
by the Series class.

        



&#9744;&#160;`validate`
-------------------------

        