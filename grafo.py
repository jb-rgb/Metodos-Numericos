from tkinter import PROJECTING
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(PROJECTING)
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
x, y = np.meshgrid(x, y)
z = x**2 + y**2
ax.plot_surface(x, y, z)
plt.xlabel('x')
plt.ylabel('y')
plt.show()