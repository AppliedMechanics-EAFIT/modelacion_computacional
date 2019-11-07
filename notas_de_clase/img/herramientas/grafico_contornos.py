#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de gráfico de contornos en matplotlib

"""
import numpy as np
from matplotlib import pyplot as plt


def f(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)


x = np.linspace(1, 5, 5)
y = np.linspace(1, 5, 5)
X, Y = np.meshgrid(x, y)

n = 256
# Creamos los valores de x e y en donde queremos evaluar la función
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# Meshgrid los combina
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(3, 3))
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap="summer")
plt.contour(X, Y, f(X, Y), 8, colors='black')
plt.savefig("grafico_contornos.pdf", bbox_inches="tight")