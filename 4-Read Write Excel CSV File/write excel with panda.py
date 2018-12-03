#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\stock.csv',skiprows=1)
#jika pada header ada rows pada baris 1 maka gunakan skiprows=argument atau header = argument
df


# In[10]:


#jika pada csv/excel file tidak memiliki header maka bisa ditambahkan dengan header=none
df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\stock.csv',header=None,names=['ticker','aps','revenue','price','people'])
df


# In[11]:


# jika ingin mengambil beberapa row maka gunakan nrows=n

df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\stock.csv',nrows=3)
df


# In[16]:


# untuk mengisi value yang kosong/ n.a 
df = pd.read_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\stock.csv',na_values={
        'eps':['not available','n.a.'],
        'revenue':['not available','n.a.',-1],
        'people':['not available','n.a.']
})
df


# In[19]:


# how to write to csv
df.to_csv('E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\new.csv',index=False)


# In[20]:


df.columns


# In[27]:


#untuk write di CSV dan spesific kolom
df.to_csv("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\new2.csv",columns=['tickers','eps'])


# In[28]:


#tanpa header
df.to_csv("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\new3.csv",header=False)


# In[39]:


# jika ingin menambahkan data dari n.a bisa menggunakan converter 

def convert_people_cell(cell):
    if cell == 'n.a.':
         return 'sam walton'
    return cell
 
def convert_eps_cell(cell):
    if cell == 'not available':
         return None
    return cell
    
    
df = pd.read_excel("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\stock_data.xlsx",'Sheet1',converters = {'people':convert_people_cell,'eps':convert_eps_cell})
df


# In[48]:


# write to excel file
df.to_excel("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\\writedataframe.xlsx", sheet_name='stocks',startrow=1,startcol=2,index=False)


# In[50]:


#untuk menulis 2 dataframe pada 2 sheet yang berbeda pada excel

df_stocks = pd.DataFrame({
    'tickers':['GOOGL','WMT','MSFT'],
    'price':[323,253,228],
    'po':[61,71,28],
    'eps':[25,4,4]  
})


df_weather =pd.DataFrame({
    'day':['1/1/2017','1/2/2017','1/3/2017'],
    'temperature':[32,23,28],
    'windspeed':[6,7,2],
    'event':['Rain','Sunny','Snow']  
})

with pd.ExcelWriter("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\4-Read Write Excel CSV File\\\stockandweather.xlsx") as writer:
    df_stocks.to_excel(writer,sheet_name="stocks")
    df_weather.to_excel(writer,sheet_name="weather")
    


# In[ ]:




