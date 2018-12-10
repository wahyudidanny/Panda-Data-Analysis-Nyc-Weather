#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_excel("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\12-Stack Unstack\\stocks.xlsx",header=[0,1])
df


# In[9]:


#df.stack()
#df.stack(level=0)
df_stacked = df.stack()
df_stacked


# In[11]:


df_stacked.unstack()


# In[13]:


df2 = pd.read_excel("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\12-Stack Unstack\\stocks_3_levels.xlsx",header=[0,1,2])
df2


# In[17]:


df2.stack(level=2)


# In[18]:


df2.stack(level=2)


# In[ ]:




