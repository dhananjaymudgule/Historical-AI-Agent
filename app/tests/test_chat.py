# app/tests/test_chat.py


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_response():
    response = client.post("/chat/", json={"message": "Tell me about the Eiffel Tower"})
    assert response.status_code == 200
    assert "reply" in response.json()
