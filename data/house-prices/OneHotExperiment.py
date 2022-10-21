# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:42:53 2022

@author: mcurral
"""

# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder


# # initializaing values
# data = {'Name':['Tom', 'Jack','Nick', 'Jonh',
#         'Tom', 'Jack','Nick','Jonh',
#         'Tom','Jack', 'Nick', 'Tom',],
#         'Time':[20,21,19,18,
#                 20, 100, 19, 18,
#                 21, 22, 21, 20]
# }

# #creating dataframe
# df = pd.DataFrame(data)

# # showing head
# df.head()



# importing pandas 
import pandas as pd
# importing numpy
import numpy as np
# importing OneHotEnconder
from sklearn.preprocessing import OneHotEncoder

# reading dataset
df = pd.read_csv('train.csv') #'house_price.csv')
df.head()

# checking features
cat = df.select_dtypes(include='O').keys()
# display variables
cat

# creating new df 
# setting columns we use
new_df = pd.read_csv('train.csv', usecols=['Neighborhood','Exterior1st','Exterior2nd'])
new_df.head()

# unique values in each columns
for x in new_df.columns:
    #printfting unique  values
    print(x, ':', len(new_df[x].unique()))


# finding the top 20 categories
new_df.Neighborhood.value_counts().sort_values(ascending=False).head(20)

# make list with top 10 variables
top_10 = [x for x in new_df.Neighborhood.value_counts().sort_values(ascending=False).head(10).index]
top_10

# make binary of labels
for label in top_10:
    new_df[label]=np.where(new_df['Neighborhood']==label,1,0)
new_df[['Neighborhood']+top_10]


pd.set_option('display.max_columns', None)

#for all categorical variables we selected
def top_x(df2, variable, top_x_labels):
    for label in top_x_labels:
        df2[variable+'_'+label] = np.where(data[variable]==label,1,0)
# read the data again
data = pd.read_csv('train.csv', usecols = ['Neighborhood', 'Exterior1st', 'Exterior2nd'])
#encode Neighborhood into the most frequent categories
top_x(data,'Neighborhood', top_10)
#display data
data.head()
