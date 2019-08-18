#!/usr/bin/env python
# coding: utf-8

# In[12]:


#numpy indexing and slicing
import numpy as np
a= np.arange(11)**2
print(a)
print(a[2])
print(a[-2])
print(a[2:])
print(a[2:-2])
print(a[:7])
print(a[:11:2])
#-ve indexing used 
print(a[::-1])
a="selva"
print(len(a))
print(a[::-1])

