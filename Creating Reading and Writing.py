# -*- coding: utf-8 -*-
"""
@author: ParkerHall
"""

#imports pandas and Kaggles feedback system
import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")
#creates a DataFrame fruits
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
#creates a DataFrame with specific indexes
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
#creates a DataFrame for a recipe
quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
ingredients= pd.Series(quantities, index=items, name='Dinner')
#Reads a csv dataset into a DataFrame called reviews
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)
#creates a DataFrame animals
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
#save this datafram to disk as a csv
animals.to_csv("cows_and_goats.csv")
