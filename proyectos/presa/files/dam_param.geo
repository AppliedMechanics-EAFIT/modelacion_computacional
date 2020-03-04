// Input .geo for dam
// author: Juan Gomez

c = 5.0; 						// for size elements
Ap = 60.0;
Ac = 30.0;
Hp = 100.0;
Hs = 50.0;
Dl = 100.0;
Dr = 100.0;

// Define vertex points 						
Point(1) = {-Dl   , -Hs , 0, c};		        // {x,y,z, size}
Point(2) = {Ap+Dr , -Hs , 0, c};
Point(3) = {Ap+Dr , 0.0 , 0, c};
Point(4) = {Ap    , 0.0 , 0, c};
Point(5) = {0.000 , 0.0 , 0, c};
Point(6) = {-Dl   , 0.0 , 0, c};
Point(7) = {Ac    , Hp  , 0, c/4};
Point(8) = {0.000 , Hp  , 0, c/4};



// Define boundary lines
Line(1) = {1, 2};					// {Initial_point, end_point}
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 1};
Line(7) = {4, 7};
Line(8) = {7, 8};
Line(9) = {8, 5};

// Joint Lines
Line Loop(1) = {1, 2, 3, 4, 5, 6};
Line Loop(2) = {-4, 7, 8, 9};


// surface for mesh 					// {Id_Loop}
Plane Surface(1) = {1};
Plane Surface(2) = {2};

// Physical surface. Two material 
Physical Surface(100) = {1};
Physical Surface(200) = {2};

//Physical line. Boundary 
Physical Line(1000) = {1};
Physical Line(2000) = {2 , 6};
Physical Line(3000) = {9};
Physical Line(4000) = {4};
Physical Line(5000) = {8};
