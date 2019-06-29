# -*- coding: utf-8 -*-
"""

@author: ParkerHall
"""
#imports pandas and Kaggles feedback system
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

#series with the index taster twitter handle from the dataset with values counting how many reviews each person wrote
reviews_written = reviews.groupby('taster_twitter_handle').size()
#series that indexes the wine prices and has values for the maximum number of points a wine costinf that much.
#sorts the values by price, ascending dollars at the top and 3300 at the bottom
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
#DataFrame that index is the variety category from the dataset and has values of min and max
price_extremes = reviews.groupby('variety').price.agg([min, max])
#sorted varieties variable contains a coy of the dataframe where varieties are sorted in descending order and based
#on min and max price
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
#series that indes is reviewers and values is the average review score given out by the reviewer
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
#series with a index that is a multiindex of country and variety pairs, sorts the values in the series in descending order
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)