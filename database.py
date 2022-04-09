import mysql.connector

config = {
    'user': 'root',
    'password': '12345678a',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()