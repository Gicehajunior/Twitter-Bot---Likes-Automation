import sqlite3 as sql

def conn():
    connection = sql.connect('credentials.db')
    
    return connection

def cursor_connection(connection):
    database_connection = connection.cursor()
    
    return database_connection

