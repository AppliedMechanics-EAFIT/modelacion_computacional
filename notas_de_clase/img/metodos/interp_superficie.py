# -*- coding: utf-8 -*-
"""
Superficie definida sobre [-1, 1]**2

@author: Nicolas Guarin-Zapata
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Axes3D
plt.rcParams["mathtext.fontset"] = "cm"



x, y = np.mgrid[-1:1:15j, -1:1:15j]
f = x**3 - 3*x*y**2
fig = plt.figure(figsize=(3, 2.5))    
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, f, cstride=1, rstride=1, cmap="viridis",
            alpha=0.6, lw=0.3, zorder=3, edgecolors="black")
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$y$", fontsize=12)
ax.set_zlabel(r"$f(x, y)$", fontsize=12)
ax.view_init(azim=60, elev=45)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-2, 2)
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])
ax.set_zticks(range(-2, 3, 2))

plt.savefig("interp_superficie.pdf", transparent=True)
plt.show()