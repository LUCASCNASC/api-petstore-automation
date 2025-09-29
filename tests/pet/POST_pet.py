import requests
from config import BASE_URL
API_PATH = "/pet"

def test_add_pet_success():
    payload = {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["name"] == payload["name"]
    assert resp_json["status"] == payload["status"]

def test_add_pet_missing_required_fields():
    payload = {
        # "id" omitido
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    # Espera erro 400 ou similar
    assert response.status_code in [400, 405]

def test_add_pet_invalid_type():
    payload = {
        "id": "string_instead_int",  # tipo inválido
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [400, 422]

def test_add_pet_empty_body():
    response = requests.post(f"{BASE_URL}/{API_PATH}", json={})
    assert response.status_code in [400, 405]

def test_add_pet_duplicate_id():
    payload = {
        "id": 12345678,  # ID já utilizado
        "category": {"id": 1, "name": "dog"},
        "name": "RexDuplicated",
        "photoUrls": ["https://example.com/img2.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    # Depende da API, pode retornar 409 ou sobrescrever
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [200, 409]