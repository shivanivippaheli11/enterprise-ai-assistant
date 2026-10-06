from fastapi import (APIRouter, Depends,HTTPException,status)

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.chat_service import ChatService
from app.services.chat_service import ChatService
from app.services.session_service import SessionOwnershipError
from app.utils.auth_dependency import get_current_user


router = APIRouter()

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    current_user: dict = Depends(
        get_current_user
    ),
):
    try:
        return chat_service.process_message(
            request=request,
            user_id=current_user["user_id"],
        )

    except SessionOwnershipError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this conversation.",
        )