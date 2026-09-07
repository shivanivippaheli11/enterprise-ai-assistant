from app.config import DATABASE_PATH
from app.repositories.conversation_repository import ConversationRepository


class MemoryService:
    """
    Manages conversation memory using persistent storage.
    """

    def __init__(self):
        self.repository = ConversationRepository(
            DATABASE_PATH
        )

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str
    ):
        """
        Store a conversation message.
        """

        self.repository.add_message(
            session_id,
            role,
            message
        )

    def get_history(
        self,
        session_id: str
    ):
        """
        Retrieve conversation history.
        """

        return self.repository.get_history(
            session_id
        )