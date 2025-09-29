import requests
from config import BASE_URL
from datetime import datetime
API_PATH = "/store/order"

def test_place_order_success():
    payload = {
        "id": 1001,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["petId"] == payload["petId"]
    assert resp_json["quantity"] == payload["quantity"]
    assert resp_json["status"] == payload["status"]
    assert resp_json["complete"] == payload["complete"]

def test_place_order_missing_required_fields():
    payload = {
        # "id" omitido
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [400, 405]

def test_place_order_invalid_type():
    payload = {
        "id": "stringInsteadInt", # tipo inválido
        "petId": 12345678,
        "quantity": "one", # tipo inválido
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [400, 422]

def test_place_order_empty_body():
    response = requests.post(f"{BASE_URL}/{API_PATH}", json={})
    assert response.status_code in [400, 405]

def test_place_order_duplicate_id():
    payload = {
        "id": 1001,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    # Depende da API, pode retornar 409 ou sobrescrever
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=payload)
    assert response.status_code in [200, 409]