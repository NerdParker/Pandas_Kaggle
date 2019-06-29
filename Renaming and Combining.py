# -*- coding: utf-8 -*-
"""

@author: ParkerHall
"""
#imports pandas and Kaggles feedback system
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")

# Load some other datasets used in this exercise
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

reviews.head()
#copy of the reviews data with columns renamed to region and locale
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))
#sets index name in dataset to wines
reindexed = reviews.rename_axis('wines', axis='rows')
#takes the preloaded data frame of products from lines 16-19 and creates a dataframe of products
combined_products = pd.concat([gaming_products, movie_products])
#load two poerlifting datasets
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
#uses the unique key of MeetID to join the tables into one
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))