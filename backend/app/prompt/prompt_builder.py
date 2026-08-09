class PromptBuilder:
    """
    Builds structured prompts for the Enterprise AI Assistant.
    """

    def build_prompt(self, user_message: str) -> str:
        return f"""
You are an Enterprise AI Assistant.

Rules:
- Answer professionally.
- Keep responses concise and accurate.
- Do not fabricate company policies or confidential information.
- If the information is unavailable, clearly state that.

Employee Question:
{user_message}
"""