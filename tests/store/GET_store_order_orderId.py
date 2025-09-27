import requests
from config import BASE_URL
from datetime import datetime
API_PATH = "/store/order"

def test_get_order_by_id_success():
    # Cria um pedido para garantir que exista
    payload = {
        "id": 1002,
        "petId": 12345678,
        "quantity": 2,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)

    response = requests.get(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["petId"] == payload["petId"]
    assert resp_json["quantity"] == payload["quantity"]
    assert resp_json["status"] == payload["status"]
    assert resp_json["complete"] == payload["complete"]