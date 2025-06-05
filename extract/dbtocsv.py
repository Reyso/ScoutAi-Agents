import sqlite3
import pandas as pd

conn = sqlite3.connect("data_fute.db")
df = pd.read_sql_query("SELECT * FROM players WHERE rating > 0 AND age > 0 AND height > 0 and transferValue > 0 ", conn)
df.to_csv("players.csv", index=False)


conn.commit()
conn.close()