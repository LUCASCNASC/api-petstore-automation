import requests
from config import BASE_URL
API_PATH = "/pet"

def test_delete_pet_success():
    # Primeiro, cria um pet para garantir que ele exista para deletar
    payload = {
        "id": 12345680,
        "category": {"id": 1, "name": "dog"},
        "name": "RexDelete",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    pet_id = payload["id"]
    # Deleta o pet
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{pet_id}")
    assert response.status_code == 200

    # Valida se realmente foi deletado
    get_response = requests.get(f"{BASE_URL}/{API_PATH}/{pet_id}")
    assert get_response.status_code == 404

def test_delete_nonexistent_pet():
    # Tenta deletar um pet que não existe
    pet_id = 99999999
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{pet_id}")
    # Pode variar entre 404 ou 400, dependendo da API
    assert response.status_code in [404, 400]

def test_delete_pet_invalid_id():
    # Tenta deletar usando um ID inválido (string)
    pet_id = "invalid"
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{pet_id}")
    assert response.status_code in [400, 404]

def test_delete_pet_without_id():
    # Tenta deletar sem informar o ID
    response = requests.delete(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]