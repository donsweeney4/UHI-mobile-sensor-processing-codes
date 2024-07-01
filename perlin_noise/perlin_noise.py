import noise
import numpy as np
import matplotlib.pyplot as plt

# Define the size of the image
width = 100
height = 100

# Define the scale 
scale = 0.1

# Create an empty image
image = np.zeros((width, height))

# Fill the image with Perlin noise
for x in range(width):
    for y in range(height):
        image[x][y] = noise.pnoise2(x*scale, 
                                     y*scale, 
                                     octaves=6, 
                                     persistence=0.5, 
                                     lacunarity=2.0, 
                                     repeatx=1024, 
                                     repeaty=1024, 
                                     base=0)

# Display the image
plt.imshow(image, cmap='gray')
plt.show()