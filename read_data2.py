import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import ast
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
# Print the data types of the columns
print(df.dtypes)

# Convert the string to a tuple
#tuple_data = ast.literal_eval(df[0])
# Print the first element of the tuple

#print(tuple_data[0])





"""  
# Replace the comma inside the parentheses with a space
df[0] = df[0].str.replace(r'(?<=\d),(?=-)', ' ')

# Remove parentheses
df[0] = df[0].str.replace(r'[()]', '')

print(df.dtypes)
print(df[0 ])


"""
# Split the line into three fields
df[['Latitude', 'Longitude', 'Temperature']] = df[0].str.split(expand=True)

print(df)   

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




