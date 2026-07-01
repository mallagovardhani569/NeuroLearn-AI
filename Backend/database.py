import sqlite3

connection = sqlite3.connect("neurolearn.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    department TEXT,
    year INTEGER
)
""")

connection.commit()
connection.close()

print("Database created successfully!")