# -*- coding: utf-8 -*-
"""
@author: ParkerHall
"""
#imports pandas and Kaggles feedback system
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")

#examine the data
reviews.head()
#selects the description column from the reviews data and assigns the result to the variable desc
desc = reviews.description
#selects first value from the description column, assign it to a variable first description
first_description = reviews.description.iloc[0]
#select the first row of data from reviews aissigning it to the variable first row
first_row = reviews.iloc[0]
#slect the first 10 values from the description column in reviews assigning the result to variable first descriptions
first_descriptions = reviews.description.iloc[:10]
#select the records with the index labels 1, 2, 3, 5, 8 assigning the result to the sample reviews variable
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]
#create a variable df that contains columns of the records with specific index labels
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
#create a variable df with the columns variety and country 
cols = ['country', 'variety']
df = reviews.loc[:99, cols]
#create DataFrame italian wines that contains reviews for wines made in italy
italian_wines = reviews[reviews.country == 'Italy']
#DataFrame for top oceania wines that contains all reviews with at least 95 points for wines from australia and new zealand
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
