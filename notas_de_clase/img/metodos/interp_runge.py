# -*- coding: utf-8 -*-
"""
Interpolaciones para explicar el fenomeno de Runge

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import sympy as sym

plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["mathtext.fontset"] = "cm"


def base_lagrange(x_datos, var, cont):
    """Crea un polinomio base de Lagrange para los datos x"""
    prod = sym.prod((var - x_datos[i])/(x_datos[cont] - x_datos[i])
                    for i in range(len(x_datos)) if i != cont)

    return sym.lambdify(var, sym.simplify(prod), "numpy")


runge = lambda x: 1/(1 + 25*x**2)
x = np.linspace(-1, 1, 201)
y = runge(x)
x_inter = np.linspace(-1, 1, 11)
y_inter = runge(x_inter)
x_cheb = -np.cos(np.linspace(0, np.pi, 11))
y_cheb = runge(x_cheb)
gris = "#969696"

plt.close("all")

#%% Funcion de Runge
plt.figure(figsize=(4, 3))
plt.plot(x, y)
plt.plot(x_inter, y_inter, "ok")
plt.xlabel("$y$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.savefig("runge_fun.pdf", bbox_inches="tight", transparent=True)


#%% Interpolacion equidistante
plt.figure(figsize=(5, 2.5))
plt.subplot(122)
plt.title("Funciones base")
for cont_base in range(11):
    if cont_base == 5:
        color = None
        zorder = 4
        linewidth = 2
    else:
        color = gris
        zorder = 3
        linewidth = 1
    base = base_lagrange(x_inter, sym.symbols("x"), cont_base)
    y_base = base(x)
    plt.plot(x, y_base, color=color, zorder=zorder, linewidth=linewidth)
    plt.xlabel("$x$", fontsize=14)
    plt.ylabel("$y$", fontsize=14)

plt.subplot(121)
plt.title("Interpolación")
plt.plot(x, y)
inter = lagrange(x_inter, y_inter)
plt.plot(x, inter(x), linestyle="dashed")
plt.plot(x_inter, y_inter, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.tight_layout()
plt.savefig("runge_equi.pdf", bbox_inches="tight", transparent=True)

#%% Interpolacion con nodes de Chebyshev
plt.figure(figsize=(5, 2.5))
plt.subplot(122)
plt.title("Funciones base")
for cont_base in range(11):
    if cont_base == 5:
        color = None
        zorder = 4
        linewidth = 2
    else:
        color = gris
        zorder = 3
        linewidth = 1
    base = base_lagrange(x_cheb, sym.symbols("x"), cont_base)
    y_base = base(x)
    plt.plot(x, y_base, color=color, zorder=zorder, linewidth=linewidth)
    plt.xlabel("$x$", fontsize=14)
    plt.ylabel("$y$", fontsize=14)

plt.subplot(121)
plt.title("Interpolación")
plt.plot(x, y)
inter = lagrange(x_cheb, y_cheb)
plt.plot(x, inter(x), linestyle="dashed")
plt.plot(x_cheb, y_cheb, "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.tight_layout()
plt.savefig("runge_cheb.pdf", bbox_inches="tight", transparent=True)

#%% Interpolacion con nodes de Chebyshev
plt.figure(figsize=(5, 2.5))
titles = ["Puntos equidistantes", "Puntos no equidistantes"]
x_sample = [x_inter, x_cheb]
for cont in range(2):
    ax = plt.subplot(1, 2, cont + 1)
    plt.title(titles[cont])
    for cont_base in [0, 5]:
        if cont_base == 0:
            linestyle = None
        else:
            linestyle = "dashed"
        base = base_lagrange(x_sample[cont], sym.symbols("x"), cont_base)
        y_base = base(x)
        plt.plot(x, y_base, linestyle=linestyle)
    
    plt.xlabel("$x$", fontsize=14)
    plt.ylim(-1.5, 7)
    if cont == 0:
        plt.ylabel("$y$", fontsize=14)
    
    
plt.legend(["Punto izquierda", "Punto central"])
ax.yaxis.set_ticks([])
ax.spines["left"].set_color("none")
plt.tight_layout()
plt.savefig("runge_comparacion.pdf", bbox_inches="tight", transparent=True)

#plt.show()