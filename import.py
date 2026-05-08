import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO game (title, price)
VALUES ('Minecraft', 29.99)
""")

cursor.execute("""
INSERT INTO game (title, price)
VALUES ('GTA V', 59.99)
""")


print("Sample data inserted successfully.")

conn.commit()
conn.close()