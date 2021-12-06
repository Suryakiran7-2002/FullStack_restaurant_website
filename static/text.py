import sqlite3 as sq

s = sq.connect('admin.db')

c  = s.cursor()

c.execute('''CREATE TABLE admin
        (email TEXT,
        password TEXT);''')
s.commit()

c.close()