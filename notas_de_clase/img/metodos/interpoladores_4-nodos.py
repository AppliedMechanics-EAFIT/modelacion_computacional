# -*- coding: utf-8 -*-
"""
Plot the interpolation functions for a 4-node isoparametric
element.

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Axes3D
plt.rcParams["mathtext.fontset"] = "cm"


def make_plot(x, y, N, cont):
    x_cords = [-1, 1, 1, -1]
    y_cords = [-1, -1, 1, 1]

    ax = plt.gca()
    ax.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], "-ko", zorder=-10)
    ax.plot([x_cords[cont], x_cords[cont]],
            [y_cords[cont], y_cords[cont]], [0, 1], "--k", zorder=-10)
    ax.plot_surface(x, y, N, cstride=1, rstride=1, cmap="viridis",
                alpha=0.6, lw=0.3, zorder=3, edgecolors="black")
    ax.view_init(azim=-60, elev=30)
    ax.set_xlabel(r"$x$", fontsize=12)
    ax.set_ylabel(r"$y$", fontsize=12)
    ax.set_zlabel(r"$N_%i(x, y)$"%(cont + 1), fontsize=12)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([0.0, 0.5, 1.0])


x, y = np.mgrid[-1:1:11j, -1:1:11j]
N1 = 0.25*(1 - x)*(1 - y)
N2 = 0.25*(1 + x)*(1 - y)
N3 = 0.25*(1 + x)*(1 + y)
N4 = 0.25*(1 - x)*(1 + y)

plt.close("all")
cont = 0
fig = plt.figure(figsize=(5, 5))    
for cont, N in enumerate([N1, N2, N3, N4]):
    ax = fig.add_subplot(2, 2, cont + 1, projection='3d')
    make_plot(x, y, N, cont)

plt.savefig("interp_4-nodos.pdf", transparent=True)
plt.show()