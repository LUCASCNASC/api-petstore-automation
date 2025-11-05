import pytest
import requests
from config import BASE_URL

API_PATH = "/pet"

@pytest.fixture
def dog_payload():
    return {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "RexGet",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }

@pytest.fixture
def cat_payload():
    return {
        "id": 12345679,
        "category": {"id": 1, "name": "cat"},
        "name": "MiaDeleted",
        "photoUrls": ["https://example.com/img2.jpg"],
        "tags": [{"id": 2, "name": "grumpy"}],
        "status": "available"
    }

@pytest.fixture
def create_dog(dog_payload):
    requests.post(f"{BASE_URL}{API_PATH}", json=dog_payload)
    yield dog_payload["id"]
    requests.delete(f"{BASE_URL}{API_PATH}/{dog_payload['id']}")

def test_get_pet_by_id_success(create_dog, dog_payload):
    response = requests.get(f"{BASE_URL}{API_PATH}/{create_dog}")
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    pet = response.json()
    assert pet["id"] == dog_payload["id"]
    assert pet["name"] == dog_payload["name"]
    assert pet["status"] == dog_payload["status"]

@pytest.mark.parametrize("pet_id,expected_status", [
    (99999999, [404]),
    ("invalid", [400, 404]),
])
def test_get_pet_by_id_invalids(pet_id, expected_status):
    response = requests.get(f"{BASE_URL}{API_PATH}/{pet_id}")
    assert response.status_code in expected_status

def test_get_pet_by_id_without_id():
    response = requests.get(f"{BASE_URL}{API_PATH}/")
    assert response.status_code in [405, 404, 400]

def test_get_pet_by_id_deleted(cat_payload):
    # Cria e deleta
    requests.post(f"{BASE_URL}{API_PATH}", json=cat_payload)
    requests.delete(f"{BASE_URL}{API_PATH}/{cat_payload['id']}")
    response = requests.get(f"{BASE_URL}{API_PATH}/{cat_payload['id']}")
    assert response.status_code == 404