import sqlite3

# Create database file if this file is not exist.


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # (NULL, ?, ?, ?, ?) - Python will create ID field automatically
    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update(id, title, author, year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")  # If we are doing select, we don't needa do commit function
    rows = cur.fetchall()
    conn.close()
    return rows

# That means parameter default value
def search(title ="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR  author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
# insert("test", "Sai", 111,  323332)
# delete("8")
# update(5, "Update test", "Mr Sai", "2017", "12312312")
# print(view())
# print(search(author="Sai"))