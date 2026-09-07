class MemoryService:
    """
    Stores conversation history for each session.
    """

    def __init__(self):
        # Dictionary to store chat history
        self.conversations = {}

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str
    ):
        """
        Add a message to a conversation.
        """

        if session_id not in self.conversations:
            self.conversations[session_id] = []

        self.conversations[session_id].append(
            {
                "role": role,
                "message": message
            }
        )

    def get_history(
        self,
        session_id: str
    ):
        """
        Return conversation history.
        """

        return self.conversations.get(session_id, [])