import trimesh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

"""
Carrega um modelo 3D de uma cabeça humana, normaliza a sua orientação e escala,
gera três camadas (osso, músculo e pele) com diferentes transparências e cria
uma animação de rotação de 180 graus. A animação é renderizada frame a frame
com Matplotlib e guardada como GIF.
"""


mesh = trimesh.load("Female_Head.obj", force='mesh')


R = trimesh.transformations.rotation_matrix(np.radians(90),
                                            [1, 0, 0])
mesh.apply_transform(R)


mesh.vertices -= mesh.center_mass
mesh.vertices /= mesh.scale

base = mesh.vertices
faces = mesh.faces


bone = base * 0.95
muscle = base * 0.98
skin = base


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

def draw(v, color, alpha, z):
    ax.plot_trisurf(
        v[:,0], v[:,1], v[:,2],
        triangles=faces,
        color=color,
        linewidth=0,
        shade=True,
        antialiased=True,
        alpha=alpha,
        zorder=z)


def update(frame):
    print(f"A renderizar frame {frame+1}/20")
    ax.clear()

    ax.set_xlim(-0.3, 0.3)
    ax.set_ylim(-0.3, 0.3)
    ax.set_zlim(-0.3, 0.3)

    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    ax.set_proj_type('persp')
    ax.computed_zorder = False

    draw(bone,   (0.9, 0.9, 0.9), 1.0, 1)   
    draw(muscle, (0.8, 0.2, 0.2), 0.8, 2)   
    draw(skin,   (0.6, 0.4, 0.2), 0.9, 3)


    ax.view_init(elev=10, azim=-90 + frame * (-9))

    ax.set_axis_off()
    ax.set_box_aspect([1,1,1])


start_time = time.time()

ani = FuncAnimation(fig, update, frames=20, interval=30)
ani.save("animacao.gif", writer="pillow", fps=15)

end_time = time.time()

print(f"Tempo de renderização: {end_time - start_time:.2f} segundos")
