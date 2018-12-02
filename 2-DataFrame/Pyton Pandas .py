#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
df=pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\2-DataFrame\\weather_example.csv')
df


# In[11]:


df.shape #for knowing the structur of the table 


# In[14]:


rows, column = df.shape
rows
column


# In[16]:


df.head() # for get data in the head of column


# In[19]:


df[2:5]


# In[24]:


df[['event','day','temperature']]


# In[27]:


df['temperature'].max()
df['event'].max()


# In[28]:


#can perform operation like sql 
df[df.temperature>=32]


# In[56]:


df[df.temperature==df.temperature.max()]


# In[63]:


df['day'][df.temperature==df.temperature].max()


# In[42]:


# to know what index
df.index


# In[58]:


df.set_index('day', inplace=True)
df


# In[60]:


df.loc['1/3/2017']


# In[62]:


df.reset_index(inplace=True) # if u want to reset index
df


# In[64]:


df.set_index('event', inplace=True)
df


# In[69]:


df.loc['Snow']


# In[ ]:




