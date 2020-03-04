if body== True:
    force_vec = ass.loadasem(loads, IBC, neq) + aux.body_forces(elements, nodes, neq, DME , force_y=aux.force_y  )   
else:
    force_vec = ass.loadasem(loads, IBC, neq) + aux.body_forces(elements, nodes, neq, DME )

UG = sol.static_sol(mat_rigidez, force_vec)
UC = pos.complete_disp(IBC, nodes, UG)
    