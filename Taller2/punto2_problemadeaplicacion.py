# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:03:26 2022

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-4,4,25)
y=np.linspace(-4,4,25)

X,Y=np.meshgrid(x,y)

def funcion_potencial (x:float ,y:float)->float:
    v=2
    r=2
    ecuacion=v*x*(1-(r**2)/(x**2+y**2))
    return ecuacion 

Phi = funcion_potencial(X, Y)
h=0.001
v_x=np.zeros((25, 25))
v_y=np.zeros((25, 25))
for i in range(0,25):
    for j in range (0,25):
        x=X[i,j]
        y=Y[i,j]
        r=np.sqrt(x**2+y**2)
        if r>2:
            v_x[i,j]=(funcion_potencial(x+h,y)-funcion_potencial(x-h,y))/(2*h)
            v_y[i,j]=(funcion_potencial(x,y+h)-funcion_potencial(x,y-h))/(2*h)

        


 
#Dibuje el campo de velocidades usando el metodo:
#ax.quiver(x[i],y[j],Vx[i,j],Vy[i,j])

o=100000
fig = plt.figure(figsize=(6,5))
plt.quiver(X,Y,v_x,v_y,color='b',alpha=0.7)
rad=np.zeros((o,2))
for i in range (o):
    rad[i]=[2*np.cos(2*np.pi*i/o),2*np.sin(2*np.pi*i/o)]
plt.plot(rad[:,0],rad[:,1],color="r")
    