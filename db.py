import mysql.connector
from time import sleep


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mysql"  # XAMPP's default database
)

# Example usage:
print("Connection successful!" if conn.is_connected() else "Connection failed.")
conn.close()
sleep(20)

