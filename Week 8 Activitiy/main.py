import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "House_Data.csv"  # Update with your file path
df = pd.read_csv(file_path)

# Display missing values before cleaning (with percentage)
print("\n🔹 Missing Values (Before Cleaning):")
missing_values = df.isnull().sum()
total_rows = len(df)
missing_percentage = (missing_values / total_rows) * 100

# Print missing values with percentages
missing_summary = pd.DataFrame({"Missing Count": missing_values, "Percentage (%)": missing_percentage})
print(missing_summary)

# Display duplicate count before cleaning
duplicate_count = df.duplicated().sum()
print(f"\n🔹 Duplicate Rows Found (Before Cleaning): {duplicate_count}")

# Data Cleaning
df_cleaned = df.drop_duplicates().copy()  # Remove duplicates and ensure a fresh copy

# Handle missing values safely
df_cleaned.loc[:, 'society'] = df_cleaned['society'].fillna("Unknown")
df_cleaned.loc[:, 'site_location'] = df_cleaned['site_location'].fillna("Unknown")
df_cleaned.loc[:, 'bath'] = df_cleaned['bath'].fillna(df_cleaned['bath'].median())
df_cleaned.loc[:, 'balcony'] = df_cleaned['balcony'].fillna(df_cleaned['balcony'].median())

# Drop rows with missing 'size' values as it is essential
df_cleaned = df_cleaned.dropna(subset=['size'])

# Display missing values after cleaning (with percentage)
print("\n✅ Missing Values (After Cleaning):")
missing_values_after = df_cleaned.isnull().sum()
missing_percentage_after = (missing_values_after / len(df_cleaned)) * 100

# Print cleaned missing values summary
missing_summary_after = pd.DataFrame({"Missing Count": missing_values_after, "Percentage (%)": missing_percentage_after})
print(missing_summary_after)

# Display duplicate count after cleaning
print(f"\n✅ Duplicate Rows Remaining (After Cleaning): {df_cleaned.duplicated().sum()}")

# Checking for Outliers
numerical_columns = ['bath', 'balcony', 'price']

for col in numerical_columns:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df_cleaned[col], vert=False)
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.show()

# Function to detect outliers using IQR method
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

# Detect outliers for each numerical column
outliers_bath = detect_outliers_iqr(df_cleaned, 'bath')
outliers_balcony = detect_outliers_iqr(df_cleaned, 'balcony')
outliers_price = detect_outliers_iqr(df_cleaned, 'price')

# Count the number of outliers detected
outlier_counts = {
    'bath': len(outliers_bath),
    'balcony': len(outliers_balcony),
    'price': len(outliers_price)
}

# Print outlier counts
print("\n📊 Outlier Counts Detected:")
for key, value in outlier_counts.items():
    print(f"   - {key}: {value} outliers")

# Check if society can be predicted from site_location
site_location_unique_society = df.groupby('site_location')['society'].nunique().reset_index()

# Count how many site_locations have only one unique society
single_society_locations = site_location_unique_society[site_location_unique_society['society'] == 1].shape[0]

# Count how many site_locations have multiple societies
multiple_society_locations = site_location_unique_society[site_location_unique_society['society'] > 1].shape[0]

# Print findings
print("\n🔎 Society Prediction Analysis:")
print(f"   - Total Unique Site Locations: {site_location_unique_society.shape[0]}")
print(f"   - Site Locations with a Single Unique Society: {single_society_locations}")
print(f"   - Site Locations with Multiple Societies: {multiple_society_locations}")

# Final Decision on Missing Society
if multiple_society_locations > single_society_locations:
    print("\n❌ Most site locations have multiple societies. Predicting missing 'society' is NOT reliable.")
    print("   ➡️ Keeping missing 'society' as 'Unknown'. ✅")
else:
    print("\n✅ Some site locations are strongly tied to a single society. Prediction may be possible.")
