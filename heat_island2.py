#   key = AIzaSyAMwa7r_cM3NeLufVtd6xR4UlIsCv93h24
# Constants for the center point and the range of temperatures - Livermore, CA

CENTER_LAT = 37.6819
CENTER_LONG = -121.7680

import random
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.interpolate import griddata



import csv
import math


MIN_TEMP = 15
MAX_TEMP = 25

# Function to generate a random GPS coordinate within 1 km of a given point
def random_gps(center_lat, center_long):
    # Approximate radius of earth in km
    R = 6378.1

    # Convert latitude and longitude from degrees to radians
    lat_rad = center_lat * (3.14159 / 180)
    long_rad = center_long * (3.14159 / 180)

    # Random distance within 1 km
    d = random.random()

    # Random bearing (direction) in radians
    brng = random.random() * (2 * 3.14159)

    # New latitude and longitude in radians
    new_lat = math.asin(math.sin(lat_rad) * math.cos(d/R) + math.cos(lat_rad) * math.sin(d/R) * math.cos(brng))
    new_long = long_rad + math.atan2(math.sin(brng) * math.sin(d/R) * math.cos(lat_rad), math.cos(d/R) - math.sin(lat_rad) * math.sin(new_lat))

    # Convert back to degrees
    new_lat = new_lat * (180 / 3.14159)
    new_long = new_long * (180 / 3.14159)

    return (new_lat, new_long)

# Function to generate a random temperature between 15 and 25 degrees C
def random_temp(min_temp, max_temp):
    return random.uniform(min_temp, max_temp)

# Generate the list of tuples
#data = [(random_gps(CENTER_LAT, CENTER_LONG), random_temp(MIN_TEMP, MAX_TEMP)) for _ in range(1000)]
print("Heat Islands 2")
data = []
longitudes = [] 
latitudes = [] 
temperatures = []    

for ii in range(200):
    coor = random_gps(CENTER_LAT, CENTER_LONG)
    temp = random_temp(MIN_TEMP, MAX_TEMP)
    data.append((coor, temp))
    latitudes.append(coor[0])   
    longitudes.append(coor[1])
    temperatures.append(temp)
    print(ii,latitudes[ii], longitudes[ii], temp)





# Create a scatter plot of the latitude and longitude data
print("Generate scatter plot")
plt.figure(1)
# plot the scatter with longitudes as the x axis
plt.scatter(longitudes,latitudes,  color='red')
# Display the plot
plt.show()


# Create a grid of points to interpolate the temperature data onto - again put the longitudes on the x axis
plt.figure(2)
grid_long,grid_lat = np.mgrid[min(longitudes):max(longitudes):200j, min(latitudes):max(latitudes):200j]

# Use scipy's griddata function to interpolate the temperature data
grid_temp = griddata((longitudes,latitudes), temperatures, (grid_long, grid_lat), method='cubic')

# Use matplotlib to create a contour plot of the interpolated temperature data
plt.contourf(grid_long, grid_lat, grid_temp, levels=15, cmap='RdYlBu')


# Display the plot
# Turn off the axis and remove the title
plt.axis('off')
plt.title('')
plt.show()



# Write the list to a .csv file
#with open('sample_points.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows(data)
