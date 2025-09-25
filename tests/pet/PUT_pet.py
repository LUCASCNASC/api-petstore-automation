import requests
from config import BASE_URL

def test_update_pet_success():
    payload = {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "Rex Atualizado",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["name"] == payload["name"]
    assert resp_json["status"] == payload["status"]