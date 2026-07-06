## Database Connection Methods

# Method 1: Direct Database Connection (mysql.connector)

This project currently uses a direct MySQL database connection through the mysql-connector-python library.

- Code
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank_app_db"
    )
    return conn

# How it works
- The application imports the mysql.connector library.
- mysql.connector.connect() establishes a connection to the MySQL server using the provided credentials.
- The connection object is returned (conn).

- A **cursor** is an object that acts as an intermediary between your Python program and the database. It is responsible for sending SQL commands to the database and retrieving the results.
- SQL queries are executed using a cursor created from the connection.
- After database operations are completed, the cursor and connection are closed manually.
- Every time the get_connection is called a new connection is made

## Method 2: Streamlit Connection API (st.connection()) 

Streamlit provides a built-in Connection API that simplifies connecting to databases by managing connections internally.

 ## Configuration

Store the database credentials in .streamlit/secrets.toml:

[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "bank_app_db"
username = "root"
password = ""

## Code
import streamlit as st

conn = st.connection("mysql", type="sql")

df = conn.query("SELECT * FROM customers")
st.dataframe(df)

## How it works
- Streamlit reads the database credentials from secrets.toml.
- st.connection() creates a managed database connection.
- Streamlit automatically reuses the connection across app reruns when possible.
- SQL queries can be executed directly using methods such as query().
- Connection management is handled automatically by Streamlit.
- write operations are less straight forward in this.