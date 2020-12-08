import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.set(xlim=(1, 5), ylim=(1, 5))

fill_color = "brown"
fill = False if not fill_color else True

tri1 = np.array([[3, 3], [2, 3.5], [2, 2.5]])
p1 = Polygon(tri1, closed=True, fill=fill, facecolor=fill_color)
ax.add_patch(p1)

tri2 = np.array([[3, 3], [2.5, 4], [3.5, 4]])
p2 = Polygon(tri2, closed=True, fill=fill, facecolor=fill_color)
ax.add_patch(p2)

tri3 = np.array([[3, 3], [4, 3.5], [4, 2.5]])
p3 = Polygon(tri3, closed=True, fill=fill, facecolor=fill_color)
ax.add_patch(p3)

tri4 = np.array([[3, 3], [2.5, 2], [3.5, 2]])
p4 = Polygon(tri4, closed=True, fill=fill, facecolor=fill_color)
ax.add_patch(p4)

plt.show()
