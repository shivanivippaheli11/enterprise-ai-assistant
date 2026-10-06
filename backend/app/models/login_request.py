from pydantic import BaseModel


class LoginRequest(BaseModel):
    """
    Represents the credentials provided during login.
    """

    email: str
    password: str