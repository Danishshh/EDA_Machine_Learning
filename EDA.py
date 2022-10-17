#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[2]:


dataset= pd.read_csv("complete-data.csv")


# In[3]:


dataset.head()


# In[5]:


dataset.info


# In[7]:


dataset.describe()


# In[8]:


dataset.tail()


# In[10]:


dataset.shape


# In[11]:


dataset.columns


# In[13]:


dataset.max()


# In[14]:


dataset.min()


# In[15]:


dataset.count()


# In[16]:


dataset.corr()


# In[66]:


dataset.isna()


# In[20]:


dataset.columns


# In[23]:


dataset['Landslide'].plot()


# In[25]:


dataset.sort_values(by = "Landslide", ascending = True)


# In[26]:


dataset.sort_values(by = "Landslide", ascending = False)


# In[31]:


dataset['Aspect'].max()


# In[32]:


dataset['Aspect'].plot()


# In[33]:


dataset['Aspect']


# In[36]:


df = dataset.loc[100:250]


# In[40]:


df['Earthquake']


# In[41]:


dataset['Earthquake'].max()


# In[43]:


dataset.duplicated().sum()


# In[60]:


mask = np.triu(np.ones_like(dataset.corr()))
fig, ax = plt.subplots(figsize=(25,25),dpi=80, facecolor='g', edgecolor='r')
sns.heatmap(dataset.corr(), mask= mask, cmap="YlGnBu", vmax=.2, annot = True, center = 0,annot_kws={"fontsize":16})


# In[63]:


list1 = ['Aspect', 'Earthquake', 'Profile', 'Landslide', 'Slope']
sns.heatmap(dataset[list1].corr(), annot = True, fmt = '.2f')
plt.show()


# In[68]:


dataset.shape


# In[73]:


dataset.plot()


# In[ ]:




