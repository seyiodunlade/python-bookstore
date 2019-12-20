import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("books.db")

        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, " 
                         "author TEXT, year INTEGER, isbn INTEGER)")

        self.conn.commit()

    def add_entry(self, title, author, year, isbn):

        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))

        self.conn.commit()

        # conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")

        rows = self.cur.fetchall()

        # self.conn.close()

        return rows

    def search_entry(self, title="", author="", year="", isbn=""):

        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))

        rows = self.cur.fetchall()

        # conn.close()

        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))

        self. conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))

        self.conn.commit()

    def __del__(self):
        self.conn.close()

# create_table()
# add_entry("Snakes paradise", "Holt Kurt", 2001, 372963473873)
# print(search_entry("", "Jon Smith", "", ""))
# update_table(20, 500.00, 'Cap')
# insert_data("Water Bottle", 20, 1000.00)
# update(4, "The last man", "Jon Smith", 2005, 6746323544353)
# print(view())
# search_entry()
