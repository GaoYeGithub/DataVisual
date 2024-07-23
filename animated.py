from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.cos(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')

surf = ax.plot_surface(x, y, z, cmap='cividis', edgecolor='black')

def update(frame):
    ax.view_init(elev=30, azim=frame)
    return surf,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

ax.set_title('Surface plot')

plt.show()
