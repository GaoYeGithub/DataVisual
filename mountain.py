import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

DataFrame = pd.read_csv('mountain.csv')
DataFrame = DataFrame.unstack()
DataFrame = DataFrame.reset_index()

DataFrame.columns = ['X', 'Y', 'Z']
DataFrame['X'] = pd.Categorical(DataFrame['X'])
DataFrame['X'] = DataFrame['X'].cat.codes

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(DataFrame['X'],
                DataFrame['Y'],
                DataFrame['Z'],
                cmap=plt.cm.jet,
                linewidth=0.2)

plt.title("San Mount Bruno")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()