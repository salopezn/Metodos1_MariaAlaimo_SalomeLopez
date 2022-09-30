

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
N=10000
F=[]
for i in range(N): 
    a=np.random.uniform(0,1)
    b=np.random.uniform(0,1)
    c=np.random.uniform(0,1)
    d=np.random.uniform(0,1)
    e=np.random.uniform(0,1)
    f=np.random.uniform(0,1)
    g=np.random.uniform(0,1)
    h=np.random.uniform(0,1)
    funcion=(2**(-7))*(a+b+c+d+e+f+g+h)**2
    F.append(funcion)
print(np.mean(F))

    
    