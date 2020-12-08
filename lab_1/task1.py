import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

circle1 = plt.Circle((2, 2), 0.6, facecolor='red', edgecolor='black')
circle2 = plt.Circle((2, 2), 0.5, facecolor='yellow', edgecolor='black')
circle3 = plt.Circle((2, 2), 0.4, facecolor='blue', edgecolor='black')
circle4 = plt.Circle((2, 2), 0.3, facecolor='orange', edgecolor='black')
circle5 = plt.Circle((2, 2), 0.2, facecolor='white', edgecolor='black')

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle5)
ax.add_artist(circle4)
ax.set(xlim=(1, 6), ylim=(1, 3))

tri1 = np.array([[4.2, 1.76], [4.8, 1.76], [4.5, 1.95]])
p1 = Polygon(tri1, closed=True, fill=False)
ax.add_patch(p1)

tri2 = np.array([[3.95, 1.7], [5.07, 1.7], [4.5, 2.05]])
p2 = Polygon(tri2, closed=True, fill=False)
ax.add_patch(p2)

tri3 = np.array([[3.67, 1.6], [5.3, 1.6], [4.5, 2.3]])
p3 = Polygon(tri3, closed=True, fill=False)
ax.add_patch(p3)

tri4 = np.array([[3.45, 1.51], [5.5, 1.51], [4.5, 2.42]])
p4 = Polygon(tri4, closed=True, fill=False)
ax.add_patch(p4)

tri5 = np.array([[3.22, 1.43], [5.7, 1.43], [4.5, 2.58]])
p5 = Polygon(tri5, closed=True, fill=False)
ax.add_patch(p5)

plt.show()
