from pathlib import Path

# Define the root directory of the project (directory of this config file)
ROOT_DIR = Path(__file__).resolve().parent

# Define the directory for database files, located one level above the project root
DB_DIR = ROOT_DIR.parent / "db"

# Full path to the SQLite database file
DB_PATH = DB_DIR / "app.db"

# Default user type value
DEFAULT_USER_TYPE = 0
