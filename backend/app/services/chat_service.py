from datetime import datetime

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse


class ChatService:

    def process_message(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            response_id="RESP001",
            session_id=request.session_id,
            response=f"AI Response: {request.message}",
            status="SUCCESS",
            timestamp=datetime.now().isoformat()
        )