import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset for assignment 2.csv")

# Ensure the column names match exactly those in your CSV file.
# For example, if your columns are "User ID", "Gender", "Age", "Activity Level",
# "Location", "App Sessions", "Distance Traveled (km)", and "Calories Burned", then:
print(df.head())  # Check the data

# 1. Generate the histogram for App Sessions
plt.figure(figsize=(8, 6))
plt.hist(df["App Sessions"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of App Sessions")
plt.xlabel("Number of App Sessions")
plt.ylabel("Frequency")
plt.savefig("app_sessions_histogram.png", dpi=300)
plt.show()

# 2. Generate the scatter plot for Distance Traveled vs Calories Burned
plt.figure(figsize=(8, 6))
plt.scatter(df["Distance Traveled (km)"], df["Calories Burned"], color="salmon", edgecolor="black")
plt.title("Distance Traveled vs. Calories Burned")
plt.xlabel("Distance Traveled (km)")
plt.ylabel("Calories Burned")
plt.savefig("scatter_distance_calories.png", dpi=300)
plt.show()
