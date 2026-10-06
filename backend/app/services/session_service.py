from app.repositories.session_repository import SessionRepository

class SessionOwnershipError(Exception):
    """
    Raised when a user attempts to access
    a session owned by another user.
    """
    pass
class SessionService:
    """
    Manages conversation session business logic.
    """

    def __init__(self):
        self.repository = SessionRepository()

    def create_session(
        self,
        session_id: str,
        user_id: str,
    ):
        existing_session = self.repository.get_session(
            session_id
        )

        if existing_session:
            if existing_session["user_id"] != user_id:
                raise SessionOwnershipError(
                    "Session belongs to another user."
                )

            return existing_session

        self.repository.create_session(
            session_id=session_id,
            user_id=user_id,
        )

        return self.repository.get_session(
            session_id
        )

    def get_session(
        self,
        session_id: str,
    ):
        return self.repository.get_session(
            session_id
        )

    def verify_session_owner(
        self,
        session_id: str,
        user_id: str,
    ) -> bool:

        session = self.repository.get_session(
            session_id
        )

        if not session:
            return False

        return session["user_id"] == user_id