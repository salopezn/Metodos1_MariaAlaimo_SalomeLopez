#!/usr/bin/env python
# coding: utf-8

# Usando la generaci´on de puntos sobre una esfera estime la siguiente integral (en C++
# y en Python), para {x
# 2 + y
# 2 + z
# 2 ≤ 1}:
# Z Z Z e
# √
# x2+y
# 2+z
# 2
# dxdydz = 4π(e − 2)

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from mpl_toolkits.mplot3d import axes3d


# In[ ]:





# In[14]:


def CreateSphere(N, R):
    
    X = np.zeros(N)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X)
    
    for i in tqdm(range(N)):
        u = np.random.rand()
        rho = R*u**(1/3)
        
        theta= np.random.uniform(0,2*np.pi)
        phi = np.random.uniform(0,np.pi)
        
        #cambio de variables
        X[i] = rho*np.sin(phi)*np.cos(theta)
        Y[i] = rho*np.sin(phi)*np.sin(theta)
        Z[i] = rho*np.cos(phi)
    
    
    return X,Y,Z


# In[15]:


X,Y,Z = CreateSphere( 10000,1 )


# In[16]:


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')

#configurar límites de los ejes
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.view_init(10, 60)

ax.scatter(X,Y,Z,color='g')


# In[17]:


def f(rho,theta,phi):
    x=rho*np.sin(phi)*np.cos(theta)
    y=rho*np.sin(phi)*np.sin(theta)
    z=rho*np.cos(phi)
    return np.exp(np.sqrt(((x**2)+(y**2)+(z**2))))


# In[18]:


def GetPoints(R):
    u = np.random.rand()
    rho = R*u**(1/3)    
    theta= np.random.uniform(0,2*np.pi)
    phi = np.random.uniform(0,np.pi)

    return rho,theta,phi


# In[19]:


N = int(1e6)
Sample = np.zeros(N)

for i in range(N):
    r,t,p = GetPoints(1)
    Sample[i] = f(r,t,p)


# In[20]:


Integral = (4/3)*np.pi * np.average( Sample )


# In[21]:


print(Integral, 4*np.pi*(np.exp(1)-2))


# In[ ]:




