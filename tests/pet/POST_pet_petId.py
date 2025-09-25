import requests
from config import BASE_URL

def test_update_pet_with_form_success():
    # Primeiro, cria um pet para garantir que ele exista
    payload = {
        "id": 12345679,
        "category": {"id": 1, "name": "dog"},
        "name": "RexForm",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/pet", json=payload)

    pet_id = payload["id"]
    new_name = "RexFormUpdated"
    new_status = "sold"
    # Atualiza o pet com form data
    response = requests.post(
        f"{BASE_URL}/pet/{pet_id}",
        data={"name": new_name, "status": new_status}
    )
    assert response.status_code == 200

    # Consulta para validar se foi atualizado
    pet_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    pet = pet_response.json()
    assert pet["name"] == new_name
    assert pet["status"] == new_status