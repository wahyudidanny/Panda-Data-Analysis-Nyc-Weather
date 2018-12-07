#!/usr/bin/env python
# coding: utf-8

# In[1]:


#melt is use to reshape data or transform data
import pandas as pd

df= pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\11-Melt\\weather.csv')
df


# In[7]:


df1 = pd.melt(df,id_vars=["day"],var_name="city",value_name="temperature")
df1
#df1[df1["variable"]=="chicago"]


# In[ ]:




