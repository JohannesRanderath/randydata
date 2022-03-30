===============
WelcomeData
===============
The ``randydata.welcome_data`` module serves for handling data import and export from Excel and MySQL and saving to
MySQL. The approach is to take observational data where from tables, where each row stores one observation. For these
observations, WelcomeData dynamically creates a data type. If, for example, your table stores patient data, where for
each patient, the date of birth is observed, you could name your data type *Patient* and WelcomeData would import the
rows as Patient objects, so you can access the patient's date of birth by (e.g.) ``Patient.dob``. You could also add a
method to calculate the patient's age as of today. Let's say you called it ``age()``, so you can access one patient's
age by calling ``Patient.age()``.
SQL table names are case-insensitive. In some operating systems and MySQL versions it is possible to create and use
Tables with upper case letters, but this causes compatibility problems with both other MySQL implementations and other
Python Packages. This is why case is ignored by welcome_data.

create_datatype_from_sql
_________________________
The ``randydata.welcome_data.create_datatype_from_sql`` function reads the rows of a MySQL table and interprets them as
observations as stated above.

Arguments:
    * name: String
        - Name, the newly created datatype class will have. E.g. "Patient"
    * database: String
        - Name of the MySQL database to read the data from
    * table: String
        - Name of the table from *database* to read the data from
    * host: String, *optional*
        - default: ``"localhost"``
        - Hostname of the database to get the data from. If not given, RandyData assumes, it is stored locally and uses
          "localhost"
    * username: String, *optional*
        - default: ``"root"``
        - MySQL username
    * password: String, *optional*
        - default: ``""``
        - Password to MySQL database. If not given, no password protection is assumed.
    * no_bool: List of Strings, *optional*
        - default: ``[]``
        - List of arguments, that could be interpreted as boolean values, but shouldn't.
        - By default, if a value in the table does not have any other value than 0, 1 or no value at all, it is assumed
          to be boolean and treated this way. If you don't want this, you can add the value to this list.
    * methods: Dict of Strings: functions, *optional*
        - default: ``{}``
        - Dict of method names and functions, to serve as the methods, the datatype should hold.

Returns:
    A list of objects of the newly generated type, one object for each row in the MySQL table.

read_excel_to_sql
____________________
The ``randydata.welcome_data.read_excel_to_sql`` function takes a naked MS Excel table and stores it in a MySQL table. If your Excel
document is more complex than that, please make sure to copy the table, which holds your data, including the headings,
to a new Excel file.

Arguments:
    * path: String
        - Path to the excel file, containing the table to be read.
    * database: String
        - Name of the MySQL database to read the data from
    * table: String
        - Name of the table from *database* to read the data from
    * host: String, *optional*
        - default: ``"localhost"``
        - Hostname of the database to get the data from. If not given, RandyData assumes, it is stored locally and uses
          "localhost"
    * username: String, *optional*
        - default: ``"root"``
        - MySQL username
    * password: String, *optional*
        - default: ``""``
        - Password to MySQL database. If not given, no password protection is assumed.
    * override_table: boolean, *optional*
        - default: ``True``
        - If not given or True, the selected table is deleted and overridden with the given data.
    * append: boolean, *optional*
        - default: ``False``
        - If True, data from the given table, is appended as new rows to the MySQL table.
        - Strongly discouraged, as this might lead to duplicate data, thus creating false analysis results.
        - Make sure to set override_table explicitly to False, for this option to have any effect.

Returns:
    - ``True``, if successful
    - ``False``, if not

create_datatype_from_attributes
____________________________________
The ``randydata.welcome_data.create_datatype_from_attributes`` dynamically creates a datatype with given attributes and methods.

Arguments:
    * name: String
        - Name of class to create
    * attributes: List of Strings
        - List of attribute names, the class should hold.
    * bool_values: List of Strings, *optional*
        - default: ``[]``
        - List of attribute names, that should be interpreted as booleans.
    * methods: Dict of Strings: functions, *optional*
        - default: ``[]``
        - Dict of method names and functions, that should serve as the datatype's methods.

Returns:
    The class of the newly created datatype.

create_datatype_from_excel
________________________________
Shorthand for:
::
    read_excel_to_sql(...)
    create_datatype_from_sql(...)
::

So the ``randydata.welcome_data.create_datatype_from_excel`` function takes a naked MS Excel table and stores it in a
MySQL table. If your Excel document is more complex than that, please make sure to copy the table, which holds your
data, including the headings, to a new Excel file.
It also interprets the rows of the Excel file as observations and loads them in a dynamically created object as stated
above.

Arguments:
    * name: String
        - Name, the newly created datatype class will have. E.g. "Patient"
    * path: String
        - Path to the excel file, containing the table to be read.
    * database: String
        - Name of the MySQL database to read the data from
    * table: String
        - Name of the table from *database* to read the data from
    * host: String, *optional*
        - default: ``"localhost"``
        - Hostname of the database to get the data from. If not given, RandyData assumes, it is stored locally and uses
          "localhost"
    * username: String, *optional*
        - default: ``"root"``
        - MySQL username
    * password: String, *optional*
        - default: ``""``
        - Password to MySQL database. If not given, no password protection is assumed.
    * override_table: boolean, *optional*
        - default: ``True``
        - If not given or True, the selected table is deleted and overridden with the given data.
    * append: boolean, *optional*
        - default: ``False``
        - If True, data from the given table, is appended as new rows to the MySQL table.
        - Strongly discouraged, as this might lead to duplicate data, thus creating false analysis results.
        - Make sure to set override_table explicitly to False, for this option to have any effect.
    * no_bool: List of Strings, *optional*
        - default: ``[]``
        - List of arguments, that could be interpreted as boolean values, but shouldn't.
        - By default, if a value in the table does not have any other value than 0, 1 or no value at all, it is assumed
          to be boolean and treated this way. If you don't want this, you can add the value to this list.
    * methods: Dict of Strings: functions, *optional*
        - default: ``{}``
        - Dict of method names and functions, to serve as the methods, the datatype should hold.

Returns:
    A list of objects of the newly generated type, one object for each row in the MS Excel table.

