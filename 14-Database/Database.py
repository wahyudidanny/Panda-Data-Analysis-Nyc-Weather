#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlalchemy


# In[6]:


engine = sqlalchemy.create_engine('mssql://DANNYWAHYUDI-PC/SQLEXPRESS/DotNetCore?trusted_connection=yes')
df = pd.read_sql_table("COSTUMER",engine)


# In[ ]:




