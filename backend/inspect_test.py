from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

payload = {
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

resp = client.post('/api/predict', json=payload)
print('status', resp.status_code)
print('text', resp.text)
try:
    print('json', resp.json())
except Exception as exc:
    print('json failed', exc)
