import uuid
from datetime import datetime

from app.repositories.user_repository import UserRepository
from app.utils.jwt_handler import create_access_token
from app.utils.password_hasher import (
    hash_password,
    verify_password,
)


class AuthService:
    """
    Handles authentication-related business logic.
    """

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(
        self,
        email: str,
        password: str,
    ):
        password_hash = hash_password(password)

        user_id = (
            f"USER-{uuid.uuid4().hex[:8].upper()}"
        )

        self.user_repository.create_user(
            user_id=user_id,
            email=email,
            password_hash=password_hash,
        )

        return {
            "user_id": user_id,
            "email": email,
            "created_at": datetime.now().isoformat(),
        }

    def login_user(
        self,
        email: str,
        password: str,
    ):
        user = self.user_repository.get_user_by_email(
            email
        )

        if not user:
            return {
                "success": False,
                "message": "Invalid email or password."
            }

        password_valid = verify_password(
            password,
            user["password_hash"],
        )

        if not password_valid:
            return {
                "success": False,
                "message": "Invalid email or password."
            }

        access_token = create_access_token(
            user_id=user["user_id"],
            email=user["email"],
        )

        return {
            "success": True,
            "user_id": user["user_id"],
            "email": user["email"],
            "access_token": access_token,
            "token_type": "bearer",
        }