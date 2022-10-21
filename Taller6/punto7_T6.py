#!/usr/bin/env python
# coding: utf-8

# In[166]:


import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
from tqdm import tqdm


# In[167]:


# Definir s3 como único elemento del vector
G=(lambda x,y,z,w: (x**2)+(y**2)+(z**2)+(w**2)-1)


# In[185]:


def GetVectorF(G,r):
    
    v = G(r[0],r[1],r[2],r[3])
        
    return np.array([v])


# In[186]:


#Jacobiano modificado con listas -> poco óptimo
""""
def GetJacobian(G,r,h=1e-6):
    j=[]
    #J = np.zeros((1,4))
    j.append([(  G(r[0]+h,r[1],r[2],r[3]) - G(r[0]-h,r[1],r[2],r[3]) )/(2*h)])
    j.append([ (  G(r[0],r[1]+h,r[2],r[3]) - G(r[0],r[1]-h,r[2],r[3]) )/(2*h)])
    j.append([ (  G(r[0],r[1],r[2]+h,r[3]) - G(r[0],r[1],r[2]-h,r[3]) )/(2*h)])
    j.append([(  G(r[0],r[1],r[2],r[3]+h) - G(r[0],r[1],r[2],r[3]-h) )/(2*h)])
    J=np.array(j)
    return J
print(GetJacobian(G,[0,0,0,1]))"""""


# In[232]:


#Jacobiano modificado con arrays
def GetJacobian(G,r,h=1e-10): 
    J = np.zeros((1,4))
    J[0,0] = (G(r[0]+h , r[1] , r[2] , r[3]) - G(r[0]-h , r[1], r[2] , r[3]))/(2*h)
    J[0,1] = (G(r[0] , r[1]+h , r[2] , r[3]) - G(r[0] , r[1]-h, r[2] , r[3]))/(2*h)
    J[0,2] = (G(r[0] , r[1] , r[2]+h , r[3]) - G(r[0] , r[1], r[2]-h , r[3]))/(2*h)
    J[0,3] = (G(r[0] , r[1] , r[2] , r[3]+h) - G(r[0] , r[1], r[2] , r[3]-h))/(2*h)
    return np.transpose(J)


# In[233]:


def GetMetric(G,r):
    v = GetVectorF(G,r)
    return np.linalg.norm(v)


# In[234]:


GetMetric(G,[1,1,1,1])


# In[235]:


#Punto aleatorio de 4 componentes
N=1
x=np.random.uniform(-1,1)
y=np.random.uniform(-1,1)
z=np.random.uniform(-1,1)
w=np.random.uniform(-1,1)
vector=np.array([x,y,z,w])
vector


# In[236]:


def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    
    d = 1
    it = 0
    Vector_F = np.array([])
    
    R_vector = np.array(r)
    
    while d > error and it < epochs:
        
        CurrentF = GetMetric(G,r)
        J = GetJacobian(G,r)
        GVector = GetVectorF(G,r)
        
        #Machine Learning
        r -= lr*np.dot(J,GVector) 
        R_vector = np.vstack((R_vector,r))
        NewF = GetMetric(G,r)
        Vector_F = np.append(Vector_F,NewF)
        d = np.abs( CurrentF - NewF )/NewF
        it += 1
        
    #if d < error:
     #   print(' Entrenamiento completo ', d, 'iteraciones', it) 
    if it == epochs:
        print(' Entrenamiento no completado ')
        
    return r


# In[237]:


#Prueba de que el vector aleatorio se ubica en algún punto de S3
xsol= GetSolve(G,vector,lr=1e-4)
print(xsol)


# In[207]:


#Repetir para 1000 puntos
n=10**3
X=np.random.uniform(-1,1,n)
Y=np.random.uniform(-1,1,n)
Z=np.random.uniform(-1,1,n)
W=np.random.uniform(-1,1,n)

resultados=np.zeros((1000,4))
for i in tqdm(range(n)):
    xsol= GetSolve(G,[X[i],Y[i],Z[i],W[i]])
    resultados[i][0]= xsol[0]
    resultados[i][1]=xsol[1]
    resultados[i][2]=xsol[2]
    resultados[i][3]=xsol[3]
    


# In[215]:


#resultados[0][3]

print(len(resultados))


# In[219]:


#verificar que los puntos pertenezcan a la esfera

numero=0
for i in range(len(resultados)):
    if G(resultados[i][0],resultados[i][1],resultados[i][2],resultados[i][3])<1:
        numero+=1
if numero==len(resultados):
    print('Todos los puntos están dentro de la esfera')
else:
    print('El algoritmo está fallando')


# In[231]:


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1,projection='3d')

ax.set_xlim3d(-1,1)
ax.set_ylim3d(-1,1)
ax.set_zlim3d(-1,1)
ax.view_init(20,100)
ax.scatter(resultados[:,0],resultados[:,1],resultados[:,2],color='r')


# In[ ]:




