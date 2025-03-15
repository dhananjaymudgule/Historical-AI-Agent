
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_email_sending():
    response = client.post("/email/send-otp/", json={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "OTP sent to your email."
