# Main project 

## General
To see a general presentation of the code see file `presentation.ipynb`


## Description
We have given tables with data for some countries in some years

* `population` – table with given population 
* `gpd` – table with given gpd 
* `co2_emmisions` – table with given co2_emissions, with different format than the two tables above (see preview of tables below). Moreover this table has some types in country names.

We have following tasks:
* **task1:** Displaying the table of 5 countries with greatest value of gdp / population for each year
* **task2:** Displaying the table of 5 countries with greatest co2 emissions per person for each year

## Instalation:
1. Clone the repo:
```sh
 $ git clone https://github.com/bognapawlus/npd/tree/master/main_project
```
2. Run by
```sh
 $ python3 projekt.py [-h] [-g | -c] [-s STARTYEAR] [-e ENDYEAR] population.csv gdp.csv co2_emission.csv
```
description of options:
*  `-h` shows info about usage
*  `-g` display table with gdp on person 
*  `-c` display table with co2_emission on person
*  `-s` choose the start considerable year
*  `-e` choose the end considerable year

Example of running:
```sh
 $ python3 project.py -c -s 1999 -e 2001 population.csv gdp.csv co2_emission.csv
```
