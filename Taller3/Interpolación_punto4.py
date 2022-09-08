#!/usr/bin/env python
# coding: utf-8

# In[21]:


pip install wget


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import sympy as sym
import os.path as path
import wget


# In[2]:


file = 'olademar.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    print('--File found---')
    Path_ = file


# In[ ]:





# In[3]:


Data = pd.read_csv(Path_,sep=',')


# In[4]:


def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod


# In[5]:


def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum


# In[6]:


X = np.float64(Data['X'])
Y = np.float64(Data['Y'])


x = np.linspace(0,8,100)
y = Poly(x,X,Y)


# In[7]:


plt.scatter(X,Y,color='r')
plt.plot(x,y,color='k')


# In[14]:


x = sym.Symbol('x')
f=Poly(x,X,Y)
c=sym.expand(f)
c


# In[10]:


c=sym.expand(f)
c


# In[16]:


b=np.polyfit(X,Y,len(X)-1)
b


# Usando 
# $$Y= y0+V0yt+0.5*g(t^2)$$
# $$X=Vxt$$
# 
# Se obtiene que:
# $$Vx^2=g/2a$$
# $$Vy=b*Vx$$
# $$theta=arctan(Vy/Vx)$$

# In[27]:


Vx=np.sqrt(-9.8/(2*b[0]))
Vy=b[1]*Vx
Vinicial=np.sqrt((Vx)**2+(Vy)**2)
theta=np.arctan(Vy/Vx)
grados=np.degrees(theta)

print(f"La velocidad inicial de la bala es {Vinicial.round(1)} m/s" )
print(f"El ángulo inicial de salida es {grados.round(1)} grados" )


# In[ ]:





# In[ ]:




