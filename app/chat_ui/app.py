import streamlit as st
import requests
import uuid  # Generate unique session IDs

# FastAPI Backend URL
# API_URL = "http://127.0.0.1:8000/chat/"  
API_URL="https://historical-ai-agent.onrender.com"

# Streamlit UI Setup
st.set_page_config(page_title="Historical Chatbot", layout="wide", page_icon="🤖")

st.title("🤖 Historical Chatbot")
st.write("Ask anything about historical monuments!")

# Generate session ID for each user
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())  

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send user input to FastAPI chatbot with session_id
    response = requests.post(API_URL, json={"session_id": st.session_state.session_id, "message": user_input})
    
    bot_reply = response.json().get("reply", "I didn't understand that.")

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
