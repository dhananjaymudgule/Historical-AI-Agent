# Historical AI Agent

## Overview
The **Historical AI Agent** is a FastAPI-based conversational AI system designed to provide information about historical monuments. It supports real-time chat with session-based memory and integrates AI-powered agents for enhanced interactions.

## Features
- FastAPI backend with modular structure
- Chatbot service for user interactions
- AI agent integration using LangGraph
- Streamlit-based frontend UI
- Session-based chat history
- CORS-enabled for frontend communication
- OTP-based email verification
- Scalable and extensible architecture

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.12+
- Virtual Environment (optional but recommended)

### Steps
```bash
# Clone the repository
git clone https://github.com/your-repo/historical-ai-agent.git
cd historical-ai-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file in the root directory and configure the following environment variables:

```ini
EMAIL_SENDER="your-email@gmail.com"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT="587"
EMAIL_PASSWORD="your-email-password"

GEMINI_LLM_MODEL_NAME="your-gemini-model"
GEMINI_API_KEY="your-gemini-api-key"
```

## Running the Project

### Start FastAPI Backend
```bash
# Run the FastAPI application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Start Streamlit Frontend
```bash
# Navigate to chat UI directory
cd app/chat_ui

# Run the Streamlit app
streamlit run app.py
```

The API will be accessible at:
- **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

The frontend will be accessible at:
- **Streamlit UI:** [http://localhost:8501](http://localhost:8501)

## API Endpoints

| Method | Endpoint      | Description                     |
|--------|-------------|---------------------------------|
| GET    | `/`         | Health check                    |
| POST   | `/chat`     | Chatbot interaction             |
| POST   | `/agent`    | AI agent interaction            |

## Project Structure
```
HISTORICAL-AI-AGENT/
│── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat.py
│   │   │   ├── agent.py
│   │── chat_ui/
│   │   ├── app.py  # Streamlit UI
│   │── core/
│   │   ├── config.py
│   │   ├── security.py
│   │── models/
│   │   ├── user.py
│   │── prompts/
│   │   ├── chatbot_prompts.py
│   │── schemas/
│   │   ├── chat.py
│   │   ├── email.py
│   │── services/
│   │   ├── chat_service.py
│   │   ├── agent_service.py
│   │   ├── email_service.py
│── main.py
│── requirements.txt
│── Dockerfile
│── README.md
```

## How It Works

### Chatbot Service (`chat_service.py`)
- Uses **Gemini LLM** for natural language processing.
- Maintains session-based chat history.
- Detects when to invoke tools (OTP-based email verification).
- Uses **LangGraph** for workflow orchestration.

### Agent Service (`agent_service.py`)
- Uses **Gemini LLM** with **LangGraph** for structured interactions.
- Can access external tools like email verification.
- Maintains chat history persistently.

### Streamlit UI (`chat_ui/app.py`)
- Provides an interactive frontend for user interaction.
- Sends user messages to FastAPI backend (`/agent` endpoint).
- Maintains chat history per session using `session_id`.

### OTP Verification Flow
1. The chatbot requests the user's email.
2. It calls `send_otp(email: str)` to send an OTP.
3. The user enters the OTP.
4. The chatbot verifies using `verify_otp(email: str, otp: str)`.
5. If valid, confirmation is sent; otherwise, the user is asked to retry.

## Future Enhancements
- Improve agent capabilities using additional AI tools.
- Implement database storage for long-term session memory.
- Enhance Streamlit UI with a more user-friendly design.
- Deploy on cloud platforms like AWS or GCP.

## License
This project is licensed under the ** License.



