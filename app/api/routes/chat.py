# app/api/routes/chat.py

from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService



# Store chat histories (simulating user sessions)
chat_histories = {}

# Initialize chatbot
chatbot = ChatService()

# router
router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """Handles user messages and maintains session-based chat history."""

    session_id = request.session_id

    # Initialize chat history for a new session
    if session_id not in chat_histories:
        chat_histories[session_id] = chatbot.chat_history  # Start with system prompt

    # Pass session-specific history to chatbot
    chatbot.chat_history = chat_histories[session_id]

    # Process user message
    reply = chatbot.handle_message(request.message)

    # Update session chat history
    chat_histories[session_id] = chatbot.chat_history  

    return {"reply": reply}


