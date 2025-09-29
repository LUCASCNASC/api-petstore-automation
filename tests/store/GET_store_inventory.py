import requests
from config import BASE_URL
API_PATH = "/store/inventory"

def test_get_inventory_success():
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Verifica se há pelo menos uma chave de status no inventário
    assert len(data) > 0

def test_get_inventory_structure():
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    assert response.status_code == 200
    data = response.json()
    # Verifica se os valores são inteiros ou zero
    for value in data.values():
        assert isinstance(value, int)
        assert value >= 0

def test_get_inventory_with_headers():
    # Testa passando headers customizados
    headers = {"Accept": "application/json"}
    response = requests.get(f"{BASE_URL}/{API_PATH}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)