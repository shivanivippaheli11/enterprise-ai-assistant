import time
import uuid
from datetime import datetime

from app.clients.gemini_client import GeminiClient
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.prompt.prompt_builder import PromptBuilder
from app.services.memory_service import MemoryService
from app.services.session_service import SessionService
from app.tools.tool_executor import ToolExecutor
from app.utils.logger import logger
from app.utils.request_id import generate_request_id


class ChatService:

    def __init__(self):
        self.gemini_client = GeminiClient()
        self.prompt_builder = PromptBuilder()
        self.memory_service = MemoryService()
        self.session_service = SessionService()
        self.tool_executor = ToolExecutor()

    def process_message(
        self,
        request: ChatRequest,
        user_id: str,
    ) -> ChatResponse:

        request_id = generate_request_id()
        response_id = f"RESP-{uuid.uuid4().hex[:8].upper()}"

        self.session_service.create_session(
            session_id=request.session_id,
            user_id=user_id,
        )

        logger.info(
            f"[{request_id}] Received chat request from "
            f"user '{user_id}' for session "
            f"'{request.session_id}'."
        )

        history = self.memory_service.get_history(
            request.session_id
        )

        logger.info(
            f"[{request_id}] Retrieved "
            f"{len(history)} previous messages from memory."
        )

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

        logger.info(
            f"[{request_id}] Calling Gemini with tools..."
        )

        start_time = time.perf_counter()

        try:
            model_response = (
                self.gemini_client.generate_response_with_tools(
                    final_prompt
                )
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

        end_time = time.perf_counter()

        logger.info(
            f"[{request_id}] Gemini responded in "
            f"{end_time - start_time:.2f} seconds."
        )

        if model_response.function_calls:

            function_call = model_response.function_calls[0]

            logger.info(
                f"[{request_id}] Gemini requested tool: "
                f"{function_call.name}"
            )

            logger.info(
                f"[{request_id}] Tool arguments: "
                f"{function_call.args}"
            )

            tool_result = self.tool_executor.execute(
                function_call.name,
                function_call.args
            )

            logger.info(
                f"[{request_id}] Tool execution completed."
            )

            logger.info(
                f"[{request_id}] Tool result: "
                f"{tool_result}"
            )

            try:
                ai_response = (
                    self.gemini_client.generate_final_response(
                        final_prompt,
                        model_response,
                        tool_result
                    )
                )

            except Exception as error:
                logger.error(
                    f"[{request_id}] Gemini final response failed: "
                    f"{error}"
                )

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

        else:
            ai_response = model_response.text

            logger.info(
                f"[{request_id}] No tool was requested."
            )

        self.memory_service.add_message(
            request.session_id,
            "user",
            request.message
        )

        self.memory_service.add_message(
            request.session_id,
            "assistant",
            ai_response
        )

        response = ChatResponse(
            response_id=response_id,
            session_id=request.session_id,
            response=ai_response,
            status="SUCCESS",
            timestamp=datetime.now().isoformat()
        )

        logger.info(
            f"[{request_id}] Returning chat response "
            f"for user '{user_id}'."
        )

        return response