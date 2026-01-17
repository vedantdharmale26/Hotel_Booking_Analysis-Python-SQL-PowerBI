import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

if conn.is_connected():
    print("MySQL connected successfully!")
