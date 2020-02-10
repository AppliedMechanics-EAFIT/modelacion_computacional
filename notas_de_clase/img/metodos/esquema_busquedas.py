# -*- coding: utf-8 -*-
"""
Ilustra el método de búsquedas incrementales de raícez

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


fun = lambda x: -x**3 - 4*x**2 + 5

x = np.linspace(-4, 0, 100)
y = fun(x)

nsample  = 20
x_sample = np.linspace(-4, 0, nsample)
y_sample = fun(x_sample)

roots = [-3.61803399, -1.38196601]


#%% Graficacion
plt.figure(figsize=(4, 3))
ax = plt.gca()
for xs, ys in zip(x_sample, y_sample):
    ax.plot([xs, xs], [0, ys], color="#3f3f3f", linewidth=1)
ax.plot(x, y, linewidth=2)
ax.plot(roots, [0, 0], marker="o",
         mec="black", mfc="black", linewidth=0)
arrowprops = dict(facecolor='black', width=1, headwidth=4,
                  frac=0.1, shrink=0.05)
ax.annotate(r"$x_R$ iroot", xy=(x_sample[7], 0), xytext=(x_sample[7], 2),
            arrowprops=arrowprops)
ax.annotate("iroot=1", xy=(roots[0], 0), xytext=(roots[0] - 0.5, -3),
            arrowprops=arrowprops)
ax.annotate("iroot=2", xy=(roots[1], 0), xytext=(roots[1] + 0.5, -3),
            arrowprops=arrowprops)
plt.xticks([-4, 0], [r"$a$", r"$b$"])
plt.yticks([])
plt.xlabel(r"$x$", horizontalalignment="right", fontsize=12)
plt.ylabel(r"$f(x)$", fontsize=12)
ax.spines['bottom'].set_position(('data',0))
ax.xaxis.set_label_coords(1.05, 0.475)
ax.yaxis.set_label_coords(-0.05, 0.9)
plt.savefig("busquedas_inc.pdf", bbox_inches="tight")
plt.savefig("busquedas_inc.svg", bbox_inches="tight", transparent=True)
plt.show()
