#!/usr/bin/env python
# coding: utf-8

# Newton
# 

# In[78]:


import numpy as np
import matplotlib.pyplot as plt


# In[79]:


# Definamos el sistema en una tupla
G=(lambda x,y,z: 6*x-2*np.cos(y*z)-1,    lambda x,y,z: 9*y+np.sqrt((x**2)+np.sin(z)+1.06)+0.9,    lambda x,y,z: 60*z+3*np.exp(-x*y)+10*np.pi-3)


# In[80]:


for i in range(3):
    print(G[i](0,0,0))


# In[81]:


def GetVectorF(G,r):
    
    dim = len(G)
    
    v = np.zeros(dim)
    
    for i in range(dim):
        v[i] = G[i](r[0],r[1],r[2])
        
    return v


# In[82]:


GetVectorF(G,[0,0,0])


# In[83]:


def GetJacobian(G,r,h=1e-6):
    
    dim = len(G)
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        J[i,0] = (  G[i](r[0]+h,r[1],r[2]) - G[i](r[0]-h,r[1],r[2]) )/(2*h)
        J[i,1] = (  G[i](r[0],r[1]+h,r[2]) - G[i](r[0],r[1]-h,r[2]) )/(2*h)
        J[i,2] = (  G[i](r[0],r[1],r[2]+h) - G[i](r[0],r[1],r[2]-h) )/(2*h)
        
    return J.T


# In[84]:


GetJacobian(G,[0,1,-1])


# In[85]:


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


# In[86]:


r,it,distancias = NewtonRaphson(G,[0,0,0])


# In[87]:


plt.plot(distancias)


# In[88]:


print(r)


# In[ ]:





# In[ ]:




