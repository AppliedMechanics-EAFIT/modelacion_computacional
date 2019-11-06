#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de gráfico de campos vectoriales en matplotlib

"""
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-2, 1, 21)
y = np.linspace(-2, 2, 21)
X, Y = np.meshgrid(x, y)
U = Y
V = -X - X**2

#%% Flechas
plt.figure(figsize=(4, 3))
plt.quiver(X, Y, U, V)
plt.savefig("grafico_flechas.pdf", bbox_inches="tight")


#%% Lineas de corriente
plt.figure(figsize=(4, 3))
plt.streamplot(X, Y, U, V)
plt.savefig("grafico_lineas_corriente.pdf", bbox_inches="tight")