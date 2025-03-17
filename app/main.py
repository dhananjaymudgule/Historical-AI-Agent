# app/main.py

from fastapi import FastAPI
from app.api.routes import chat
from app.api.routes import agent


app = FastAPI(title="Historical Monuments Bot")

app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(agent.router, prefix="/agent", tags=["agent"])

# app.include_router(email_verification.router, prefix="/email", tags=["email"])
