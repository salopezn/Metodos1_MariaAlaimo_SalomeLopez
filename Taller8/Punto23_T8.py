#!/usr/bin/env python
# coding: utf-8

# Se tienen 9 llaves: 3 rojas, 3 azules y 3 verdes. Si elegimos 4, ¿de cuántas formas se
# pueden distribuir los colores?

# **Combinación con repetición**
# 
# -> No importa el orden de las llaves
# 
# -> Los colores de las llaves se pueden repetir
# 
# -> La intercalación de colores es importante

# In[21]:


import numpy as np


# In[22]:


def com_rep(r,n):
    return (np.math.factorial(r+n-1))/((np.math.factorial(r))*(np.math.factorial(n-1)))


# In[23]:


#se restan los tres casos en que quedan las 4 bolas del mismo color (RRRR), ya que no son posibles
com_rep(4,3)-3


# In[ ]:





# In[ ]:




