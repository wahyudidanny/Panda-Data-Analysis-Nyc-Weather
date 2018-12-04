#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\5-Handling Missing Data\\weather.csv', parse_dates=['day'])
#type(df.day[0])
df.set_index('day',inplace=True)
df


# In[8]:


now_df = df.fillna(0)
now_df


# In[9]:


now_df = df.fillna({
    'temperature' : 0,
    'windspeed' : 0,
    'event' : 'no_event'
})
now_df


# In[13]:


now_df = df.fillna(method="ffill",limit=1) #limit for fill the data
#now_df = df.fillna(method="bfill")
#now_df = df.fillna(method="bfill",axis="columns")
#now_df = df.fillna(method="ffill")
now_df


# In[15]:


now_df = df.interpolate(method="time")
now_df


# In[18]:


#want to drop the n.a.
#now_df = df.dropna()
#now_df = df.dropna(how="all") # jika dalam row tidak memiliki data n.a
#now_df = df.dropna(thresh=1) #at least n argument n.a
now_df


# In[20]:


#fill data 
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
df


# In[ ]:




