"""Sierpinski Triangle - Classic geometric fractal"""
import numpy as np
import matplotlib.pyplot as plt

def sierpinski_triangle(iterations=10000):
    """Generate Sierpinski triangle using the chaos game"""
    # Three vertices of an equilateral triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    
    # Start at random point
    point = np.random.random(2)
    points = []
    
    for _ in range(iterations):
        # Pick random vertex
        vertex = vertices[np.random.randint(3)]
        # Move halfway to that vertex
        point = (point + vertex) / 2
        points.append(point.copy())
    
    return np.array(points)

def plot_sierpinski():
    points = sierpinski_triangle(50000)
    
    plt.figure(figsize=(10, 10))
    plt.scatter(points[:, 0], points[:, 1], s=0.1, c='black')
    plt.title('Sierpinski Triangle (Chaos Game)')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

def sierpinski_carpet(size=243, iterations=5):
    """Generate Sierpinski carpet by subdivision"""
    carpet = np.ones((size, size))
    
    def remove_middle_square(arr, x, y, size):
        if size < 3:
            return
        
        third = size // 3
        # Remove middle square
        arr[y + third:y + 2*third, x + third:x + 2*third] = 0
        
        # Recurse on remaining 8 squares
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:  # Skip middle
                    continue
                remove_middle_square(arr, x + i*third, y + j*third, third)
    
    remove_middle_square(carpet, 0, 0, size)
    return carpet

def plot_carpet():
    carpet = sierpinski_carpet()
    
    plt.figure(figsize=(10, 10))
    plt.imshow(carpet, cmap='binary', origin='lower')
    plt.title('Sierpinski Carpet')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    plot_sierpinski()
    plot_carpet()