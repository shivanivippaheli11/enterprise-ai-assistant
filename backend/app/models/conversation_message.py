class ConversationMessage:
    """
    Represents a single message from a conversation history.
    """

    def __init__(
        self,
        role: str,
        message: str,
    ):
        self.role = role
        self.message = message