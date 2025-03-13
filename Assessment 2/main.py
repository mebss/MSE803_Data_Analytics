import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Data Loading and Preprocessing
# -----------------------------
# Load the dataset and standardize column names by stripping whitespace
df = pd.read_csv("dataset for assignment 2.csv")
df.columns = df.columns.str.strip()  # Remove extra whitespace

# Print column names to verify
print("Columns in the dataset:", df.columns)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# For simplicity, drop rows with any missing values
df = df.dropna()

# -----------------------------
# Regression Model for Prediction
# -----------------------------
# We use "App Sessions" and "Distance Traveled (km)" to predict "Calories Burned"
X = df[["App Sessions", "Distance Traveled (km)"]]
y = df["Calories Burned"]

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and fit the linear regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = reg_model.predict(X_test)

# Evaluate the regression model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nLinear Regression Model Evaluation:")
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Visualize regression results: Actual vs Predicted Calories Burned
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='black')
plt.xlabel("Actual Calories Burned")
plt.ylabel("Predicted Calories Burned")
plt.title("Actual vs Predicted Calories Burned")

# Plot ideal line
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--')

# Save and show
plt.savefig("actual_vs_predicted_calories_burned.png", dpi=300)
plt.show()

# -----------------------------
# Clustering Analysis
# -----------------------------
# For clustering, we use "App Sessions", "Distance Traveled (km)", and "Calories Burned"
X_cluster = df[["App Sessions", "Distance Traveled (km)", "Calories Burned"]]

# Standardize features for clustering
scaler = StandardScaler()
X_cluster_scaled = scaler.fit_transform(X_cluster)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
K = range(1, 6)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cluster_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,6))
plt.plot(K, inertia, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.savefig("kmeans_elbow_method.png", dpi=300)
plt.show()

# Assume the optimal number of clusters is 2 based on the Elbow plot
optimal_k = 2
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_cluster_scaled)
df["Cluster"] = clusters

# Evaluate clustering using silhouette score (only valid if k > 1)
if optimal_k > 1:
    sil_score = silhouette_score(X_cluster_scaled, clusters)
    print("\nClustering Evaluation:")
    print(f"Silhouette Score for k = {optimal_k}:", sil_score)

# Visualize clusters: Scatter plot of App Sessions vs Calories Burned
plt.figure(figsize=(8,6))
plt.scatter(df["App Sessions"], df["Calories Burned"], c=clusters, cmap='viridis', edgecolor='black')
plt.xlabel("App Sessions")
plt.ylabel("Calories Burned")
plt.title("User Clusters Based on App Sessions and Calories Burned")
plt.savefig("user_clusters_app_sessions_vs_calories.png", dpi=300)
plt.show()
