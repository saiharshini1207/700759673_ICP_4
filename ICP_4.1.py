import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data.csv')  # your file path

# Basic statistical description
description = df.describe()

# Check for null values
null_values = df.isnull().sum()

# Replace null values with the mean
df_filled = df.fillna(df.mean())

# Aggregate two columns
aggregated_data = df_filled[['Calories', 'Pulse']].agg(['min', 'max', 'count', 'mean'])

# Filter rows with Calories between 500 and 1000
filtered_500_1000 = df_filled[(df_filled['Calories'] >= 500) & (df_filled['Calories'] <= 1000)]

# Filter rows with Calories > 500 and Pulse < 100
filtered_calories_pulse = df_filled[(df_filled['Calories'] > 500) & (df_filled['Pulse'] < 100)]

# Create new DataFrame without 'Maxpulse'
df_modified = df_filled.drop(columns=['Maxpulse'])

# Delete 'Maxpulse' from original DataFrame
df.drop(columns=['Maxpulse'], inplace=True)

# Convert 'Calories' to integer
df_filled['Calories'] = df_filled['Calories'].astype(int)

# Scatter plot for 'Duration' and 'Calories'
plt.figure(figsize=(10, 7))
plt.scatter(df_filled['Duration'], df_filled['Calories'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Duration vs Calories')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.grid(True)
plt.show()
