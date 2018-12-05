#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
df1 = pd.DataFrame({
    "city" : ["new york","chicago","orlando","baltimore"],
    "temperature" : [21,14,35,32],
})
df1


# In[10]:


df2 = pd.DataFrame({
    "city" : ["chicago","new york","san fransisco"],
    "humidity" : [68,65,51]
})
df2


# In[15]:


df3=pd.merge(df1,df2,on="city",how="outer",indicator="True")
df3


# In[16]:


df1 = pd.DataFrame({
    "city" : ["new york","chicago","orlando","baltimore"],
    "temperature" : [21,14,35,32],
    "humidity"  : [65,68,71,75],
})
df1


# In[17]:


df2 = pd.DataFrame({
    "city" : ["new york","chicago","san diego"],
    "temperature" : [21,14,35],
    "humidity"  : [65,68,71],
})
df2


# In[19]:


df3 = pd.merge(df1,df2,on="city",suffixes=('_left','_right'))
df3


# In[ ]:




