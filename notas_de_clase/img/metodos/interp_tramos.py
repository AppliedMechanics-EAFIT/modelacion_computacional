# -*- coding: utf-8 -*-
"""
Interpolaciones para explicar el fenomeno de Runge

"""
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["mathtext.fontset"] = "cm"



def graficar_bases(x_inter, y_inter, colors):
    npts = len(x_inter)
    for cont in range(npts - 1):
        plt.plot([x_inter[cont], x_inter[cont + 1]], [0,1],
                 colors[cont])
        plt.plot([x_inter[cont], x_inter[cont + 1]], [1,0],
                 colors[cont], linestyle="dashed")


def graficar_derivada(x_inter, y_inter, color, linestyle="dashed"):
    npts = len(x_inter)
    for cont in range(npts - 1):
        deriv = ((y_inter[cont + 1] - y_inter[cont])/
                 (x_inter[cont + 1] - x_inter[cont]))
        plt.plot([x_inter[cont], x_inter[cont + 1]], [deriv, deriv],
                 color, linestyle=linestyle)



fun = lambda x: x**3 + 4*x**2 - 10
grad = lambda x: 3*x**2 + 8*x
x = np.linspace(-1, 1, 201)
y = fun(x)
x_inter = np.linspace(-1, 1, 5)
y_inter = fun(x_inter)
gris = "#969696"
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.close("all")

#%% Funciones base
plt.figure(figsize=(4, 2.5))
graficar_bases(x_inter, y_inter, colors)
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$L(x)$", fontsize=14)
plt.savefig("interp_local_bases.pdf", bbox_inches="tight", transparent=True)

#%% Funcion y derivada
plt.figure(figsize=(5, 2.5))
plt.subplot(121)
plt.plot(x, y)
plt.plot(x_inter, y_inter, linestyle="dashed")
plt.plot(x_inter, y_inter, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$f(x)$", fontsize=14)

ax = plt.subplot(122)
plt.plot(x, grad(x))
graficar_derivada(x_inter, y_inter, color=colors[1])
plt.plot(x_inter, grad(x_inter), "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel(r"$\frac{\mathrm{d}f(x)}{\mathrm{d}x}$", fontsize=14)
plt.tight_layout()
plt.savefig("interp_local_fun.pdf", bbox_inches="tight", transparent=True)

