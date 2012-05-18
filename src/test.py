from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math 
import scipy
from scipy import *

a = 10.0
b = 10.0
c = 10.0
E = 1.0
t = 1.0
n = 1
hbar = 6.62606957e-34
x = np.arange(0.0, a, 0.1)
y = np.arange(0.0, b, 0.1)
z = np.arange(0.0, c, 0.1)

Px = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * x) / a) 
Py = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * y) / a) 
Pz = np.sin((np.pi * n * z) / a) 


fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y = np.mgrid[0:6*np.pi:0.25, 0:4*np.pi:0.25]
Z = np.sqrt(np.abs(np.cos(X) + np.cos(Y)))

surf = ax.plot_surface(X + 1e5, Y + 1e5, Z, cmap='autumn', cstride=2, rstride=2)
ax.set_xlabel("X-Label")
ax.set_ylabel("Y-Label")
ax.set_zlabel("Z-Label")
ax.set_zlim(0, 2)

plt.show()
