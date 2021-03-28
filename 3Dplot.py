import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mpot3d import axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x1 = np.random.rand(10)
y1 = np.random.rand(10)
z1 = np.random.rand(10)

x2 = np.random.rand(10)
y2 = np.random.rand(10)
z2 = np.random.rand(10)

ax.scatter(x1, y1, z1,s=10, color='blue')

plt.show()