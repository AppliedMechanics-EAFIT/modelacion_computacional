# -*- coding: utf-8 -*-
"""
Ilustra el método de bisección

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


fun = lambda x: x**3 + 4*x**2 - 5

x = np.linspace(-3, -0.5, 100)
y = fun(x)
roots = [-1.38196601]


#%% Graficacion
plt.figure(figsize=(4, 3))
ax = plt.gca()
ax.text(-1.0, 3.5, r"$x_3 = \frac{1}{2}(x_1 + x_2)$")
ax.plot(x, y, linewidth=2)
ax.plot(roots, [0], marker="o",
         mec="black", mfc="black", linewidth=0)
plt.xticks([-3, -1.75, -0.5], [r"$x_1$", r"$x_3$", r"$x_2$"])

plt.yticks([])
plt.xlabel(r"$x$", horizontalalignment="right", fontsize=12)
plt.ylabel(r"$f(x)$", fontsize=12)
ax.spines['bottom'].set_position(('data',0))
ax.xaxis.set_label_coords(1.05, 0.475)
ax.yaxis.set_label_coords(-0.05, 0.9)
plt.savefig("biseccion.pdf", bbox_inches="tight")
plt.savefig("biseccion.svg", bbox_inches="tight", transparent=True)
plt.show()
