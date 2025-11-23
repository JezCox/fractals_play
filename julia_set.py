"""Julia Sets - Mandelbrot's beautiful cousins"""
import numpy as np
import matplotlib.pyplot as plt

def julia_set(c_param, xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=100):
    """Julia set: z = z² + c where c is fixed, z varies"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y  # Starting z values (not c!)
    
    iterations = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c_param  # Fixed c parameter
        iterations[mask] = i
    
    return iterations

def plot_julia(c_param, title_suffix=""):
    """Plot a Julia set for given c parameter"""
    result = julia_set(c_param, max_iter=100)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(result, extent=[-2, 2, -2, 2], cmap='hot', origin='lower')
    plt.colorbar(label='Iterations to escape')
    plt.title(f'Julia Set: c = {c_param} {title_suffix}')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == '__main__':
    # Famous Julia sets
    plot_julia(-0.7269 + 0.1889j, "(Dragon)")
    plot_julia(-0.8 + 0.156j, "(Rabbit)")
    plot_julia(0.285 + 0.01j, "(Cauliflower)")
    plot_julia(-0.4 + 0.6j, "(Lightning)")