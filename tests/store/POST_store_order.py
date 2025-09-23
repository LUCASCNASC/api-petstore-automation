import requests
from datetime import datetime

BASE_URL = "https://petstore.swagger.io/v2"

def test_place_order_success():
    payload = {
        "id": 1001,
        "petId": 12345678,
        "quantity": 1,
        "shipDate": datetime.now().isoformat() + "Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == payload["id"]
    assert resp_json["petId"] == payload["petId"]
    assert resp_json["quantity"] == payload["quantity"]
    assert resp_json["status"] == payload["status"]
    assert resp_json["complete"] == payload["complete"]