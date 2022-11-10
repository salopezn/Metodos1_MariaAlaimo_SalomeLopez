#!/usr/bin/env python
# coding: utf-8

# ¿Cuántas sumas de 3 enteros no negativos dan 10?

# **Combinación con repetición**
# 
# -> No importa el orden
# 
# -> Se pueden repetir los números

# In[12]:


import numpy as np


# In[18]:


def com_rep(r,n):
    return (np.math.factorial(r+n-1))/((np.math.factorial(r))*(np.math.factorial(n-1)))


# In[19]:


com_rep(10,3)


# In[ ]:




