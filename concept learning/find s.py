#!/usr/bin/env python
# coding: utf-8

# # find S algorithm

# ### importing libraries

# In[5]:


import pandas as pd
import numpy as np


# ### reading dataset

# In[6]:


dataset=pd.read_csv("D:\Downloads\play_tennis.csv") 
dataset


# In[7]:


## converting data to list
data_list=dataset.values.tolist()
data_list


# ### find S algorithm

# In[8]:



attribute_count=len(data_list[0])-1
print("initial hypothesis : ",end="")
hypothesis=['0']*attribute_count
print(hypothesis)
for i in range(len(data_list)):
    if (data_list[i][attribute_count]=="Yes"):
        print("\niteration ",i+1," : positive instance")
        for j in range(attribute_count):
            if((hypothesis[j]==data_list[i][j]) or (hypothesis[j]=='0')):
               hypothesis[j]=data_list[i][j]
            else:
                hypothesis[j]='?'
        print("h",i+1," : ",hypothesis)
    else:
        print("\niteration ",i+1," : negative instance")
        print("h",i+1," : ",hypothesis)
print("------------------------------------------------------------------------")
print("\nmaximally specific hypothesis for the given dataset is : ",hypothesis)
               


# In[ ]:




