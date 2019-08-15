#!/usr/bin/env python
# coding: utf-8

# In[3]:


#universal Functions
#Trignomattery
#we not directly convert angles to
import numpy as np
angles = np.array([0,30,45,60,90,180,360])
radians = angles*np.pi/180
signvalue = np.sin(radians)
print("sign value:",signvalue)
cosvalue = np.cos(radians)
print("cos value:",cosvalue)
tanvalue = np.tan(radians)
print("tan value:",tanvalue)


# In[28]:


#Statistcal Functions
import sys
import numpy as np
from io import BytesIO
#sam = D:\advancepython\data\realtimedatasetsnumpy\salary.csv
salary = np.genfromtxt('salary.csv')
#np.set_printoptions(threshold=sys.maxsize)
#Mean
print("Mean:",np.mean(salary))

#Median
print("Median",np.median(salary))
#Standard Deviation
print("SD:",np.std(salary))
#Variance
print("Variance",np.var(salary))
#Average
print("Variance",np.average(salary))

