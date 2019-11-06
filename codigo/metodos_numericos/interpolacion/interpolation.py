#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interpolation module

We have analytic interpolation using SymPy and numerical interpolation
that returns an evaluable function.
"""
import sympy as sym

#%% Analytic interpolation
def basis_lagrange(x_data, var, i):
    """
    Compute the basis interpolant polynomial corresponding to the
    i-th  point given in x_data

    Parameters
    ----------
    x_data : list
        List with x coordinates for the interpolation.
    var : SymPy symbol
        Variable to be used for the interpolation
    i : int
        Point number for the interpolant.

    Returns
    -------
    poly : SymPy expression
        Interpolant polynomial in variable var.

    """
    prod = 1
    num = len(x_data)
    for j in range(num):
        if j == i:
            continue
        prod = prod * (var - x_data[j])/(x_data[i] - x_data[j])
    return sym.simplify(prod)


def lagrange_poly(x_data, y_data, var):
    """
    Compute the interpolant polynomial corresponding to the
    points given in (x_data, y_data)

    Parameters
    ----------
    x_data : list
        List with x coordinates for the interpolation.
    y_data : list
        List with y coordinates for the interpolation.
    var : SymPy symbol
        Variable to be used for the interpolation

    Returns
    -------
    poly : SymPy expression
        Interpolant polynomial in variable var.

    """
    poly = 0
    num = len(x_data)
    for i in range(num):
        poly = poly + y_data[i] * basis_lagrange(x_data, var, i)
    return poly


#%% Numerical interpolation
def lagrange(x_data, y_data):
    """
    Compute the interpolant polynomial corresponding to the
    points given in (x_data, y_data)

    Parameters
    ----------
    x_data : list
        List with x coordinates for the interpolation.
    y_data : list
        List with y coordinates for the interpolation.

    Returns
    -------
    fun_poly : Python function
        Interpolant polynomial as evaluable function.

    """
    def fun_poly(x):
        num = len(x_data)
        acu = 0
        for i in range(num):
            prod = 1
            for j in range(num):
                if i == j:
                    continue
                prod = prod * (x - x_data[j])/(x_data[i] - x_data[j])
            acu = acu + prod * y_data[i]
        return acu
    return fun_poly
