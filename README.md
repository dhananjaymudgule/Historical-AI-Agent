# Historical-AI-Agent


Both `chat_service.py` and `agent_service.py` implement conversational AI using **Gemini LLM** and **LangGraph**, but they take different approaches in structuring the chatbot. Here's a breakdown of their differences:

---

### **1️⃣ Chat Service (`chat_service.py`): LangGraph with Tool Nodes**
#### **How it Works:**
- Uses **LangGraph** explicitly to build a stateful chatbot workflow.
- Maintains **conversation history (`messages` list)** throughout interactions.
- Defines a **state schema (`State`)** using `TypedDict` to ensure structured inputs.
- **Tool invocation**:
  - The chatbot first processes the input message.
  - If the response requires calling a function (tool), it executes it and appends the result to the conversation.
  - Otherwise, it returns the LLM's response.
- Implements **a structured workflow** with:
  - **Nodes** (`assistant` and `tools`).
  - **Edges** (directing flow between nodes).
- Stores **conversation history persistently** in `ChatService`.

#### **Pros:**
✅ **More structured and scalable**: Uses a modular, graph-based approach.  
✅ **Better control over tool execution**: Explicit handling of function calls.  
✅ **Retains chat history** across messages.  
✅ **Easier debugging** with clear function call execution tracking.  

#### **Cons:**
❌ Slightly more complex setup due to explicit state handling and LangGraph edges.  
❌ Requires manually managing the flow between nodes.

---

### **2️⃣ Agent Service (`agent_service.py`): LangGraph's `create_react_agent`**
#### **How it Works:**
- Uses `create_react_agent`, a **prebuilt LangGraph agent** for reasoning and action execution.
- No explicit conversation state management.
- Defines **tools** (`send_otp`, `verify_otp`) and passes them directly to the agent.
- The **agent internally decides** whether to call a tool or respond normally.
- Uses `SYSTEM_PROMPT` as a **state modifier**.
- Simply **invokes the agent** with the user query (`state={"messages": query}`).

#### **Pros:**
✅ **Easier to implement**: Uses a high-level agent API with minimal manual state handling.  
✅ **Less boilerplate**: No need to define state management explicitly.  
✅ **More natural tool usage**: The agent decides when to call tools.  

#### **Cons:**
❌ **Less control over execution flow**: You can't define explicit transitions like in LangGraph.  
❌ **No explicit chat history**: You'd need to handle persistence separately.  
❌ **Debugging is harder**: No clear function execution tracking.  

---

### **Which One is Better?**
| Feature                  | **Chat Service (`chat_service.py`)** | **Agent Service (`agent_service.py`)** |
|--------------------------|--------------------------------------|--------------------------------------|
| **Ease of Implementation** | ❌ More setup required              | ✅ Simpler, fewer lines of code |
| **Scalability**            | ✅ Highly modular & structured       | ❌ Less modular, relies on agent internals |
| **Control Over Workflow**  | ✅ Explicit node transitions         | ❌ Agent decides actions |
| **Tool Invocation**        | ✅ Manual, explicit execution        | ✅ Automatic but less controllable |
| **Chat History Handling**  | ✅ Persistent across messages       | ❌ Needs external storage |
| **Debugging**              | ✅ Clear execution tracking          | ❌ Harder to debug |

#### **Best Choice?**
- **For a simple chatbot with tool usage** → `agent_service.py` (easier to set up).
- **For a production-ready, scalable chatbot with structured workflow** → `chat_service.py` (better control and history handling).

🚀 **If you're building a serious Gen AI application, `chat_service.py` is the better choice!**