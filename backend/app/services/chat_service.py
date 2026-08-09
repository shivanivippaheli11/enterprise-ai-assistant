import time
from datetime import datetime

from app.clients.gemini_client import GeminiClient
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.prompt.prompt_builder import PromptBuilder
from app.utils.logger import logger
from app.utils.request_id import generate_request_id


class ChatService:

    def __init__(self):
        # Initialize dependencies only once
        self.gemini_client = GeminiClient()
        self.prompt_builder = PromptBuilder()

    def process_message(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        # Generate a unique request ID
        request_id = generate_request_id()

        # Log incoming request
        logger.info(
            f"[{request_id}] Received chat request from user "
            f"'{request.user_id}' for session '{request.session_id}'."
        )

        # Build enterprise prompt
        final_prompt = self.prompt_builder.build_prompt(
            request.message
        )

        logger.info(
            f"[{request_id}] Prompt built successfully."
        )

        # Call Gemini API
        logger.info(
            f"[{request_id}] Calling Gemini API..."
        )

        # Start timer
        start_time = time.time()

        try:
            # Generate AI response
            ai_response = self.gemini_client.generate_response(
                final_prompt
            )

        except Exception as error:
            logger.error(
                f"[{request_id}] Gemini API failed: {error}"
            )

            ai_response = (
                "The AI service is temporarily unavailable. "
                "Please try again later."
            )

        # Stop timer
        end_time = time.time()

        logger.info(
            f"[{request_id}] Received response from Gemini "
            f"in {end_time - start_time:.2f} seconds."
        )

        # Build response object
        response = ChatResponse(
            response_id="RESP001",
            session_id=request.session_id,
            response=ai_response,
            status="SUCCESS",
            timestamp=datetime.now().isoformat()
        )

        logger.info(
            f"[{request_id}] Returning chat response."
        )

        return response