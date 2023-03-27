#main part

import os
import numpy as np
import pandas as pd
import argparse
import task1
import task2

# $ python3 projekt.py [-h] [-g | -c] [-s STARTYEAR] [-e ENDYEAR] population.csv gdp.csv co2_emission.csv
# for example
# $ python3 project.py -c -s 1970 -e 2001 population.csv gdp.csv co2_emission.csv


#- options:
#-> -h shows info about usage
#->-> -g display table with gdp on person 
#->-> -c display table with co2_emission on person

###
# 1. PART: Arguments:
###
parser = argparse.ArgumentParser(description="Tool to displaying sorted tables")
group = parser.add_mutually_exclusive_group()
#group.add_argument("-h", "--help", action="store_true")

#choose table
group.add_argument("-g", "--gdponperson", action="store_true", help="choose a table with gdp")
group.add_argument("-c", "--co2emission", action="store_true", help="choose a table with co2emission")

#csv files:
parser.add_argument("population_file", help="initial table with population")
parser.add_argument("gdp_file", help="initial table with gdp")
parser.add_argument("co2_emission_file", help="initial table with co2_emission")

#years:
parser.add_argument("-s", "--startyear", type=int, default=2000, help="number of shifts, default = 2000")
parser.add_argument("-e", "--endyear", type=int, default=2010, help="number of shifts, default = 2010")

args = parser.parse_args()


###
# 2. PART: importing data
##
#table with population:
population = pd.read_csv(args.population_file, skiprows=4)
population = population.drop("Unnamed: 66", axis=1)

#table with co2 emissions:
co2_emissions = pd.read_csv(args.co2_emission_file, skiprows=0)

#table with gdp
gdp = pd.read_csv(args.gdp_file, skiprows=4)
gdp = gdp.drop("Unnamed: 66", axis=1)


###
# 3. PART
###
if args.gdponperson:
	print("TASK1: Table with gdp on person. \n5 countries for each year with greatest values")
	start_year = args.startyear
	end_year = args.endyear

	for i in range(start_year,end_year + 1):
	    y = str(i)
	    cnl = population["Country Name"].to_numpy()
	    pl = population[y].to_numpy()
	    gdpl = gdp[y].to_numpy()

	    tab = task1.find_5_countries_gdp(cnl, pl, gdpl, y)
	    print(tab)
	
else:
	print("TASK2: Table with co2_emission on person. \n5 countries for each year with greatest values \nLoading...")
	tab2 = task2.co2_emissions_per_person(population, co2_emissions, args.startyear, args.endyear)
	ans = tab2.groupby(level='Year')['Total'].nlargest(5)
	print(ans)
