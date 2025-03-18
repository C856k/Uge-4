import mysql.connector
from db_utils import create_connection

def create_order(order):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO orders (id, date_time, customer_name, customer_email, product_name, product_price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (order['id'], order['date_time'], order['customer_name'], order['customer_email'], order['product_name'], order['product_price']))
    connection.commit()
    cursor.close()
    connection.close()

def read_orders():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_order(order_id, updated_order):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE orders
        SET date_time = %s, customer_name = %s, customer_email = %s, product_name = %s, product_price = %s
        WHERE id = %s
    """, (updated_order['date_time'], updated_order['customer_name'], updated_order['customer_email'], updated_order['product_name'], updated_order['product_price'], order_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_order(order_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    connection.commit()
    cursor.close()
    connection.close()