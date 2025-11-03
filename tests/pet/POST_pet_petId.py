import pytest
import requests
from config import BASE_URL

API_PATH = "/pet"

@pytest.fixture
def pet_for_form_update():
    payload = {
        "id": 12345679,
        "category": {"id": 1, "name": "dog"},
        "name": "RexForm",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=payload)
    yield payload["id"]
    requests.delete(f"{BASE_URL}{API_PATH}/{payload['id']}")

@pytest.fixture
def pet_for_missing_fields():
    payload = {
        "id": 12345680,
        "category": {"id": 1, "name": "dog"},
        "name": "NoFields",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=payload)
    yield payload
    requests.delete(f"{BASE_URL}{API_PATH}/{payload['id']}")

def test_update_pet_with_form_success(pet_for_form_update):
    pet_id = pet_for_form_update
    new_name = "RexFormUpdated"
    new_status = "sold"
    response = requests.post(
        f"{BASE_URL}{API_PATH}/{pet_id}",
        data={"name": new_name, "status": new_status}
    )
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"

    pet_response = requests.get(f"{BASE_URL}{API_PATH}/{pet_id}")
    pet = pet_response.json()
    assert pet["name"] == new_name
    assert pet["status"] == new_status

@pytest.mark.parametrize("pet_id,expected_status", [
    ("invalid", [400, 404]),
    (99999999, [404, 400])
])
def test_update_pet_with_form_invalid_id(pet_id, expected_status):
    response = requests.post(
        f"{BASE_URL}{API_PATH}/{pet_id}",
        data={"name": "Test", "status": "sold"}
    )
    assert response.status_code in expected_status

def test_update_pet_with_form_missing_fields(pet_for_missing_fields):
    pet = pet_for_missing_fields
    pet_id = pet["id"]
    response = requests.post(
        f"{BASE_URL}{API_PATH}/{pet_id}",
        data={}
    )
    assert response.status_code in [200, 400]
    pet_response = requests.get(f"{BASE_URL}{API_PATH}/{pet_id}")
    pet_after = pet_response.json()
    assert pet_after["name"] == pet["name"]
