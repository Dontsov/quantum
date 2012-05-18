# -*- coding: utf-8 -*-
'''from numpy import *
import sys
import scipy, pylab
import scipy.optimize
#from __future__ import division
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
res = []
i = 0
while i < 4:
    E = ((2 * 3)/4) * (2 + 4 + 8) * i
    res.append(E)
    i = i + 1
print res
s = [1, 3, 5, 6]
plt.plot(res, s)
plt.figure()
plt.savefig("example.png")'''

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
hbar = 6.62606957e-34
x = np.arange(0.0, a, 0.1)
y = np.arange(0.0, b, 0.1)
z = np.arange(0.0, c, 0.1)
n = 2
def Psi(n):
    return ((np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * x) / a) 
                                                     * np.sqrt(2 / b) * np.sin((np.pi * n * y) / b) 
                                                     * np.sqrt(2 / c) * np.sin((np.pi * n * z) / c))

print np.sin(np.pi)
'''x = 1
y = 1
while x <= 100:             
    Px = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * x) / a)
    Py = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * y) / a)    
    print Px, Py, Px            
    x = x + 1
    y = y + 1'''
'''     
Px = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * x) / a) 
Py = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * y) / a) 
Pz = (np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * z) / a) 
P = Px * Py * Pz'''

f = open('data.txt', 'w')
f.write(Psi(n))
f.close()

fig = plt.figure()
ax = fig.gca(projection='3d')
x, y = np.meshgrid(x, y)
ax.plot(Px, Py, z)


plt.show()








