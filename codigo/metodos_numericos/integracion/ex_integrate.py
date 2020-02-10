# -*- coding: utf-8 -*-
"""
Examples for numerical integration

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
from integrate import trapz, simps, gauss1d, gauss2d

#%% Integrals in 1D
fun = lambda x: x**3 + 4*x**2 - 10
inte_analytic = -52/3
inte_trapz = trapz(fun, -1, 1, 5)
inte_simps = simps(fun, -1, 1, 5)
inte_gauss = gauss1d(fun, -1, 1, 2)
print("Comparison in 1D\n" + "="*15 + "\n")
print("Analytic integral: {:.6f}".format(inte_analytic))
print("Trapezoid integral: {:.6f}".format(inte_trapz))
print("Simpsons integral: {:.6f}".format(inte_simps))
print("Gauss integral: {:.6f}".format(inte_gauss))


#%% Integral in 2D
fun = lambda x, y: x**2 * y**2
inte_analytic = 4/9
inte_gauss = gauss2d(fun, -1, 1, -1, 1, 2, 2)
print("\n\nComparison in 2D\n" + "="*15 + "\n")
print("Analytic integral: {:.6f}".format(inte_analytic))
print("Gauss integral: {:.6f}".format(inte_gauss))