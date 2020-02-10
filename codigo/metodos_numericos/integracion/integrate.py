# -*- coding: utf-8 -*-
"""
Routines for numerical integration

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function 
import numpy as np
# Gauss points and weights
from scipy.special import roots_legendre


def trapz(fun, x0, x1, n):
    """Trapezoidal rule for integration

    Parameters
    ----------
    fun : callable
        Function to integrate.
    x0 : float
        Initial point for the integration interval.
    x1 : float
        End point for the integration interval.
    n : int
        Number of points to take in the interval.

    Returns
    -------
    inte : float
        Approximation of the integral

    """
    x = np.linspace(x0, x1, n)
    y = fun(x)
    dx = x[1] - x[0]
    inte = 0.5*dx*(y[0] + y[-1])
    for cont in range(1, n - 1):
        inte = inte + dx*y[cont]
    return inte


def simps(fun, x0, x1, n):
    """Simpson's rule for integration

    Parameters
    ----------
    fun : callable
        Function to integrate.
    x0 : float
        Initial point for the integration interval.
    x1 : float
        End point for the integration interval.
    n : int
        Number of points to take in the interval.

    Returns
    -------
    inte : float
        Approximation of the integral

    """
    # We need an odd number of points
    # in case of having an even one
    # we add one point more
    if n%2 == 0:
        n = n + 1
    x = np.linspace(x0, x1, n)
    y = fun(x)
    dx = x[1] - x[0]
    inte = 0
    for cont in range(1, n//2 + 1):
        inte = inte + dx/3 * (y[2*cont - 2] + 4*y[2*cont - 1] + y[2*cont])
    return inte


def gauss1d(fun, x0, x1, n):
    """Gauss quadrature in 1D

    Parameters
    ----------
    fun : callable
        Function to integrate.
    x0 : float
        Initial point for the integration interval.
    x1 : float
        End point for the integration interval.
    n : int
        Number of points to take in the interval.

    Returns
    -------
    inte : float
        Approximation of the integral

    """
    xi, wi = roots_legendre(n)
    inte = 0
    h = 0.5 * (x1 - x0)
    xm = 0.5 * (x0 + x1)
    for cont in range(n):
        inte = inte + h * fun(h * xi[cont] + xm) * wi[cont]
    return inte


def gauss2d(fun, x0, x1, y0, y1, nx, ny):
    """Gauss quadrature for a rectangle in 2D

    Parameters
    ----------
    fun : callable
        Function to integrate.
    x0 : float
        Initial point for the integration interval in x.
    x1 : float
        End point for the integration interval in x.
    y0 : float
        Initial point for the integration interval in y.
    y1 : float
        End point for the integration interval in y.
    nx : int
        Number of points to take in the interval in x.
    ny : int
        Number of points to take in the interval in y.

    Returns
    -------
    inte : float
        Approximation of the integral

    """
    xi, wi = roots_legendre(nx)
    yj, wj = roots_legendre(ny)
    inte = 0
    hx = 0.5 * (x1 - x0)
    hy = 0.5 * (y1 - y0)
    xm = 0.5 * (x0 + x1)
    ym = 0.5 * (y0 + y1)
    for cont_x in range(nx):
        for cont_y in range(ny):
            f = fun(hx * xi[cont_x] + xm, hy * yj[cont_y] + ym)
            inte = inte + hx* hy * f * wi[cont_x] * wj[cont_y]
    return inte
