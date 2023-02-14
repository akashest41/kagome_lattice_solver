#import relevant packages
from kagome_lattice_construct import *
from hamiltonian_solver import *
from anderson_bound import *
import numpy as np

#define the main function
def main():
    for patch_index in np.arange(1):
    	node_list, edge_list = kagome_raw_lattice_construct(1+patch_index,2,2+patch_index,2,2+patch_index,2,1+patch_index,2)
    	vqe_estimate = -3
    	node_list, edge_list = kagome_raw_lattice_reduce(node_list, edge_list)
    	lattice_obj = construct_Lattice_object(node_list, edge_list)
    	ham = construct_ham(lattice_obj)
    	gs_energy = compute_ground_state_energy(ham)
    	anderson_bound = compute_anderson_bound(vqe_estimate,1+patch_index,2,2+patch_index,2,2+patch_index,2,1+patch_index,2)
    	print("Computed ground state energy for Patch", patch_index+1, "is: ", gs_energy)
    	print("Estimated Anderson Bound for Patch", patch_index+1, "is: ", anderson_bound)

#run the main function
if __name__== '__main__':
    main()
