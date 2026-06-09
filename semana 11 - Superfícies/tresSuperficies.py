import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Gera três superfícies 3D translúcidas das funções sin(r), cos(r) e sin(r+1),
onde r = sqrt(x² + y²), usando diferentes colormaps do Matplotlib, e guarda
a imagem final como ficheiro PNG.
"""


x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)


R = np.sqrt(X**2 + Y**2)


Z1 = np.sin(R)
Z2 = np.cos(R)
Z3 = np.sin(R + 1)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(X, Y, Z1, alpha=0.6, cmap='autumn', edgecolor='none', antialiased=True, shade=True)
ax.plot_surface(X, Y, Z2, alpha=0.6, cmap='winter', edgecolor='none', antialiased=True, shade=True)
ax.plot_surface(X, Y, Z3, alpha=0.6, cmap='cool', edgecolor='none', antialiased=True, shade=True)

ax.set_title('Três Superfícies Translúcidas')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.savefig('superficies_radiais.jpg', dpi=300)
plt.show()
