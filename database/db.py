import mysql.connector

def db_connection():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_backend"
    )
    return con


