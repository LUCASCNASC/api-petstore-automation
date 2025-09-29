import requests
from datetime import datetime
from config import BASE_URL
API_PATH = "/store/order"

def test_delete_order_success():
    # Cria um pedido para garantir que existe para deletar
    payload = {
        "id": 1003,
        "petId": 12345678,
        "quantity": 3,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    # Deleta o pedido
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert response.status_code == 200

    # Garante que o pedido foi deletado
    get_response = requests.get(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert get_response.status_code == 404

def test_delete_order_nonexistent_id():
    # Tenta deletar um pedido que não existe
    order_id = 99999999
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code in [404, 400]

def test_delete_order_invalid_id():
    # Tenta deletar com id inválido (string)
    order_id = "invalid"
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code in [400, 404]

def test_delete_order_without_id():
    # Tenta deletar sem informar o id
    response = requests.delete(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]