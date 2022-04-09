import mysql.connector

config = {
    'user': 'root',
    'password': '12345678a',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()