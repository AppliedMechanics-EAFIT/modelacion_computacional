# -*- coding: utf-8 -*-
"""
Raíces para la función

    x - tan(x)

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

plt.rcParams["mathtext.fontset"] = "cm"


def mult_roots(fun, a, b):
    """Roots of the function fun in the interval [a, b]"""
    roots = []
    for x0 in np.linspace(-10, 10, 100):
        roots.append(fsolve(fun, x0)[0])
    return list(set(np.round(roots, 1)))


fun = lambda x: x - np.tan(x)
x = np.linspace(-10, 10, 2000)
y = fun(x)
y[np.abs(y) > 20] = np.nan
x_roots = mult_roots(fun, -10, 10)

plt.figure(figsize=(4, 3))
plt.plot(x, y)
plt.plot(x_roots, np.zeros_like(x_roots), marker="o",
         mec="black", mfc="white", linewidth=0)
plt.grid(alpha=0.5)
plt.xlabel("Coordenada $x$")
plt.ylabel(u"Función")
plt.legend([r"$x - \tan(x)$"])
plt.yticks(np.linspace(-10, 10, 5))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.savefig("tan.pdf", bbox_inches="tight")
plt.show()