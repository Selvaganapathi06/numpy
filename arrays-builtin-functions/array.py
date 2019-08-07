#!/usr/bin/env python
# coding: utf-8

# In[1]:


#identity matrix
#get 1 as diagnal value
import numpy as np

arr_eye = np.eye(3)
arr_eye


# In[2]:


#we mentioned row, column, datatype
import numpy as np

arr_eye = np.eye(3,4,dtype=int)
arr_eye


# In[4]:


#builtin functions
#arange
import numpy as np

arr_eye = np.arange(2,20,2)
arr_eye


# In[6]:


#arange in float
import numpy as np

arr_eye = np.arange(2,3,0.2)
arr_eye


# In[12]:


#2d array
import numpy as np
arr2d = np.array([[1,2,3],[4,5,6]])
arr2d


# In[11]:


#2d array verification
import numpy as np
arr2d = np.array([[1,2,3],[4,5,6]])
arr2d.shape


# In[13]:


#multi dimensional
import numpy as np
arrnd = np.arange(6).reshape(3,2)
arrnd

