#punto 3 multipliacacion de dos matrices 
import numpy as np


A=np.array([[1,0,0],[5,1,0],[-2,3,1]])
B=np.array([[4,-2,1],[0,3,7],[0,0,2]])

def multiplicarM (m1,m2):
    rta=np.matmul(m1,m2)
    return rta

print(multiplicarM(A,B))


