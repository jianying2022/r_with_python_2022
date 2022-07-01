#!/usr/bin/env python
# coding: utf-8

# # load dependencs

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# # load data

# In[7]:


dataset = pd.read_csv("regrex1.csv")
dataset


# # regression 
# 

# In[8]:


# Fitting Linear Regression to the Dataset
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[['y']], dataset[['x']])
model.score(dataset[['y']], dataset[['x']])


# # plot

# In[9]:


#Visualizing the Linear Regression results
import matplotlib.pyplot as plt
plt.scatter(dataset[['y']], dataset[['x']], color = 'red')
plt.plot(dataset[['y']], model.predict(dataset[['y']]), color = 'blue')
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[ ]:




