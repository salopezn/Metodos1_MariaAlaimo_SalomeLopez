#!/usr/bin/env python
# coding: utf-8

# In[64]:


import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import sympy as sym
import random
import scipy.special as sc


# In[65]:


def func(x,a=2,b=4):
    l = lambda n : np.math.factorial(n-1)
    f=(((l(a+b))/(l(a)*l(b))))*(x**(a-1))*((1-x)**(b-1))
    return f    


# In[66]:


def acep_rechazo(a,b,f,N):
    lis=[]
    x=np.zeros(N)
    fx=np.zeros_like(x)
    y=np.zeros_like(x)
    for i in range(N):
        x[i]=random.uniform(a,b)
        fx[i]=f(x[i])
    y_max=np.max(fx)
    for i in range(N):
        y[i]=random.uniform(0,y_max)
        if y[i]<fx[i]:
            lis.append(x[i])
    return lis, y_max 


# In[71]:


N=1000
prueba,y_max=acep_rechazo(0,1,func,N)
n=len(prueba)
#el volumen es el punto max * el ancho del intervalo (area del paralelpipedo)
V=y_max*1
A = (n/N)*V
print(A)


# In[ ]:




