import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Basic Information
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Convert Date Columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# KPIs
print("\n" + "=" * 50)
print("KEY METRICS")
print("=" * 50)

print("Total Sales :", round(df['Sales'].sum(), 2))
print("Total Profit :", round(df['Profit'].sum(), 2))
print("Total Orders :", df['Order ID'].nunique())

# Sales by Region
sales_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

print("\nSales by Region:")
print(sales_region)

# Profit by Region
profit_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

print("\nProfit by Region:")
print(profit_region)

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products:")
print(top_products)

# Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# ---------------- Charts ----------------

# Sales by Region
plt.figure(figsize=(8, 5))
sales_region.plot(kind='bar')
plt.title('Sales by Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Profit by Region
plt.figure(figsize=(8, 5))
profit_region.plot(kind='bar')
plt.title('Profit by Region')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

# Monthly Sales Trend
plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Top Products
plt.figure(figsize=(12, 5))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Sales')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

print("\nAnalysis Completed Successfully!")