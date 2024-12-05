import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your dataset (replace 'fake_dataset.csv' with the correct path if needed)
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows to ensure the data is loaded correctly
print(df.head())

# Convert 'irrigation_time' to numerical values (assuming it's in HH:MM format, we convert to minutes)
df['irrigation_time_minutes'] = df['irrigation_time'].apply(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1]))

# Create a seaborn scatter plot with a regression line
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.regplot(x='temperature', y='irrigation_time_minutes', data=df, scatter_kws={'color':'blue', 'alpha':0.6}, line_kws={'color':'red'}, ci=None)

# Adding labels and title
plt.xlabel('Temperature (°C)')
plt.ylabel('Irrigation Time (Minutes)')
plt.title('Relationship between Temperature and Irrigation Time')

# Display the plot
plt.show()
