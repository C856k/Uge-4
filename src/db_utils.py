import mysql.connector
import csv
from db_config import db_config

def create_connection():
    return mysql.connector.connect(
        
        host = db_config['host'],
        user = db_config['user'],
        passwd = db_config['passwd'],
        database = db_config['db']
    )

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
    # Opretter forbindelse til databasen
    connection = create_connection()
    cursor = connection.cursor()
    
    # Åbner CSV-filen og læser indholdet
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        # Itererer over hver række i CSV-filen
        for row in csv_reader:
            # Indsætter rækken i den rigtige tabel
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
    # Committer ændringerne til databasen
    connection.commit()
    
    # Lukker cursor og forbindelsen
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