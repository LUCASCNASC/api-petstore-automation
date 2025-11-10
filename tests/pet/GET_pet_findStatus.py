import pytest
import requests
from config import BASE_URL
API_PATH = "/pet/findByStatus"

@pytest.mark.parametrize("status", ["pending"])
def test_find_pet_by_status_success(status):
    response = requests.get(f"{BASE_URL}{API_PATH}", params={"status": status})
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    pets = response.json()
    assert isinstance(pets, list)
    for pet in pets:
        assert pet["status"] == status

@pytest.mark.parametrize("status", ["unknownstatus"])
def test_find_pet_by_status_invalid(status):
    response = requests.get(f"{BASE_URL}{API_PATH}", params={"status": status})
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert pets == [] or all(pet["status"] == status for pet in pets)

def test_find_pet_by_status_missing_param():
    response = requests.get(f"{BASE_URL}{API_PATH}")
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert isinstance(pets, list)

def test_find_pet_by_status_multiple():
    status = "available,pending"
    response = requests.get(f"{BASE_URL}{API_PATH}", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    allowed_status = set(status.split(","))
    for pet in pets:
        assert pet["status"] in allowed_status