
import numpy as np
import sympy as sym
from scipy.special import legendre

#Punto 1.9.4 Calcular todas las raıces reales de los primeros 20 polinomios de 
#LEGENDRE


def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-9):
    
    error = 1
    it=0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
    
    if it == itmax:
        return False
    else:
        return xn
    
def GetAllRoots(x, f, tolerancia=8):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(f,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

R=np.array([])

x=np.linspace(-1,1,1000)
for i in range(21): 
    f=legendre(i)
    raices = GetAllRoots(x,f)
    print(np.append(R, raices))
    
 




