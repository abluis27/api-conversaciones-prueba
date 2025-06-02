from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.conversations import router as conversations_router
from dotenv import load_dotenv
from src.routes.users import router as user_router
import uvicorn
import os

load_dotenv()  # ensures environment is loaded early

# Define allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://atencionprimaria.riberadeltajo.es"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],              # allow all HTTP methods
    allow_headers=["*"],              # allow all headers
)

app.include_router(conversations_router)
app.include_router(user_router)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)