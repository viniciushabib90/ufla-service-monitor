from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "UFLA Service Monitor"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_services():
    response = client.get("/services")

    assert response.status_code == 200
    assert response.json()["total"] == 3
    assert len(response.json()["services"]) == 3
