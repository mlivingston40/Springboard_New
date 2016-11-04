# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:07:38 2016

@author: mjlivingston

This is for a case where you have a dataframe and want to plot mutiple graphs.
The case is where you would like to see a given series (ie. classification set)
grouped by the series and all other factors.

The idea is that you want to see this series plotted against another factor
and the grouped frequency in the data set.


Has to be a dataframe of unique entries.  Already aggregated list might not
make sense.

"""

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8,4)})

#def frequency_plots(df,series,colname):
#    df.groupby([series, colname]).size().unstack(series).plot()
#    for colname, col in plotdata.iteritems():
#        print(groupings())
        
def frequency_plots(df,series):      
    for colname, col in df.iteritems():
        print(df.groupby([series, colname]).size().unstack(series).plot())

"""""" 

# Ryans way

group_vars = [('race', 'yearsexp'), ('race', 'sex')] for series, x in group_vars: data2 = data.groupby([series, x]).size() data2.unstack(series).plot()
 