import mysql.connector
from db_config import db_config 


database = mysql.connector.connect(
    host = db_config['host'],
    user = db_config['user'],
    passwd = db_config['passwd'],
    db = db_config['db']
)

print(database)

database.close()