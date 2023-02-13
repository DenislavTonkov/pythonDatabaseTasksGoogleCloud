import sqlite3
import sqlite_database
import csv
import pandas as pd
from datetime import datetime

# Fast Api import
from fastapi import FastAPI
#

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Insert the customer data into the customer_numbers table
with open("db.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    customers = {}
    for row in reader:
        customer_id = int(row[0])
        customer_name = row[1]
        if customer_id not in customers:
            cursor.execute("INSERT OR IGNORE INTO customer_numbers (id, name) VALUES (?, ?);",
                           (customer_id, customer_name))
            customers[customer_id] = True

with open("db.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        customer_id = int(row[0])
        order_date = row[2]
        order_id = int(row[3])
        product_name = row[5]
        try:
            cursor.execute("INSERT INTO orders (id, name, date, customer_number_id) VALUES (?, ?, ?, ?);",
                           (order_id, product_name, order_date, customer_id))
        except sqlite3.IntegrityError as e:
            if str(e) == "UNIQUE constraint failed: orders.id":
                print(f"Order with ID {order_id} already exists. Skipping...")
                continue
            else:
                raise e
        # cursor.execute("INSERT INTO orders (id, name, date, customer_number_id) VALUES (?, ?, ?, ?);",
        #                (order_id, product_name, order_date, customer_id))

with open("db.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    products = {}
    for row in reader:
        # print(row)
        product_id = int(row[4])
        product_name = row[5]
        product_price = float(row[6])  # In case it is not a whole num
        if product_id not in products:
            cursor.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (?, ?, ?)",
                           (product_id, product_name, product_price))
            products[product_id] = (product_name, product_price)  # Serves as a flag to indicate that the product with
            # that ID has already been inserted into the table

with open("db.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        # print(row)
        customer_id = int(row[0])
        customer_name = row[1]
        order_date = row[2]
        order_id = int(row[3])
        product_id = int(row[4])
        product_name = row[5]
        product_price = int(row[6])
        order_quantity = int(row[7])
        try:
            cursor.execute(
                "INSERT INTO all_data (customer_id, customer_name, order_date, order_id, product_id, product_name, product_price, order_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (customer_id, customer_name, order_date, order_id, product_id, product_name, product_price, order_quantity))
        except sqlite3.IntegrityError:
            print("Duplicate data found. Skipping...")

        # cursor.execute(
        #     "INSERT INTO all_data (customer_id, customer_name, order_date, order_id, product_id, product_name, product_price, order_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        #     (customer_id, customer_name, order_date, order_id, product_id, product_name, product_price, order_quantity))

# conn.commit()  # VERY IMPORTANT LINE IN ORDER TO COMMIT THE DATA. Otherwise nothing will be stored!!!
# conn.close()

# For testing if the insertion was successful!

# cursor.execute("SELECT * FROM all_data")
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)


# Connect to the database
conn = sqlite3.connect("database.db")

# Read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM all_data", conn)
print(df)


# # Total sales per customer
total_sales_per_customer = df.groupby(['customer_name'])[['product_price', 'order_quantity']].agg({'product_price': 'sum', 'order_quantity': 'sum'})
total_sales_per_customer['total_sales'] = total_sales_per_customer['product_price'] * total_sales_per_customer['order_quantity']
print(total_sales_per_customer)

print("-"*100)

# # Total sales per product
total_sales_per_product = df.groupby(['product_name'])[['product_price', 'order_quantity']].agg({'product_price': 'sum', 'order_quantity': 'sum'})
total_sales_per_product['total_sales'] = total_sales_per_product['product_price'] * total_sales_per_product['order_quantity']
print(total_sales_per_product)

print("-"*100)

# # Total sales per year
df['order_date'] = pd.to_datetime(df['order_date'])
df['year'] = df['order_date'].dt.year
total_sales_per_year = df.groupby(['year'])[['product_price', 'order_quantity']].agg({'product_price': 'sum', 'order_quantity': 'sum'})
total_sales_per_year['total_sales'] = total_sales_per_year['product_price'] * total_sales_per_year['order_quantity']
print(total_sales_per_year)

print("-"*100)

# # Average order value per customer
average_order_value_per_customer = total_sales_per_customer['total_sales'] / total_sales_per_customer['order_quantity']
print(average_order_value_per_customer)

print("-"*100)

# Most popular product
if len(total_sales_per_product) > 0:
    most_popular_product = total_sales_per_product.sort_values(by='total_sales', ascending=False).reset_index().iloc[0, :]
else:
    most_popular_product = None

print(most_popular_product)
