import sqlite3

conn = sqlite3.connect("/media/rey/bk/projects/Scout/data_fute.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM teams LIMIT 5")
print(cursor.fetchall())

conn.close()
