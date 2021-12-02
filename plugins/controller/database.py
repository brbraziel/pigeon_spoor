import mysql.connector

class Database():

    connection = mysql.connector.connect(
        host='127.0.0.1'
    )
