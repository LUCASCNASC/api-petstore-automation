import pytest
import requests
from config import BASE_URL

API_PATH = "/pet"

@pytest.fixture
def valid_payload():
    return {
        "id": 12345678,
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }

def test_add_pet_success(valid_payload):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=valid_payload)
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    resp_json = response.json()
    assert resp_json["id"] == valid_payload["id"]
    assert resp_json["name"] == valid_payload["name"]
    assert resp_json["status"] == valid_payload["status"]
    # Limpeza
    requests.delete(f"{BASE_URL}{API_PATH}/{valid_payload['id']}")

@pytest.mark.parametrize("payload,expected_status", [
    ({ # id omitido
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }, [400, 405]),
    ({ # tipo inválido
        "id": "string_instead_int",
        "category": {"id": 1, "name": "dog"},
        "name": "Rex",
        "photoUrls": ["https://example.com/img1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }, [400, 422]),
    ({}, [400, 405]) # corpo vazio
])
def test_add_pet_invalid_cases(payload, expected_status):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=payload)
    assert response.status_code in expected_status, f"Status inesperado: {response.status_code}"

def test_add_pet_duplicate_id(valid_payload):
    # Cria o pet
    requests.post(f"{BASE_URL}{API_PATH}", json=valid_payload)
    # Tenta criar de novo com mesmo id
    payload_dup = valid_payload.copy()
    payload_dup["name"] = "RexDuplicated"
    response = requests.post(f"{BASE_URL}{API_PATH}", json=payload_dup)
    assert response.status_code in [200, 409]
    # Limpeza
    requests.delete(f"{BASE_URL}{API_PATH}/{valid_payload['id']}")