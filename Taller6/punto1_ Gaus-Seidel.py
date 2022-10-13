import numpy as np


M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

def Gaus_seidel(A,b,itmax=1000,error = 1e-10):
    
    M,N = A.shape
    
    x = np.zeros(N)
    
    sumk = np.zeros_like(x)
    
    x = [13,20,-1]
    
    it = 0
    
    residuo = np.linalg.norm( b - np.dot(A,x) )
    
    while ( residuo > error and it < itmax ):
        
        it += 1
        
          
        for i in range(M):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j]*x[j]
            if A[i,i] != 0:
                x[i] = (b[i] - sum_)/A[i,i]
            else:
                print('No invertible con Jacobi')
        
        #print(x)
        residuo = np.linalg.norm( b - np.dot(A,x) )

        
    return ("Resultado: ", x ), (" Cantidad de iteraciones: ", it), ("El residuo es: ", residuo)
print(Gaus_seidel(M,b))