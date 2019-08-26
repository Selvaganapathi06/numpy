#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
a = np.array([("germany","france","hungary","austria")])
a.shape
c= a.ravel()
print(c)
d = a.T
print(d)
e = a.T.ravel()
print(e)

