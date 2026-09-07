import time
import uuid
from datetime import datetime

from app.clients.gemini_client import GeminiClient
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.prompt.prompt_builder import PromptBuilder
from app.services.memory_service import MemoryService
from app.utils.logger import logger
from app.utils.request_id import generate_request_id


class ChatService:

    def __init__(self):
        # Initialize dependencies only once
        self.gemini_client = GeminiClient()
        self.prompt_builder = PromptBuilder()
        self.memory_service = MemoryService()

    def process_message(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        # Generate a unique request ID
        request_id = generate_request_id()

        # Generate a unique response ID
        response_id = f"RESP-{uuid.uuid4().hex[:8].upper()}"

        # Log incoming request
        logger.info(
            f"[{request_id}] Received chat request from user "
            f"'{request.user_id}' for session '{request.session_id}'."
        )

        # Get previous conversation history
        history = self.memory_service.get_history(
            request.session_id
        )

        logger.info(
            f"[{request_id}] Retrieved "
            f"{len(history)} previous messages from memory."
        )

        # Build enterprise prompt using previous history
        # and the current question
        final_prompt = self.prompt_builder.build_prompt(
            history,
            request.message
        )

        logger.info(
            f"[{request_id}] Prompt built successfully."
        )

        logger.info(
            f"[{request_id}] Prompt length: "
            f"{len(final_prompt)} characters."
        )

        # Call Gemini API
        logger.info(
            f"[{request_id}] Calling Gemini API..."
        )

        start_time = time.perf_counter()

        try:
            # Generate AI response
            ai_response = self.gemini_client.generate_response(
                final_prompt
            )

        except Exception as error:
            end_time = time.perf_counter()

            logger.error(
                f"[{request_id}] Gemini API failed: {error}"
            )

            logger.error(
                f"[{request_id}] Gemini request failed "
                f"after {end_time - start_time:.2f} seconds."
            )

            # Return an error response
            return ChatResponse(
                response_id=response_id,
                session_id=request.session_id,
                response=(
                    "The AI service is temporarily unavailable. "
                    "Please try again later."
                ),
                status="ERROR",
                timestamp=datetime.now().isoformat()
            )

        # Stop timer after successful Gemini response
        end_time = time.perf_counter()

        logger.info(
            f"[{request_id}] Received response from Gemini "
            f"in {end_time - start_time:.2f} seconds."
        )

        # Store user message after successful AI processing
        self.memory_service.add_message(
            request.session_id,
            "user",
            request.message
        )

        # Store AI response in memory
        self.memory_service.add_message(
            request.session_id,
            "assistant",
            ai_response
        )

        # Build successful response
        response = ChatResponse(
            response_id=response_id,
            session_id=request.session_id,
            response=ai_response,
            status="SUCCESS",
            timestamp=datetime.now().isoformat()
        )

        logger.info(
            f"[{request_id}] Returning chat response."
        )

        return response