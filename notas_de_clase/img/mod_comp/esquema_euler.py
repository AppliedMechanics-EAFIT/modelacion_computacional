# -*- coding: utf-8 -*-
"""
Ilustra el método de Euler

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False



t = [1, 2, 3]
v = [1, 2, 5]
plt.figure(figsize=(4, 2.5))
plt.plot(t, v)
plt.plot(t, v, "ok")
plt.xticks([1, 2, 3], [r"$t$", r"$t + \Delta t$", r"$t + 2\Delta t$"])
plt.yticks([1, 2, 5],
           [r"$v(t)$", r"$v(t + \Delta t)$", r"$v(t + 2\Delta t)$"])
plt.text(1.5, 1.2, r"$v'(t)$")
plt.text(2.5, 3.2, r"$v'(t + \Delta t)$")
plt.savefig("euler.pdf", bbox_inches="tight")
plt.show()
