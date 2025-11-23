"""Animated Julia Set - c parameter changes"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set(c_param, xmin=-2, xmax=2, ymin=-2, ymax=2, width=400, height=400, max_iter=50):
    """Generate Julia set for given c parameter"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    iterations = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c_param
        iterations[mask] = i
    
    return iterations

def animate_julia_circle():
    """Animate Julia set as c moves around a circle"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Initial plot
    c = 0.7885 * np.exp(1j * 0)
    initial_data = julia_set(c)
    im = ax.imshow(initial_data, extent=[-2, 2, -2, 2], cmap='hot', origin='lower')
    ax.set_title(f'Julia Set Animation: c = {c:.3f}')
    
    def animate(frame):
        # Move c around a circle
        angle = frame * 0.1
        c = 0.7885 * np.exp(1j * angle)
        
        data = julia_set(c)
        im.set_array(data)
        ax.set_title(f'Julia Set: c = {c:.3f}')
        return [im]
    
    anim = animation.FuncAnimation(fig, animate, frames=63, interval=100, blit=True, repeat=True)
    plt.show()
    return anim

def animate_julia_line():
    """Animate Julia set as c moves along a line"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    c = -0.8 + 0j
    initial_data = julia_set(c)
    im = ax.imshow(initial_data, extent=[-2, 2, -2, 2], cmap='hot', origin='lower')
    ax.set_title(f'Julia Set: c = {c:.3f}')
    
    def animate(frame):
        # Move c along real axis
        t = frame / 50.0
        c = -0.8 + 0.6 * t + 0.6j * np.sin(t * 3)
        
        data = julia_set(c)
        im.set_array(data)
        ax.set_title(f'Julia Set: c = {c:.3f}')
        return [im]
    
    anim = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True, repeat=True)
    plt.show()
    return anim

if __name__ == '__main__':
    
    # First animation - circular motion
    anim1 = animate_julia_circle()
    
    # Second animation - complex path
    anim2 = animate_julia_line()