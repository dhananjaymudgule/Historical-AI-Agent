# Historical AI Agent

## 📌 Overview

The **Historical AI Agent** is a **FastAPI-based conversational AI system** using **Agentic Workflow - LangGraph**. It is a conversational bot that has **only the knowledge of historical monuments** across the world. Users can chat with the bot to ask any questions relevant to historical monuments. Within the conversational journey, the bot will be able to **ask for the user’s email address and verify it** by executing the OTP workflow within the chat itself. It supports real-time chat with session-based memory and integrates AI-powered agents for enhanced interactions.

## 🚀 Features
- 🏛 **Historical Knowledge**: The chatbot answers only historical monument-related queries.
- 💬 **Conversational AI**: Uses **LangGraph** for structured, session-based interactions.
- 📧 **Email Verification**: Bot asks for and verifies email via OTP during the chat.
- 🔄 **Session-Based Memory**: Retains chat history for contextual conversations.
- ⚡ **FastAPI Backend**: Efficient and scalable API framework.
- 🌍 **Web UI**: Interactive frontend using **Streamlit**.
- 🔒 **CORS Enabled**: Allows secure communication between frontend and backend.
- 🛠 **Modular & Scalable**: Well-structured, extensible architecture.
- ✅ **Automated Testing**: Ensures system stability with Pytest.

## 🏗 Directory Structure
```
HISTORICAL-AI-AGENT/
│── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat.py         # Chatbot endpoint (LangGraph-based)
│   │   │   ├── agent.py        # AI agent endpoint (LangGraph-based)
│   │── chat_ui/
│   │   ├── app.py              # Streamlit UI
│   │── core/
│   │   ├── config.py           # App settings & environment variables
│   │── models/
│   │   ├── user.py             # User model (if needed)
│   │── prompts/
│   │   ├── chatbot_prompts.py  # System prompts for the chatbot
│   │── schemas/
│   │   ├── chat.py             # Pydantic models for request/response validation
│   │── services/
│   │   ├── chat_service.py     # Handles chat interactions with LangGraph
│   │   ├── agent_service.py    # Manages AI agent responses
│   │   ├── email_service.py    # Handles OTP-based email verification
│   │── tests/
│   │   ├── test_chat.py        # Tests for chat service
│   │── utils/
│   │   ├── otp.py              # OTP-related functions
│── main.py                     # FastAPI entry point
│── requirements.txt            # Dependencies
│── Dockerfile                  # Containerization setup
│── README.md                   # Project documentation
```

## 📦 Installation & Setup

### **1️⃣ Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the project root by referring to `.env.example` and update it with your credentials.

```ini
# API Configuration
VERSION=1.0.0
HOST=127.0.0.1
PORT=8000
PROJECT_NAME="Historical Monuments Bot"
PROJECT_DESCRIPTION="Historical Monuments Bot"

# Email Configuration
EMAIL_SENDER=your_email@example.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_PASSWORD=your_email_password

# AI Model Configuration
GEMINI_LLM_MODEL_NAME=gemini-2.0-flash
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🏃‍♂️ Running the Project

### **1️⃣ Start FastAPI Backend**
```bash
uvicorn app.main:app --reload
```
- **Swagger UI (API Docs)** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Health Check** → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### **2️⃣ Start Streamlit Frontend**
```bash
cd app/chat_ui
streamlit run app.py
```

## 🛠 API Endpoints
### **1️⃣ Chat API (`chat.py`)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/chat` | Handles chatbot interactions via LangGraph |

### **2️⃣ AI Agent API (`agent.py`)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/agent` | LangGraph-based AI agent handling historical monument queries and OTP verification |

## 🏗 Project Architecture
### **🔹 1️⃣ API Layer (`api/routes/`)**
- **`chat.py`** → Handles chatbot interactions.
- **`agent.py`** → Processes AI agent interactions.

### **🔹 2️⃣ Business Logic (`services/`)**
- **`chat_service.py`** → Manages chat history & processing.
- **`agent_service.py`** → Manages AI agent logic.
- **`email_service.py`** → Handles OTP-based email verification.

### **🔹 3️⃣ Prompt Management (`prompts/`)**
- **`chatbot_prompts.py`** → Stores system and user prompts.

### **🔹 4️⃣ Utilities (`utils/`)**
- **`otp.py`** → OTP-related functions for email verification.

## 🎯 Future Enhancements
- ✅ Improve **multi-turn conversation handling**.
- ✅ Add **database storage for chat history**.
- ✅ Implement **better response ranking and retrieval**.
- ✅ Deploy on **AWS/GCP with CI/CD automation**.

## 📜 License
This project is licensed under the **License**.

---


