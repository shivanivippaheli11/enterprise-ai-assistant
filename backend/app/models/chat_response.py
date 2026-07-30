class ChatResponse:
    """
    Represents the response returned to the employee after processing a chat request.
    """

    def __init__(
            self,
            response_id: str,
            session_id: str,
            response: str,
            status: str,
            timestamp: str,
    ):
        self.response_id = response_id
        self.session_id = session_id
        self.response = response
        self.status = status
        self.timestamp = timestamp