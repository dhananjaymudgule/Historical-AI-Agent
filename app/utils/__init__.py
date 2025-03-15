from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat/")
async def chat_endpoint(user_input: UserInput):
    state = {"user_message": user_input.message}
    response = graph.run(state)
    return {"reply": response["message"]}
