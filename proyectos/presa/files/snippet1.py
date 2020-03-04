mesh = meshio.read("files/dam_param.msh")
points = mesh.points
cells  = mesh.cells
cell_data  = mesh.cell_data
aux.script_mesh(mesh)

H_p   = 100.0
A_c   = 30.0
gamma = 9.8e3
cargas = aux.dam_loading(cells, cell_data, 3000, points, 0.0, gamma, H_p)
#cargas = aux.uniform_loading(cells, cell_data, 3000, points, gamma, H_p)
np.savetxt("files/Dloads.txt", cargas, fmt=("%d", "%.3g", "%.3g"))