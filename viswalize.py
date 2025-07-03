import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
# Create a file named 'weather.csv' and paste the provided data into it.
try:
    df = pd.read_csv('weather.csv')
except FileNotFoundError:
    print("Error: 'weather.csv' not found. Please make sure the file is in the same directory.")
    exit()

# --- 1. Data Preparation ---
# Convert 'date' column to datetime objects for proper time-series plots
df['date'] = pd.to_datetime(df['date'])

# Extract month and year 
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

print("Data loaded and prepared. Generating plots...")

# --- 2. Time Series Analysis ---

# Plot 1: Max and Min Temperature Over Time
fig1 = px.line(
    df, 
    x='date', 
    y=['temp_max', 'temp_min'],
    title='Max and Min Temperature Over Time Periods',
    labels={'value': 'Temperature (°C)', 'date': 'Date'},
    color_discrete_map={'temp_max': 'red', 'temp_min': 'green'}
)
fig1.show()




fig2 = px.bar(
    df, 
    x='date', 
    y='precipitation',
    title='Daily Precipitation Over Time',
    labels={'precipitation': 'Precipitation (mm)', 'date': 'Date'},
    color='precipitation',
    color_continuous_scale=px.colors.sequential.Blues
)
fig2.show()

# --- 3. Feature Distributions ---

# Plot 3: Distribution of Weather Types
weather_counts = df['weather'].value_counts().reset_index()
weather_counts.columns = ['weather', 'count']
fig3 = px.bar(
    weather_counts,
    x='weather',
    y='count',
    title='Distribution of Weather Types',
    labels={'count': 'Number of Days', 'weather': 'Weather Condition'},
    color='weather'
)
fig3.show()