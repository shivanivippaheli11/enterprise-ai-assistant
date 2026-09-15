from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.logger import logger
from app.routers.chat_router import router as chat_router


logger.info("Application started successfully.")


app = FastAPI(

    title="Enterprise AI Assistant API",

    version="1.0.0",

    description="Backend API for the Enterprise AI Assistant",

)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def read_root():

    return {
        "message": "Enterprise AI Assistant API is running"
    }


app.include_router(
    chat_router
)


@app.get("/")
def read_root():
    return {"message": "Enterprise AI Assistant API is running"}


app.include_router(chat_router)