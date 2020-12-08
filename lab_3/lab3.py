from random import choice

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vertices of a pyramid
v = np.array([[-1, -1, -1], [1, 0, -1],  [-1, 1, -1], [-0.74, 0.21, 1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[3]], [v[0],v[2],v[3]], [v[2],v[1],v[3]], [v[0],v[1],v[2]]]

# plot sides
global sides_color
sides_color = "cyan"
ax.add_collection3d(Poly3DCollection(verts, facecolors="white", linewidths=1, edgecolors='r',alpha=1))


def update(i):
    global sides_color
    available_colors = ["red", "cyan", "blue", "green", "black"]
    if i == 0:
        sides_color = choice(available_colors)
    plt.cla()
    # vertices of a pyramid
    v = np.array([[-1, -1, -1], [1, 0, -1], [-1, 1, -1], [-0.74, 0.21, 1]])
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    # generate list of sides' polygons of our pyramid
    verts = [[v[0], v[1], v[3]], [v[0], v[2], v[3]], [v[2], v[1], v[3]], [v[0], v[1], v[2]]]
    ax.add_collection3d(Poly3DCollection(verts, facecolors=sides_color, linewidths=0.09*i, edgecolors='r', alpha=.06*i))
    plt.draw()

animation = FuncAnimation(fig, update, frames=np.arange(0, 10, 0.1), interval=100)

plt.show()
