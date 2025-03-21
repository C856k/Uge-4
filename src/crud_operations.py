import mysql.connector
import csv
from db_config import db_config

# Opretter forbindelse til databasen ved hjælp af konfigurationsvariablerne
def create_connection():
    return mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        passwd = db_config['passwd'],
        db = db_config['db']
    )

# Opretter databasen hvis ikke den eksisterer
def create_database():
    connection = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        passwd = db_config['passwd']
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS orders_db")
    cursor.close()
    connection.close()

# Opretter tabellerne i databasen
def create_tables():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(255),
            email VARCHAR(255)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY,
            product_name VARCHAR(255),
            price FLOAT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            date_time TIMESTAMP,
            customer_id INT,
            product_id INT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)
    
    cursor.close()
    connection.close()

def insert_data_from_csv(csv_file_path, table_name):
    connection = create_connection()
    cursor = connection.cursor()
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if table_name == 'customers':
                cursor.execute("""
                    INSERT INTO customers (customer_id, customer_name, email)
                    VALUES (%s, %s, %s)
                """, (row['id'], row['name'], row['email']))
            elif table_name == 'products':
                cursor.execute("""
                    INSERT INTO products (product_id, product_name, price)
                    VALUES (%s, %s, %s)
                """, (row['id'], row['name'], row['price']))
            elif table_name == 'orders':
                cursor.execute("""
                    INSERT INTO orders (order_id, date_time, customer_id, product_id)
                    VALUES (%s, %s, %s, %s)
                """, (row['id'], row['date_time'], row['customer'], row['product']))
    connection.commit()
    cursor.close()
    connection.close()

def drop_database():
    connection = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        passwd = db_config['passwd']
    )
    cursor = connection.cursor()
    cursor.execute("DROP DATABASE IF EXISTS orders_db")
    cursor.close()
    connection.close()

# CRUD operationer

# Læser data fra en tabel
def read_data(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

# Opdaterer en række i en tabel
def update_data(table_name, column_value, condition):
    connection = create_connection()
    cursor = connection.cursor()
    set_clause = ', '.join([f"{col} = %s" for col in column_value.keys()])
    sql = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    cursor.execute(sql, list(column_value.values()))
    connection.commit()
    cursor.close()
    connection.close()

# Sletter en række fra en tabel
def delete_data(table_name, condition):
    connection = create_connection()
    cursor = connection.cursor()
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()