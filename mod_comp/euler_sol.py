# -*- coding: utf-8 -*-
"""
Soluciona una ecuacion diferencial usando el método de Euler

@author: Nicolas Guarin-Zapata
@date: Febrero, 2018
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


#%% Datos de entrada
rho = 1.22 # kg/m**3
g = 9.81 # m/s**2
Ca = 1.2
A = 0.43 # m**2
m = 80.0 # kg
v_inf = np.sqrt(2*m*g/(rho * Ca * A))


plt.figure(figsize=(4, 2.5))
#%% Solucion analitica
t = np.linspace(0, 10, 100)
plt.plot(t, v_inf * np.tanh(g*t/v_inf))

#%% Solucion numerica
t = np.linspace(0, 10, 10)
niter = len(t)
v = np.zeros(niter)
for cont in range(1, niter):
    dt = t[cont] - t[cont - 1]
    v[cont] = v[cont - 1] + dt * g * (1 - v[cont - 1]**2/v_inf**2)

plt.plot(t, v, marker=".")
plt.xlabel("Tiempo (s)")
plt.ylabel("Rapidez (m/s)")
plt.legend([u"Analítico", u"Numérico"])
plt.savefig("euler_caida.pdf", bbox_inches="tight")
plt.show()
