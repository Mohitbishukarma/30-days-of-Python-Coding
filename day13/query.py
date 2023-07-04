import sqlite3
conn = sqlite3.connect("my.db")
c    = conn.cursor()

# getting data from db
data = c.execute("SELECT * FROM marks")
for name , mark in data:
    print(f"{name}  :  {mark}")
    