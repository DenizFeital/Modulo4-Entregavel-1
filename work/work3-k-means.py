import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset (replace the path with your actual file path)
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows of the DataFrame to ensure it's loaded correctly
print(df.head())

# Selecting feature columns for clustering (excluding any non-numeric columns)
X = df[['humidity', 'temperature', 'duration']]  # Features for clustering

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # You can adjust the number of clusters (n_clusters)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Plotting the clusters
plt.figure(figsize=(10, 6))

# Scatter plot for clustering results
plt.scatter(df['humidity'], df['temperature'], c=df['cluster'], cmap='viridis', s=50)
plt.title('K-means Clustering of Humidity and Temperature')
plt.xlabel('Humidity')
plt.ylabel('Temperature')

# Show the plot
plt.colorbar(label='Cluster')
plt.show()
