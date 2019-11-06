// Puntos
Point(1) = {-3, -3, 0, 1.0};
Point(2) = {3, -3, 0, 1.0};
Point(3) = {3, 3, 0, 1.0};
Point(4) = {-3, 3, 0, 1.0};

// Lineas
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};// Gmsh project created on Sun Mar  4 16:47:52 2018


// Superficie
Line Loop(1) = {3, 4, 1, 2};
Plane Surface(1) = {1};

// Mallado
Transfinite Line {4, 2} = 4 Using Progression 1;
Transfinite Line {3, 1} = 7 Using Progression 1;
Transfinite Surface {1};
Recombine Surface {1};
