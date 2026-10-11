import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from .symbols import z

def visualize(function, start=-3.14, end=3.14, num_points=25):
    
    mapping_function = sp.lambdify(z, function, 'numpy')

    re_vals = np.linspace(start, end, num_points)
    im_vals = np.linspace(start, end, num_points)

    def grids(re_vals, im_vals):
        num_points = len(re_vals)

        h_grid = np.zeros((num_points, num_points), dtype=complex)
        for h in range(num_points):
            h_grid[h] = re_vals + im_vals[h] * 1j

        v_grid = np.zeros((num_points, num_points), dtype=complex)
        for v in range(num_points):
            v_grid[v] = re_vals[v] + im_vals * 1j

        return h_grid, v_grid