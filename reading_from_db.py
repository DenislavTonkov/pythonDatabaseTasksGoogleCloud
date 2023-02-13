import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customer_numbers")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

