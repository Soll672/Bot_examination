import sqlite3
import os

DB_PATH = os.path.join("database", "db.sqlite3")

def init_db():
    conn = sqlite3.connect(DB_PATH)
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

def save_homework_to_db(name, group_name, homework_number, github_link):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO homeworks (name, group_name, homework_number, github_link)
    VALUES (?, ?, ?, ?)
    ''', (name, group_name, homework_number, github_link))
    conn.commit()
    conn.close()
