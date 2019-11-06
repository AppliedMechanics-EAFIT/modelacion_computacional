# -*- coding: utf-8 -*-
"""
Ejemplo de uso matplotlib, un gráfico sencillo

"""
import numpy as np
from matplotlib import pyplot as plt

#%% Grafico sencillo
x = np.linspace(-np.pi, np.pi, 101)
cos = np.cos(x)
sin = np.sin(x)

plt.figure(figsize=(4, 3))
plt.plot(x, cos)
plt.plot(x, sin)

plt.savefig("grafico_sencillo.pdf")


#%% Version mejorada

# Creemos una figura de 6×4 in²
plt.figure(figsize=(4, 3))

# Usemos una línea solida,negra para el coseno de grosor 3
# y una línea punteada,roja para el coseno de grosor 1
plt.plot(x, cos, color="black", linestyle="solid", linewidth=2)
plt.plot(x, sin, color="red", linestyle="dashed", linewidth=1)

# Limitemos los ejes
plt.xlim(-4.0, 4.0)
plt.ylim(-1.5, 1.5)

# Asignemos nombre a cada eje
plt.xlabel("Eje x")
plt.ylabel("Eje y")

# Creemos una leyenda
plt.legend(["Coseno", "Seno"])
plt.savefig("grafico_sencillo_mejorado.pdf", bbox_inches="tight")


#%% Subplots
plt.figure(figsize=(5, 2.5))

# Usemos una rejila 2×1

# Primer sub-gráfico
plt.subplot(1, 2, 1)
plt.plot(x, cos)

# Segundo sub-gráfico
plt.subplot(1, 2, 2)
plt.plot(x, sin)

plt.savefig("subplots.pdf", bbox_inches="tight")




plt.show()