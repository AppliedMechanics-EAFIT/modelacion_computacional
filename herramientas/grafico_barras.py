#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de gráfico de barras en matplotlib

"""
import numpy as np
from matplotlib import pyplot as plt


edad = np.array(['80 y más', '75 a 79', '70 a 74', '65 a 69',
                 '60 a 64', '55 a 59', '50 a 54', '45 a 49',
                 '40 a 44', '35 a 39', '30 a 34', '25 a 29',
                 '20 a 24', '18 a 19', '15 a 17', '10 a 14'])
hombres = np.array([ 52,  33,  50,  62,  77,  99, 101, 134,
                    100, 145, 148, 191, 231, 95, 100,  37])
mujeres = np.array([ 6,  1,  4,  8, 13, 17, 22, 20, 19, 27, 41,
                    53, 71, 29, 49, 33])

plt.figure(figsize=(5, 3))
posiciones = range(len(edad))
# El parámetro opcional tick_label nos permite añadir cada rango de edades
plt.barh(posiciones, mujeres, tick_label=edad, color="#81bbea")
# Modificamos el alto de las barras para que no cubran las barras anteriores
plt.barh(posiciones, hombres, tick_label=edad, height=0.3, color="#377eb8")
plt.xlabel("Número de suicidios")
plt.ylabel("Edad")
plt.legend(["Mujeres", "Hombres"])
# El próximo comando obliga a Matplotlib a mostrar el gráfico completo
plt.tight_layout()

plt.savefig("grafico_barras.pdf", bbox_inches="tight")