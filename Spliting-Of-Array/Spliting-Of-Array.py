#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Spliting Of Array
import numpy as np
x = np.arange(9)
print("Split the array 3 equal sized sub arrays")
np.split(x,3)
print(np.split(x,3))


# In[7]:


#hsplit
import numpy as np
y = np.array([("germany","france","hungary","austria"),("berlin","paris","budpest","vienna")])
p1,p2 = np.hsplit(y,2)
print(p1)
print(p2)


# In[9]:


p_1,p_2 = np.split(y,2)
print(p_1)
print(p_2)


# In[10]:


#Array Unpackaging
countries,capitals = y
print(countries)
print(capitals)

