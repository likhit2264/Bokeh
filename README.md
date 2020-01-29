# BOKEH
Bokeh Python Library Project - Kaushik I. Likhit G.


The Auto-Grapher
Software Needed/Used
Python (Coding Language) Version 3.8.1
Bokeh (Python Plotting Library) Version 1.4.0
Numpy (Python Math Library) Version 1.1.7
Pandas (Python File Reading Library) Version 0.25.3
SQLite (Database Language) Version 3.0
Atom (Code Editor) Version 1.42.0
Docker (Hosting Application) Version 2.5
MSSQL Server (Database Server)

Purpose

Nearly all manufacturing companies use large databases to keep track of information on their products. Companies like Apple and Samsung use testing groups to analyze the behavior of their targeted consumers. Generally, the collected data is used to improve the advertisement efficiency of the company. To use a table of data on iPhone devices, characterized by ID Number, and create accurate graphs and models that would visualize trends between the various data input, including phone color, age, owner’s age, remaining battery, and more. (Keep in mind that we had to create our own data since  we don’t have access to Apple’s databases.)


Code Walkthrough

Step 1: install and initiate Docker
Step 2: create and host local MSSQL Server on MACOSX
Step 3: create a .sql script with the artifical data
Step 4: run the sql script into the SQL server
Step 5: create a cursor to the database using SQLite3
Step 6: change the data into objects based on a Class
Step 7: run objects into a list
Step 8: send list to main.py
Step 9: initate empty variables
Step 10: iterate through the objects
Step 11: parse the Object's data
Step 12: increment associated variables
Step 13: generate individual graphs using Bokeh based on the Object's attritibutes
Step 14: append the figures to a list
Step 15: use the show and column command on the list of figures
Step 16: change the destination html file
Step 17: create figures based off of the entire database
Step 18: show the final figures
Step 19: Fix/individualize any css elements of the figures
