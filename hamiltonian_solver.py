import numpy as np

import rustworkx as rx

from qiskit_nature.problems.second_quantization.lattice import Lattice

# Custom Heisenberg couplings
from heisenberg_model import HeisenbergModel

from qiskit_nature.mappers.second_quantization import LogarithmicMapper

from qiskit.algorithms import NumPyEigensolver

def construct_ham(lattice_obj):
    heis = HeisenbergModel.uniform_parameters(
    lattice=lattice_obj,
    uniform_interaction=1.0,  # same spin-spin interaction weight as used in graph
    uniform_onsite_potential=0.0,  # No single site external field
    )
    
    log_mapper = LogarithmicMapper()
    
    ham = 4 * log_mapper.map(heis.second_q_ops().simplify())
    
    return ham

def compute_ground_state_energy(ham):
    exact_solver = NumPyEigensolver(k=3)
    exact_result = exact_solver.compute_eigenvalues(ham)
    
    gs_energy = np.round(exact_result.eigenvalues[0], 4)
    
    return gs_energy
