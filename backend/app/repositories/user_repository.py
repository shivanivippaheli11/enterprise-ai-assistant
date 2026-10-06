import sqlite3
from datetime import datetime

from app.config import DATABASE_PATH


class UserRepository:
    """
    Handles persistent storage of application users.
    """

    def __init__(self):
        self.database_path = DATABASE_PATH
        self._create_table()

    def _create_table(self):
        connection = sqlite3.connect(
            self.database_path
        )

        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    email TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

        finally:
            connection.close()

    def create_user(
        self,
        user_id: str,
        email: str,
        password_hash: str,
    ):
        connection = sqlite3.connect(
            self.database_path
        )

        try:
            connection.execute(
                """
                INSERT INTO users
                (user_id, email, password_hash, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    user_id,
                    email,
                    password_hash,
                    datetime.now().isoformat(),
                ),
            )

            connection.commit()

        finally:
            connection.close()

    def get_user_by_email(
        self,
        email: str,
    ):
        connection = sqlite3.connect(
            self.database_path
        )

        try:
            cursor = connection.execute(
                """
                SELECT
                    user_id,
                    email,
                    password_hash,
                    created_at
                FROM users
                WHERE email = ?
                """,
                (email,),
            )

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "user_id": row[0],
                "email": row[1],
                "password_hash": row[2],
                "created_at": row[3],
            }

        finally:
            connection.close()