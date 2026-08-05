from fastapi.testclient import TestClient

from backend.main import app

VALID_PAYLOAD = {
    "location": "mumbai",
    "carpet_area_sqft": 1200.0,
    "floor_num": 5,
    "bathroom": 2,
    "balcony": 1,
    "furnishing": "Semi-Furnished",
    "transaction": "Resale",
    "ownership": "Freehold",
    "facing": "East",
}


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_predict_happy_path():
    with TestClient(app) as client:
        response = client.post("/api/predict", json=VALID_PAYLOAD)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert isinstance(data["predicted_price"], float)


def test_predict_invalid_input():
    payload = {**VALID_PAYLOAD, "carpet_area_sqft": "not-a-number"}
    with TestClient(app) as client:
        response = client.post("/api/predict", json=payload)
        assert response.status_code == 422
