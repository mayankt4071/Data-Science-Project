# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:16:02 2020

@author: Vaishnavi
"""

# -*- coding: utf-8 -*-



import pandas as pd


data_regional=pd.read_excel('Book1.xlsx',sheet_name='Regional and global estimates')#reading excel sheet1
print(data_regional)
print('\n Information:\n' )
print(data_regional.info())
print('\n describe: \n',data_regional.describe())
print('\n DATA TYPES: \n')
print(data_regional.dtypes)#datatypes of 

print('\n ATTRIBUTES OF DATAFRAME \n')
print(data_regional.set_index("Region Name"))#indexing on ISO Code col

print('\n index row labels \n',data_regional.index)
print('\n columns name: \n',data_regional.columns)
print('\n dataframe size \n',data_regional.size)
print('\n dimentions of dataframe \n',data_regional.shape)
print('\n array dimentions \n',data_regional.ndim)
print('\n memory used by dataframe: \n',data_regional.memory_usage())

print('\n MAX VALUE OF EACH COL: \n')
max_value_regional=data_regional.max()
print(data_regional.max())

print('\n MIN VALUE OF EACH COL: \n')
min_value_regional=data_regional.min()
print(data_regional.min())

print('\n NULL VALUES ARE PRESENT OR NOT: \n')
print(pd.notnull('Book1.xlsx'))#null values are present or not

print('\n COUNT OF NULL VALUES: \n')
null_columns=data_regional.columns[data_regional.isnull().any()]
Null_value_regional=data_regional[null_columns].isnull().sum()

print('\n TOTAL NO. OF COLS CONTAINING NULL VALUES: \n')
null_columns=data_regional.columns[data_regional.isnull().any()]
data_regional[null_columns].isnull().sum()
missing_regional=data_regional[data_regional.isnull().any(axis=1)]
print('No. of cols containing null values: ',null_columns) 

print('\n SELECTING DATA: \n')
print('\n diplay 3 rows and 2 cols \n',data_regional.iloc[:3,:2])#diplay 3 rows and 2 cols
print('\n Display first 3 rows using head: \n',data_regional.head(3))
print('\n Display last 3 rows using tail: \n',data_regional.tail(3))

print('\n SORT DATAFRAME: \n')
print(data_regional.sort_values(by=["Region Name"]))

print('\n diplay 3 rows and 2 cols \n',data_regional.iloc[:6,:6])#diplay 3 rows and 2 cols

print('\n Mean of each column:\n')
mean_regional=data_regional.mean()
print(data_regional.mean())


print('\n Mode of each column:\n')
mode_regional=data_regional.mode()
print(data_regional.mode())


print('\n Median of each column:\n')
median_regional=data_regional.median()
print(data_regional.median())

data_regional2_copy=data_regional.copy(deep=True)

