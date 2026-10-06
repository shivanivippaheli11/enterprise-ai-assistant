from datetime import datetime, timedelta, timezone

import jwt

from app.config import JWT_SECRET_KEY


JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 30


def create_access_token(
    user_id: str,
    email: str,
) -> str:
    """
    Creates a JWT access token for an authenticated user.
    """

    expiration_time = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=JWT_EXPIRATION_MINUTES
        )
    )

    payload = {
        "user_id": user_id,
        "email": email,
        "exp": expiration_time,
    }

    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    return token


def decode_access_token(
    token: str,
) -> dict:
    """
    Decodes and validates a JWT access token.
    """

    payload = jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )

    return payload