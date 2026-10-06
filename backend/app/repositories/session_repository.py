import sqlite3
from datetime import datetime

from app.config import DATABASE_PATH


class SessionRepository:
    """
    Handles persistent storage of conversation sessions.
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
                CREATE TABLE IF NOT EXISTS conversation_sessions (
                    session_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

        finally:
            connection.close()

    def create_session(
        self,
        session_id: str,
        user_id: str,
    ):
        connection = sqlite3.connect(
            self.database_path
        )

        try:
            connection.execute(
                """
                INSERT INTO conversation_sessions
                (
                    session_id,
                    user_id,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    session_id,
                    user_id,
                    datetime.now().isoformat(),
                ),
            )

            connection.commit()

        finally:
            connection.close()

    def get_session(
        self,
        session_id: str,
    ):
        connection = sqlite3.connect(
            self.database_path
        )

        try:
            cursor = connection.execute(
                """
                SELECT
                    session_id,
                    user_id,
                    created_at
                FROM conversation_sessions
                WHERE session_id = ?
                """,
                (session_id,),
            )

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "session_id": row[0],
                "user_id": row[1],
                "created_at": row[2],
            }

        finally:
            connection.close()