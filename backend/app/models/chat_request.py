class ChatRequest:
    def __init__(
        self,
        user_id: str,
        session_id: str,
        message: str,
    ):
        # validations

        if not user_id.strip():
            raise ValueError("User ID cannot be empty.")

        if not session_id.strip():
            raise ValueError("Session ID cannot be empty.")

        if not message.strip():
            raise ValueError("Message cannot be empty.")

        
        self.user_id = user_id
        self.session_id = session_id
        self.message = message