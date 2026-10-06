from fastapi import APIRouter, Depends, HTTPException, status

from app.services.memory_service import MemoryService
from app.services.session_service import SessionService
from app.utils.auth_dependency import get_current_user


router = APIRouter()

memory_service = MemoryService()
session_service = SessionService()


@router.get("/chat/history/{session_id}")
def get_chat_history(
    session_id: str,
    current_user: dict = Depends(
        get_current_user
    ),
):

    is_owner = session_service.verify_session_owner(
        session_id=session_id,
        user_id=current_user["user_id"],
    )

    if not is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this conversation.",
        )

    history = memory_service.get_history(
        session_id
    )

    return history