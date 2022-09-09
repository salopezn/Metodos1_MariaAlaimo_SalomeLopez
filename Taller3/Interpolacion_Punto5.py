#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import matplotlib.pyplot as plt
import wget
import pandas as pd
import os.path as path
import sympy as sym


# In[36]:


file="Newton_gregory.csv"
url="https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv"
if not path.exists(file):
    Path_=wget.download(url,file)
else:
    print('--File found---')
    Path_ = file


# In[37]:


Data = pd.read_csv(Path_,sep=',')


# In[38]:


Data


# In[39]:


X = np.float64(Data['X'])
Y = np.float64(Data['Y'])


# In[40]:


Diff = np.zeros((len(X),len(Y)))
Diff[:,0]= Y
Diff


# In[41]:


def NewtonGregory(X,Y,x):
    
    Sum_ = Y[0]
    
    Diff = np.zeros((len(X),len(Y)))
    Diff[:,0] = Y
    
    poly = 1.0
    
    for i in range(1,len(X)):
        
        poly *= ( x - X[i-1] )
        
        for j in range(i, len(X)):
            h = X[j] - X[j-i]
            Diff[j,i] = (Diff[j,i-1]-Diff[j-1,i-1])/h
        Sum_ += poly*(Diff[i,i])
    
    return Sum_


# In[42]:


x = np.linspace(np.min(X),np.max(X),100)
y = NewtonGregory(X,Y,x)


# In[43]:


plt.scatter(X,Y,color='r')
plt.plot(x,y)


# In[44]:


x = sym.Symbol('x')
f=NewtonGregory(X,Y,x)
f=f.expand()
f


# Metodo lagrange

# In[ ]:




