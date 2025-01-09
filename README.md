#### Author: Kamni Marquis - 230228315  DAT5902: Professional Software and Career Practices Final Project

## Overview:
This project analyses global suicide rates by gender using data from the **Our world in Data**. The analysis focuses on identifying patterns and trends across countries and continents, with visualisations that highlight disparities between male and female suicide rates.

### Hypothesis:
The suicide rate for males is higher than that for females across all countries and years, and social factors such as cultural norms and economic conditions contribute significantly to this disparity. 

### Project Structure:
- config.yml: CircleCI configuration file for automating the setup, testing, and execution of the Python script.
- data/: Folder containing the dataset (CSV file) with match statistics.
- graph images/: Folder where the generated images (graphs and charts) will be saved.
- tests and graphs/: Python script to read the dataset, process the data, and generate graphs and Unit tests to ensure data integrity, graph generation, and correct functionality of the code.
- key_tests.txt: File to provide a comprehensive description of the unit tests implemented in the project.
- requirements.txt: file that ensures all necessary dependencies for the project are installed correctly.

### Dependencies:
The project requires the following Python packages:
- pandas
- matplotlib
- unittest
- pytest
- pycountry-convert

## Data sources:
- Our World in Data: https://ourworldindata.org/suicide

## Folders/Files:
.circleci folder contains the config file used to connect circleci project.

Data folder contains the csv documentation of the data used to create the graphs and analyses. This folder contains a csv file named:
- suicide-rate-male-female-who-mdb.csv

Graph images folder contains the images of the graphs produced. It contains 2 png files named:
- avg suicide rates by gender by continent.png
- top 10 countries males vs females suicide rates.png

Tests and graphs folder contains all of the code used to create both graphs which will be used in analysis and the unit tests for each of the codes. It contains 4 py files named: 
- main.py
- test_main.py
- graph2.py
- test_graph2.py

