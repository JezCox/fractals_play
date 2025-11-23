"""Burning Ship Fractal - Like Mandelbrot but with absolute values"""
import numpy as np
import matplotlib.pyplot as plt

def burning_ship(xmin=-2.5, xmax=1.5, ymin=-2, ymax=2, width=800, height=800, max_iter=100):
    """Burning Ship: z = (|Re(z)| + i|Im(z)|)² + c"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    Z = np.zeros_like(C)
    iterations = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        # Key difference: take absolute value of real and imaginary parts
        Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag))**2 + C[mask]
        iterations[mask] = i
    
    return iterations

def plot_burning_ship():
    result = burning_ship(max_iter=100)
    
    plt.figure(figsize=(12, 10))
    plt.imshow(result, extent=[-2.5, 1.5, -2, 2], cmap='hot', origin='lower')
    plt.colorbar(label='Iterations to escape')
    plt.title('Burning Ship Fractal')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == '__main__':
    plot_burning_ship()