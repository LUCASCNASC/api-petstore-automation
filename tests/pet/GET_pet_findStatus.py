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

# Testa status inválido
def test_find_pet_by_status_invalid():
    status = "unknownstatus"
    response = requests.get(f"{BASE_URL}/{API_PATH}", params={"status": status})
    # Pode retornar 200 com lista vazia ou 400
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert pets == [] or all(pet["status"] == status for pet in pets)

# Não envia o parâmetro status
def test_find_pet_by_status_missing_param():
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    # Pode retornar erro ou lista padrão
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        pets = response.json()
        assert isinstance(pets, list)

# Busca múltiplos status
def test_find_pet_by_status_multiple():
    status = "available,pending"
    response = requests.get(f"{BASE_URL}/{API_PATH}", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    for pet in pets:
        assert pet["status"] in status.split(",")