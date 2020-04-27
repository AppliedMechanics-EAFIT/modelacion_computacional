/*
Archivo de geometría para una presa triangular.

Nicolás Guarín-Zapata
Abril 2020
*/


// Parámetros
lado = 100.0;


// Puntos
Point(1) = {0, 0, 0, 1.0};
Point(2) = {lado/2, 0, 0, 1.0};
Point(3) = {lado, 0, 0, 1.0};
Point(4) = {0, lado, 0, 1.0};


// Líneas
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line(5) = {2, 4};


// Contornos y superficies
Line Loop(1) = {1, 5, 4};
Plane Surface(1) = {1};
Line Loop(2) = {2, 3, -5};
Plane Surface(2) = {2};

// Grupos físicos
Physical Line(1) = {4};  // Línea de carga
Physical Line(2) = {1, 2};  // Línea horizontal
Physical Line(3) = {5};  // Diagonal
Physical Surface(3) = {1, 2};  // Superficie
