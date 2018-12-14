#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import sqlalchemy
import pyodbc 


# In[15]:


#engine = sqlalchemy.create_engine('mssql+pymssql://DANNYWAHYUDI-PC//DotNetCore')
#df = pd.read_sql_table("Employees",engine)

sql_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DANNYWAHYUDI-PC;DATABASE=DotNetCore;Trusted_Connection=yes')
query = "SELECT * FROM [Employees]"
df = pd.read_sql(query, sql_conn)
df


# In[ ]:




