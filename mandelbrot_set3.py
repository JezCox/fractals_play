"""
Mandelbrot Set - Educational Version
Shows the core logic clearly with step-by-step explanations
"""
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_point(c, max_iter=100):
    """
    Test if a single complex number c is in the Mandelbrot set.
    
    The Mandelbrot set consists of complex numbers c for which
    the sequence z₀=0, z₁=z₀²+c, z₂=z₁²+c, ... stays bounded.
    
    Returns: number of iterations before |z| > 2 (or max_iter if bounded)
    """
    z = complex(0, 0)  # Start with z = 0
    
    for iteration in range(max_iter):
        # Check if z has "escaped" (magnitude > 2 means it will diverge)
        if abs(z) > 2:
            return iteration
        
        # Core Mandelbrot formula: z = z² + c
        z = z * z + c
    
    # If we got here, the point didn't escape - it's in the set
    return max_iter

def create_complex_grid(xmin, xmax, ymin, ymax, width, height):
    """
    Create a grid of complex numbers covering the specified region.
    Each point represents a candidate for the Mandelbrot set.
    """
    # Create arrays of real and imaginary coordinates
    real_coords = np.linspace(xmin, xmax, width)
    imag_coords = np.linspace(ymin, ymax, height)
    
    # Create 2D grids - every combination of real + imaginary
    real_grid, imag_grid = np.meshgrid(real_coords, imag_coords)
    
    # Combine into complex numbers: each point is real + i*imaginary
    complex_grid = real_grid + 1j * imag_grid
    
    print(f"Created {width}x{height} grid of complex numbers")
    print(f"Range: {xmin} to {xmax} (real), {ymin} to {ymax} (imaginary)")
    print(f"Sample points: {complex_grid[0,0]}, {complex_grid[0,-1]}")
    
    return complex_grid

def mandelbrot_set_detailed(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    """
    Generate Mandelbrot set with detailed explanations of each step.
    """
    print("=== Mandelbrot Set Generation ===")
    
    # Step 1: Create the complex plane grid
    complex_plane = create_complex_grid(xmin, xmax, ymin, ymax, width, height)
    
    # Step 2: Initialize result array to store iteration counts
    iterations = np.zeros((height, width), dtype=int)
    
    # Step 3: Test each point in the complex plane
    print(f"Testing {width * height} points...")
    
    for row in range(height):
        for col in range(width):
            # Get the complex number at this grid position
            c = complex_plane[row, col]
            
            # Test how many iterations this point takes to escape
            escape_time = mandelbrot_point(c, max_iter)
            iterations[row, col] = escape_time
        
        # Progress indicator
        if row % (height // 10) == 0:
            print(f"Progress: {100 * row // height}%")
    
    print("Generation complete!")
    return iterations

def plot_mandelbrot_detailed(iterations, xmin, xmax, ymin, ymax, max_iter):
    """
    Plot the Mandelbrot set with detailed labeling.
    """
    plt.figure(figsize=(12, 10))
    
    # Create the plot
    img = plt.imshow(iterations, extent=[xmin, xmax, ymin, ymax], 
                     cmap='hot', origin='lower', interpolation='bilinear')
    
    # Add informative labels
    plt.colorbar(img, label=f'Iterations to escape (max: {max_iter})')
    plt.title('Mandelbrot Set\n(Bright regions are IN the set, dark regions escape quickly)')
    plt.xlabel('Real axis')
    plt.ylabel('Imaginary axis')
    
    # Add some reference points
    plt.axhline(y=0, color='white', linestyle='--', alpha=0.3, linewidth=0.5)
    plt.axvline(x=0, color='white', linestyle='--', alpha=0.3, linewidth=0.5)
    
    plt.tight_layout()
    plt.show()

def demo_single_points():
    """
    Demonstrate the Mandelbrot test on individual complex numbers.
    """
    print("\n=== Testing Individual Points ===")
    
    test_points = [
        complex(0, 0),      # Origin - definitely in set
        complex(-1, 0),     # Real axis - in set
        complex(0.5, 0),    # Real axis - escapes
        complex(-0.5, 0.5), # Upper left - in set
        complex(1, 1),      # Upper right - escapes quickly
    ]
    
    for c in test_points:
        iterations = mandelbrot_point(c, 100)
        status = "IN SET" if iterations == 100 else f"escapes after {iterations} iterations"
        print(f"Point {c}: {status}")

if __name__ == '__main__':
    # First, demonstrate individual point testing
    demo_single_points()
    
    # Generate and plot a small Mandelbrot set for clarity
    print("\nGenerating Mandelbrot set...")
    result = mandelbrot_set_detailed(-2.0, 0.5, -1.25, 1.25, 200, 200, 50)
    plot_mandelbrot_detailed(result, -2.0, 0.5, -1.25, 1.25, 50)