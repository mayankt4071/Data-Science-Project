
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils

os.chdir('G:\syllabus\DS\Prax')

ds=pd.read_csv('India Mortality.csv')

ds.info()

ds.head(5)

#plotting the scatter plot to process Naive model
plt.scatter(ds['YEAR'],ds['IND'],c='red')
plt.title('Scatter plot of year vs ind rate')
plt.xlabel('Year')
plt.ylabel('Rate(India)')
plt.show()

#spliting the data in train and test parametes
x_train, x_test, y_train, y_test = train_test_split(ds[['YEAR']], ds.IND, test_size=0.9)

#test parameter
x_test

#train parameter
x_train

#importing library
from sklearn.naive_bayes import GaussianNB

#naming the model
model1=GaussianNB()

#converting the float values to int 
lab_enc = preprocessing.LabelEncoder()
y_train_encoded = lab_enc.fit_transform(y_train)
print(y_train_encoded)
print(utils.multiclass.type_of_target(y_train))
print(utils.multiclass.type_of_target(y_train.astype('int')))
print(utils.multiclass.type_of_target(y_train_encoded))

#performing the fit function to run the model
model1.fit(x_train,y_train_encoded)

#prediction of the model
model1.predict(x_test)

model1.predict_proba(x_test)

#score of the model
model1.score(x_train,y_train_encoded)

#Now taking the data of Australia

plt.scatter(ds['YEAR'],ds['AUS'],c='red')
plt.title('Scatter plot of year vs ind rate')
plt.xlabel('Year')
plt.ylabel('Rate(Australia)')
plt.show()

#spliting the data in train and test parametes
x_train, x_test, y_train, y_test = train_test_split(ds[['YEAR']], ds.AUS, test_size=0.9)

#naming the model
model2=GaussianNB()

#converting the float values to int 
lab_enc = preprocessing.LabelEncoder()
y_train_encoded = lab_enc.fit_transform(y_train)
print(y_train_encoded)
print(utils.multiclass.type_of_target(y_train))
print(utils.multiclass.type_of_target(y_train.astype('int')))
print(utils.multiclass.type_of_target(y_train_encoded))

model2.fit(x_train,y_train_encoded)

model2.predict(x_test)

model2.score(x_train,y_train_encoded)

model2.predict_proba(x_test)




