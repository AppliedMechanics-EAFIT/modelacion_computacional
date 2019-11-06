#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:55:55 2018

@author: nguarinz
"""
from sympy import *
import matplotlib.pyplot as plt
from sympy.plotting import plot3d

x, y = symbols("x y")

#%% Grafico sencillo
plot(sin(x), (x, -pi, pi))
plt.gcf().figsize = 4, 3
plt.savefig("sympy_grafico.pdf", bbox_inches="tight")

#%% Grafico 3D
monkey_saddle = x**3 - 3*x*y**2
p = plot3d(monkey_saddle, (x, -2, 2), (y, -2, 2))
plt.gcf().figsize = 4, 3
plt.savefig("sympy_grafico_3D.pdf", bbox_inches="tight")


#%% Lambdify
fun = diff(sin(x)*cos(x**3) - sin(x)/x, x)
fun_numpy = lambdify(x, fun, "numpy")
pts = np.linspace(0, 5, 1000)
fun_pts = fun_numpy(pts + 1e-6) # Para evitar división por 0
plt.figure(figsize = (4,3))
plt.plot(pts, fun_pts)
plt.savefig("sympy_lambdify.pdf", bbox_inches="tight")