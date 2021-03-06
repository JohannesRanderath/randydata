===============
RandyData
===============
Purpose
_______________
*RandyData* serves as a simple tool to automate data handling tasks, when working with MySQL Databases and Excel tables,
storing one observation per row.

It helps reading the Excel table into a MySQL database and creates custom classes for every observation. Furthermore, it
helps automate some basic formatting tasks to present your results.

welcome_data
________________
The ``randydata.welcome_data`` module is made to simplify the process of importing excel files and reading SQL tables to
memory. It uses an object oriented approach and dynamically creates a class, storing the observed parameters and adding
user specified methods to make data handling more easy.

data_layout
_______________
The ``randydata.data_layout`` module simplifies some more common formatting tasks to present the results you got from
analysing the observed data. It uses html to quickly add some structure to your data.

Feedback
_______________
I am very happy about any kind of feedback or suggestion by email: `randydata@randerath.eu <mailto:randydata@randerath.eu>`_

Module documentation
_________________________
..  toctree::
    :maxdepth: 2

    modules/welcome_data.rst
    modules/data_layout.rst
