from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
import math 

x = [i for i in range(0, 200, 100)] 
y = [i for i in range(0, 200, 100)] 

X, Y = np.meshgrid(x, y) 
Z = [] 
for i in x: 
    t = [] 
    for j in y: 
        t.append(math.sin(math.sqrt(i*2+j*2))) 
    Z.append(t) 

fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour3D(X, Y, Z, 50, cmap=cm.cool) 
ax.set_xlabel('a') 
ax.set_ylabel('b') 
ax.set_zlabel('c') 
ax.set_title('3D contour Plot for sine') 
plt.show() 