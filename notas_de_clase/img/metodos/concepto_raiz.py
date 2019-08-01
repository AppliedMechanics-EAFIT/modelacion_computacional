# -*- coding: utf-8 -*-
"""
Ilustración de una raíz de una función

La función usada es

    x**3 + 4*x**2 - 10

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

x = np.linspace(-4, 2, 200)
y = x**3 + 4*x**2 - 10

plt.figure(figsize=(4, 3))
plt.plot(x, y)
plt.plot(1.3652, 0, color="white", marker="o", mec="black")
plt.grid(alpha=0.5)
plt.xlabel("Coordenada $x$")
plt.ylabel(u"Función")
plt.legend([r"$x^3 + 4x^2 - 10$"])
plt.tight_layout()
plt.savefig("raiz.pdf", bbox_inches="tight")
plt.savefig("raiz.svg", bbox_inches="tight", transparent=True)
plt.show()