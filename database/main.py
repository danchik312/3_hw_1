import sqlite3
from config import DB_FILENAME

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILENAME)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS telegram_users (
                                id INTEGER PRIMARY KEY,
                                user_id INTEGER,
                                username TEXT)''')
        self.connection.commit()

    def add_user(self, user_id, username):
        self.cursor.execute("INSERT INTO telegram_users (user_id, username) VALUES (?, ?)", (user_id, username))
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM telegram_users")
        return self.cursor.fetchall()