import sqlite3
import pandas as pd
from datetime import datetime

# Connect to the database
conn = sqlite3.connect("database.db")

# Read data from the orders table into a pandas DataFrame
orders_df = pd.read_sql_query("SELECT * FROM orders", conn)
print(orders_df)
# Convert the order date column to a datetime type and extract the year
orders_df['Order Date'] = pd.to_datetime(orders_df['Order Date'])
orders_df['Year'] = orders_df['Order Date'].dt.year

# Total sales per customer
total_sales_per_customer = orders_df.groupby('Customer ID')['Total'].sum().reset_index()

# Total sales per product
total_sales_per_product = orders_df.groupby('Product ID')['Total'].sum().reset_index()

# Total sales per year
total_sales_per_year = orders_df.groupby('Year')['Total'].sum().reset_index()

# Average order value per customer
average_order_value = orders_df.groupby('Customer ID')['Total'].mean().reset_index()

# Most popular product
most_popular_product = orders_df.groupby('Product ID')['Quantity Ordered'].sum().reset_index().sort_values(by='Quantity Ordered', ascending=False).head(1)



# import sqlite3
# import pandas as pd
# from datetime import datetime
#
# # Connect to the database
# conn = sqlite3.connect("database.db")
#
# # Read data from the orders table into a pandas DataFrame
# orders_df = pd.read_sql_query("SELECT * FROM orders", conn)
# cursor = conn.cursor()
# cursor.execute("PRAGMA table_info(orders)")
# print(cursor.fetchall())
#
# # Convert the order date column to a datetime type and extract the year
# orders_df['date'] = pd.to_datetime(orders_df['date'])
# orders_df['Year'] = orders_df['date'].dt.year
#
# # Total sales per customer
# total_sales_per_customer = orders_df.groupby('customer_number_id')['Total'].sum().reset_index()
#
# # Total sales per product
# total_sales_per_product = orders_df.groupby('Product ID')['Total'].sum().reset_index()
#
# # Total sales per year
# total_sales_per_year = orders_df.groupby('Year')['Total'].sum().reset_index()
#
# # Average order value per customer
# average_order_value = orders_df.groupby('Customer ID')['Total'].mean().reset_index()
#
# # Most popular product
# most_popular_product = orders_df.groupby('Product ID')['Quantity Ordered'].sum().reset_index().sort_values(by='Quantity Ordered', ascending=False).head(1)
