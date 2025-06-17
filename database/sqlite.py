# database/sqlite.py
from contextlib import contextmanager
import sqlite3
from config.settings import SQLiteSettings

_sqlite = SQLiteSettings()

@contextmanager
def get_connection():
    conn = sqlite3.connect(_sqlite.path)
    try:
        yield conn
    finally:
        conn.close()
