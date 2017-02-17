"""
Psycopg, a PostgreSQL database adapter.
http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg

pip install the_file_name_you_download_psycopg2

psycopg2 won't use ? as sqlite3, it will use %s
"""
import psycopg2

# Create database file if this file is not exsit.
def create_table():
	conn = psycopg2.connect("dbname='myTestingDataBase', user='testing', password='testing', host='localhost',port='5432'")
	cur = conn.cursor()
	conn.commit()
	conn.close

def insert(item, quantity, price):
	conn = psycopg2.connect("dbname='myTestingDataBase', user='testing', password='testing', host='localhost',port='5432'")
	cur = conn.cursor()
	# This may cause SQL injection
	# cur.execute("INSERT INTO store VALUES('%s', '%s', '%S')" % (item, quantity, price))
	cur.execute("INSERT INTO store VALUES(%s, %s, %S)", (item, quantity, price))
	conn.commit()
	conn.close

def update(quantity, price, item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
	conn.commit()
	conn.close

def delete(item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item=%s", (item,)) 
	conn.commit()
	conn.close()
	
def view():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")  # If we are doing select, we don't needa do commit function
	rows = cur.fetchall()
	conn.close()
	return rows

# delete("Wine Glass")
# insert('Wine Glass',8, 10.5)
# update(2, 5.5, 'Wine Glass')
# print(view())