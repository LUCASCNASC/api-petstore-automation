import requests
from datetime import datetime

BASE_URL = "https://petstore.swagger.io/v2"

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
    requests.post(f"{BASE_URL}/store/order", json=payload)

    # Deleta o pedido
    response = requests.delete(f"{BASE_URL}/store/order/{payload['id']}")
    assert response.status_code == 200

    # Garante que o pedido foi deletado
    get_response = requests.get(f"{BASE_URL}/store/order/{payload['id']}")
    assert get_response.status_code == 404