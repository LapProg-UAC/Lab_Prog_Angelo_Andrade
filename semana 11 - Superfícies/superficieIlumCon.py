import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D

"""
Gera uma superfície 3D com transparência combinando sin(r) e um plano base,
onde r = sqrt(x² + y²), aplicando um gradiente de cores e alfa variável,
e guarda o resultado como imagem PNG.
"""



x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)


R = np.sqrt(X**2 + Y**2)


Z_top = np.sin(R)
Z_base = np.zeros_like(X)


norm = Normalize(vmin=R.min(), vmax=R.max())
cores_base = cm.plasma(norm(R))


alpha_map = np.abs(np.cos(R))
cores = cores_base.copy()
cores[..., -1] = alpha_map

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(X, Y, Z_top, alpha=0.6, cmap='plasma', edgecolor='none', antialiased=True, shade=True)
ax.plot_surface(X, Y, Z_base, facecolors=cores, edgecolor='none', antialiased=True, shade=True)

ax.set_title('Superfície com Gradiente e Transparência')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.savefig('superficie_transparente.jpg', dpi=300)
plt.show()
