import csv
import sqlite3
import pandas as pd
import pyodbc

csv_db_data = pd.read_csv(r'db.csv')
df = pd.DataFrame(csv_db_data)

# print(df)


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS csv_data (customerNumb INTEGER, orders INTEGER, products TEXT);")

# Create the customer_numbers table
cursor.execute("CREATE TABLE IF NOT EXISTS customer_numbers (id INTEGER PRIMARY KEY, name TEXT);")

# Create the orders table
cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, date TEXT, customer_number_id INTEGER, FOREIGN KEY (customer_number_id) REFERENCES customer_numbers(id));")

# Create the products table
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL);")

# Creating a data of all the columns
cursor.execute("CREATE TABLE IF NOT EXISTS all_data (customer_id INTEGER, customer_name TEXT, order_date TEXT, order_id INTEGER, product_id INTEGER, product_name TEXT, product_price INTEGER, order_quantity INTEGER);")

conn.commit()
conn.close()