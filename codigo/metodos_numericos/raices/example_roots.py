# -*- coding: utf-8 -*-
"""
Examples of root finding

@author: Nicolas Guarin-Zapata
@date: Febr, 2018
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from roots import newton, bisection


npts = 201
a = -1.0
b = 10.0
fun = lambda x: x**3 + 4.0*x**2 - 10.0
deriv = lambda x: 3.0*x**2 + 8.0*x

#%% Plot
x = np.linspace(a, b, npts)
y = fun(x)
plt.plot(x, y)
plt.grid(True)
plt.ylim(-40, 100)
plt.xlabel("x")
plt.ylabel("y")

#%% Bisection
print("Bisection solution")
print("="*25)
bisection(fun, a, b, verbose=True)

#%% Newton-Raphson
print("\n\n")
print("Newton-Raphson solution")
print("="*25)
newton(fun, deriv, 10, verbose=True, ftol=1e-16)

plt.show()