#!/usr/bin/env python
# coding: utf-8

# Newton
# 

# In[9]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


# Definamos el sistema en una tupla
G=(lambda x,y: np.log10((x**2)+(y**2))-np.sin(x*y)-np.log10(2)-np.log10(np.pi),    lambda x,y: np.exp(x-y)+np.cos(x*y))


# In[11]:


for i in range(2):
    print(G[i](2,2))


# In[12]:


def GetVectorF(G,r):
    
    dim = len(G)
    
    v = np.zeros(dim)
    
    for i in range(dim):
        v[i] = G[i](r[0],r[1])
        
    return v


# In[13]:


GetVectorF(G,[2,2])


# In[14]:


def GetJacobian(G,r,h=1e-6):
    
    dim = len(G)
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        J[i,0] = (  G[i](r[0]+h,r[1]) - G[i](r[0]-h,r[1]) )/(2*h)
        J[i,1] = (  G[i](r[0],r[1]+h) - G[i](r[0],r[1]-h) )/(2*h)
        
    return np.transpose(J)


# In[15]:


GetJacobian(G,[2,2])


# In[16]:


def NewtonRaphson(G,r,error=1e-10):
    
    it = 0
    d = 1
    Vector_d = np.array([])
    
    while d > error:
        
        it += 1
        
        rc = r
        
        F = GetVectorF(G,r)
        J = GetJacobian(G,r)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot( InvJ, F )
        
        diff = r - rc
        print(diff)
        
        d = np.linalg.norm(diff)
        
        Vector_d = np.append( Vector_d , d )
        
    return r,it,Vector_d


# In[17]:


r,it,distancias = NewtonRaphson(G,[2,2])


# In[18]:


plt.plot(distancias)


# In[19]:


print(r)


# In[ ]:





# In[ ]:




