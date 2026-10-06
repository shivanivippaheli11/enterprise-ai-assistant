from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Represents a chat request from an authenticated user.
    """

    session_id: str
    message: str