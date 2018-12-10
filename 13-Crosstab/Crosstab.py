#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_excel("E:\\Github Repository\\Panda-Data-Analysis-Nyc-Weather\\13-Crosstab\\survey.xls")
df
#the purpose of cross tab is to showing the frequency of spesific variable in table


# In[11]:


#pd.crosstab(df.Nationality,df.Handedness)
#pd.crosstab(df.Sex,df.Handedness,margins=True)
#pd.crosstab(df.Sex,[df.Handedness,df.Nationality],margins=True)
pd.crosstab([df.Sex],[df.Handedness],normalize='index')


# In[17]:


pd.crosstab([df.Sex],[df.Handedness],normalize='index')


# In[19]:


import numpy as np
pd.crosstab([df.Sex],[df.Handedness], values=df.Age, aggfunc=np.average)


# In[ ]:





# In[ ]:




