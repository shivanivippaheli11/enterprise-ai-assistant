from pydantic import BaseModel


class ChatResponse(BaseModel):
    response_id: str
    session_id: str
    response: str
    status: str
    timestamp: str