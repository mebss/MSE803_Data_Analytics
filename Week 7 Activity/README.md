
# Data Cleaning and Analysis with Iris Dataset

This script demonstrates basic data cleaning and exploration using the **Iris dataset** from the `scikit-learn` library. Below is an explanation of the script's functionality and instructions on calculating feature correlations.

---

## Script Overview

### 1. **Loading the Dataset**
The Iris dataset is loaded using `datasets.load_iris()` from `scikit-learn`. This dataset contains measurements of iris flowers, including:
- Sepal length (`sepal_len`)
- Sepal width (`sepal_wid`)
- Petal length (`petal_len`)
- Petal width (`petal_wid`)
- Class (`class`) – target variable representing the flower species.

The data is stored in a Pandas DataFrame for easy manipulation and analysis.

---

### 2. **Analyzing Missing Data**
To identify and analyze missing data:
- **Number of Missing Values:** The script uses `iris_df.isnull().sum()` to count missing values in each column.
- **Mean of Missing Values:** The mean is calculated using `missing_counts.mean()` to provide an overview of missing data across the entire dataset.

**Example Output:**
```plaintext
Number of missing values in each column:
sepal_len    0
sepal_wid    0
petal_len    0
petal_wid    0
class        0

Mean of missing values across all columns:
0.0
```

---

### 3. **Cleaning Data**
The script removes rows with all missing values using:
```python
iris_df.dropna(how="all", inplace=True)
```

---

### 4. **Subset Selection**
A subset of the dataset (first 5 rows and selected columns) is extracted using:
```python
iris_X = iris_df.iloc[:5, [0, 1, 2, 3]]
```
This is useful for previewing and validating the data structure.

---

### 5. **Calculating Feature Correlations**
To analyze relationships between features, you can calculate pairwise correlations using:
```python
correlation_matrix = iris_df.corr()
print(correlation_matrix)
```

This calculates Pearson correlation coefficients between all numerical columns in the dataset.

**Example Correlation Output:**
```plaintext
            sepal_len  sepal_wid  petal_len  petal_wid     class
sepal_len    1.000000  -0.117570   0.871754   0.817941  0.782561
sepal_wid   -0.117570   1.000000  -0.428440  -0.366126 -0.426658
petal_len    0.871754  -0.428440   1.000000   0.962865  0.949035
petal_wid    0.817941  -0.366126   0.962865   1.000000  0.956547
class        0.782561  -0.426658   0.949035   0.956547  1.000000
```

---

## Key Learnings
- **Missing Data Handling:** Identifying and handling missing values ensures data quality for analysis.
- **Correlation Analysis:** Correlation coefficients help understand relationships between numerical features, which is critical for feature engineering and statistical modeling.

---

## Running the Script
To execute the script:
1. Install required libraries: `pandas` and `scikit-learn`.
2. Run the script in a Python environment such as VS Code or Jupyter Notebook.
3. Analyze the output printed in the terminal.

---
