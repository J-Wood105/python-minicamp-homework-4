import sqlite3

connection = sqlite3.connect('database.db')
print('Connection established')

connection.execute('CREATE TABLE movies (name TEXT, rating TEXT)')
print('Table created')
