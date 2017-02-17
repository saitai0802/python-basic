import sqlite3

# Create database file if this file is not exsit.
def create_table():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	conn.commit()
	conn.close

def insert(item, quantity, price):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
	conn.commit()
	conn.close

def update(quantity, price, item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
	conn.commit()
	conn.close

def delete(item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item=?", (item,)) 
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
update(2, 5.5, 'Wine Glass')
print(view())