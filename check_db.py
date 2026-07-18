import sqlite3

conn = sqlite3.connect("moy.db")
cursor = conn.cursor()

print("Parents Table:")
cursor.execute("SELECT * FROM parents")
rows = cursor.fetchall()

for row in rows:
    print(row)

print("\nMoy Records:")
cursor.execute("SELECT * FROM moy_records")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()