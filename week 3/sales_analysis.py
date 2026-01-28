# Week 3 - Sales Data Analysis
# Intern: Deven Nirmal

import pandas as pd

# -------------------------------
# Step 1: Load Dataset
# -------------------------------
df = pd.read_csv(r"D:\D drive\Internship\Developer arena\week 3\sales_data.csv")

print("First 5 rows of dataset:")
print(df.head())

# -------------------------------
# Step 2: Explore Data
# -------------------------------
print("\nDataset Information:")
print(df.info())

print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# -------------------------------
# Step 3: Data Cleaning
# -------------------------------

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing Quantity with mean
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

# Fill missing Total_Sales using Quantity * Price
df['Total_Sales'] = df['Quantity'] * df['Price']

# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# -------------------------------
# Step 4: Sales Analysis
# -------------------------------

total_revenue = df['Total_Sales'].sum()
average_sale = df['Total_Sales'].mean()
highest_sale = df['Total_Sales'].max()

best_selling_product = (
    df.groupby('Product')['Total_Sales']
    .sum()
    .idxmax()
)

print("\n--- Sales Analysis Results ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{average_sale:,.2f}")
print(f"Highest Single Sale: ₹{highest_sale:,.2f}")
print(f"Best Selling Product: {best_selling_product}")

# -------------------------------
# Step 5: Save Cleaned Data
# -------------------------------
df.to_csv("cleaned_sales_data.csv", index=False)
print("\nCleaned data saved as cleaned_sales_data.csv")
