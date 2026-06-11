# app/tests/test_main.py
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ask_endpoint():
    response = client.post("/ask", json={"question": "¿Qué es la IA?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "session_id" in data


def test_history_not_found():
    response = client.get("/history/sesion_invalida_123")
    assert response.status_code == 404
