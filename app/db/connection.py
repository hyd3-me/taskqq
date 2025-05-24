import sqlite3


def create_database(test_mode: int = 0):
    if test_mode:
        conn = sqlite3.connect(":memory:")
    else:
        conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(64) NOT NULL,
            email VARCHAR(64) NOT NULL,
            hashed_password VARCHAR(64) NOT NULL,
            user_type INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    return conn
