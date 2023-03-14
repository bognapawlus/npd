#module to sort co2_emissions with respect to years and countries

import os
import numpy as np
import pandas as pd
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def is_equel(s1, s2):
    if s1 in s2:
        return 1
    if s2 in s1:
        return 1
    if similar(s1, s2) > 0.75:
        return 2
    return 0
    
def co2_emissions_per_person(population, co2_emissions):
	#1. setting indexes
	co2_emissions = co2_emissions.set_index(['Year', 'Country'])
	population = population.set_index('Country Name')

	#2. removing years existing only in co2_emissions from (co2_emmisions)
	population_top = population.columns
	indexes_pop = np.array(population_top)
	indexes_pop = np.delete(indexes_pop, [0,1,2]).astype(int)

	##usuwanie kraju
	indexes_co2 = np.array(co2_emissions.index)
	indexes_co2 = np.array([i[0] for i in indexes_co2])
	indexes_co2 = np.unique(indexes_co2)

	###nowa lista z elementami z indexes_co2 \ indexes_pop
	to_deleting = np.setdiff1d(indexes_co2, indexes_pop)
	co2_emissions2 = co2_emissions.drop(to_deleting, axis=0) #indeksy które są i w countries i w co2_emissions
	
	#4. deleting all collumns except Total from co2_emmisions
	co2_emissions3 = co2_emissions2.loc[:, co2_emissions2.columns.intersection(['Total'])]
	co2_emissions3.index
	s = []
	for t in co2_emissions3.index:
	    s.append(t[1])
	s = np.array(s)
	s = np.unique(s) #list of countries from co2_emissions
	
	population.index = population.index.str.upper()
	ss = np.array(population.index) #list of countries form population, it's different than s
	
	#countries which are in s (co2.emmisions) but not in ss.population
	zle = np.setdiff1d(s, ss, assume_unique=True)

	#countries to deleting from co2_emmisions, for witch we can't find a proper country's name in population
	num = 0
	for zle_var in zle:
	    for ss_var in ss:
	        if is_equel(zle_var, ss_var) == 1:
	            zle = np.delete(zle, num)
	            co2_emissions3.rename(index={zle_var:ss_var},inplace=True)
	            num -= 1
	            break
	        if is_equel(zle_var, ss_var) == 2:
	            zle = np.delete(zle, num)
	            co2_emissions3.rename(index={zle_var:ss_var},inplace=True)
	            num -= 1
	    num += 1

	##delete indexes zle from co2.emmisions:
	zle
	co2_emissions4 = co2_emissions3.drop(zle, level=1, axis=0)
	co2_emissions4.to_excel("pom.xlsx", sheet_name='deleting')
	co2_emissions4

	co2_emissions4 = co2_emissions4.sort_index()
	for y, c in co2_emissions4.index:
		co2_emissions4.loc[(y, c)] = co2_emissions4.loc[(y, c)] / population[str(y)].loc[c]
	
	return co2_emissions4





