import sqlite3

conn = sqlite3.connect("../homework_db.sqlite")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS homeworks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    homework_number INTEGER NOT NULL,
    github_link TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Таблица 'homeworks' успешно создана в базе данных 'homework_db.sqlite'.")
