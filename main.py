import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the CSV file
data = pd.read_csv('model.csv', header=None, names=['X', 'Y', 'Z'])

# Convert 'X', 'Y', and 'Z' to numeric if necessary
for col in ['X', 'Y', 'Z']:
    data[col] = pd.to_numeric(data[col])

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data
surf = ax.plot_trisurf(data['X'], data['Y'], data['Z'], cmap=plt.cm.jet, linewidth=0.2)
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

plt.show()
