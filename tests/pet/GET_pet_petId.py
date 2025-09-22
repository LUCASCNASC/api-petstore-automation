import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_get_pet_by_id_success():
    # Primeiro, cria um pet para garantir que ele exista
    payload = {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "RexGet",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/pet", json=payload)

    response = requests.get(f"{BASE_URL}/pet/{payload['id']}")
    assert response.status_code == 200
    pet = response.json()
    assert pet["id"] == payload["id"]
    assert pet["name"] == payload["name"]
    assert pet["status"] == payload["status"]