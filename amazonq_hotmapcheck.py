import matplotlib.pyplot as plt
import numpy as np
# Test hot colormap
data = np.array([[0, 25, 50], [75, 100, 100]])
plt.imshow(data, cmap='hot')
plt.colorbar()
plt.title('Hot colormap: 0=dark, 100=bright')
plt.show()
print('0 (low) = dark/black')
print('100 (high) = bright/white')