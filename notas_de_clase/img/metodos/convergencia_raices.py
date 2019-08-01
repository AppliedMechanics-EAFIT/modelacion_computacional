# -*- coding: utf-8 -*-
"""
Ilustración de convergencia para la función

  x**3 + 4*x**2 - 10

En el método de bisección con intervalo inicial [-10, 10]
y el método de Newton con punto inicial 10.
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

bisect_iter = range(1, 24)
bisect_vals = np.array(
    [2.81835283e-01, 7.25321011e-01, 2.21742864e-01,
     3.00462092e-02, 9.58483275e-02, 3.29010591e-02, 1.42742500e-03,
     1.43093921e-02, 6.44098360e-03, 2.50677930e-03, 5.39677200e-04,
     4.43873900e-04, 4.79016352e-05, 1.97986100e-04, 7.50422486e-05,
     1.35703067e-05, 1.71656642e-05, 1.79767510e-06, 5.88631946e-06,
     2.04432218e-06, 1.23319879e-07, 8.37177610e-07, 3.56928866e-07])

newton_iter = range(1, 8)
newton_vals = np.array(
      [3.64544817e+00, 1.91051800e+00, 8.38074358e-01,
       2.55532915e-01, 3.47978598e-02, 7.83164200e-04, 4.10194615e-07])

plt.figure(figsize=(4, 3))
plt.plot(bisect_iter, bisect_vals*100)
plt.plot(newton_iter, newton_vals*100)
plt.xscale("log")
plt.yscale("log")
plt.xlabel(u"Número de iteraciones")
plt.ylabel("Porcentaje de error")
plt.legend([u"Bisección", "Newton"])
plt.savefig("convergencia.pdf", bbox_inches="tight")
plt.savefig("convergencia.svg", bbox_inches="tight", transparent=True)
plt.show()