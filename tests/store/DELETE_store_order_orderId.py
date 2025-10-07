import requests
from datetime import datetime
from config import BASE_URL
API_PATH = "/store/order"

# Cria um pedido para garantir que existe para deletar
def test_delete_order_success():
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

# Tenta deletar um pedido que não existe
def test_delete_order_nonexistent_id():
    order_id = 99999999
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code in [404, 400]
    
# Tenta deletar com id inválido (string)
def test_delete_order_invalid_id():
    order_id = "invalid"
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code in [400, 404]

# Tenta deletar sem informar o id
def test_delete_order_without_id():
    response = requests.delete(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]