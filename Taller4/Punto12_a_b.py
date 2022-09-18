#!/usr/bin/env python
# coding: utf-8

# In[18]:



import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


# **Punto a**
# n=2

# In[19]:


Rootsa,Weightsa = np.polynomial.legendre.leggauss(2)


# In[20]:


a = 1
b = 2
f = lambda x : 1/(x**2)
ta = 0.5*((b-a)*Rootsa + a + b)


# In[21]:


Integral = 0.5*(b-a)*np.sum( Weightsa*f(ta) )
real=lambda x : -1/x
Integral,real(2)-real(1)


# In[ ]:





# **Punto b**
# n=3

# In[22]:


Rootsb,Weightsb = np.polynomial.legendre.leggauss(3)


# In[23]:


a = 1
b = 2
f = lambda x : 1/(x**2)
ta = 0.5*((b-a)*Rootsb + a + b)


# In[24]:


Integral = 0.5*(b-a)*np.sum( Weightsb*f(ta) )
real=lambda x : -1/x
Integral,real(2)-real(1)


# In[ ]:




