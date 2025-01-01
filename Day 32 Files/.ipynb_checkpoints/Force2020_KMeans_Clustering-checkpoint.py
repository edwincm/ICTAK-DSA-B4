
# Force2020 Data Analysis

## Step 1: Load and Explore the Data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('force2020_data.csv')

# Display the first few rows of the dataset
print("Dataset Head:")
print(data.head())

# Basic information about the dataset
print("Dataset Info:")
print(data.info())

# Summary statistics
print("Dataset Description:")
print(data.describe())

## Step 2: K-Means Clustering

# Standardizing the data for better clustering results
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.select_dtypes(include='number'))

# Applying K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Adding cluster labels to the original dataset
data['Cluster'] = clusters

# Visualizing the clusters
plt.figure(figsize=(8, 6))
plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=clusters, cmap='viridis', s=50)
plt.title('K-Means Clustering (K=3)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()

## Step 3: Experimenting with Different K Values

# Determine the optimal number of clusters using the Elbow Method
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow Curve
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker='o')
plt.title('Elbow Curve')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.show()

# Interpret the Elbow Curve and decide the optimal K (e.g., 3 or 4)

## Step 4: Uploading to GitHub
# After completing this notebook, save it and upload it to your GitHub repository.
# Provide the GitHub link to submit the project.
