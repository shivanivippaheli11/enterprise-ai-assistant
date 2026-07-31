from fastapi import FastAPI
from app.routers.chat_router import router as chat_router

app = FastAPI(
    title="Enterprise AI Assistant API",
    version="1.0.0",
    description="Backend API for the Enterprise AI Assistant",
)


@app.get("/")
def read_root():
    return {"message": "Enterprise AI Assistant API is running"}


app.include_router(chat_router)