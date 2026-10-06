import os

from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/conversations.db"
)
JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY"
)


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured."
    )


if not GEMINI_MODEL:
    raise ValueError(
        "GEMINI_MODEL is not configured."
    )

