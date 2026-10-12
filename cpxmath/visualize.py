import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from .symbols import z

def visualize(function, start=-3.14, end=3.14, num_points=20):
    
    mapping_function = sp.lambdify(z, function, 'numpy')

    re_vals = np.linspace(start, end, num_points)
    im_vals = np.linspace(start, end, num_points)

    def grids(re_vals, im_vals):
        num_points = len(re_vals)

        v_grid = np.zeros((num_points, num_points), dtype=complex)
        for v in range(num_points):
            v_grid[v] = re_vals[v] + im_vals * 1j

        h_grid = np.zeros((num_points, num_points), dtype=complex)
        for h in range(num_points):
            h_grid[h] = re_vals + im_vals[h] * 1j

        return v_grid, h_grid

    def mapping_points(mapping_function, v_grid, h_grid):
        w_v = mapping_function(v_grid)
        w_h = mapping_function(h_grid)
        return w_v, w_h

    def plots(function, v_grid, h_grid, w_v, w_h):
        num_points = v_grid.shape[0]

        plt.figure(figsize=(13, 7))

        plt.subplot(1, 2, 1)
        for i in range(num_points):
            plt.plot(v_grid[i].real, v_grid[i].imag)
            plt.plot(h_grid[i].real, h_grid[i].imag)
        plt.title("z-plane (Original)")
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.grid(True)
        plt.axis("equal")

        plt.subplot(1, 2, 2)
        for i in range(num_points):
            plt.plot(w_v[i].real, w_v[i].imag)
            plt.plot(w_h[i].real, w_h[i].imag)
        plt.title(f"w-plane (Mapped: w = {function})")
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.grid(True)
        plt.axis("equal")

        plt.suptitle("Complex Function Mapping", fontsize=14, fontweight="bold")
        plt.tight_layout()
        plt.show()

    v_grid, h_grid = grids(re_vals, im_vals)
    w_v, w_h = mapping_points(mapping_function, v_grid, h_grid)
    plots(function, v_grid, h_grid, w_v, w_h)