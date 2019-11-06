// Puntos
Point(1) = {0, 0, 0, 2.0};
Point(2) = {1, 0, 0, 2.0};
Point(3) = {1, 1, 0, 2.0};
Point(4) = {0, 1, 0, 2.0};

// Lineas
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

// Superficie
Line Loop(1) = {1, 2, 3, 4 };
Plane Surface(1) = {1};

// Grupos Fisicos
Physical Line(1) = {1};
Physical Line(2) = {3};
Physical Surface(4) = {1}

// Mallado regular
Transfinite Surface {1};
