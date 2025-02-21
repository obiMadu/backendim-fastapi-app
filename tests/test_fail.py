from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_failing_root():
    # This will fail because of the wrong expected message
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wrong Message"}


def test_failing_item():
    # This will fail because of the missing field assertion
    response = client.get("/items/99")
    assert response.status_code == 200
    assert "nonexistent_field" in response.json()
