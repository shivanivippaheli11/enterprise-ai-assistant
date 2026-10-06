class User:
    """
    Represents an authenticated application user.
    """

    def __init__(
        self,
        user_id: str,
        email: str,
        password_hash: str,
        created_at: str,
    ):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at