from fastapi import APIRouter

from app.services.memory_service import MemoryService

router = APIRouter()

memory_service = MemoryService()


@router.get("/chat/history/{session_id}")
def get_chat_history(session_id: str):

    history = memory_service.get_history(
        session_id
    )

    return history