#!/usr/bin/env python
# coding: utf-8

# In[2]:


#cara pertama untuk membuat dataframe
import pandas as pd
df=pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\3-Different way create DF\\weather.csv')
df


# In[6]:


# cara ke dua untuk membuat Data frame
df = pd.read_excel('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\3-Different way create DF\\weather.xlsx','weather')
df


# In[7]:


#cara ke 3 untuk create dataframe
weather_data =[
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow'),
]
df = pd.DataFrame(weather_data, columns=['day','temperature','windspeed','event'])
df


# In[8]:


# cara keempat data frame
weather_data ={
    'day':['1/1/2017','1/2/2017','1/3/2017'],
    'temperature':[32,23,28],
    'windspeed':[6,7,2],
    'event':['Rain','Sunny','Snow']  
}
df = pd.DataFrame(weather_data)
df


# In[9]:


# create df 5 ways
weather_data = [
    {'day':'1/1/2017','temperature':32,'windspeed':6 , 'event':'Rain'},
    {'day':'1/2/2017','temperature':35,'windspeed':7 , 'event':'Sunny'},
    {'day':'1/3/2017','temperature':28,'windspeed':2 , 'event':'Snow'}
]

df= pd.DataFrame(weather_data)
df


# In[ ]:




