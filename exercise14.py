# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:12:04 2018

@author: Sila
"""

# Python version
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#Vores cost funktion
def cost(a,b):
### Evaluate half MSE (Mean square error)
   #
   m = len(Ydots)
   # Vores cost funktion
   error = a + b*Xdots - Ydots
   J = np.sum(error ** 2)/(2*m)
   return J

#Beskrevet i 1.3
Xdots = 2 * np.random.rand(100, 1)
Ydots = -5 + 7 * Xdots + np.random.randn(100, 1)

# For at vi kan vise det i 3d med x,y,z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Beskrevet i 13
ainterval = np.arange(-10,10, 0.05)
binterval = np.arange(-10,10, 0.05)

# Her angiver vi så de forskellige x, y, z værdier
X, Y = np.meshgrid(ainterval, binterval)
zs = np.array([cost(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
ax.set_xlabel('Thete0')
ax.set_ylabel('Theta1')
ax.set_zlabel('Cost')
plt.show()

