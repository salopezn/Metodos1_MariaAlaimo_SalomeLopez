#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


# Punto común a las tres líneas

# In[3]:


a = lambda x,y: 2*x-y-2
b= lambda x,y: x+2*y-1
c=lambda x,y:x+y-4


# In[32]:


A = np.array([[2,-1],[1,2],[1,1]])
b = np.array([[2],[1],[4]])
m= (A.T)@A
n=(A.T)@b
a=np.linalg.solve(m,n)
#print(A)
print('El punto común a las tres líneas es:')
print(a)


# Gráfica de las líneas y la solución

# In[3]:


x=np.linspace(-2,8,10)
ya=[]
yb=[]
yc=[]
for i in range(len(x)):
    ya=2*x-2
    yb=(1-x)/2
    yc=4-x 


# In[30]:


print(x)
print(ya)
print(yb)
print(yc)


# In[53]:


fig, ax = plt.subplots()
ax.scatter(*a, color='r',label='r+')
plt.plot(x,ya)
plt.plot(x,yb)
plt.plot(x,yc)
plt.ylim(-7,7)


# Búsqueda iterativa

# In[39]:


x=np.arange(-5,5,0.01)
y=np.arange(-5,5,0.01)
X, Y = np.meshgrid(x,y)
Z=np.zeros(np.shape(X))
m, n =np.shape(X)
for i in range(m):
    for j in range(n):
        x_=X[i][j]
        y_=Y[i][j]
        v=np.array([[x_],[y_]])
        d= (A@v)-b
        Z[i][j]=np.linalg.norm(d)
        
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z,cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('(x)p')
ax.view_init(20, 60)


# In[41]:


mini=np.argwhere(Z == np.min(Z))
print(mini)
print(X[543][646])
print(Y[543][643])


# Se obtuvo un resultado muy cercano al de mínimos cuadrados, pero en resumen, ambos puntos obtenidos coinciden.

# In[ ]:




