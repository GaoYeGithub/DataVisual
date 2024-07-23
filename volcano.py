from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('volcano.csv')

df = data.unstack().reset_index()
df.columns = ['X', 'Y', 'Z']

df['X'] = pd.Categorical(df['X'])
df['X'] = df['X'].cat.codes

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.2)

surf = ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.2)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()