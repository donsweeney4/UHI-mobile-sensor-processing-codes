import pandas as pd

# Read the .csv file into a DataFrame
df = pd.read_csv('sample_points.csv', header=None)

# Remove parentheses and split the first column into latitude and longitude
df[0] = df[0].str.replace(r'[()]', '')
df[['Latitude', 'Longitude']] = df[0].str.split(', ', expand=True)

# Convert the columns to the correct data types
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Temperature'] = df[1].astype(float)

# Now you can access the temperatures with df['Temperature']
latitude = df['Latitude'].values
longitude = df['Longitude'].values
temperature = df['Temperature'].values

print('Latitude:', latitude)
print('Longitude:', longitude)
print('Temperature:', temperature)



