import pandas as pd


df = pd.read_csv('weather.csv')  # Load the weather data from a CSV file

#basic overview of the DataFrame

print("DataFrame Overview:")
print(df.head())

#basic sample of the DataFrame
print("\nDataFrame Sample:")
print(df.sample(10))  # Display a random sample of 10 rows from the DataFrame

# Display the shape of the DataFrame
print("\nDataFrame Shape:")
print(df.shape)

# Display summary statistics
print("\nDataFrame Summary Statistics:")
print(df.describe())

# missing values in the DataFrame
print("\nMissing Values in DataFrame:")
print(df.isnull().sum())