# -*- coding: utf-8 -*-
"""Punto5_lissajous.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QUHOoerVavNVJ91BvcnrefvrtSRlUXWP
"""

import matplotlib.pyplot as plt
import numpy as np

def lissajous(nx,ny,delta):
  theta=np.linspace(0,2*np.pi,num=20000)
  x=np.sin(nx*theta)
  y=np.sin(ny*theta+delta)
  return x,y  
     
plt.figure()
deltas=[0,np.pi/4,np.pi/2]

k=0
while k<3:
  for ny in range(1,6):
    for nx in range(1,ny+1):
      angulo=deltas[k]
      x,y=lissajous(nx,ny,angulo)
      plt.subplot(6,6,6*nx+ny)
      plt.plot(x,y)
      plt.axis("off")
    plt.axis("off")
  plt.figure()
  k+=1