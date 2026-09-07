import sqlite3
from datetime import datetime


class ConversationRepository:
    """
    Handles persistent storage of conversation messages.
    """

    def __init__(self, database_path: str):
        self.database_path = database_path

        self._create_table()

    def _create_table(self):
        """
        Create the conversation table if it does not already exist.
        """

        connection = sqlite3.connect(self.database_path)

        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS conversation_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    message TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

        finally:
            connection.close()

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str
    ):
        """
        Store a conversation message in the database.
        """

        connection = sqlite3.connect(self.database_path)

        try:
            connection.execute(
                """
                INSERT INTO conversation_messages
                (session_id, role, message, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    session_id,
                    role,
                    message,
                    datetime.now().isoformat()
                )
            )

            connection.commit()

        finally:
            connection.close()

    def get_history(
        self,
        session_id: str
    ):
        """
        Retrieve conversation history for a session.
        """

        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.execute(
                """
                SELECT role, message
                FROM conversation_messages
                WHERE session_id = ?
                ORDER BY id ASC
                """,
                (session_id,)
            )

            rows = cursor.fetchall()

            return [
                {
                    "role": row[0],
                    "message": row[1]
                }
                for row in rows
            ]

        finally:
            connection.close()