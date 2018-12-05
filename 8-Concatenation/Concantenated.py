#!/usr/bin/env python
# coding: utf-8

# In[2]:


#concatenate
import pandas as pd
india_weather = pd.DataFrame({
    "city" : ["mumbai","delhi","bangalore"],
    "temperature" : [32,45,30],
    "humidity" : [80,60,78]
})
india_weather


# In[3]:


us_weather = pd.DataFrame({
    "city" : ["new york","chicago","orlando"],
    "temperature" : [21,14,35],
    "humidity" : [68,65,75]
})
us_weather


# In[6]:


df = pd.concat([india_weather,us_weather], ignore_index=True)
df


# In[7]:


df = pd.concat([india_weather,us_weather], keys=["india","us"])
df


# In[9]:


df.loc["us"]


# In[19]:


temperature_df = pd.DataFrame({
    "city" : ["mumbai","delhi","banglore"],
    "temperature" : [32,45,30],
},index=[0,1,2])
temperature_df


# In[20]:


windspeed_df = pd.DataFrame({
    "city" : ["delhi","mumbai"],
    "temperature" : [7,12],
},index=[1,0])
windspeed_df


# In[22]:


df = pd.concat([temperature_df,windspeed_df],axis=1)
df


# In[23]:


temperature_df


# In[25]:


s = pd.Series(["Humid","Dry","Rain"],name="event")
s


# In[26]:


df = pd.concat([temperature_df,s],axis=1)
df


# In[ ]:




