#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:32:04 2020

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
import meshio
import solidspy.preprocesor as msh

def filtered(nodes, elements, field, threshold, fig=None):
    """Plot contours for values higher than threshold"""
    if fig is None:
        plt.figure()
    plt.triplot(nodes[:, 1], nodes[:, 2], elements[:, 3:], zorder=3,
                color="#757575")
    if threshold < 0.0 and threshold > field.min():
        plt.tricontourf(nodes[:, 1], nodes[:, 2], elements[:, 3:], field,
                        levels=[field.min(), threshold], zorder=4, cmap="PuRd")
    if threshold > 0.0 and threshold < field.max():
        plt.tricontourf(nodes[:, 1], nodes[:, 2], elements[:, 3:], field,
                        levels=[threshold, field.max()], zorder=4, cmap="PuRd")
    plt.axis("image")
    return None

def energy(E_nodes, S_nodes):
    """Compute deformation energy density for the model"""
    small_pi = 0.5 * np.sum(S_nodes * E_nodes, axis=1)
    return small_pi


def res_forces(KG, UG, IBC, neq, nodes, cells , cell_data , phy_lin):
    """
    Encuentra las fuerzas nodales a lo largo de la linea fisica
    phy_lin usando el producto de F= KG*UG
    Parameters
    ----------
    KG: array
        Array storing the glopbal stiffness matrix of the system
    physical_line : int
        Physical line identifier.
    nodes : array
        Array with the coordinates of the mesh.
    Returns
    -------
    dof_id : list
            Lista identificando los grados de libertad asociados con las fuerza.
    react_group: array
         Arreglo con las fuerzas sobre la linea fisica.

    """
    F = np.zeros((neq))
    F = KG.dot(UG)
    nodes_id, line_x, line_y = locate_pts_line(phy_lin, nodes , cells , cell_data)
    true_nodes_id = IBC[nodes_id]
    dof_id = true_nodes_id.flatten()
    react_group = F[dof_id]
    return dof_id, react_group 



def readin():
    nodes = np.loadtxt('files/Dnodes.txt', ndmin=2)
    mats = np.loadtxt('files/Dmater.txt', ndmin=2)
    elements = np.loadtxt('files/Deles.txt', ndmin=2, dtype=np.int)
    loads = np.loadtxt('files/Dloads.txt', ndmin=2)
    return nodes, mats, elements, loads

def locate_pts_line(physical_line, points , cells , cell_data):
    """
    Find the nodes located on a physical line and their coordinates.

    Parameters
    ----------
    physical_line : int
        Physical line identifier.
    points : array
        Array with the coordinates of the mesh.

    Returns
    -------
    nodes_line : list
        Number identifier for nodes on the physical line.
    line_x : array
        Array with the x coordinates for the nodes locates in the
        physical line.
    line_y : array
        Array with the y coordinates for the nodes locates in the
        physical line.
    """
    lines = cells["line"]
    phy_line = cell_data["line"]["gmsh:physical"]
    id_carga = [cont for cont in range(len(phy_line))
                if phy_line[cont] == physical_line]
    nodes_line = lines[id_carga]
    nodes_line = nodes_line.flatten()
    nodes_line = list(set(nodes_line))
    line_x = points[nodes_line][:, 0]
    line_y = points[nodes_line][:, 1]
    return nodes_line, line_x, line_y


def dam_loading(cells, cell_data, phy_lin, nodes, P_y,  gamma_h, Hdam):
    """
    Impone cargas nodales que varían linealmente con intensidad máxima en la pata
    de la presa consistentes con presión hidriestática.

    Parameters
    ----------
        cell : diccionario
            Diccionario creado por meshio con información de las celdas.
        cell_data: diccionario
            Diccionario creado por meshio con información de campo de las celdas.
        phy_lin : int
            Linea fisica sobre la que se aplicaran las cargas.            
        nodes: int
            Arreglo con la informacion nodal y usado para calcular las cragas.
            Array with the nodal data and to be modified by BCs.
        P_y : float
            Magnitud de la carga en la direccion  y.
        gamma_h: float
            Peso especifico del fluido
        Hdam  : float
            Altura de la presa.

    Returns
    -------
        cargas : int
            Arreglo de cargas nodales para SolidsPy.

    """
    lines = cells["line"]
    phy_line = cell_data["line"]["gmsh:physical"]
    id_carga = [cont for cont in range(len(phy_line))
                if phy_line[cont] == phy_lin]
    nodes_carga = lines[id_carga]
    nodes_carga = nodes_carga.flatten()
    nodes_carga = list(set(nodes_carga))
    ncargas = len(nodes_carga)
    nodes_line, line_x, line_y = locate_pts_line(phy_lin, nodes , cells , cell_data)
    cargas = np.zeros((ncargas, 3))
    cargas[:, 0] = nodes_carga
    cargas[:, 1] = 0.5*gamma_h*(Hdam-line_y)*Hdam/ncargas
    cargas[:, 2] = P_y/ncargas
    return cargas

def uniform_loading(cells, cell_data, phy_lin, nodes, gamma_h , Hdam):
    """
    Impone cargas nodales que varían linealmente con intensidad máxima en la pata
    de la presa consistentes con presión hidriestática.

    Parameters
    ----------
        cell : diccionario
            Diccionario creado por meshio con información de las celdas.
        cell_data: diccionario
            Diccionario creado por meshio con información de campo de las celdas.
        phy_lin : int
            Linea fisica sobre la que se aplicaran las cargas.            
        nodes: int
            Arreglo con la informacion nodal y usado para calcular las cragas.
            Array with the nodal data and to be modified by BCs.
        P_y : float
            Magnitud de la carga en la direccion  y.
        gamma_h: float
            Peso especifico del fluido
        Hdam  : float
            Altura de la presa.

    Returns
    -------
        cargas : int
            Arreglo de cargas nodales para SolidsPy.

    """
    lines = cells["line"]
    phy_line = cell_data["line"]["gmsh:physical"]
    id_carga = [cont for cont in range(len(phy_line))
                if phy_line[cont] == phy_lin]
    nodes_carga = lines[id_carga]
    nodes_carga = nodes_carga.flatten()
    nodes_carga = list(set(nodes_carga))
    ncargas = len(nodes_carga)
    nodes_line, line_x, line_y = locate_pts_line(phy_lin, nodes , cells , cell_data)
    cargas = np.zeros((ncargas, 3))
    cargas[:, 0] = nodes_carga
    cargas[:, 1] = gamma_h*Hdam*Hdam/ncargas
    return cargas 


def body_forces(elements, nodes, neq, DME, force_x=None, force_y=None):
    """Compute nodal forces due to body"""
    if force_x is None:
        def force_x(x, y): return 0
    if force_y is None:
        def force_y(x, y): return 0
    force_vec = np.zeros((neq))
    nels = elements.shape[0]
    for el in range(nels):
        verts = nodes[elements[el, 3:], 1:3]
        centroid = (verts[0, :] + verts[1, :] + verts[2, :])/3
        area = 0.5 * np.linalg.det(np.column_stack((verts, np.ones(3))))
        floc = np.array([force_x(*centroid), force_y(*centroid),
                         force_x(*centroid), force_y(*centroid),
                         force_x(*centroid), force_y(*centroid)])
        floc = floc * area
        dme = DME[el, :6]
        for row in range(6):
            glob_row = dme[row]
            if glob_row != -1:
                force_vec[glob_row] = force_vec[glob_row] + floc[row]
    return force_vec

def force_y(x, y):
    """Body force due to self-weight"""
    return -2.3 * 9.8e3

def script_mesh(mesh):
    
    mesh = meshio.read("files/dam_param.msh")
    points = mesh.points
    cells  = mesh.cells
    point_data = mesh.point_data
    cell_data  = mesh.cell_data
    field_data = mesh.field_data

    nodes_array    = msh.node_writer(points, point_data)
    nf, els1_array = msh.ele_writer(cells, cell_data, "triangle", 100, 3, 0, 0)
    nini = nf
    nf, els2_array = msh.ele_writer(cells, cell_data, "triangle", 200, 3, 1, nini)
    els_array      = np.append(els1_array, els2_array, axis=0)

    nodes_array = msh.boundary_conditions(cells, cell_data, 2000, nodes_array, -1, 0)
    nodes_array = msh.boundary_conditions(cells, cell_data, 1000, nodes_array, 0, -1)

    np.savetxt("files/Deles.txt", els_array, fmt="%d")
    np.savetxt("files/Dnodes.txt", nodes_array, fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
    
    return 