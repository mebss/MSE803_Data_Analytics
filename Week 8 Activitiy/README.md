# Data Cleaning and Outlier Detection

## Project Overview
This project focuses on loading a dataset, performing data cleaning, and detecting outliers using Python. The dataset contains real estate data, and the script ensures that missing values, duplicate entries, and outliers are identified and handled appropriately.

---

## 1. Requirements
### Software & Environment
- Python 3.x
- PyCharm (or any Python IDE)
- Required Libraries:
  - `pandas`
  - `matplotlib`

To install the required libraries, run:
```bash
pip install pandas matplotlib
```

---

## 2. Steps Performed in the Script
### Step 1: Load the Data
- Reads the dataset from a CSV file.
- Displays the first few rows to get an overview.

### Step 2: Data Cleaning
- **Check for Null Values:**  
  - Identifies missing values in each column.
  - Fills missing values based on data type:
    - Categorical columns (`society`, `site_location`): Filled with `"Unknown"`.
    - Numerical columns (`bath`, `balcony`): Filled with the **median** value.
    - Essential columns (`size`): Rows with missing values are **removed**.

- **Check for Duplicate Entries:**  
  - Removes duplicate rows using `drop_duplicates()`.

### Step 3: Outlier Detection
- **Visualizing Outliers:**  
  - Boxplots are generated for numerical columns (`bath`, `balcony`, `price`).
- **Using IQR (Interquartile Range) Method:**  
  - Outliers are detected by computing the **Q1 (25th percentile) and Q3 (75th percentile)**.
  - Any data points beyond **1.5 times the IQR** from Q1 and Q3 are considered outliers.
  - Counts of detected outliers are printed.

---

## 3. How to Run the Script
1. Place the dataset (`House_Data.csv`) in the same directory as the script.
2. Open the script in **PyCharm** (or any preferred Python environment).
3. Run the script.

---

## 4. Expected Output
- Summary of missing values.
- Number of duplicate rows found and removed.
- Boxplots for outlier detection.
- Count of outliers detected in `bath`, `balcony`, and `price`.

---

## 5. Future Improvements
- Instead of removing outliers, implement **capping techniques**.
- Use **machine learning models** to predict missing values instead of filling with median values.
- Automate feature engineering to handle `size` and `total_sqft` more effectively.

---

### Author
**Mehrab Bhuiyan** 🚀  
This script provides a structured approach to **data cleaning** and **outlier detection** for real estate data analysis. 🎯
