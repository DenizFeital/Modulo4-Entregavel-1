import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your first dataset (farm_dataset.csv)
df1 = pd.read_csv('farm_dataset_original.csv')

# Load your second dataset (farm_dataset1.csv)
df2 = pd.read_csv('farm_dataset_updated.csv')

# Check the first few rows
print("Dataset 1:")
print(df1.head())
print("\nDataset 2:")
print(df2.head())

# Create the first seaborn 
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.regplot(x='temperature', y='duration', data=df1, scatter_kws={'color':'blue', 'alpha':0.6}, line_kws={'color':'red'}, ci=None)

# Adding labels and title for the first plot
plt.xlabel('Temperatura (°C)')
plt.ylabel('Duração (Minutos)')
plt.title('Relação entre temperatura e duração da irrigação (Dataset original)')

# Display the first plot
plt.show()

# Create the second seaborn
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.regplot(x='temperature', y='duration', data=df2, scatter_kws={'color':'green', 'alpha':0.6}, line_kws={'color':'orange'}, ci=None)

# Adding labels and title for the second plot
plt.xlabel('Temperatura (°C)')
plt.ylabel('Duração (Minutos)')
plt.title('Relação entre temperatura e duração da irrigação (Dataset ajustado)')

# Display the second plot
plt.show()