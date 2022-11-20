#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import matplotlib.pyplot as plt


# # Prueba con números aleatorios y su gráfica

# In[56]:


#Probabilidades de la urna 1
PU1=np.array([3/10,1/10,6/10])
F1=np.cumsum(PU1)#array([3/10,4/10,1])
F1


# In[57]:


PU=np.array([1/3,2/3])
FU=np.cumsum(PU)
PU1=np.array([3/10,1/10,6/10])
PU2=np.array([6/10,2/10,2/10])
P=np.array([PU1,PU2])
P


# In[58]:


FU


# In[59]:


x1


# In[60]:


F=np.cumsum(P,axis=1)
F


# In[61]:


color=np.zeros(1000)
for i,(x1,x2) in enumerate(np.random.rand(1000,2)):
    num_urna=np.searchsorted(FU,x1)
    color[i]=np.searchsorted(F[num_urna],x2)


# In[62]:


#print(color)


# In[63]:


plt.hist(color,bins=[0,1,2,3],density=True)


# In[64]:


nombres = {0:"Rojo",1:"Negro",2:"Verde"}


# In[65]:


plt.hist([nombres[x] for x in color])


# # Comprobación de la gráfica con procesos analíticos

# Probabilidad de que sea roja (1/2)
# 
# P(R)=P(R/U1)P(U1)+P(R/U2)P(U2)

# In[84]:


PR=PU1[0]*PU[0]+PU2[0]*PU[1]
print(PR)


# Probabilidad de que sea negra (1/6)
# 
# P(N)=P(N/U1)P(U1)+P(N/U2)P(U2)

# In[85]:


PN=PU1[1]*PU[0]+PU2[1]*PU[1]
print(PN)


# Probabilidad de que sea de la urna 1 si se ha obtenido una bola negra (1/5)
# 
# Usar teorema de Bayes:
# P(U1/N)=P(N/U1)·P(U1)/P(N)

# In[86]:


PU1N=(PU1[1]*PU[0])/(PN)

print(PU1N)


# Probabilidad de que sea de la urna 2 si se ha obtenido una bola negra: (4/5)
# 
# Usar teorema de Bayes:
# P(U2/N)=P(N/U2)·P(U2)/P(N)

# In[89]:


PU2N=(PU2[1]*PU[1])/(PN)

print(PU2N)


# In[ ]:




