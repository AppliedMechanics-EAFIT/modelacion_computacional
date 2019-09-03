/*
Ejemplo de creacion de malla para un anillo
*/

// -- Definicion geometria --

// Parametros
rad_int = 2.0;  // Radio interior
rad_ext = 4.0;  // Redio exterior

// Puntos
Point(1) = {0.0, 0.0, 0, 1.0};
Point(2) = {-rad_ext, 0.0, 0, 1.0};
Point(3) = { rad_ext, 0.0, 0, 1.0};
Point(4) = {-rad_int, 0.0, 0, 1.0};
Point(5) = { rad_int, 0.0, 0, 1.0};

// Lineas
Circle(1) = {3, 1, 2};
Circle(2) = {2, 1, 3};
Circle(3) = {5, 1, 4};
Circle(4) = {4, 1, 5};
Line(5) = {2, 4};
Line(6) = {5, 3};

// Bucles y superficies
Line Loop(7) = {1, 5, -3, 6};
Plane Surface(8) = {7};
Line Loop(9) = {2, -6, -4, -5};
Plane Surface(10) = {9};

// Grupos fisicos
Physical Line(11) = {1, 2};
Physical Line(12) = {3, 4};
Physical Surface(13) = {8, 10};


// -- Parametros de malla --

// Subdivision de lineas
ndiv_arco = 44;  // Subdivisiones de los arcos
ndiv_rad = 12;    // Subdivisiones en la direccion radial
Transfinite Line {5, 6} = ndiv_rad Using Progression 1;
Transfinite Line {1, 3, 4, 2} = ndiv_arco Using Progression 1;

// Subdivision superficies
Transfinite Surface {8};
Transfinite Surface {10};

// Recombinar triangulos en cuadrilateros
Recombine Surface {8, 10};
