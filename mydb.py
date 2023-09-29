import mysql.connector

database = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = '123456789'
)

obj=database.cursor()

obj.execute("CREATE DATABASE Dashboard")
print("Done")