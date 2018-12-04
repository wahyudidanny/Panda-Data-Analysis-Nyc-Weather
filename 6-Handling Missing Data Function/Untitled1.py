#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np

df = pd.read_csv("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\6-Handling Missing Data Function\\weather.csv")
df


# In[14]:


#new_df = df.replace(-99999,np.NaN)
new_df = df.replace({
        'temperature':-99999,
        'windspeed':-99999,
        'event' : '0'
        },np.NaN)

new_df


# In[15]:


new_df = df.replace({
         -9999:np.NaN,
         'No Event':'Sunny'
        })
new_df


# In[17]:


#removing with regex
new_df = df.replace({'temperature':'[A-Za-z]',
                     'windspeed' : '[A-Za-z]'},
                    '',regex=True)
new_df


# In[18]:


df = pd.DataFrame({
    'score':['exceptional','average','good','poor','average','exceptional'],
    'student':['rob','maya','parthiv','tom','julian','erica']    
})
df


# In[21]:


new_df= df.replace(['poor','averange','good','exceptional'],[1,2,3,4])
new_df


# In[ ]:




