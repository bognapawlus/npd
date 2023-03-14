#module to print a table of 5 countries with greatest gpd on person for each year

import os
import numpy as np
import pandas as pd

def find_5_countries_gdp(countries_names_list, population_list, gpd_list, year): #tu już mamy w np.array
    if np.isnan(population_list).any():
        population_list = np.nan_to_num(population_list, nan=-1)
        #wypisać które państwo
        print("WARNING: There are countries with no data regarding population in year", end="")
        print(year)
    if np.isnan(gpd_list).any():
        #wypisać gdzie nie ma gpd
        gpd_list = np.nan_to_num(gpd_list, nan=0)
        print("WARNING: There are countries with no data regarding gpd in year")
        print(year)
    
    #co gdy mniej niż 5 krajów
    gpd_on_person = gpd_list/population_list

    indexes = np.argsort(gpd_on_person)[::-1][:5]
    kraj = countries_names_list[indexes]
    gpdDpopul = gpd_on_person[indexes]

    gpd_sum = gpd_list[indexes]
    ##########problem z population_list, chyba ma 0
    tabelka = np.array([kraj, gpdDpopul, gpd_sum])
    tabelka = np.transpose(tabelka)
    df = pd.DataFrame(tabelka, columns = ['kraj', 'gpdDpopul', 'gpd_sum'])
    return df

