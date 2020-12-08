import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y1 = 5 * 0.01 * np.sin(x)
y2 = (5 + 3) * 0.01 * np.sin(x)
y3 = 5 * 0.01 * np.cos(x)


fig, ax = plt.subplots(
    2,
    2,
    constrained_layout=True,
    gridspec_kw={
        'width_ratios': [1, 1],
        'height_ratios': [1, 1]
    },
    figsize=(6, 6)
)
plt.subplots_adjust(hspace=0.5)
ax[0][0].plot(y1, color='red', lw=1)
ax[0][1].plot(y2, color='green', lw=1)
ax[1][0].plot(y3, color='orange', lw=1)
ax[1][1].plot(y1, color='red', lw=1, scalex=True, scaley=True)
ax[1][1].plot(y2, color='green', lw=1, scalex=True, scaley=True)
ax[1][1].plot(y3, color='orange', lw=1, scalex=True, scaley=True)

plt.show()
