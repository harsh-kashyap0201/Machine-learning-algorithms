#!/usr/bin/env python
# coding: utf-8

# # knn hard code (20bkt0039)

# ## importing libraries and dataset

# In[57]:


import math
import pandas as pd
#importing dataset
dataset = pd.read_csv('D:\Downloads\speed_agitality.csv')
dataset    


# ## knn algorithm

# In[58]:


#splitting dataset into points and labels
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
#testing point
p = (6.75,3.5)
n= dataset.shape[0] #number of observations
for k in range(3,10,2): 
    #loop to check for different values of k
    #since number of observations is odd choose odd values of k
    distance=[]
    for i in range(n):
        #finding euclidian distance
        euclidian_distance=math.sqrt((x[i][0]-p[0])**2 +(x[i][1]-p[1])**2)
        distance.append((euclidian_distance,(x[i],y[i])))
    # sorting distance list in ascending order and selecting first k distances
    distance = sorted(distance)[:k]
    yes_count = 0 #count of yes
    no_count = 0 #count of no
    for i in range (k):
            if distance[i][1][1] == "yes":
                yes_count=yes_count+1
            elif distance[i][1][1] == "no":
                no_count=no_count+1
    if(yes_count>no_count):
        #if number of yes is more
        print("for k = ",k, "classification = yes")
    else:
        #if number of no is more
         print("for k = ",k,"classification = no")

