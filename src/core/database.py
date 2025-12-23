# Import Libraries

import sqlite3
from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class DatabaseManager(ABC):
    """Interface for interacting with databases"""

    @abstractmethod
    def add_screenshot(self, timestamp: str, file_path: str | Path):
        """Add screenshot in database"""
        pass

    @abstractmethod
    def get_recent_screenshots(self, limit=10):
        """Getting the latest screenshots"""
        pass


class SQLiteDatabase(DatabaseManager):
    """SQLiteDatabase interface"""

    def __init__(self, db_path: str | Path = "src/data/databases/sqlite.db"):
        self.db_path = Path(db_path)
        self._init_db()

    def _init_db(self):
        """Creating folders and initializing the database file"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.db_path.exists():
            print(f"Creating a new database at {self.db_path}...")
        else:
            print(f"Connecting to existing database at {self.db_path}...")

        conn = sqlite3.connect(self.db_path)
        try:
            with conn:
                conn.execute(
                    """CREATE TABLE IF NOT EXISTS screenshots (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             timestamp TEXT NOT NULL,
                             file_path TEXT NOT NULL
                             )"""
                )
        finally:
            conn.close()

    def add_screenshot(self, timestamp: str, file_path: str | Path):
        """Add screenshot in the database"""
        conn = sqlite3.connect(self.db_path)

        try:
            with conn:
                conn.execute(
                    "INSERT INTO screenshots (timestamp, file_path) VALUES (?, ?)",
                    (timestamp, file_path),
                )
        finally:
            conn.close()
