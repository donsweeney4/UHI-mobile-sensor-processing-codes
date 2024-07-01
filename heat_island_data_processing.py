# Constants for the center point and the range of temperatures - Livermore, CA
##CENTER_LAT = 37.6581
CENTER_LONG = -121.8040
#37.6581558","-121.8040354
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import csv

# Load data from CSV file corrected for column order
def load_data_from_csv(filename):
    longitudes = []
    latitudes = []
    temperatures = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                # Adjusting to the correct column order
                if(float(row[1])< 37.662):
                    latitude, longitude, temperature = float(row[2]), float(row[1]), float(row[3])
                    longitudes.append(longitude)
                    latitudes.append(latitude)
                    temperatures.append(temperature)
            except ValueError:
                # Skip rows with invalid data
                continue
    return longitudes, latitudes, temperatures

# Main function to generate plots
def main():
    print("Heat Islands 2")
    filename = 'data.csv'  # Update with the path to your actual data file
    longitudes, latitudes, temperatures = load_data_from_csv(filename)

    # Create a scatter plot of the latitude and longitude data
    print("Generate scatter plot")
    plt.figure(1)
    plt.scatter(longitudes, latitudes, c=temperatures, cmap='RdYlBu')
    plt.colorbar(label='Temperature (°C)')
    plt.show()

    # Create a grid of points to interpolate the temperature data onto
    plt.figure(2)
    grid_long, grid_lat = np.mgrid[min(longitudes):max(longitudes):200j, min(latitudes):max(latitudes):200j]

    # Use scipy's griddata function to interpolate the temperature data
    grid_temp = griddata((longitudes, latitudes), temperatures, (grid_long, grid_lat), method='cubic')

    # Use matplotlib to create a contour plot of the interpolated temperature data
    plt.contourf(grid_long, grid_lat, grid_temp, levels=15, cmap='RdYlBu')
    plt.colorbar(label='Temperature (°C)')

    # Display the plot
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()