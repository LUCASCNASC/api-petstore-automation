import requests
from config import BASE_URL
API_PATH = "/pet"

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
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    pet_id = payload["id"]
    new_name = "RexFormUpdated"
    new_status = "sold"
    # Atualiza o pet com form data
    response = requests.post(
        f"{BASE_URL}/{API_PATH}/{pet_id}",
        data={"name": new_name, "status": new_status}
    )
    assert response.status_code == 200

    # Consulta para validar se foi atualizado
    pet_response = requests.get(f"{BASE_URL}/{API_PATH}/{pet_id}")
    pet = pet_response.json()
    assert pet["name"] == new_name
    assert pet["status"] == new_status

def test_update_pet_with_form_invalid_id():
    pet_id = "invalid"
    response = requests.post(
        f"{BASE_URL}/{API_PATH}/{pet_id}",
        data={"name": "Test", "status": "sold"}
    )
    assert response.status_code in [400, 404]

def test_update_pet_with_form_missing_fields():
    # Cria um pet
    payload = {
        "id": 12345680,
        "category": {"id": 1, "name": "dog"},
        "name": "NoFields",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    pet_id = payload["id"]
    # Não envia nenhum campo para atualização
    response = requests.post(
        f"{BASE_URL}/{API_PATH}/{pet_id}",
        data={}
    )
    # Pode retornar erro ou manter original
    assert response.status_code in [200, 400]
    pet_response = requests.get(f"{BASE_URL}/{API_PATH}/{pet_id}")
    pet = pet_response.json()
    # Se não atualizou, mantém o nome original
    assert pet["name"] == payload["name"]

def test_update_pet_with_form_nonexistent_id():
    pet_id = 99999999
    response = requests.post(
        f"{BASE_URL}/{API_PATH}/{pet_id}",
        data={"name": "ShouldNotExist", "status": "pending"}
    )
    assert response.status_code in [404, 400]