import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Load data from your CSV file
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows of your dataset to make sure it has the correct structure
print(df.head())

# Feature columns for clustering
X = df[['humidity', 'temperature', 'duration']]  # Example feature columns

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Plotting the 2D scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['temperature'], c=df['cluster'], cmap='viridis')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.title('2D K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()

# Plotting the 3D scatter plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df['humidity'], df['temperature'], df['duration'], c=df['cluster'], cmap='viridis')

ax.set_xlabel('Humidity')
ax.set_ylabel('Temperature')
ax.set_zlabel('Duration')
ax.set_title('3D K-means Clustering')
plt.colorbar(scatter, label='Cluster')
plt.show()

# Cluster Centers (centroids of the clusters)
print("Cluster centers (centroids):")
print(kmeans.cluster_centers_)

# Optionally, inspect the first few rows of the dataframe with the cluster assignments
print("\nData with cluster assignments:")
print(df.head())

# Example of cluster interpretation (optional):
# You can analyze the centroids to understand each cluster better
# For instance, cluster 0 might have a low humidity, moderate temperature, and short duration
print("\nCluster interpretation:")
for i in range(kmeans.n_clusters):
    cluster_data = df[df['cluster'] == i]
    print(f"Cluster {i} - Humidity: {cluster_data['humidity'].mean():.2f}, "
          f"Temperature: {cluster_data['temperature'].mean():.2f}, "
          f"Duration: {cluster_data['duration'].mean():.2f}")

