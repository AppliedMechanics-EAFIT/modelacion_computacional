#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:38:18 2018

@author: nguarinz
"""
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 51
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)


#%% Superficie
fig = plt.figure(figsize=(4, 3))
# Luego de crear la figura, creamos un contenedor (Axes3D)
ax = Axes3D(fig)
ax.plot_surface(X, Y, f(X,Y), cmap="viridis")
plt.savefig("grafico_superficie.pdf", bbox_inches="tight")


#%% Superficie
fig = plt.figure(figsize=(4, 3))
# Luego de crear la figura, creamos un contenedor (Axes3D)
ax = Axes3D(fig)
ax.contour(X, Y, f(X,Y), 20)
plt.savefig("grafico_contorno3D.pdf", bbox_inches="tight")

#%% Superficie
fig = plt.figure(figsize=(4, 3))
# Luego de crear la figura, creamos un contenedor (Axes3D)
ax = Axes3D(fig)
ax.contourf(X, Y, f(X,Y), 20)
plt.savefig("grafico_contorno_lleno_3D.pdf", bbox_inches="tight")
