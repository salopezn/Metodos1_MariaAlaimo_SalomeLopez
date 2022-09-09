#!/usr/bin/env python
# coding: utf-8

# Punto 3 Raíces de:
# $$3x^5+5x^4-x^3$$

# In[27]:


import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


# In[28]:


def Function(x):
    return (3*np.power(x,5))+(5*np.power(x,4))-(np.power(x, 3))


# In[29]:


def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)


# In[30]:


def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    error = 1
    it=0
    while error > precision and it < itmax:
        try:
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
        except ZeroDivisionError:
            print('Division por cero')
        xn = xn1
        it += 1
    if it == itmax:
        return False
    else:
        return xn


# In[31]:


def GetAllRoots(x,tolerancia=1e-5):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(Function,Derivative,i)
        
        if root != False:
            condicion=True
            for j in Roots:
              if abs(root-j)<tolerancia:
                condicion=False
            
            if condicion:

                Roots = np.append(Roots,root)
                
    Roots.sort()
    
    return Roots


# In[32]:


xtrial = np.linspace(-10,12,100)
Roots = GetAllRoots(xtrial)
Roots


# In[33]:


print(f"Las raíces del polinomio son: {Roots[0]},{Roots[1]},{Roots[2]}" )


# In[ ]:




