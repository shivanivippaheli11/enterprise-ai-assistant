from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Assistant API",
    version="1.0.0",
    description="Backend API for the Enterprise AI Assistant"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Enterprise AI Assistant API!"
    }