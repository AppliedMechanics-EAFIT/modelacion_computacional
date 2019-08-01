# -*- coding: utf-8 -*-
"""
Interpolaciones de diferente orden para la funcion

  2*exp(x) + sin(3*x)

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


def deriv_base_lagrange(x_datos, var, cont):
    """Crea un polinomio base de Lagrange para los datos x"""
    prod = sym.prod((var - x_datos[i])/(x_datos[cont] - x_datos[i])
                    for i in range(len(x_datos)) if i != cont)
    return sym.lambdify(var, sym.simplify(prod.diff(var)), "numpy")


fun = lambda x: 2*np.exp(x) + np.sin(3*x)
grad = lambda x: 2*np.exp(x) + 3*np.cos(3*x)
x = np.linspace(-1, 1, 101) 
y = fun(x)
dy = grad(x)

plt.close("all")
plt.figure(figsize=(5, 6))

npts = [2, 3, 5]
for cont in range(3):
    ax = plt.subplot(3, 2, 2*cont + 1)
    if cont==0:
        plt.title("Interpolación")
    x_inter = np.linspace(-1, 1, npts[cont])
    y_inter = fun(x_inter)
    f_inter = lagrange(x_inter, y_inter)
    plt.plot(x, y)
    plt.plot(x, f_inter(x), linestyle="dashed",
             label="Orden {}".format(npts[cont] - 1))
    plt.plot(x_inter, y_inter, "ok")
    plt.ylabel("$y$", fontsize=14)
    plt.legend(frameon=False)
    if cont != 2:
        ax.xaxis.set_ticks([])
        ax.spines["bottom"].set_color("none")
    if cont == 2:
        plt.xlabel("$x$", fontsize=14)

for cont in range(3):
    ax = plt.subplot(3, 2, 2*cont + 2)
    if cont==0:
        plt.title("Funciones base")
    for cont_base in range(npts[cont]):
        x_inter = np.linspace(-1, 1, npts[cont])
        base = base_lagrange(x_inter, sym.symbols("x"), cont_base)
        y_base = base(x)
        plt.plot(x, y_base)
        plt.ylim(-0.6, 1.2)
        plt.yticks(np.linspace(-0.5, 1, 4))
        plt.ylabel("$y$", fontsize=14)
    if cont != 2:
        ax.xaxis.set_ticks([])
        ax.spines["bottom"].set_color("none")
    if cont == 2:
        plt.xlabel("$x$", fontsize=14)

plt.tight_layout()
plt.savefig("interp_multiple.pdf", bbox_inches="tight", transparent=True)


#%% Derivadas
plt.figure(figsize=(5, 2.5))
plt.subplot(122)
plt.title("Funciones base")
x_inter = np.linspace(-1, 1, 5)
y_inter = fun(x_inter)
dy_inter = np.zeros_like(x)
for cont_base in range(5):
    deriv_base = deriv_base_lagrange(x_inter, sym.symbols("x"), cont_base)
    y_base = deriv_base(x)
    dy_inter += y_base * y_inter[cont_base]
    plt.plot(x, y_base)
    plt.xlabel("$x$", fontsize=14)
    plt.ylabel("$y$", fontsize=14)

plt.subplot(121)
plt.title("Derivadas")
plt.plot(x, dy)
plt.plot(x, dy_inter, linestyle="dashed")
plt.plot(x_inter, grad(x_inter), "ok")
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)
plt.tight_layout()
plt.savefig("interp_multiple_deriv.pdf", bbox_inches="tight", transparent=True)
#plt.show()