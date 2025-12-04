import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
print("CURRENT FOLDER:", os.getcwd())

# Load data
df = pd.read_csv(r"C:\Users\ACER\OneDrive\Desktop\Python_assignment\weather-data-visualizer-amaan\weatherdata.csv")


# Clean data
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
df = df[['date', 'temperature', 'rainfall', 'humidity']]

# Add month column
df['month'] = df['date'].dt.month

# Save cleaned data
df.to_csv("cleaned_weather.csv", index=False)

# Daily temp line chart
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature")
plt.savefig("daily_temp.png")
plt.close()

# Monthly rainfall chart
monthly_rain = df.groupby('month')['rainfall'].sum()
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall")
plt.savefig("rainfall.png")
plt.close()

# Scatter - humidity vs temp
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.savefig("scatter.png")
plt.close()

# Combined plots
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])

plt.subplot(1,2,2)
plt.scatter(df['temperature'], df['humidity'])

plt.savefig("combined.png")
plt.close()
