from fastapi import FastAPI, Depends

from config import get_settings, Settings


app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "enviroment": settings.environment,
        "tesing": settings.testing
    }