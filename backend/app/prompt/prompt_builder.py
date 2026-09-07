class PromptBuilder:
    """
    Builds structured prompts for the Enterprise AI Assistant.
    """

    def build_prompt(
        self,
        history: list,
        user_message: str
    ) -> str:

        conversation = ""

        for message in history:
            conversation += (
                f"{message['role'].capitalize()}: "
                f"{message['message']}\n"
            )

        return f"""
You are an Enterprise AI Assistant.

Rules:
- Answer professionally.
- Keep responses concise and accurate.
- Do not fabricate company policies.
- If information is unavailable, clearly state that.

Conversation History:
{conversation}

Current Question:
{user_message}
"""