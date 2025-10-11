import pytest
import requests
from config import BASE_URL

API_PATH = "/pet"

@pytest.fixture
def valid_update_payload():
    return {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "Rex Atualizado",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "pending"
    }

def test_update_pet_success(valid_update_payload):
    response = requests.put(f"{BASE_URL}{API_PATH}", json=valid_update_payload)
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    resp_json = response.json()
    assert resp_json["id"] == valid_update_payload["id"]
    assert resp_json["name"] == valid_update_payload["name"]
    assert resp_json["status"] == valid_update_payload["status"]

@pytest.mark.parametrize("payload,expected_status", [
    ({
        "id": 99999999,
        "category": {"id": 1, "name": "dog"},
        "name": "NotFound",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }, [404, 400]),
    ({
        "id": "invalid",
        "category": {"id": 1, "name": "dog"},
        "name": "Invalid",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }, [400, 422]),
    ({
        # "id" omitido
        "category": {"id": 1, "name": "dog"},
        "name": "NoId",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [],
        "status": "pending"
    }, [400, 405]),
    ({}, [400, 405])
])
def test_update_pet_invalid_cases(payload, expected_status):
    response = requests.put(f"{BASE_URL}{API_PATH}", json=payload)
    assert response.status_code in expected_status, f"Status inesperado: {response.status_code}"