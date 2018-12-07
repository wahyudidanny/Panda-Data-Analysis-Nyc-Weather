#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\10-Pivot\\weather.csv')
df


# In[18]:


#pivot table is used to summerize and aggregate data inside dataframe
df.pivot(index="humidity",columns="city")


# In[14]:


da = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\10-Pivot\\weather2.csv')
da


# In[23]:


da.pivot_table(index="city",columns="date",margins=True)


# In[24]:


dc = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\10-Pivot\\weather3.csv')
dc


# In[26]:


df['date']=pd.to_datetime(df['date'])
df


# In[29]:


type(df['date'][0])


# In[30]:


df.pivot_table(index=pd.Grouper(freq="M",key="date"),columns="city")


# In[ ]:




