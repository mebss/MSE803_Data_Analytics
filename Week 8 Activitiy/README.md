# Data Cleaning and Outlier Detection

## Project Overview
This project focuses on loading a dataset, performing data cleaning, and detecting outliers using Python.  
The script also analyzes whether missing `society` values can be predicted based on `site_location`.  
The dataset contains real estate data, and the script ensures that missing values, duplicate entries, and outliers are identified and handled appropriately.

---

## 1. Requirements
### **Software & Environment**
- Python 3.x
- PyCharm (or any Python IDE)
- Required Libraries:
  - `pandas`
  - `matplotlib`

### **Installation**
To install the required libraries, run:
```bash
pip install pandas matplotlib
```

---

## 2. Steps Performed in the Script

### **Step 1: Load the Data**
- Reads the dataset from a CSV file.
- Displays the first few rows to get an overview.

### **Step 2: Data Cleaning**
- **Check for Null Values:**  
  - Identifies missing values in each column **before** and **after** cleaning.
  - Fills missing values based on data type:
    - Categorical columns (`society`, `site_location`): Filled with `"Unknown"`.
    - Numerical columns (`bath`, `balcony`): Filled with the **median** value.
    - Essential columns (`size`): Rows with missing values are **removed**.

- **Check for Duplicate Entries:**  
  - **Displays duplicate counts before and after cleaning.**
  - **Removes all but the first occurrence of a duplicate row** using `drop_duplicates()`.

### **Step 3: Outlier Detection**
- **Visualizing Outliers:**  
  - **Generates boxplots** for numerical columns (`bath`, `balcony`, `price`) to **identify outliers**.
- **Using IQR (Interquartile Range) Method:**  
  - Computes **Q1 (25th percentile) and Q3 (75th percentile)**.
  - Any data points beyond **1.5 times the IQR** from Q1 and Q3 are considered outliers.
  - **Counts the number of outliers in each column and prints the results.**

### **Step 4: `society` Prediction Analysis**
- The script checks whether missing `society` values can be **inferred from `site_location`**.
- **Findings:**
  - **96 out of 97 `site_location` values contain multiple societies.**
  - **Only 1 `site_location` has a single society.**
  - ❌ **Conclusion:** Predicting `society` from `site_location` is **NOT reliable**.
  - ✅ **Decision:** Missing `society` values are filled with `"Unknown"`.

---

## 3. How to Run the Script

1. Ensure **Python 3.x** is installed.
2. Install dependencies using:
   ```bash
   pip install pandas matplotlib
   ```
3. Place the dataset (`House_Data.csv`) in the same directory as the script.
4. Open the script in **PyCharm** (or any preferred Python environment).
5. Run the script.

---

## 4. Expected Output
- **Summary of missing values before and after cleaning.**
- **Number of duplicate rows before and after removal.**
- **Boxplots for outlier detection.**
- **Count of outliers detected in `bath`, `balcony`, and `price`.**
- **Results of `society` prediction analysis.**
  - Shows whether `society` can be inferred from `site_location`.

---

## 5. Future Improvements
- Instead of removing outliers, implement **capping techniques**.
- Use **machine learning models** to predict missing values instead of filling with median values.
- Automate feature engineering to handle `size` and `total_sqft` more effectively.
- Use **statistical tests** to analyze relationships between features.

---

## 6. Troubleshooting
### **Common Issues & Fixes**
1. **ModuleNotFoundError: No module named ‘pandas’ or ‘matplotlib’**  
   - Ensure you installed dependencies with:
     ```bash
     pip install pandas matplotlib
     ```

2. **FileNotFoundError: No such file or directory ‘House_Data.csv’**  
   - Ensure the dataset is in the same directory as the script.

3. **Warnings About Future Pandas Changes**  
   - This script is updated for **Pandas 3.0** compatibility, so there should be no warnings.

---

### **Author**
**Mehrab Bhuiyan** 🚀  
This script provides a structured approach to **data cleaning, outlier detection, and exploratory data analysis** for real estate data. 🎯
