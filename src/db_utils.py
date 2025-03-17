import mysql.connector
import csv

def create_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Velkommen25",
        database = "orders_db"
    )

def create_database():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Velkommen25"
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS orders_db")
    cursor.close()
    connection.close()

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT PRIMARY KEY,
            date_time VARCHAR(255),
            customer_name VARCHAR(255),
            customer_email VARCHAR(255),
            product_name VARCHAR(255),
            product_price FLOAT
        )
    """)
    cursor.close()
    connection.close()

def insert_data_from_csv(csv_file_path):
    connection = create_connection()
    cursor = connection.cursor()
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cursor.execute("""
                INSERT INTO orders (id, date_time, customer_name, customer_email, product_name, product_price)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row['id'], row['date_time'], row['customer_name'], row['customer_email'], row['product_name'], row['product_price']))
    connection.commit()
    cursor.close()
    connection.close()

def drop_database():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Velkommen25"
    )
    cursor = connection.cursor()
    cursor.execute("DROP DATABASE IF EXISTS orders_db")
    cursor.close()
    connection.close()