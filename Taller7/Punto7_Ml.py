#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install wget')
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.stats import chi2
import os.path as path
import wget


# In[2]:


file ="Sigmoid.csv"
url = "https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv"
if not path.exists(file):
    Path_ = wget.download(url,file)
    print('File loaded')
else:
    Path_ = file


# In[3]:


data = np.loadtxt(Path_,delimiter=",",skiprows=1)
x = data[:,0]
y = data[:,1]
N = len(x)
sigma = np.array([ 2. for i in range(N) ])
sigma = np.random.uniform(1,5,size=N)
sigma
plt.scatter(x,y)


# In[4]:


# a) Defina el modelo de ajuste:

def GetFit(x,y,n):
    DataSize = x.shape[0] 
    b = y 
    A = np.ones((DataSize,n+1))
    for i in range(1,n+1):
        A[:,i] = x**i 
    AT = np.dot(A.T,A)
    bT = A.T @ b
    xsol = np.linalg.solve(AT,bT)
    return xsol
param=GetFit(x,y,2)
param


# In[5]:



def modelo(x, p:np.array):
    f=(p[1])+(sym.exp(-p[2]*x))
    funcion=(p[0])/f
    return funcion 


# In[6]:


def save(x, p):
    value=[]
    vaores=np.append([])
    valores=np.zeros(len(x))
    for i in range (len(x)):
        value=modelo(x[i],p)
        valores.append(value)
    return valores


# In[7]:


#y = data[:,1]
X = sym.Symbol('x',real=True)
modelo(X,param)


# In[8]:


# b) Defina la metrica (funcion de costo) a minimizar como la sumatoria:

def metrica (param):
    x = data[:,0]
    y = data[:,1]
    costo=0
    for i in range(len(y)):
        M=modelo(x[i],param)
        costo+=(y[i]-M)**2 
    return  costo


# In[9]:


import scipy.optimize as spo
Metrica= lambda *p:metrica(*p)
x0=np.array([1.,1.,1.])
result = spo.minimize( Metrica, x0, options={"disp":True}, method="Nelder-Mead" )
print(result)


# In[10]:


minimo=result.nfev
minimo


# In[15]:


#grafica con la funcion metrica 
u = np.linspace(np.min(x),np.max(x),100)
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)
a, b = np.polyfit(x, y, 1)
ax.scatter(x,y)
#pa=np.array([4.40086606, 0.97515686, 2.78201155])
#modelo(u,pa)
#plt.plot(u,save(u,pa))
plt.plot(x, a*x+b)


# In[ ]:




