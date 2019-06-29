# -*- coding: utf-8 -*-
"""
@author: ParkerHall
"""
#load data and Kaggle feedback system
import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

# median points of the column in the reviews DataFrame
median_points = reviews.points.median()
#countries represented in dataset
countries = reviews.country.unique()
# series reviews per country mapping countries to the count of wines from that country
reviews.country.value_counts()
#variable centered price containing a version of the price column with mean price subtracted
centered_price = reviews.price - reviews.price.mean()
#title of the wine with the highest points to price ratio in the dataset
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
#series counting how many times each word appears in the description column of the dataset (tropical and fruity)n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
#a star rating system for wines with the number of stars corresponding to each review in the dataset
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis='columns')