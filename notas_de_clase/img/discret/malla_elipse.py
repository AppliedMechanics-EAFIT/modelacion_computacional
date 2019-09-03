# -*- coding: utf-8 -*-
"""
Ejemplo de malla estructurada para una sección
de elipse.

Visualizamos el campo escalar

  f(x, y) = x**2 + y**3
  
sobre una sección de una elipse.

@author: Nicolas Guarin-Zapata
@date: Abril 2018
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
# Primero, creamos una serie de divisiones en el radio
# y en la variable angular
rad = np.linspace(1, 2, 11)
angle = np.linspace(0, np.pi/2, 21)

#%%
# Luego usamos la función meshgrid de NumPy que nos
# permite combinar las subdivisiones para tener la
# malla que queremos
rad, angle = np.meshgrid(rad, angle)

#%%
# Creamos las coordenadas x, y de los puntos usando
# las ecuaciones paramétricas de una elipse
a = 2.0 # semieje mayor
b = 1.0 # semieje menor
x = a * rad * np.cos(angle)
y = b * rad * np.sin(angle)
campo = x**2 + y**3

#%%
# Visualizamos
plt.figure(figsize=(5, 2.5))
plt.subplot(1, 2, 1)
plt.plot(x, y, color="black", marker=".", linewidth=0, markersize=3)
plt.xticks([0, 2, 4])
plt.axis("image")
plt.subplot(1, 2, 2)
plt.contourf(x, y, campo)
plt.xticks([0, 2, 4])
plt.axis("image")
plt.savefig("elipse_vis.pdf", transparent=True, bbox_inches="tight")