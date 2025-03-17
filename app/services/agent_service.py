# app/services/agent_service.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langgraph.prebuilt import create_react_agent
from langgraph.graph.message import add_messages

from typing import Annotated
from typing_extensions import TypedDict

from app.core.config import settings
from app.services.email_service import send_otp, verify_otp
from app.prompts.chatbot_prompts import SYSTEM_PROMPT


# Initialize LLM
gemini_llm = ChatGoogleGenerativeAI(
    google_api_key=settings.GEMINI_API_KEY,
    model=settings.GEMINI_LLM_MODEL_NAME,
    temperature=0
)

# Define available tools
tools = [send_otp, verify_otp]


# Define Chat State Schema
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history


# Chat Service Class
class AgentService:
    def __init__(self):
        self.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]  # Persistent chat history

        # Initialize the agent once
        self.agent = create_react_agent(
            model=gemini_llm,
            tools=tools,
            state_modifier=SYSTEM_PROMPT
        )

    def handle_message(self, message: str):
        """Processes user input using the agent and maintains chat history."""
        
        # Add user message to history
        self.chat_history.append(HumanMessage(content=message))

        # Prepare state with messages
        state = {"messages": self.chat_history}

        # Invoke LangGraph Agent
        response = self.agent.invoke(state)

        # Extract AI response
        messages = response.get("messages", [])
        ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

        if ai_messages:
            ai_response = ai_messages[-1]
            self.chat_history.append(AIMessage(content=ai_response))  # Store AI response persistently
            return ai_response

        return "No response generated."
