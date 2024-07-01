#   key = AIzaSyAMwa7r_cM3NeLufVtd6xR4UlIsCv93h24
import pandas as pd
import matplotlib.pyplot as plt
import re
import ast

# Read the .csv file into a DataFrame
df = pd.read_csv('sample_points.csv', header=None)

# Split the DataFrame into two series
latitudes = df[0]
print(df[0].dtype)
print(latitudes)
longitudes = df[1]
print(df[1].dtype)
print(longitudes    )

# Create a scatter plot of the latitude and longitude data
plt.scatter(latitudes, longitudes, color='red')

# Display the plot
plt.show()