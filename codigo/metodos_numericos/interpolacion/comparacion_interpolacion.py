# -*- coding: utf-8 -*-
"""
Compara dos polinomios graficamente

@author: Nicolas Guarin-Zapata
"""
import numpy as np
import matplotlib.pyplot as plt

x_pts = [-1, 0, 1]
y_pts = [-7, -10, -5]

x = np.linspace(-1, 1, 50)
poli_3 = x**3 + 4*x**2 -10
poli_2 = 4*x**2 + x - 10

plt.plot(x, poli_3, label="Polinomio original")
plt.plot(x, poli_2, label="Polinomio interpolante",
         linestyle="dashed")
plt.plot(x_pts, y_pts, "ok")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
