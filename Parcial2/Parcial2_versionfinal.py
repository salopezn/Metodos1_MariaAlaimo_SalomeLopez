#!/usr/bin/env python
# coding: utf-8

# # Parcial 2 Métodos computacionales 1
# 

# **Salomé López y Maria Alaimo**

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


# -**Punto a**-

# In[2]:


#Definir vector P con sympy (paramétro de la funcion)
a00=sym.Symbol('a00',Real=True)
a10=sym.Symbol('a10',Real=True)
a01=sym.Symbol('a01',Real=True)
a11=sym.Symbol('a11',Real=True)
P=np.array([a00,a01,a10,a11])


# In[3]:


#Función que define la interpolación con símbolos
def funcion_simbolica(P):
    x=sym.Symbol('x',Real=True)
    y=sym.Symbol('y',Real=True)
    
    lista=[]
    for i in range(2):
        for j in range(2):
            f=(x**i)*(y**j)
            lista.append(f)
            
    arreglo=np.array(lista)
    
    completado=np.dot(arreglo,P)
    return completado


# In[4]:


print(funcion_simbolica(P))


# -**Punto b**-

# In[5]:


#Defina el vector de posición de los vértices
position = np.zeros((4,2)) 
position[0]=[1,1]
position[1]=[-1,1]
position[2]=[-1,-1]
position[3]=[1,-1]
print(position)


# -**Punto c**-

# In[6]:


#evaluar la funcion en los vértices ya teniendo los valores de ij
def funcion_aevaluar(i,j,x,y):
    funcion=(x**i)*(y**j)
    return funcion


# In[7]:


def funcion_evaluada(x,y,h):
    lista=[]
    for i in range(2):
        for j in range(2):
            f=funcion_aevaluar(i,j,x,y)
            lista.append(f)
    arreglo=np.array(lista)
    
    completado=np.dot(arreglo,h)
    return completado


# In[8]:


#calcula la matriz de coeficientes a partir de cuatro vértices
def coef_matriz(position):
    matriz=np.zeros((4,4))
    
    for x in range(np.shape(position)[0]):
        vector=position[x]
        listaa=[]
        for i in range(2):
            for j in range(2):
                f=funcion_aevaluar(i,j,*vector)
                listaa.append(f)
            arreglo=np.array(listaa)
            
        matriz[x]=arreglo
    return matriz
#print(coef_matriz(position))       
      


# In[9]:


#Definir matriz de coeficientes de la interpolación y hallar valores aij
M=coef_matriz(position)
b=[1,2,0.5,0.3]
a00,a01,a10,a11=np.linalg.solve(M,b)
h=np.array([a00,a01,a10,a11])
print(h)


# -**Punto d**-

# In[10]:


#Verifique que la temperatura en los vértices cumpla con las condiciones de frontera
print(funcion_evaluada(1,1,h))
print(funcion_evaluada(-1,1,h))
print(funcion_evaluada(-1,-1,h))
print(funcion_evaluada(1,-1,h))


# -**Punto e**-

# In[11]:


#Grafique el mapa de temperatura en la regi´on donde est´a el espejo
x=np.arange(-1,1,0.03)
y=np.arange(-1,1,0.03)
X, Y = np.meshgrid(x,y)


Z=X+Y
for i in range(np.shape(X)[0]):
    for j in range(np.shape(X)[1]):
        Z[i][j]=funcion_evaluada(X[i,j],Y[i,j],h)
        

fig=plt.figure(figsize=(10,10))
ax1= fig.add_subplot(1,2,2,projection='3d')
ax2=fig.add_subplot(1,2,1)

ax1.plot_surface(X,Y,Z,cmap='coolwarm')
ax1.scatter(1,1,1)
ax1.scatter(-1,1,2)
ax1.scatter(1,-1,0.3)
ax1.scatter(-1,-1,0.5)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('T(X,Y)')

ax2.pcolor(x,y,Z,cmap='coolwarm')
ax2.scatter(1,1)
ax2.scatter(-1,1)
ax2.scatter(1,-1)
ax2.scatter(-1,-1)
plt.show()


# -**Punto f**-

# In[12]:


#Estime la temperatura en el punto donde se da˜no el sensor
print(funcion_evaluada(0,0.5,h))


# -**Punto g**-

# In[13]:


#rotacion de los cuatro vertices dentro de la funcion
def rotar_vertices(t):
    m=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    new=position.copy()
    for i in range(np.shape(new)[0]):
        new[i]=np.dot(m,position[i].T)
    return new

#PRUEBA EVALUANDO t EN PI
#print(rotar_vertices(3.14))


# In[14]:


#rotacion de cualquier vector x,y
def rotar_vector(t,x,y):
    M=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    v=np.array([x,y])
    H=np.dot(M,v.T)
    return H

#PRUEBA EVALUANDO t EN PI
#print(rotar_vector(3.14,1,1))
#print(rotar_vector(3.14,-1,1))
#print(rotar_vector(3.14,-1,-1))
#print(rotar_vector(3.14,1,-1))


# -**Punto h**-

# In[16]:


#funcion para obtener temperatura en un punto, para algun ángulo t
def in_tem(x,y,t):
    new_position=rotar_vertices(t)
    nueva_matriz=coef_matriz(new_position)
    b=[1,2,0.5,0.3]
    a00,a01,a10,a11=np.linalg.solve(nueva_matriz,b)
    nueva_h=np.array([a00,a01,a10,a11])
    temp=(funcion_evaluada(x,y,nueva_h))
    return temp

#print(in_tem(0,0.5,3.14))


# -**Punto i**-

# In[17]:


#para qué ángulo entre 0-2pi se minimiza la temperatura en (0,0.5)?
theta=np.linspace(0,2*np.pi,200)
resultados=np.zeros(len(theta))
for i in range(len(theta)):
    resultados[i]=in_tem(0,0.5,theta[i])

minimo=np.min(resultados)
posicion_min=np.where(resultados==minimo)

angulo=theta[posicion_min]
#print(angulo)
print('Usando un ángulo de  '+str(angulo[0])+' se encontró la temperatura mínima ' +str(minimo)+' del espejo en el punto P ')


# In[ ]:




