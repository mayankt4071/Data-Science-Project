#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils


# In[2]:


os.chdir('G:\syllabus\DS\Prax')


# In[3]:


ds= pd.read_csv('India Mortality.csv')


# In[4]:


ds.info()


# In[ ]:





# In[ ]:





# In[7]:


#plotting the scatter plot to process Logistic Regression
plt.scatter(ds['YEAR'],ds['IND'],c='red')
plt.title('Scatter plot of year vs ind rate')
plt.xlabel('Year')
plt.ylabel('Rate(India)')
plt.show()


# In[53]:


#size of the columns and rows
ds.shape


# In[ ]:





# In[8]:


#spliting the data in train and test parametes
x_train, x_test, y_train, y_test = train_test_split(ds[['YEAR']], ds.IND, test_size=0.5)


# In[9]:


#test parameter
x_test


# In[10]:


#train parameter
x_train


# In[11]:


from sklearn.linear_model import LinearRegression


# In[14]:


#creating a model
model1=LinearRegression(normalize=True)


# In[15]:


#using 'fit' function on train parameters
model1.fit(x_train,y_train)


# In[ ]:





# In[32]:


#the model works
model1.fit(x_train,y_train_encoded)


# In[36]:


#prediction of the test parameters
model1.predict(x_test)


# In[ ]:





# In[37]:


model1.score(x_train,y_train)


# In[20]:


#plotting the model for AUS
plt.scatter(ds['YEAR'],ds['AUS'],c='red')
plt.title('Scatter plot of year vs ind rate')
plt.xlabel('Year')
plt.ylabel('Rate(India)')
plt.show()


# In[21]:


x_train, x_test, y_train, y_test = train_test_split(ds[['YEAR']], ds.AUS, test_size=0.5)


# In[22]:


x_test


# In[23]:


x_train


# In[24]:


model2=LinearRegression(normalize=True)


# In[ ]:





# In[29]:


model2.fit(x_train,y_train)


# In[30]:


model2.predict(x_test)


# 

# In[ ]:





# In[31]:


model2.score(x_train,y_train_encoded)


# In[ ]:




