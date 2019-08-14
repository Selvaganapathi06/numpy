#!/usr/bin/env python
# coding: utf-8

# In[4]:


#convert list as a numpy array
import numpy as np
lst = [1,2,3,4]
c = np.array(lst)
c
#print(c)


# In[5]:


#2d array
d = np.array([[1,2],[3,4]])
d


# In[8]:


#3d array
e =np.array([[1,2,3],[4,5,6],[7,8,9]])
e


# In[12]:


#shape and data type checking
f = np.array([[1,2],[3,4]])
print(f.shape)
print(f.dtype)


# In[14]:


#shape and data type checking
g = np.array([[1.0,2.0],[3.0,4.0]])
print(g.shape)
print(g.dtype)


# In[16]:


#zeros and ones
h = np.zeros([2,2])
print(h)


# In[18]:


#zeros and ones
i = np.zeros([3,3],dtype= 'int')
print(i)


# In[19]:


#ones
j = np.ones([3,3],dtype= 'int')
print(j)


# In[22]:


#return empty array
k = np.empty([2,2])
print(k)


# In[23]:


#return empty array
l = np.empty([2,2],dtype='int')
print(l)


# In[24]:


#return empty array
m = np.empty([2,2],dtype='float')
print(m)


# In[25]:


#identity matrix
#only value one is diagnal positions and remaining zeros
n = np.eye(5,5)
print(n)


# In[34]:


#reshape
o = np.array([[1,2,3],[4,5,6]])
print(o)
print("\nafter reshape:")
p =o.reshape(3,2)
print(p)
#flaten
print("\n FLatten:")
q = p.flatten()
print(q)


# In[42]:


#arange
#it is look like python range. we will generate values dynamically. we need to specify only start position and end position and increasing steps.
r = np.arange(12)
print(r)


# In[2]:


import numpy as np
s=np.arange(12).reshape(3,4)
print(s)

