# -*- coding: utf-8 -*-
"""
Ilustra el método de Newton-Raphson

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False



fun = lambda x: 0.3*np.abs(x)*x
grad = lambda x: 0.6*np.abs(x)

x = np.linspace(-2, 4, 100)
y = fun(x)



#%% Graficacion
plt.figure(figsize=(4, 3))
ax = plt.gca()
ax.plot(x, y, linewidth=2)
x0 = 4
x_iter = [x0]
ax.plot([x0, x0], [fun(x0), 0], color="#3f3f3f", linewidth=1.5,
        linestyle="dashed")
ax.plot([x0], [fun(x0)], marker="o", mec="black", mfc="white",
        linewidth=0, zorder=5)
for cont in range(3):
    x1 = x0 - fun(x0)/grad(x0)
    x_iter.append(x1)
    ax.plot([x0, x1], [fun(x0), 0], color="#3f3f3f", linewidth=1.5,
            linestyle="dashed", zorder=4)
    ax.plot([x1, x1], [fun(x1), 0], color="#3f3f3f", linewidth=1.5,
            linestyle="dashed", zorder=4)
    ax.plot([x1], [fun(x1)], marker="o", mec="black",
            mfc="white", linewidth=0, zorder=5)
    x0 = x1
ax.plot([0], [0], marker="o",
         mec="black", mfc="black", linewidth=0)
plt.xticks(x_iter + [0], [r"$x_{}$".format(k) for k in range(4)] + [r"$x^*$"])
plt.yticks([])
plt.xlabel(r"$x$", horizontalalignment="right", fontsize=12)
plt.ylabel(r"$f(x)$", fontsize=12)
ax.spines['bottom'].set_position(('data',0))
ax.xaxis.set_label_coords(1.05, 0.25)
ax.yaxis.set_label_coords(-0.05, 0.9)
plt.savefig("newton_iter.pdf", bbox_inches="tight")
plt.savefig("newton_iter.svg", bbox_inches="tight", transparent=True)
plt.show()
