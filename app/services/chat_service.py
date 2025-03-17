# app/services/chat_service 

import requests
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langgraph.graph import StateGraph, START
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
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

# OTP storage (Temporary)
otp_storage = {}

tools = [send_otp, verify_otp]

llm_with_tools = gemini_llm.bind_tools(tools)


# Define Chat State Schema
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history


def chatbot(state: State):
    """Processes user input, invokes tools if required, and appends responses to chat history."""

    messages = state["messages"]

    # Invoke LLM with history
    response = llm_with_tools.invoke(messages)

    print(f"🔍 LLM Response: {response}")  # Debugging output

    # Check if LLM wants to call a function
    function_call = response.additional_kwargs.get("function_call")
    if function_call:
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])

        # Find the tool function
        tool_function = next((t for t in tools if t.__name__ == function_name), None)

        if tool_function:
            print(f"🚀 Executing Tool: {function_name} with arguments {function_args}")  # Debugging
            tool_response = tool_function(**function_args)  # Execute the tool

            # Ensure tool_response is a string before appending to messages
            if not isinstance(tool_response, str):
                tool_response = "Error: Tool execution failed."

            messages.append(AIMessage(content=tool_response))  # Append tool response
        else:
            print(f"❌ Tool {function_name} not found!")  # Debugging
            messages.append(AIMessage(content=f"Error: Tool {function_name} not found."))
    else:
        # Normal LLM response
        response_text = response.get("content", str(response)) if isinstance(response, dict) else response.content
        messages.append(AIMessage(content=response_text))

    return {"messages": messages}


# Define LangGraph Workflow
def build_chatbot():
    graph_builder = StateGraph(State)

    # Define nodes
    graph_builder.add_node("assistant", chatbot)
    graph_builder.add_node("tools", ToolNode(tools))

    # Define edges
    graph_builder.add_edge(START, "assistant")
    graph_builder.add_conditional_edges("assistant", tools_condition)
    graph_builder.add_edge("tools", "assistant")

    return graph_builder.compile()


# Instantiate LangGraph chatbot
chatbot_graph = build_chatbot()


# Chat Service Class
class ChatService:
    def __init__(self):
        self.graph = chatbot_graph
        self.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]  # Store chat history persistently

    def handle_message(self, message: str):
        """Processes user input and maintains chat history."""
        
        # Add user message to history
        self.chat_history.append(HumanMessage(content=message))

        # Prepare state with messages
        state = State(messages=self.chat_history)

        # Invoke LangGraph
        next_state = self.graph.invoke(state)

        # Extract AI response
        if next_state["messages"]:
            ai_response = next_state["messages"][-1].content
            self.chat_history.append(AIMessage(content=ai_response))  # Store AI response persistently
            return ai_response

        return "No response generated."
