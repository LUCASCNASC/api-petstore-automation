import pytest
import requests
from datetime import datetime
from config import BASE_URL
API_PATH = "/store/order"

@pytest.fixture
def order_payload_delete():
    return {
        "id": 1003,
        "petId": 12345678,
        "quantity": 3,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }

def test_delete_order_success(order_payload_delete):
    requests.post(f"{BASE_URL}{API_PATH}", json=order_payload_delete)
    response = requests.delete(f"{BASE_URL}{API_PATH}/{order_payload_delete['id']}")
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    # Garante que foi deletado
    get_response = requests.get(f"{BASE_URL}{API_PATH}/{order_payload_delete['id']}")
    assert get_response.status_code == 404

@pytest.mark.parametrize("order_id,expected_status", [
    (99999999, [404, 400]),
    ("invalid", [400, 404])
])
def test_delete_order_invalid(order_id, expected_status):
    response = requests.delete(f"{BASE_URL}{API_PATH}/{order_id}")
    assert response.status_code in expected_status

def test_delete_order_without_id():
    response = requests.delete(f"{BASE_URL}{API_PATH}/")
    assert response.status_code in [405, 404, 400]