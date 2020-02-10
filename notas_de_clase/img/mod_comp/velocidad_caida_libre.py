# -*- coding: utf-8 -*-
"""
Ilustra el método de Newton-Raphson

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


def vel(t, rho, g, Ca, A, m):
    vf = vel_terminal(rho, g, Ca, A, m)
    return vf * np.tanh(g*t/vf)


def vel_terminal(rho, g, Ca, A, m):
    return np.sqrt(2*m*g/(rho * Ca * A))


rho = 1.22 # kg/m**3
g = 9.81 # m/s**2
# Datos para un hombre adulto
Ca = 1.2
A = 0.43 # m**2
m = 80 # kg
vf = vel_terminal(rho, g, Ca, A, m)
t = np.linspace(0, 10, 100)
v = vel(t, rho, g, Ca, A, m)



#%% Graficacion
plt.figure(figsize=(4, 2.5))
plt.plot(t, v, linewidth=2)
plt.hlines(vf, 0, 10, linestyle="dashed")
plt.annotate(r"96% de $v_\infty$", xy=(10, v.max()), xytext=(6, 30),
            arrowprops=dict(arrowstyle="->", facecolor='black'))
plt.xlabel(r"$t$ (s)")
plt.ylabel(r"$v$ (m/s)")
plt.savefig("velocidad_caida_libre.pdf", bbox_inches="tight")
plt.show()
