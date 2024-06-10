
Databoxes
==========

`Databoxes` extend the standard `dict` class (technically, they are a
subclass), serving as a universal tool for storing and manipulating
unstructured data organized as key-value pairs. The values stored within
`Databoxes` can be of any type.

`Databoxes` can use any methods implemented for the standard `dict`
objects, and have additional functionalities for data item manipulation,
batch processing, importing and exporting data, and more.
    


Categorical list of functions
-------------------------------

### Creating new databoxes ###

Function | Description
----------|------------
[Databox.empty](#databoxempty) | Create an empty Databox
[Databox.from_array](#databoxfrom_array) | Create a new `Databox` from a numpy array
[Databox.from_dict](#databoxfrom_dict) | Create a new `Databox` from a `dict`


### Getting information about databoxes ###

Function | Description
----------|------------
[filter](#filter) | Filter items in a Databox
[get_missing_names](#get_missing_names) | Identify names not present in a Databox
[get_names](#get_names) | Get all item names from a Databox
[get_series_names_by_frequency](#get_series_names_by_frequency) | Retrieve time series names by frequency
[get_span_by_frequency](#get_span_by_frequency) | Retrieve the date span for time series by frequency


### Manipulating databoxes ###

Function | Description
----------|------------
[apply](#apply) | Apply a function to items in a Databox
[copy](#copy) | Create a copy of the Databox
[keep](#keep) | Keep specified items in a Databox
[remove](#remove) | Remove specified items from a Databox
[rename](#rename) | Rename items in a Databox


### Importing and exporting databoxes ###

Function | Description
----------|------------
[Databox.from_csv](#databoxfrom_csv) | Create a new Databox by reading time series from a CSV file
[to_csv](#to_csv) | Write Databox time series to a CSV file





Directly accessible properties
------------------------------

Property | Description
----------|------------
[num_items](#num_items) | Number of items in the databox



☐ `Databox.empty`
-------------------

==Create an empty Databox==

Generate a new, empty Databox instance. This class method is useful for 
initializing a Databox without any pre-existing data.

    Databox.empty()


### Input arguments ###

No input arguments are required for this method.


### Returns ###


???+ returns "Databox"
    Returns a new instance of an empty Databox.
        



☐ `Databox.from_array`
------------------------

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
        



☐ `Databox.from_dict`
-----------------------

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
        



☐ `apply`
-----------


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

        



☐ `copy`
----------

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
        



☐ `Databox.from_csv`
----------------------


==Create a new Databox by reading time series from a CSV file==


    self = Databox.from_csv(
        file_name,
        *,
        date_creator=None,
        start_date_only=False,
        description_row=False,
        delimiter=",",
        csv_reader_settings={},
        numpy_reader_settings={},
        name_row_transform=None,
    )


### Input arguments ###


???+ input "file_name"
    Path to the CSV file to be read.

???+ input "date_creator"
    A callable for creating date objects from string representations. If `None`,
    a default method based on the SDMX string format is used.

???+ input "start_date_only"
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
        



☐ `filter`
------------


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

        



☐ `get_missing_names`
-----------------------

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
        



☐ `get_names`
---------------

==Get all item names from a Databox==


    names = self.get_names()


### Input arguments ###


No input arguments are required for this method.


### Returns ###


???+ returns "names"
    A tuple containing all the names of items in the Databox.
        



☐ `get_series_names_by_frequency`
-----------------------------------

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
        



☐ `get_span_by_frequency`
---------------------------

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
        



☐ `keep`
----------

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
        



☐ `remove`
------------

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

        



☐ `rename`
------------

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

        



☐ `to_csv`
------------

==Write Databox time series to a CSV file==


    self.to_csv(
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

        



☐ `validate`
--------------

        