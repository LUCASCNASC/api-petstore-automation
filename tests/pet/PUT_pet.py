import requests
from config import BASE_URL
API_PATH = "/pet"

def test_update_pet_success():
    payload = {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "Rex Atualizado",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["name"] == payload["name"]
    assert resp_json["status"] == payload["status"]

def test_update_pet_nonexistent_id():
    payload = {
        "id": 99999999,
        "category": {"id": 1, "name": "dog"},
        "name": "NotFound",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [404, 400]

def test_update_pet_invalid_type():
    payload = {
        "id": "invalid",
        "category": {"id": 1, "name": "dog"},
        "name": "Invalid",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [400, 422]

def test_update_pet_missing_required_fields():
    payload = {
        # "id" omitido
        "category": {"id": 1, "name": "dog"},
        "name": "NoId",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [400, 405]

def test_update_pet_empty_body():
    response = requests.put(f"{BASE_URL}/{API_PATH}", json={})
    assert response.status_code in [400, 405]