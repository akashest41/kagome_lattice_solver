import numpy as np

import rustworkx as rx

from qiskit_nature.problems.second_quantization.lattice import Lattice

def kagome_raw_lattice_construct(cub1_x, cub1_y, cub2_x, cub2_y, cub3_x, cub3_y, cub4_x, cub4_y):
    #input parameters for the repeat units for each cubic sublattice unit cell
    #each parameter should be an integer greater than or equal to 0
    
    node_list = [] #list of 3-tuples, each containing the node index and the node coordinates in the order
    edge_list = []
    
    node_curr_index = 0

    # Edge weight
    t = 1.0 #default edge weight of 1.0
    
    for c1y in np.arange(cub1_y):
        for c1x in np.arange(cub1_x):
            c1_node0_index = node_curr_index
            c1_node0_x = 1.5 + (c1x*2)
            c1_node0_y = 4*c1y
    
            c1_node1_index = node_curr_index + 1
            c1_node1_x = 2 + (c1x*2)
            c1_node1_y = 1 + (4*c1y)
        
            c1_node2_index = node_curr_index + 2
            c1_node2_x = 1 + (c1x*2)
            c1_node2_y = 1 + (4*c1y)
        
            node_curr_index += 3
        
            node_list.append([c1_node0_index, c1_node0_x, c1_node0_y])
            node_list.append([c1_node1_index, c1_node1_x, c1_node1_y])
            node_list.append([c1_node2_index, c1_node2_x, c1_node2_y])
        
            edge_list.append([c1_node0_index,c1_node1_index,t])
            edge_list.append([c1_node1_index,c1_node2_index,t])
            edge_list.append([c1_node2_index,c1_node0_index,t])
            
    for c2y in np.arange(cub2_y):
        for c2x in np.arange(cub2_x):
            c2_node0_index = node_curr_index
            c2_node0_x = c2x*2
            c2_node0_y = 1 + (4*c2y)
    
            c2_node1_index = node_curr_index + 1
            c2_node1_x = 1 + (c2x*2)
            c2_node1_y = 1 + (4*c2y)
        
            c2_node2_index = node_curr_index + 2
            c2_node2_x = 0.5 + (c2x*2)
            c2_node2_y = 2 + (4*c2y)
        
            node_curr_index += 3
        
            node_list.append([c2_node0_index, c2_node0_x, c2_node0_y])
            node_list.append([c2_node1_index, c2_node1_x, c2_node1_y])
            node_list.append([c2_node2_index, c2_node2_x, c2_node2_y])
        
            edge_list.append([c2_node0_index,c2_node1_index,t])
            edge_list.append([c2_node1_index,c2_node2_index,t])
            edge_list.append([c2_node2_index,c2_node0_index,t])
            
    for c3y in np.arange(cub3_y):
        for c3x in np.arange(cub3_x):
            c3_node0_index = node_curr_index
            c3_node0_x = 0.5 + (c3x*2)
            c3_node0_y = 2 + (4*c3y)
    
            c3_node1_index = node_curr_index + 1
            c3_node1_x = 1 + (c3x*2)
            c3_node1_y = 3 + (4*c3y)
        
            c3_node2_index = node_curr_index + 2
            c3_node2_x = (c3x*2)
            c3_node2_y = 3 + (4*c3y)
        
            node_curr_index += 3
        
            node_list.append([c3_node0_index, c3_node0_x, c3_node0_y])
            node_list.append([c3_node1_index, c3_node1_x, c3_node1_y])
            node_list.append([c3_node2_index, c3_node2_x, c3_node2_y])
        
            edge_list.append([c3_node0_index,c3_node1_index,t])
            edge_list.append([c3_node1_index,c3_node2_index,t])
            edge_list.append([c3_node2_index,c3_node0_index,t])
            
    for c4y in np.arange(cub4_y):
        for c4x in np.arange(cub4_x):
            c4_node0_index = node_curr_index
            c4_node0_x = 1 + (c4x*2)
            c4_node0_y = 3 + (4*c4y)
    
            c4_node1_index = node_curr_index + 1
            c4_node1_x = 2 + (c4x*2)
            c4_node1_y = 3 + (4*c4y)
        
            c4_node2_index = node_curr_index + 2
            c4_node2_x = 1.5 + (c4x*2)
            c4_node2_y = 4 + (4*c4y)
        
            node_curr_index += 3
        
            node_list.append([c4_node0_index, c4_node0_x, c4_node0_y])
            node_list.append([c4_node1_index, c4_node1_x, c4_node1_y])
            node_list.append([c4_node2_index, c4_node2_x, c4_node2_y])
        
            edge_list.append([c4_node0_index,c4_node1_index,t])
            edge_list.append([c4_node1_index,c4_node2_index,t])
            edge_list.append([c4_node2_index,c4_node0_index,t])
            
    return node_list, edge_list

def kagome_raw_lattice_reduce(node_list, edge_list):
    #resolving node coincidence conflicts

    for nodes in node_list:
        curr_x = nodes[1]
        curr_y = nodes[2]
        keep_index = nodes[0]
        del_list = []
        del_entries = 0
        for seq_nodes in node_list:
            if ((seq_nodes[1] == curr_x) and (seq_nodes[2] == curr_y) and (seq_nodes[0] != keep_index)):
                del_entries += 1
                if (keep_index < seq_nodes[0]):
                    del_list.append([seq_nodes[0], seq_nodes[1], seq_nodes[2], keep_index]) #a coincidence clash can only happen between two nodes being shared by two adjacent cells
    
        if (del_entries != 0):
            for del_node in del_list:
                for edges in edge_list:
                    if (edges[0] == del_node[0]):
                        edges[0] = del_node[3]
                    if (edges[1] == del_node[0]):
                        edges[1] = del_node[3]
                for nodes in node_list:
                    if (nodes[0] > del_node[0]):
                        for edges in edge_list:
                            if (edges[0] == nodes[0]):
                                edges[0] = edges[0] - 1
                            if (edges[1] == nodes[0]):
                                edges[1] = edges[1] - 1
                        nodes[0] = nodes[0] - 1
            for del_node in del_list:
                del_node_entry = [del_node[0], del_node[1], del_node[2]]
                node_list.remove(del_node_entry)
                
    return node_list, edge_list

def get_num_sites(node_list):
    num_sites = len(node_list)
    return num_sites

def get_pos_dict(node_list):
    
    lattice_pos = {}
    
    for nodes in node_list:
        lattice_pos[nodes[0]] = [nodes[1], nodes[2]]
        
    return lattice_pos

def get_edge_list_tuple(edge_list):
    
    edge_list_tuple = []
    for edges in edge_list:
        edge_list_tuple.append(tuple(edges))
        
    return edge_list_tuple

def construct_Lattice_object(node_list, edge_list):

    graph = rx.PyGraph(multigraph=False)
    graph.add_nodes_from(range(get_num_sites(node_list)))

    # Generate graph from the list of edges
    graph.add_edges_from(get_edge_list_tuple(edge_list))

    # Make a Lattice from graph
    kagome_unit_cell = Lattice(graph)

    return kagome_unit_cell
