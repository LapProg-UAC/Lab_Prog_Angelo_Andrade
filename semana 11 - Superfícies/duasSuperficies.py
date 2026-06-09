import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Gera duas superfícies 3D translúcidas das funções sin(r) e cos(r), onde
r = sqrt(x² + y²), usando NumPy e Matplotlib, e guarda o resultado como PNG.
"""

x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)


R = np.sqrt(X**2 + Y**2)
Z1 = np.sin(R)
Z2 = np.cos(R)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(X, Y, Z1, alpha=0.5, color='gold', edgecolor='none')
ax.plot_surface(X, Y, Z2, alpha=0.3, color='lightgreen', edgecolor='none')

ax.set_title('Duas Superfícies Translúcidas')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.savefig("duassuperficies.png", dpi=300, bbox_inches='tight')
plt.show()
