import requests
from config import BASE_URL
API_PATH = "/pet"

# Primeiro, cria um pet para garantir que ele exista
def test_get_pet_by_id_success():
    payload = {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "RexGet",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    response = requests.get(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert response.status_code == 200
    pet = response.json()
    assert pet["id"] == payload["id"]
    assert pet["name"] == payload["name"]
    assert pet["status"] == payload["status"]

def test_get_pet_by_id_nonexistent():
    pet_id = 99999999
    response = requests.get(f"{BASE_URL}/{API_PATH}/{pet_id}")
    assert response.status_code == 404

def test_get_pet_by_id_invalid_id():
    pet_id = "invalid"
    response = requests.get(f"{BASE_URL}/{API_PATH}/{pet_id}")
    assert response.status_code in [400, 404]

def test_get_pet_by_id_without_id():
    response = requests.get(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]

# Cria e deleta um pet, depois tenta buscar
def test_get_pet_by_id_deleted():
    payload = {
        "id": 12345679,
        "category": {"id": 1, "name": "cat"},
        "name": "MiaDeleted",
        "photoUrls": ["https://example.com/img2.jpg"],
        "tags": [{"id": 2, "name": "grumpy"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    requests.delete(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    response = requests.get(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert response.status_code == 404