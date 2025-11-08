import requests
from config import BASE_URL
API_PATH = "/store/inventory"

def test_get_inventory_success():
    response = requests.get(f"{BASE_URL}{API_PATH}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0

def test_get_inventory_structure():
    response = requests.get(f"{BASE_URL}{API_PATH}")
    assert response.status_code == 200
    data = response.json()
    for value in data.values():
        assert isinstance(value, int)
        assert value >= 0

def test_get_inventory_with_headers():
    headers = {"Accept": "application/json"}
    response = requests.get(f"{BASE_URL}{API_PATH}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)