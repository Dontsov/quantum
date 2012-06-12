from qutip import *
import numpy as np
b=Bloch()
b.zlabel=['$\left|1\\right>$','$\left|0\\right>$']
th = 45
#b.zlabel()
#vec=[0,1/np.sqrt(2), 0]
#vec=[cos(th),sin(th), sin(th)]
vec = [0,cos(th),sin(-th)]
b.add_vectors(vec)

b.show()