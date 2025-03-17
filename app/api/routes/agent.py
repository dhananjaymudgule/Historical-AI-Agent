# app/api/routes/agent.py

from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import AgentService

# Store chat histories (simulating user sessions)
chat_histories = {}

# Initialize AgentService
agent = AgentService()

# Create API router
router = APIRouter()

@router.post("/", response_model=ChatResponse)
def agent_endpoint(request: ChatRequest): 
    """
    API Endpoint to interact with the Agent using LangGraph and email tools.
    """

    session_id = request.session_id

    # Initialize chat history for a new session
    if session_id not in chat_histories:
        chat_histories[session_id] = agent.chat_history  # Start with system prompt

    # Pass session-specific history to agent
    agent.chat_history = chat_histories[session_id]

    # Process user message
    response = agent.handle_message(request.message)

    # Update session chat history
    chat_histories[session_id] = agent.chat_history  

    return {"response": response}