# -*- coding: utf-8 -*-
from __future__ import division, print_function
from numpy import log2, ceil, abs, zeros


def bracketing(fun, a, b, N):
    """Estimate the root of a real function using bracketing

    Parameters
    ----------
    fun : function
        Function.
    a : float
        Initial point of the interval.
    b : float
        Final point of the interval.
    N : int
        NUmber of subdivisions for the interval


    Returns
    -------
    xR : array
        Array with initial estimates for roots.
    msg : string
        Message regarding the success of the method.

    """
    msg = "Maximum number of iterations reached."
    dx = (b - a)/(N - 1)
    iroot = 0
    x2 = a
    xR = zeros(N, float)
    for i in range(0, N):
        x1 = x2
        x2 = x1 + dx
        if (fun(x1) * fun(x2)) < 0:
            msg = "A change of sign was found."
            iroot = iroot + 1
            xR[i] = x1
    return xR, msg


def bisection(fun, a, b, xtol=1e-6, ftol=1e-12, verbose=False):
    """Use bisection method to estimate the root of a real function

    Parameters
    ----------
    fun : function
        Function.
    grad : function
        Derivative of the function.
    a : float
        Initial point of the interval.
    b : float
        Final point of the interval.
    xtol : float, optional
        Tolerance for the interval.
    ftol : float, optional
        Tolerance for the root.
    verbose : bool, optional
        If True, prints each iteration.

    Returns
    -------
    x : array
        Approximated root.
    msg : string
        Message regarding the success of the method.
    """
    if fun(a) * fun(b) > 0:
        c = None
        msg = "The function should have a sign change in the interval."
    else:
        nmax = int(ceil(log2((b - a)/xtol)))
        for cont in range(nmax):
            c = 0.5*(a + b)
            if verbose:
                print("n: {}, x: {}".format(cont, c))
            if abs(fun(c)) < ftol:
                msg = "Root found with desired accuracy."
                break
            elif fun(a) * fun(c) < 0:
                b = c
            elif fun(b) * fun(c) < 0:
                a = c
            msg = "Maximum number of iterations reached."
    return c, msg


def newton(fun, grad, x, niter=50, ftol=1e-8, verbose=False):
    """Use Newton method to estimate the root of a real function

    Parameters
    ----------
    fun : function
        Function.
    grad : function
        Derivative of the function.
    x : float
        Initial estimate.
    niter : int, optional
        Maximum number of iterations.
    ftol : float, optional
        Tolerance for the root.
    verbose : bool, optional
        If True, prints each iteration.

    Returns
    -------
    x : array
        Approximated root.
    msg : string
        Message regarding the success of the method.
    """
    msg = "Maximum number of iterations reached."
    for cont in range(niter):
        if abs(grad(x)) < ftol:
            x = None
            msg = "Derivative near to zero."
            break
        if verbose:
            print("n: {}, x: {}".format(cont, x))
        x = x - fun(x)/grad(x)
        if abs(fun(x)) < ftol:
            msg = "Root found with desired accuracy."
            break
    return x, msg
