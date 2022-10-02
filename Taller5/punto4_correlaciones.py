
import numpy as np
import matplotlib.pyplot as plt
#from tqdm import tqdm 

N= np.random.uniform(size=10**4)
coeficientes=[]
np.array(coeficientes)

def calidad_generador (N,x):
    k=30
    total=0
    for l in range (1,k):
        i=1
        for j in range (x-k):
            i=N[j+l]*N[j]
            total+=i
        total=total/x
        coeficientes.append(total)
        
    return coeficientes 

#los primeros k = 30 y N = 10**4
#fluctuar alrededor del valor teorico C(k) = 1/4.
plt.title("Generador Numpy con K=30")          
plt.plot(calidad_generador(N,10**4))
plt.xlim(-2,31)
plt.ylim(0.2,0.3)
plt.grid()    
