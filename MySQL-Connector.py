import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def __init__(self, host, database, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(f"Error: '{e}'")
            self.connection = None
    
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print('Disconnected from MySQL database')
    
    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
        return self.connection