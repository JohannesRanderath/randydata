==============
DataLayout
==============
The ``randydata.data_layout`` module helps you format the results of your data analysis to make it easier to present
them. For now, it doesn't include a lot of tools, but more will follow.

make_table
______________
The ``randydata.data_layout.make_table`` function creates a table using HTML for your data.

Arguments:
    * headings: List
        - Table headings. Required.
        - Displayed in first row as headings to the columns
    * data: List of lists
        - Every element of the list should be a list representing the data for one row (or column, see below)
        - Make sure, every row contains the same amount of elements and to have a heading for each column.
    * columns: boolean, *optional*
        - default: ``False``
        - If True, the data is interpreted as columns, instead of rows.
        - Each element of data is a list of data for one column.
    * row_headings: List, *optional*
        - default: ``None``
        - If given, a first column is inserted, serving as headings for each row.
