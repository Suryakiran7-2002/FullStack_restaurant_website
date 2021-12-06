import sqlite3 as sq

conn = sq.connect('bookings.sqlite3')

c = conn.cursor()

c.execute('''INSERT INTO admin_details (id,email,password) VALUES (1,'admin@hk.com','admin@123')''')
conn.commit()