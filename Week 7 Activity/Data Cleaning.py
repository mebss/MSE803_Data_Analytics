# Import necessary libraries
import pandas as pd
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Since this is a Bunch object, create a DataFrame
iris_df = pd.DataFrame(iris.data)
iris_df['class'] = iris.target

# Set column names
iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

### TASK 1: Find the number and mean of missing data
# Count the number of missing values in each column
missing_counts = iris_df.isnull().sum()
print("Number of missing values in each column:")
print(missing_counts)

# Calculate the mean of missing values across all columns
mean_missing = missing_counts.mean()
print("\nMean of missing values across all columns:")
print(mean_missing)

# Remove any empty lines of data
iris_df.dropna(how="all", inplace=True)

# Extract a subset of the DataFrame (first 5 rows and selected columns)
iris_X = iris_df.iloc[:5, [0, 1, 2, 3]]
print("\nSubset of the data:")
print(iris_X)

### TASK 2: Write a README to explain the above code and calculate correlations
