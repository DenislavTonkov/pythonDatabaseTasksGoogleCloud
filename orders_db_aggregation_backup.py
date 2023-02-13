import sqlite3
import pandas as pd

# Connect to SQLite database and create 'orders' table
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    CustomerID INTEGER,
    CustomerName TEXT,
    OrderDate TEXT,
    OrderID INTEGER,
    ProductID INTEGER,
    ProductName TEXT,
    ProductPrice REAL,
    QuantityOrdered INTEGER
)
""")
conn.commit()

# Load the data from the CSV file into the database table
data = pd.read_csv("db.csv")
data.to_sql("orders", conn, if_exists="replace", index=False)

# Total sales per customer
total_sales_per_customer = pd.read_sql("""
SELECT 
    CustomerID,
    CustomerName,
    SUM(ProductPrice * QuantityOrdered) AS TotalSales
FROM orders
GROUP BY CustomerID
""", conn)

# Total sales per product
total_sales_per_product = pd.read_sql("""
SELECT 
    ProductID,
    ProductName,
    SUM(ProductPrice * QuantityOrdered) AS TotalSales
FROM orders
GROUP BY ProductID
""", conn)

# Total sales per year
total_sales_per_year = pd.read_sql("""
SELECT 
    strftime('%Y', OrderDate) AS Year,
    SUM(ProductPrice * QuantityOrdered) AS TotalSales
FROM orders
GROUP BY Year
""", conn)

# Average order value per customer
average_order_value_per_customer = pd.read_sql("""
SELECT 
    CustomerID,
    CustomerName,
    AVG(ProductPrice * QuantityOrdered) AS AverageOrderValue
FROM orders
GROUP BY CustomerID
""", conn)

# Most popular product
most_popular_product = pd.read_sql("""
SELECT 
    ProductID,
    ProductName,
    SUM(QuantityOrdered) AS TotalQuantityOrdered
FROM orders
GROUP BY ProductID
ORDER BY TotalQuantityOrdered DESC
LIMIT 1
""", conn)

# Close the database connection
conn.close()

# Print the results
print("Total sales per customer:")
print(total_sales_per_customer)

print("\nTotal sales per product:")
print(total_sales_per_product)

print("\nTotal sales per year:")
print(total_sales_per_year)

print("\nAverage order value per customer:")
print(average_order_value_per_customer)

print("\nMost popular product:")
print(most_popular_product)
