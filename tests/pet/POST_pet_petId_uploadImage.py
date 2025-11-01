import pytest
import requests
from config import BASE_URL
API_PATH = "/pet"

@pytest.fixture
def existing_pet_id():
    # Altere conforme necessário para garantir um pet existente
    pet_id = 1
    return pet_id

def test_upload_pet_image_success(existing_pet_id):
    url = f"{BASE_URL}{API_PATH}/{existing_pet_id}/uploadImage"
    metadata = "Foto do cachorro feliz"
    files = {
        "file": ("dog.jpg", b"fake image content", "image/jpeg")
    }
    data = {
        "additionalMetadata": metadata
    }
    response = requests.post(url, data=data, files=files)
    assert response.status_code == 200, f"Esperado 200, veio {response.status_code}"
    json_data = response.json()
    assert "code" in json_data
    assert "type" in json_data
    assert "message" in json_data

def test_upload_pet_image_missing_file(existing_pet_id):
    url = f"{BASE_URL}{API_PATH}/{existing_pet_id}/uploadImage"
    data = {
        "additionalMetadata": "Sem arquivo"
    }
    response = requests.post(url, data=data)
    assert response.status_code in [400, 422]

@pytest.mark.parametrize("pet_id,expected_status", [
    ("invalid", [400, 404]),
    (99999999, [404, 400])
])
def test_upload_pet_image_invalid_or_nonexistent_id(pet_id, expected_status):
    url = f"{BASE_URL}{API_PATH}/{pet_id}/uploadImage"
    files = {
        "file": ("dog.jpg", b"fake image content", "image/jpeg")
    }
    response = requests.post(url, files=files)
    assert response.status_code in expected_status