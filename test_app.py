from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "RAG API"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_search():
    response = client.get("/search?query=test")
    assert response.status_code == 200
    assert response.json()["query"] == "test"
    assert len(response.json()["results"]) == 2
