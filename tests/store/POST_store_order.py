import pytest
import requests
from datetime import datetime
from config import BASE_URL
API_PATH = "/store/order"

@pytest.fixture
def valid_order_payload():
    return {
        "id": 1001,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }

def test_place_order_success(valid_order_payload):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=valid_order_payload)
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    resp_json = response.json()
    assert resp_json["id"] == valid_order_payload["id"]
    assert resp_json["petId"] == valid_order_payload["petId"]
    assert resp_json["quantity"] == valid_order_payload["quantity"]
    assert resp_json["status"] == valid_order_payload["status"]
    assert resp_json["complete"] == valid_order_payload["complete"]

@pytest.mark.parametrize("payload,expected_status", [
    ({
        # id omitido
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }, [400, 405]),
    ({
        "id": "stringInsteadInt", # tipo inválido
        "petId": 12345678,
        "quantity": "one", # tipo inválido
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }, [400, 422]),
    ({}, [400, 405])
])
def test_place_order_invalid_cases(payload, expected_status):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=payload)
    assert response.status_code in expected_status, f"Status inesperado: {response.status_code}"

def test_place_order_duplicate_id(valid_order_payload):
    # Cria o pedido com mesmo id duas vezes
    requests.post(f"{BASE_URL}{API_PATH}", json=valid_order_payload)
    response = requests.post(f"{BASE_URL}{API_PATH}", json=valid_order_payload)
    assert response.status_code in [200, 409]
    # Limpeza
    requests.delete(f"{BASE_URL}{API_PATH}/{valid_order_payload['id']}")