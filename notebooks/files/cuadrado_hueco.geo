/*
Archivo de geometría para un cuadrado con un agujero circular

Nicolás Guarín-Zapata
Abril 2020
*/


// Parámetros
radio_in = 1.0;
semi_lado = 10.0;
ndiv_rad = 161;
ndiv_arc = 81;


// Puntos
Point(1) = {0, 0, 0, 1.0};
Point(2) = {radio_in*Cos(Pi/4), radio_in*Cos(Pi/4), 0, 1.0};
Point(3) = {-radio_in*Cos(Pi/4), radio_in*Cos(Pi/4), 0, 1.0};
Point(4) = {-radio_in*Cos(Pi/4), -radio_in*Cos(Pi/4), 0, 1.0};
Point(5) = {radio_in*Cos(Pi/4), -radio_in*Cos(Pi/4), 0, 1.0};
Point(6) = {semi_lado, semi_lado, 0, 1.0};
Point(7) = {-semi_lado, semi_lado, 0, 1.0};
Point(8) = {-semi_lado, -semi_lado, 0, 1.0};
Point(9) = {semi_lado, -semi_lado, 0, 1.0};


// Líneas
Line(1) = {8, 9};
Line(2) = {9, 6};
Line(3) = {6, 7};
Line(4) = {7, 8};
Line(5) = {8, 4};
Line(6) = {5, 9};
Line(7) = {2, 6};
Line(8) = {3, 7};
Circle(9) = {2, 1, 3};
Circle(10) = {3, 1, 4};
Circle(11) = {4, 1, 5};
Circle(12) = {5, 1, 2};


// Contornos y superficies
Line Loop(1) = {1, -6, -11, -5};
Plane Surface(1) = {1};
Line Loop(2) = {2, -7, -12, 6};
Plane Surface(2) = {2};
Line Loop(3) = {7, 3, -8, -9};
Plane Surface(3) = {3};
Line Loop(4) = {8, 4, 5, -10};
Plane Surface(4) = {4};


// Grupos físicos
Physical Line(1) = {9, 10, 11, 12};
Physical Line(2) = {7};
Physical Surface(3) = {1, 2, 3, 4};


// Parámetros mallado
Transfinite Line {5, 6, 7, 8} = ndiv_rad Using Progression 1;
Transfinite Line {4, 10, 9, 3, 12, 2, 1, 11} = ndiv_arc Using Progression 1;
Transfinite Surface {1};
Transfinite Surface {2};
Transfinite Surface {3};
Transfinite Surface {4};
