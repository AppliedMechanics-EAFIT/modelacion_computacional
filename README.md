# Modelación computacional

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AppliedMechanics-EAFIT/modelacion_computacional/master)

## Introducción
Este repositorio contiene recursos de aprendizaje para el curso **Modelación Computacional** dictado a estudiantes de segundo año (4to semestre) del programa de Ingeniería Civil de la Universidad EAFIT. El curso cubre aspectos básicos de uso de herramientas computacionales, algunos métodos numéricos fundamentales y elementos comunes a la simulación numérica de problemas asociados con fenoménos mecánicos (v-gr., mecánica de sólidos, mecánica de los medios continuos, análisis estructural, elementos finitos, etc). El curso utiliza Python como lenguaje de programación así como herramientas de uso libre disponibles en línea. En lo que sigue se presentan instrucciones para descargar o clonar el repositorio. Adicionalmente, usando la opción de binder es posible ejecutar los Notebooks aún sin tener una instalación de Python o Jupyter en el computador de trabajo.

## Aprendizaje activo

En un alto porcentaje de este curso se utilizan estrategias pedagogícas de aprendizaje activo, particularmente en algunas de las sesiones se seguirá una metodología de aula inversa. En esta se otorga una mayor responsabilidad al estudiante durante el proceso de aprendizaje. Para desarrollar este proceso se han desarrollado los siguientes recursos:

* **Notas de clase:** con los archivos fuente y el documento en
  [pdf](https://github.com/AppliedMechanics-EAFIT/modelacion_computacional/raw/master/notas_de_clase/notas_modelacion.pdf).

* **Actvididades de aprendizaje activo:** en Notebooks de [Jupyter](http://jupyter.org/).

* **Códigos de ejemplo.**

## Contenidos

Las actividades de aprendizaje activo usan Notebooks de Jupyter que permiten tener
en un único documento texto, gráficos y código.

A continuación se presentan las actividades disponibles.

1. [Búsqueda de raíces](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/01_busqueda_raices.ipynb)

2. Interpolación

    1. [Interpolación 1D](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/02a_interpolacion.ipynb)

    2. [Interpolación por tramos](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/02b_interpolacion_tramos.ipynb)

    3. [Interpolación en 2D](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/02c_interpolacion_2d.ipynb)

3. [Integración numérica](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/03_integracion_numerica.ipynb)

4. Elementos finitos y análisis estructural

    1. Generalidades sobre el análisis estructural y los elementos finitos

        1. [Introducción](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/06a_analisis_estructural.ipynb)

        2. [Ejemplo de ensamblaje de ecuaciones](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/06b_ensamblaje.ipynb)

        3. [Ensamblaje paso a paso](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/06c_ensamble_paso_a_paso.ipynb)

    2. Cerchas

        1. [Elementos tipo cercha](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/07a_cerchas.ipynb)

        2. [Cambio de coordenadas para elementos tipo cercha](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/07b_cerchas_cambio_coordenadas.ipynb)

    3. [Elementos tipo pórtico](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/08_porticos.ipynb)

    4. [Ejemplo de aplicación: Cercha de von Mises](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/modelacion_computacional/blob/master/notebooks/09_cercha_mises.ipynb)


## Descarga del material

Se puede clonar el repositorio usando:

    git clone https://github.com/AppliedMechanics-EAFIT/modelacion_computacional

o directamente usar la opción de descarga desde GitHub.

## Instrucciones de instalación

Para correr los notebooks de Jupyter, es necesario [Python](https://www.python.org/)
y algunos paquetes:

- [IPython](http://ipython.org/), un shell interactivo que añade funcionalidades  extra al modo interactivo incluido con Python, como resaltado de líneas y errores mediante colores, una sintaxis adicional para el shell, autocompletado mediante tabulador de variables, módulos y atributos; entre otras funcionalidades.

- [NumPy](http://www.numpy.org/), una extensión de Python, que le agrega mayor
soporte para vectores y matrices, constituyendo una biblioteca de funciones
matemáticas de alto nivel para operar con esos vectores o matrices.

- [SciPy](http://www.scipy.org/), una biblioteca de herramientas y algoritmos matemáticos para Python.

- [matplotlib](http://matplotlib.org/),  una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de
programación Python y su extensión matemática NumPy.

y el [Sistema de Álgebra por computadora (CAS)](https://en.wikipedia.org/wiki/Computer_algebra_system) [Sympy](http://www.sympy.org/).

El método sugerido es usar una distribución de Python, preferiblemente  [Anaconda](https://www.anaconda.com/). Esta incluye todos los paquetes mencionados arriba.

## Licencia

El contenido de este repositorio está licenciado bajo una licencia [Creative Commons Attribution 4.0](http://choosealicense.com/licenses/cc-by-4.0/),
y el código fuente que le acompaña bajo una
[licencia MIT](https://opensource.org/licenses/mit-license.php).

## Citación

Para citar estas notas de clase use

> Juan Gómez, Nicolás Guarín-Zapata y Edward Villegas-Pulgarín (2019).
  Notas de clase: Modelación computacional. Universidad EAFIT,
  Disponible en: https://github.com/AppliedMechanics-EAFIT/modelacion_computacional.

Una entrada de BibTeX para los usuarios de LaTeX es

    @misc{notas_modelacion,
     title = {Notas de clase: Modelación computacional},
     author = {Gómez, Juan and Guarín-Zapata, Nicolás and
               Villegas-Pulgarín, Edward. },
     year = {2019},
     keywords = {Modelación computacional, Python,
                Mecánica computacional},
     publisher = {Universidad EAFIT},
     url = {https://github.com/AppliedMechanics-EAFIT/modelacion_computacional}
    }
