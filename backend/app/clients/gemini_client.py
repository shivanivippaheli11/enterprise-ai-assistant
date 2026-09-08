import httpx

from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.tools.employee_tool_schema import EMPLOYEE_TOOL_SCHEMA


class GeminiClient:

    def __init__(self):

        # Force Gemini API traffic through IPv4.
        # The local network has broken IPv6 connectivity.
        ipv4_transport = httpx.HTTPTransport(
            local_address="0.0.0.0"
        )

        http_options = types.HttpOptions(
            client_args={
                "transport": ipv4_transport
            },
            timeout=60000,
            retry_options=types.HttpRetryOptions(
                attempts=1
            )
        )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY,
            http_options=http_options
        )

    def generate_response(
        self,
        prompt: str
    ) -> str:

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=300,
                thinking_config=types.ThinkingConfig(
                    thinking_level="minimal"
                ),
            ),
        )

        return response.text

    def generate_response_with_tools(
        self,
        prompt: str
    ):

        employee_tool = types.Tool(
            function_declarations=[
                EMPLOYEE_TOOL_SCHEMA
            ]
        )

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=300,
                tools=[
                    employee_tool
                ],
                thinking_config=types.ThinkingConfig(
                    thinking_level="minimal"
                ),
                automatic_function_calling=(
                    types.AutomaticFunctionCallingConfig(
                        disable=True
                    )
                ),
            ),
        )

        return response

    def generate_final_response(
        self,
        prompt: str,
        model_response,
        tool_result: dict
    ):

        employee_tool = types.Tool(
            function_declarations=[
                EMPLOYEE_TOOL_SCHEMA
            ]
        )

        user_prompt_content = types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=prompt
                )
            ]
        )

        # Preserve Gemini's original model response,
        # including the function call information.
        function_call_content = (
            model_response.candidates[0].content
        )

        function_call = model_response.function_calls[0]

        function_response_part = (
            types.Part.from_function_response(
                name=function_call.name,
                response={
                    "result": tool_result
                },
            )
        )

        function_response_content = types.Content(
            role="user",
            parts=[
                function_response_part
            ]
        )

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                user_prompt_content,
                function_call_content,
                function_response_content,
            ],
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=300,
                tools=[
                    employee_tool
                ],
                thinking_config=types.ThinkingConfig(
                    thinking_level="minimal"
                ),
                automatic_function_calling=(
                    types.AutomaticFunctionCallingConfig(
                        disable=True
                    )
                ),
            ),
        )

        return response.text