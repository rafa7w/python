# Integrated library
import sqlite3

def create_table():
  conn=sqlite3.connect('lite.db')
  cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
  conn.commit()
  conn.close()
  

def insert(item, qtd, price):  
  conn=sqlite3.connect('lite.db')
  cursor=conn.cursor()
  cursor.execute('INSERT INTO store VALUES (?, ?, ?)', (item, qtd, price))
  conn.commit()
  conn.close()


def update(item, qtd, price):  
  conn=sqlite3.connect('lite.db')
  cursor=conn.cursor()
  cursor.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (qtd, price, item))
  conn.commit()
  conn.close()


def delete(item):  
  conn=sqlite3.connect('lite.db')
  cursor=conn.cursor()
  cursor.execute('DELETE FROM store WHERE item=?', (item,))
  conn.commit()
  conn.close()


def view():
  conn=sqlite3.connect('lite.db')
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM store')
  rows=cursor.fetchall()
  conn.close()
  return rows

print(view())