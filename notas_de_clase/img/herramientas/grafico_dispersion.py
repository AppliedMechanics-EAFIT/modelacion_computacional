#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de graficos de dispersion en matplotlib
"""
import numpy as np
from matplotlib import pyplot as plt

# Definimos las coordenadas aleatoriamente
n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

# Calculamos el ángulo usando  la función arcotangente
# que devuelve el ángulo en [-pi, pi]
angle = np.arctan2(y, x)


plt.figure(figsize=(3, 3))
plt.scatter(x, y, 20, angle, alpha=0.5)
plt.savefig("grafico_dispersion.pdf", bbox_inches="tight")