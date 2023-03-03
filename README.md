# Python FastAPI and SQLite Database Project

In this project, I demonstrate the use of Python's `sqlite3` library to create a SQLite database for a data engineering task.

## Overview

I start by reading data from an Excel file named `db.csv` using the `pandas` library and storing it in a data frame called `df`. Then, I create a database connection using `sqlite3.connect("database.db")` and set up a cursor to execute SQL commands.

I create four tables in the SQLite database: `customer_numbers`, `orders`, `products`, and `all_data`. The first three tables represent customers, orders, and products respectively and establish relationships between them. The `all_data` table is a combination of all columns from the other three tables.

I use SQL commands to define the schema for each table, specifying the column names and data types. I also define foreign key constraints to establish relationships between the tables.

After creating the tables, I insert data into them from the Excel file using SQLite's built-in support for importing CSV files. This allows me to easily populate my database with data from an external source.

## Cloud Hosting

I host this application on a Google Cloud server. To deploy it to the cloud, I follow these steps:

1. Create a new project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the App Engine API and create a new App Engine application.
3. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) on my local machine.
4. Authenticate with my Google Cloud account using `gcloud auth login`.
5. Deploy the application using `gcloud app deploy`.

For more detailed instructions and information on hosting applications on Google Cloud, please refer to their [official documentation](https://cloud.google.com/appengine/docs/standard/python3/building-app).

## Repository

This project is hosted on GitHub at https://github.com/DenislavTonkov/pythonDatabaseTasksGoogleCloud/.
