# -*- coding: utf-8 -*-
"""
Graficos relacionados con la seccion de interpolacion.

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["mathtext.fontset"] = "cm"



fun = lambda x: x**3 + 4*x**2 - 10
x = np.linspace(-1, 1, 5)
y = fun(x)
x_inter = np.linspace(-1, 1, 101)
y_inter = fun(x_inter)

plt.close("all")

#%% Puntos a interpolar
plt.figure(figsize=(4, 2.5))
plt.plot(x, y, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y = f(x)$", fontsize=14)
plt.savefig("interp_puntos.pdf", bbox_inches="tight", transparent=True)

#%% Interpolacion global
plt.figure(figsize=(4, 2.5))
plt.plot(x_inter, y_inter, linestyle="dashed")
plt.plot(x, y, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y = f(x)$", fontsize=14)
plt.savefig("interp_continua.pdf", bbox_inches="tight", transparent=True)

#%% Interpolacion a tramos
plt.figure(figsize=(4, 2.5))
plt.plot(x, y, linestyle="dashed")
plt.plot(x, y, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y = f(x)$", fontsize=14)
plt.savefig("interp_tramos.pdf", bbox_inches="tight", transparent=True)

#%% Interpoladores base
plt.figure(figsize=(4, 3))
ax = plt.subplot(111)
plt.plot(x_inter, -0.5*(1 - x_inter)*x_inter, label="$L_1(x)$")
plt.plot(x_inter, 0.5*(1 + x_inter)*x_inter, label="$L_2(x)$")
plt.plot(x_inter, 1 - x_inter**2, label="$L_3(x)$")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height*0.8])
plt.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.2))
plt.savefig("interp_base.pdf", bbox_inches="tight", transparent=True)

#%% Interpoladores comparacion
plt.figure(figsize=(4, 3))
ax = plt.subplot(111)
fun2 = lambda x: 4*x**2 + x -10
plt.plot(x_inter, y_inter, label="$f(x)$")
plt.plot(x_inter, fun2(x_inter), linestyle="dashed", label="$p(x)$")
plt.plot([-1, 0, 1], fun(np.array([-1, 0, 1])), "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height*0.8])
plt.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.2))
plt.savefig("interp_comparacion.pdf", bbox_inches="tight", transparent=True)

#%% Interpoladores y derivada
plt.figure(figsize=(4, 3))
ax = plt.subplot(111)
deriv1 = lambda x: 3*x**2 + 8*x
deriv2 = lambda x: 8*x + 1
plt.plot(x_inter, deriv1(x_inter), label=r"$\frac{\mathrm{d}f(x)}{\mathrm{d}x}$")
plt.plot(x_inter, deriv2(x_inter), linestyle="dashed",
         label=r"$\frac{\mathrm{d}p(x)}{\mathrm{d}x}$")
plt.plot([-1, 0, 1], deriv1(np.array([-1, 0, 1])), "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height*0.8])
plt.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.2))
plt.savefig("interp_deriv.pdf", bbox_inches="tight", transparent=True)


#plt.show()