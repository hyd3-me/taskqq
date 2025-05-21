import sqlite3

def test_sqlite_in_memory_db_accessible():
    # Test data variables
    test_email = "test@example.com"
    test_username = "testuser"
    test_hashed_password = "fakehash"

    # Create an in-memory SQLite database and a users table
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            username TEXT NOT NULL,
            hashed_password TEXT NOT NULL
        )
    """)
    conn.commit()

    # Insert a test user into the users table using variables
    cursor.execute(
        "INSERT INTO users (email, username, hashed_password) VALUES (?, ?, ?)",
        (test_email, test_username, test_hashed_password)
    )
    conn.commit()

    # Query the inserted user to verify the insertion
    cursor.execute("SELECT email, username FROM users WHERE email = ?", (test_email,))
    user = cursor.fetchone()
    conn.close()

    # Assert that the user was successfully inserted and retrieved
    assert user is not None
    assert user[0] == test_email
    assert user[1] == test_username
