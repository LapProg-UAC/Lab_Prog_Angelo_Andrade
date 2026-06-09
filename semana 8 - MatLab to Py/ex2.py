import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Gera uma superfície 3D usando NumPy e Matplotlib,
e guarda o gráfico como imagem PNG.
"""

X, Y = np.meshgrid(np.linspace(-3,3,100), np.linspace(-3,3,100))   
Z = np.sin(np.sqrt(X**2 + Y**2))                                   
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')                         
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.tight_layout()
fig.savefig('surface.png')                                         
