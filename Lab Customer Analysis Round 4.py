#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


df = pd.read_csv("marketing_customer_analysis (1).csv")

pd.read_csv ("marketing_customer_analysis (1).csv")


# In[29]:


numerical = df.select_dtypes(include=np.number)
categoricals = df.select_dtypes(include=object)

numerical.dtypes


# In[30]:


categoricals.dtypes


# In[31]:





# In[33]:


for column in numerical.columns:
    plt.hist(numerical[column])  
    
    plt.show()


# In[39]:


for column in numerical.columns:
    plt.hist(numerical[column])
    plt.title(f'Histogram for {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# In[40]:


correlation_matrix = numerical.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# In[ ]:




