#!/usr/bin/env python
# coding: utf-8

# In[8]:


#dot function
#look like matrix multiplication
import numpy as np
A = np.array([[1,2],[0,1]])
B = np.array([[2,0],[3,4]])
c= np.dot(A,B)
print(c)
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2])
g = np.array([4,5])
### 1*4+2*5
np.dot(f, g)


# In[13]:


#Aggregation
import numpy as np
h = np.array([3,56,78,90,34,56,34,72])
#sum
print("sum of h:",h.sum())
#max
print("max of h:",h.max())
#min
print("min of h:",h.min())


# In[21]:


#Aggregation in axis based
import numpy as np
i = np.arange(12).reshape(3,4)
print(i)
#sum
print("sum",i.sum())
print("sum",i.sum(axis = 0))
print("sum",i.sum(axis = 1))
#min
print("min",i.min())
print("min",i.min(axis = 0))
print("min",i.min(axis = 1))
#max
print("max",i.max())
print("max",i.max(axis = 0))
print("max",i.max(axis = 1))

