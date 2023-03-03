# pythonDatabaseTasksGoogleCloud
Python FastAPI DB tasks for a data engineering task.
This code is creating a SQLite database using Python's sqlite3 library. It starts by reading a CSV file named "db.csv" using pandas' read_csv method and storing the data in a data frame called df. Then, it creates a database connection using sqlite3.connect("database.db") and sets up a cursor to execute SQL commands.
The code creates four tables in the SQLite database: "customer_numbers", "orders", "products", and "all_data". The first three tables represent customers, orders, and products and establish relationships between them. The "all_data" table is a combination of all the columns from the other three tables. The code creates these tables using cursor.execute method and executes the SQL commands to create the tables.
It's important to note that the code only creates the tables but doesn't insert any data into them.
