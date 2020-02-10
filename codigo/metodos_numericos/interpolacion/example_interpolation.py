#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of interpolation

@author: Nicolas Guarin-Zapata
@date: Sep, 2018
"""
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from interpolation import basis_lagrange, lagrange_poly, lagrange

# Initial data
x_data = [-1, 0, 1]
y_data = [-7, -10, -5]

#%% Analytic polynomial

# Sympy variable
x = sym.symbols("x")

# Basis polynomials
for cont in range(3):
    basis = basis_lagrange(x_data, x, 0)
    sym.pprint(basis)

# Interpolant polynomial
poly = lagrange_poly(x_data, y_data, x)
sym.pprint(poly)
sym.pprint(sym.expand(poly))

# Plot the polynomial
sym.plot(poly, (x, -1, 1))


#%% Numerical polynomial
x_interp = np.linspace(-1, 1, 101)
fun = lagrange(x_data, y_data)
y_interp = fun(x_interp)

# Plot
plt.figure()
plt.plot(x_interp, y_interp)
plt.show()
