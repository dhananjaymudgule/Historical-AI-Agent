from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_response():
    response = client.post("/chat/", json={"session_id": "test-session", "message": "Tell me about the Eiffel Tower"})
    assert response.status_code == 200
    assert "response" in response.json()
