from datetime import datetime

from app.clients.gemini_client import GeminiClient
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse


class ChatService:

    def __init__(self):
        self.gemini_client = GeminiClient()

    def process_message(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        ai_response = self.gemini_client.generate_response(
            request.message
        )

        return ChatResponse(
            response_id="RESP001",
            session_id=request.session_id,
            response=ai_response,
            status="SUCCESS",
            timestamp=datetime.now().isoformat()
        )