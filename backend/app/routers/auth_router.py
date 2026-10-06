from fastapi import APIRouter

from app.models.login_request import LoginRequest
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

auth_service = AuthService()


@router.post("/register")
def register(
    email: str,
    password: str,
):
    return auth_service.register_user(
        email=email,
        password=password,
    )


@router.post("/login")
def login(
    request: LoginRequest,
):
    return auth_service.login_user(
        email=request.email,
        password=request.password,
    )