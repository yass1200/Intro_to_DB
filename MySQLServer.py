# MySQLServer.py

import mysql.connector

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error while connecting to MySQL:", err)

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except:
        pass
