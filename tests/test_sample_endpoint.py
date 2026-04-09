from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sample_endpoint_returns_double():
    response = client.post("/api/sample", json={"value": 4})
    assert response.status_code == 200
    assert response.json() == {
        "input": 4,
        "output": 8,
        "message": "Sample endpoint returned a result.",
    }
