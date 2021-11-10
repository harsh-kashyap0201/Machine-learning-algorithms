#!/usr/bin/env python
# coding: utf-8

# ## importing libraries

# In[85]:


import numpy as np 
import pandas as pd


# ## reading dataset

# In[86]:


df = pd.read_csv('D:\Downloads\play_tennis.csv')
df


# In[87]:


df.shape
df.head()


# ## spliting data in feature and target

# In[88]:


# Show the list of columns 
feature=list(df.columns[0:5])
print("Feature columns: \n{}".format(feature))
#Separate the data into feature data and target data (X_all and y_all, respectively)
x= df[feature].values
y= df['play'].values
x


# ## naive bayes algorithm

# In[89]:


#function to calculate conditional probablity
def conditional_prob(feature,col_num,out):
    num=0
    den=0
    for i in range(len(y)):
        if ((x[i][col_num].lower()==feature.lower()) and (y[i].lower()==out.lower())):
            num=num+1
    for item in y:
        if (item.lower()==out.lower()):
            den=den+1
    return num/den
            


# In[90]:


#function to calculate prior probablity
def prior_prob(out):
    num=0
    for item in y:
        if (item.lower()==out.lower()):
            num=num+1
    return num/len(y)


# In[91]:


def nb(new_instance):   
    p_yes=prior_prob("Yes")
    for i in range(len(feature)-1):
        p_yes=p_yes*conditional_prob(new_instance[i],i+1,"Yes")
    p_no=prior_prob("No")
    for i in range(len(feature)-1):
        p_no=p_no*conditional_prob(new_instance[i],i+1,"No")
    #normalization
    pnb_y=p_yes/(p_yes+p_no)
    pnb_n=p_no/(p_yes+p_no)
    print("probablity of yes : ",pnb_y)
    print("probablity of no : ",pnb_n)
    if(pnb_y>pnb_n):
        print("classification = yes")
    else:
         print("classification = no")
  


# ## new instance for classification

# In[92]:


new_instance=[]
print("enter new instance : ")
for i in range(len(feature)-1):
    new_instance.append(input())
nb(new_instance)

