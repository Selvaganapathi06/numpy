#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy Iterating:
#example:
import numpy as np
a=np.arange(12)**2
for i in a:
    print(i**(1/2))


# In[3]:


#Iterating in arrays
students = np.array([['selva','gana','pati'],[99,98,97],[100,98,98]])
for i in students:
    print(i)


# In[4]:


#Flatten[Using to fetching values in one by one.row wise,coloumn wise]
#row
students = np.array([['selva','gana','pati'],[99,98,97],[100,98,98]])
for i in students.flatten():
    print(i)


# In[5]:


#FLatten Column wise
students = np.array([['selva','gana','pati'],[99,98,97],[100,98,98]])
for i in students.flatten(order = 'f'):
    print(i)


# In[10]:


#ndtier[Similer to the flatten but ndtier gave best background cpu utilization]
#nditer row wise
import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
for i in np.nditer(a):
    print(i)


# In[12]:


#nditer coloumn wise
import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
for i in np.nditer(a,order = 'F'):
    print(i)

