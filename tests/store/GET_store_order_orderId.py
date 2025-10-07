import requests
from config import BASE_URL
from datetime import datetime
API_PATH = "/store/order"

# Cria um pedido para garantir que exista
def test_get_order_by_id_success():
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

def test_get_order_by_id_nonexistent():
    order_id = 99999999
    response = requests.get(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code == 404

def test_get_order_by_id_invalid():
    order_id = "invalid"
    response = requests.get(f"{BASE_URL}/{API_PATH}/{order_id}")
    assert response.status_code in [400, 404]

# Cria, deleta e tenta buscar
def test_get_order_by_id_deleted():
    payload = {
        "id": 1004,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    requests.delete(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    response = requests.get(f"{BASE_URL}/{API_PATH}/{payload['id']}")
    assert response.status_code == 404