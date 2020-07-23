# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:10:28 2020

@author: Vaishnavi
"""


import pandas as pd


data_country=pd.read_excel('Book1.xlsx',sheet_name='Country estimates')#reading excel sheet1
print(data_country)
print('\n Information:\n' )
print(data_country.info())
print('\n describe: \n',data_country.describe())
print('\n DATA TYPES: \n')
print(data_country.dtypes)#datatypes of 

print('\n ATTRIBUTES OF DATAFRAME \n')
print(data_country.set_index("ISO Code"))#indexing on ISO Code col

print('\n index row labels \n',data_country.index)
print('\n columns name: \n',data_country.columns)
print('\n dataframe size \n',data_country.size)
print('\n dimentions of dataframe \n',data_country.shape)
print('\n array dimentions \n',data_country.ndim)
print('\n memory used by dataframe: \n',data_country.memory_usage())

print('\n MAX VALUE OF EACH COL: \n')
max_value_country=data_country.max()
print(data_country.max())

print('\n MIN VALUE OF EACH COL: \n')
min_value_country=data_country.min()
print(data_country.min())

print('\n NULL VALUES ARE PRESENT OR NOT: \n')
print(pd.notnull('Book1.xlsx'))#null values are present or not

print('\n COUNT OF NULL VALUES: \n')
null_columns=data_country.columns[data_country.isnull().any()]
Null_value_country=data_country[null_columns].isnull().sum()

print('\n TOTAL NO. OF COLS CONTAINING NULL VALUES: \n')
null_columns=data_country.columns[data_country.isnull().any()]
data_country[null_columns].isnull().sum()
missing_country=data_country[data_country.isnull().any(axis=1)]
print('No. of cols containing null values: ',null_columns) 

print('\n SELECTING DATA: \n')
print('\n diplay 3 rows and 2 cols \n',data_country.iloc[:3,:2])#diplay 3 rows and 2 cols
print('\n Display first 3 rows using head: \n',data_country.head(3))
print('\n Display last 3 rows using tail: \n',data_country.tail(3))

print('\n SORT DATAFRAME: \n')
print(data_country.sort_values(by=["ISO Code"]))

print('\n diplay 3 rows and 2 cols \n',data_country.iloc[:6,:6])#diplay 3 rows and 2 cols

print('\n Mean of each column:\n')
mean_country=data_country.mean()
print(data_country.mean())


print('\n Mode of each column:\n')
mode_country=data_country.mode()
print(data_country.mode())


print('\n Median of each column:\n')
median_country=data_country.median()
print(data_country.median())

data_country2_copy=data_country.copy(deep=True)

