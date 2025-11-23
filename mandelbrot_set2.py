''' This is Q's effort - rather better to be fair'''
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    """Generate Mandelbrot set using vectorized operations for better performance."""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    Z = np.zeros_like(C)
    iterations = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        iterations[mask] = i
    
    return iterations

def plot_mandelbrot(xmin=-2.0, xmax=0.5, ymin=-1.25, ymax=1.25, 
                   width=800, height=800, max_iter=100, cmap='hot'):
    """Plot Mandelbrot set with customizable parameters."""
    mandelbrot = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot, extent=[xmin, xmax, ymin, ymax], 
               cmap=cmap, origin='lower', interpolation='bilinear')
    plt.colorbar(label='Iterations to divergence')
    plt.title(f'Mandelbrot Set ({width}x{height}, {max_iter} iterations)')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

def main():
    plot_mandelbrot()    
    # Zoomed regions
    # plot_mandelbrot(-0.74877, -0.74872, 0.06505, 0.06510, 800, 800, 256)
    # plot_mandelbrot(-0.7436438870, -0.7436438870, 0.1318259042, 0.1318259042, 800, 800, 512)

if __name__ == '__main__':
    plot_mandelbrot()