# Plot a mandelbrot set using matplotlib
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

def display(xmin,xmax,ymin,ymax,width,height,max_iter):
    d = mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    plt.imshow(d[2], extent=(xmin, xmax, ymin, ymax))
    plt.show()

if __name__ == '__main__':
    display(-2.0,0.5,-1.25,1.25,800,800,256)    
    display(-0.74877, -0.74872, 0.06505, 0.06510, 800, 800, 256)
    display(-0.743643887037158704752191506114774, -0.743643887035151680835750303218269, 0.131825904205311970493132056385139, 0.131825904207318994409573259281644, 800, 800, 256)
    display(-0.743643135, -0.743642635, 0.131825910, 0.131826410, 800, 800, 256)