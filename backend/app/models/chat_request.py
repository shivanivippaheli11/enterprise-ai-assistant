from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Represents a chat request sent by the employee.
    """

    user_id: str = Field(..., min_length=1)
    session_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)