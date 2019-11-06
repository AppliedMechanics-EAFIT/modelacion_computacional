# -*- coding: utf-8 -*-
"""
Compara dos polinomios graficamente

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt

x_pts = [-1, 0, 1, -0.5, 0.5]
y_pts = [-7, -10, -5, -9.125, -8.785]

x = np.linspace(-1, 1, 50)
x1 = np.linspace(-1, 0, 50)
x2 = np.linspace(0, 1, 50)
poli = x**3 + 4*x**2 -10
poli_1 = 2.5*x1**2 - 0.5*x1 - 10
poli_2 = 5.5*x2**2 - 0.5*x2 - 10

plt.plot(x, poli, label="Polinomio original")
plt.plot(x1, poli_1, label="Tramo 1",
         linestyle="dashed")
plt.plot(x2, poli_2, label="Tramo 2",
         linestyle="dashed")
plt.plot(x_pts, y_pts, "ok")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
