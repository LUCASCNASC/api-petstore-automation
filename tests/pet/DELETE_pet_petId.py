import pytest
import requests
from config import BASE_URL

API_PATH = "/pet"

@pytest.fixture
def pet_payload():
    return {
        "id": 12345680,
        "category": {"id": 1, "name": "dog"},
        "name": "RexDelete",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }

@pytest.fixture
def create_and_cleanup_pet(pet_payload):
    # Cria o pet
    resp = requests.post(f"{BASE_URL}{API_PATH}", json=pet_payload)
    yield pet_payload["id"]
    # Garante limpeza (deleta se existir)
    requests.delete(f"{BASE_URL}{API_PATH}/{pet_payload['id']}")

def test_delete_pet_success(create_and_cleanup_pet):
    pet_id = create_and_cleanup_pet
    response = requests.delete(f"{BASE_URL}{API_PATH}/{pet_id}")
    assert response.status_code == 200, f"Esperado 200 ao deletar, veio {response.status_code}"

    get_response = requests.get(f"{BASE_URL}{API_PATH}/{pet_id}")
    assert get_response.status_code == 404, f"Esperado 404 após deleção, veio {get_response.status_code}"

@pytest.mark.parametrize("pet_id,expected_status", [
    (99999999, [404, 400]),         # Pet inexistente
    ("invalid", [400, 404]),        # ID inválido
])
def test_delete_pet_invalid_cases(pet_id, expected_status):
    response = requests.delete(f"{BASE_URL}{API_PATH}/{pet_id}")
    assert response.status_code in expected_status, f"Status inesperado: {response.status_code}"

def test_delete_pet_without_id():
    response = requests.delete(f"{BASE_URL}{API_PATH}/")
    assert response.status_code in [405, 404, 400], f"Status inesperado: {response.status_code}"