# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:11:37 2016

@author: mjlivingston
"""

import pandas as pd

"""reading data and joining reviews and categories data sets"""

# read in portion of reviews data to sample (actual is 2GB total)

reviews = pd.read_csv('reviews.csv', nrows = 10000)
reviews.drop(reviews.columns[[0]], axis=1, inplace=True)
reviews.head()

# read in all of categories data with name (18 MB)

categories = pd.read_csv('names_categories.csv')
categories.drop(categories.columns[[0]], axis=1, inplace=True)
categories.head()

#inner join reviews onto categories across business_id. 
#This will be mutiple level as each business has mutiple categories 
#This could increase file by ~5x

categories_reviews = categories.merge(reviews, left_on = 'business_id',
                                      right_on = 'business_id', how='inner')
                                      
"""cleaning up data"""
  
# strip out ('b') first, then ('\'')  and then ('\"') around all the data                                  

columns = ('categories','business_id','name','text')
for c in columns:
    categories_reviews[c] = categories_reviews[c].str.strip('b')
    categories_reviews[c] = categories_reviews[c].str.strip('\'"')
    categories_reviews[c] = categories_reviews[c].str.strip()
    
# lower case name and text, strip punctuation from name and text  
    
import string
def remove_punctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s
    
columns = ('name','text')
for c in columns:
    categories_reviews[c] = categories_reviews[c].str.lower()    
    categories_reviews[c] = categories_reviews[c].apply(remove_punctuation)
    
"""The remove_punctuation takes a while to go through text column 
This will proabably have to be optimized as full data set will be much bigger
"""

#remove name from text, if it is in its row

categories_reviews['text'] = [t.replace(n, '') 
for t, n in zip(categories_reviews.text.astype
('str'), categories_reviews.name.astype('str'))]

"""Best way to do it and really fast"""








