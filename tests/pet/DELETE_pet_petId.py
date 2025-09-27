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