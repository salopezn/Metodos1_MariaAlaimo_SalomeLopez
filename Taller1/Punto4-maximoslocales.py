#punto 4, taller 1
#Maria Alaimo y Salome Lopez 
#un algoritmo para encontrar todos los maximos locales en una serie de datos 


import numpy as np
import matplotlib.pyplot as plt

def maximos_locales(fname: str)->list:
    datos=np.loadtxt(fname)
    x_maximo=[]
    y_maximo=[]
    s=np.size(datos)//2
    hasta=s-1
    for i in range (1,hasta,1):
        if datos[i-1,1]<datos[i,1] and datos[i+1,1]<datos[i,1]:
           x_maximo.append(datos[i,0])
           y_maximo.append(datos[i,1])

    grafica=(plt.plot(datos[:,0],datos[:,1]))
    grafica2=plt.scatter(x_maximo, y_maximo, color="r")
    return (grafica, grafica2)



print (maximos_locales("EstrellaEspectro.txt"))



