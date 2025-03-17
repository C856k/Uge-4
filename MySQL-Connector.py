import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Velkommen25"
)

print(database)

database.close()