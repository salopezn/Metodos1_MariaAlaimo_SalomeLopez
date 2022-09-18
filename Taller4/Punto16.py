#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


# **Punto a**

# In[109]:


Roots,Weights = np.polynomial.laguerre.laggauss(3)


# In[110]:


a = -1
b = 1
f = lambda x : (x**3 * np.exp(x))/((np.exp(x))-1)
t = 0.5*((b-a)*Roots + a + b)


# In[119]:


Integral = np.sum( Weights*f(t))
real=(np.pi**4)/15
Integral,real


# **Punto b**

# In[79]:


x=[2,3,4,5,6,7,8,9,10]


# In[117]:


n=1
errores=[]
for i in range(2,11):
    Roots,Weights = np.polynomial.laguerre.laggauss(i)
    t = 0.5*((b-a)*Roots + a + b)
    integral = np.sum( Weights*f(t))
    error=(integral/real)
    errores.append(error)
    i+=1
errores


# In[118]:


plt.figure(figsize=(5,5))
plt.grid()
plt.title("Laguerre cuadrature accuracy")
plt.plot(x,errores,"o")


# In[ ]:




