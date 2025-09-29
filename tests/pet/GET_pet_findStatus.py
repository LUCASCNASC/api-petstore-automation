import requests
from config import BASE_URL
API_PATH = "/pet/findByStatus"

def test_find_pet_by_status_success():
    status = "pending"
    response = requests.get(f"{BASE_URL}/{API_PATH}", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    for pet in pets:
        assert pet["status"] == status

def test_find_pet_by_status_invalid():
    # Testa status inválido
    status = "unknownstatus"
    response = requests.get(f"{BASE_URL}/{API_PATH}", params={"status": status})
    # Pode retornar 200 com lista vazia ou 400
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert pets == [] or all(pet["status"] == status for pet in pets)

def test_find_pet_by_status_missing_param():
    # Não envia o parâmetro status
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    # Pode retornar erro ou lista padrão
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert isinstance(pets, list)

def test_find_pet_by_status_multiple():
    # Busca múltiplos status
    status = "available,pending"
    response = requests.get(f"{BASE_URL}/{API_PATH}", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    for pet in pets:
        assert pet["status"] in status.split(",")