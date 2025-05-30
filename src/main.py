from fastapi import FastAPI
from src.routes.conversations import router as conversations_router
from dotenv import load_dotenv
from src.routes.users import router as user_router
import uvicorn
import os

load_dotenv()  # ensures environment is loaded early

app = FastAPI()
app.include_router(conversations_router)
app.include_router(user_router)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)