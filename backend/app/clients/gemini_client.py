from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate_response(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={
                "temperature": 0.2,
                "max_output_tokens": 300,
            },
        )

        return response.text