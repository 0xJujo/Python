from sklearn.cluster import KMeans
import numpy as np
# Generating some random data for clustering
np.random.seed(0)
X = np.random.rand(100, 2)
# Define the number of clusters (K)
k = 3
# Initialize the KMeans object
kmeans = KMeans(n_clusters=k)
# Fit the KMeans model to the data
kmeans.fit(X)
# Get the cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
# Print the cluster labels and centroids
print("Cluster Labels:")
print(labels)
print("\nCentroids:")
print(centroids)