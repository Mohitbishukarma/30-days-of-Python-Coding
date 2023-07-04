import sqlite3
conn = sqlite3.connect("my.db")
c = conn.cursor()

c.execute("""CREATE TABLE marks (name text , marks real)""")

c.execute("INSERT INTO marks values('Physics', 95)")

conn.commit()
conn.close()