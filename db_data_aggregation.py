import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("db.csv")

# Calculate total sales per customer
df["Sales"] = df["Product Price"] * df["Quantity Ordered"]
total_sales_per_customer = df.groupby("Customer Name").agg({"Sales": "sum"})

# Calculate total sales per product
total_sales_per_product = df.groupby("Product Name").agg({"Sales": "sum"})

# Calculate total sales per year
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
total_sales_per_year = df.groupby("Year").agg({"Sales": "sum"})

# Calculate average order value per customer
average_order_value = df.groupby("Customer Name").agg({"Sales": "mean"})

# Find the most popular product
most_popular_product = df.groupby("Product Name").agg({"Quantity Ordered": "sum"}).sort_values("Quantity Ordered", ascending=False).head(1)

print(total_sales_per_customer)
print("-"*20)
print(total_sales_per_product)
print("-"*20)
print(total_sales_per_year)