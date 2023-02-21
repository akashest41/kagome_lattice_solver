def compute_anderson_bound(vqe_estimate, cub1_x, cub1_y, cub2_x, cub2_y, cub3_x, cub3_y, cub4_x, cub4_y):
    anderson_bound = vqe_estimate*((cub1_x*cub1_y) + (cub2_x*cub2_y) + (cub3_x*cub3_y) + (cub4_x*cub4_y))
    return anderson_bound
