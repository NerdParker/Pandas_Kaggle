# -*- coding: utf-8 -*-
"""

@author: ParkerHall
"""
#imports pandas and Kaggles feedback system
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

#data type of the points in the column dataset
dtype = reviews.points.dtype
#series from the points column, converts the entries to strings
point_strings = reviews.points.astype(str)
#finds the number of reviews in the dataset that are missing a price
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
#series counting the number of times values occur in the region 1 field, it replaces missing values with Unknown
#sorts in descending order
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)