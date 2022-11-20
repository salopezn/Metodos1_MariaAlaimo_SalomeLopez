#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


# a) Distribución con info a priori

# In[40]:


States = np.array([0,1]) 
Prior =  np.array([0.4,0.6])


# In[3]:


# Definimos matrices de emisión y transmision
T = np.array([[0.8,0.2],[0.2,0.8]])

E = np.array([[0.5,0.9],[0.5,0.1]])
E


# In[4]:


DictH = {0:'Justa',1:'Sesgada'}
DictH[0]


# In[5]:


DictO = {0:'Cara',1:'Sello'}
DictO[1]


# In[6]:


Obs = np.array([1,0,0,0,1,0,1,0])


# In[7]:


def GetHiddenStates(States, N):
    
    CStates = list( combinations_with_replacement(States,N) )
    
    Permu = []
    
    for it in CStates:
        p = list(permutations(it,N))
        
        for i in p:
            if i not in Permu:
                Permu.append(i)
    
    #print(CStates)
    return np.array(Permu)


# In[8]:


#Justa o sesgada
HiddenStates = GetHiddenStates(States,8)
len(HiddenStates)


# In[9]:


#cara o sello
ObsStates = GetHiddenStates([0,1],8)
ObsStates
print(len(ObsStates))


# In[10]:


def GetProb(T,E,Obs,State,Prior):
    
    n = len(Obs)
    p = 1.
    
    p *= Prior[State[0] ]
    
    for i in range(n-1):
        p *= T[ State[i+1], State[i] ]
    
    
    
    for i in range(n):
        p *= E[ Obs[i], State[i] ]
        
    #print(p, State)
    
    return p


# b) Hallar secuencia oculta más probabñe

# In[41]:



dim = HiddenStates.shape[0]
P = np.zeros(dim)

for i in range(dim):
    P[i] = GetProb(T,E,Obs,HiddenStates[i],Prior)
    
print(len(P))


# In[42]:


Pobs=np.sum(P)
print(Pobs)


# In[43]:


maxP1 = np.max(P)
ii = np.where( P == np.amax(P))
print(HiddenStates[ii],maxP1)


# In[44]:


plt.plot(P,color='k')
plt.axhline(y=maxP1,color='r')
plt.legend(['Probabilidad por secuencia','MaxP = 0.00019'])
plt.grid(axis='both')


# c) Probabilidades de cada estado observable

# In[45]:


NObs = ObsStates.shape[0]

PObs = np.zeros(NObs)

for j in range(NObs):
    
    dim = HiddenStates.shape[0]
    P = np.zeros(dim)
    
    for i in range(dim):
        P[i] = GetProb(T,E,ObsStates[j],HiddenStates[i],Prior)
        
    PObs[j] = np.sum(P)


# In[46]:


len(PObs)


# In[47]:


maxP = np.max(PObs)
ii = np.where( PObs == np.amax(PObs))
print(ObsStates[ii],maxP)


# In[48]:


plt.plot(PObs)
plt.axhline(y=maxP, color='r')
plt.legend(['Probabilidad de cada estado observable','MaxP = 0.136'])
plt.grid(axis='both')


# d. Verificar sumatoria de los estados observables =1

# In[49]:


Ptotal=np.sum(PObs)
Ptotal


# e. ¿Depende el resultado de la probabilidad a-priori?

# Se ve un cambio evidente en la secuencia oculta más probable y su valor de probabilidad, dado que se inicia el cálculo de las probabilidades desde un número diferente, por lo que los resultados se ven afectados. Por otro lado, las probabilidades de todos los estados observables se ven afectadas levemente, pero si hay variaciones notables. En resumen, el valor a priori si afecta los resultados, ya que de dicho valor se parte para calcular las probabilidades de la respectiva secuencia oculta o estado observable.

# In[ ]:




