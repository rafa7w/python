# Integrated library
import sqlite3

# Connect to a database
conn=sqlite3.connect('lite.db')

# Create a cursor object
cursor=conn.cursor()

# Write an SQL query
cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
cursor.execute('INSERT INTO store VALUES ("Wine Glass", 8, 10.5)')

# Commit changes
conn.commit()

# Close database connection
conn.close()