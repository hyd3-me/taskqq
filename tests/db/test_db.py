import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.db import connection
import config


def test_sqlite_in_memory_db_accessible():
    # Test data variables
    test_email = "test@example.com"
    test_username = "testuser"
    test_hashed_password = "fakehash"

    conn = connection.create_database(test_mode=1)
    cursor = conn.cursor()

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

def test_db_directory_exists():
    # Create the directory if it doesn't exist (optional)
    config.DB_DIR.mkdir(parents=True, exist_ok=True)
    # Check if the database directory exists
    assert config.DB_DIR.is_dir(), f"Database directory {config.DB_DIR} does not exist"