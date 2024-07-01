import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.interpolate import griddata



# Define a function to split a string into latitude, longitude, and temperature
def split_line(line):
    match = re.match(r'\s*\((.*), (.*)\)\s*,\s*(.*)\s*', line)   
    if match is not None:
        return match.groups()
    else:
        return pd.NA, pd.NA, pd.NA

# Apply the function to each line in the DataFrame
# Read the .csv file into a DataFrame

df = pd.read_csv('sample_points.csv', header=None)

# Use a regular expression to split the column into three parts
df = df[0].str.extract(r'\((.*), (.*)\),(.*)')





# Rename the columns
df.columns = ['Latitude', 'Longitude', 'Temperature']

# Convert the columns to the correct data types
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Temperature'] = df['Temperature'].astype(float)
print(df)

# Now you can access the temperatures with df['Temperature']
temperatures = df['Temperature']
latitudes = df['Latitude']  
longitudes = df['Longitude']    

#print(latitudes)
#print(longitudes)
#print (temperatures)




# Create a grid of points to interpolate the temperature data onto
grid_lat, grid_long = np.mgrid[min(latitudes):max(latitudes):100j, min(longitudes):max(longitudes):100j]

# Use scipy's griddata function to interpolate the temperature data
grid_temp = griddata((latitudes, longitudes), temperatures, (grid_lat, grid_long), method='cubic')

# Use matplotlib to create a contour plot of the interpolated temperature data
plt.contourf(grid_lat, grid_long, grid_temp, levels=15, cmap='RdYlBu_r')


# Display the plot
plt.show()