#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sym


# **Método Simpson 3/8**
# 

# **x0=0,
# x1=h,
# x2=2h,
# x3=3h**

# a. Funciones cardinales (cada polinomio)

# In[38]:


x = sym.Symbol("x",Real=True)
h = sym.Symbol("h",Real=True)


# In[39]:


#Primer polinimio interpolador
d1=(x-h)*(x-2*h)*(x-3*h)
n1=(0-h)*(0-2*h)*(0-3*h)
p1=d1/n1
p1


# In[40]:


#Integral Primer polinimio interpolador
i1=sym.integrate(p1,(x,0,3*h))
i1


# In[19]:


#Segundo polinimio interpolador
d2=(x-0)*(x-2*h)*(x-3*h)
n2=(h-0)*(h-2*h)*(h-3*h)
p2=d2/n2
p2


# In[22]:


#Integral segundo polinimio interpolador
i2=sym.integrate(p2,(x,0,3*h))
i2


# In[31]:


#Tercer polinimio interpolador
d3=(x-0)*(x-h)*(x-3*h)
n3=(2*h-0)*(2*h-h)*(2*h-3*h)
p3=d3/n3
p3


# In[34]:


#Integral tercer polinimio interpolador
i3=sym.integrate(p3,(x,0,3*h))
i3


# In[35]:


#Cuarto polinimio interpolador
d4=(x-0)*(x-h)*(x-2*h)
n4=(3*h-0)*(3*h-h)*(3*h-2*h)
p4=d4/n4
p4


# In[41]:


#Integral cuarto polinimio interpolador
i4=sym.integrate(p4,(x,0,3*h))
i4


# De esta forma, la integral se aproxima como

# In[43]:


y0 = sym.Symbol("y0",Real=True)
y1 = sym.Symbol("y1",Real=True)
y2 = sym.Symbol("y2",Real=True)
y3 = sym.Symbol("y3",Real=True)

i1*(y0)+i2*(y1)+i3*(y2)+i4*(y3)


# Lo que es igual a

# In[44]:


i1*((y0)+3*(y1)+3*(y2)+(y3))


# b. Valores de los puntos intermedios

# In[45]:


b = sym.Symbol("b",Real=True)
a = sym.Symbol("a",Real=True)
x1 = sym.Symbol("x1",Real=True)
x2 = sym.Symbol("x2",Real=True)


# In[56]:


#Primer punto intermedio, x1
h=(b-a)/3
h=(b/3)-(a/3)

x1=a+h
x1=a+b/3-a/3
x1=(b/3)+(2*a)/3
x1


# In[58]:


#Segundo punto intermedio, x2
h=(b/3)-(a/3)

x2=a+2*h
x2=a+(2*b/3)-(2*a/3)
x2=(2*b/3)+(a)/3
x2


# In[ ]:




