# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:29:32 2016

@author: mjlivingston
"""


import pandas as pd

##reading data and joining reviews and categories data sets

# read in portion of reviews data (2GB total)
reviews = pd.read_csv('reviews.csv', nrows = 1000)
reviews.drop(reviews.columns[[0]], axis=1, inplace=True)
reviews.head()

# read in all of categories data (12.3MB)
categories = pd.read_csv('categories.csv')
categories.drop(categories.columns[[0]], axis=1, inplace=True)
categories.head()

#remove extra white spaces in categories
categories['categories'] = categories['categories'].str.strip()

# read in b_ids and name
names = pd.read_csv('B_ID_NAME.csv')
names.drop(names.columns[[0]], axis=1, inplace=True)

#inner join names onto categories across business_id





