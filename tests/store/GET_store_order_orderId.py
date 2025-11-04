import pytest
import requests
from datetime import datetime
from config import BASE_URL
API_PATH = "/store/order"

@pytest.fixture
def order_payload():
    return {
        "id": 1002,
        "petId": 12345678,
        "quantity": 2,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }

def test_get_order_by_id_success(order_payload):
    requests.post(f"{BASE_URL}{API_PATH}", json=order_payload)
    response = requests.get(f"{BASE_URL}{API_PATH}/{order_payload['id']}")
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    resp_json = response.json()
    assert resp_json["id"] == order_payload["id"]
    assert resp_json["petId"] == order_payload["petId"]
    assert resp_json["quantity"] == order_payload["quantity"]
    assert resp_json["status"] == order_payload["status"]
    assert resp_json["complete"] == order_payload["complete"]
    # Limpeza
    requests.delete(f"{BASE_URL}{API_PATH}/{order_payload['id']}")

@pytest.mark.parametrize("order_id,expected_status", [
    (99999999, [404]),
    ("invalid", [400, 404])
])
def test_get_order_by_id_invalid(order_id, expected_status):
    response = requests.get(f"{BASE_URL}{API_PATH}/{order_id}")
    assert response.status_code in expected_status

def test_get_order_by_id_deleted():
    payload = {
        "id": 1004,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=payload)
    requests.delete(f"{BASE_URL}{API_PATH}/{payload['id']}")
    response = requests.get(f"{BASE_URL}{API_PATH}/{payload['id']}")
    assert response.status_code == 404