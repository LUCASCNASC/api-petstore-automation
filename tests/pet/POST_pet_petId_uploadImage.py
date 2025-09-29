import requests
from config import BASE_URL
API_PATH = "/pet"

def test_upload_pet_image_success():
    # Dados do teste
    pet_id = 1  # ID de um pet existente na API (altere conforme necessário)
    url = f"{BASE_URL}/{API_PATH}/{pet_id}/uploadImage"
    metadata = "Foto do cachorro feliz"
    # Crie um arquivo de imagem de teste (pode ser qualquer arquivo pequeno, até um .txt)
    files = {
        "file": ("dog.jpg", b"fake image content", "image/jpeg")
    }
    data = {
        "additionalMetadata": metadata
    }

    response = requests.post(url, data=data, files=files)
    assert response.status_code == 200
    json_data = response.json()
    # Valide se retornou as chaves esperadas
    assert "code" in json_data
    assert "type" in json_data
    assert "message" in json_data

def test_upload_pet_image_missing_file():
    pet_id = 1
    url = f"{BASE_URL}/{API_PATH}/{pet_id}/uploadImage"
    data = {
        "additionalMetadata": "Sem arquivo"
    }
    response = requests.post(url, data=data)
    assert response.status_code in [400, 422]

def test_upload_pet_image_invalid_id():
    pet_id = "invalid"
    url = f"{BASE_URL}/{API_PATH}/{pet_id}/uploadImage"
    files = {
        "file": ("dog.jpg", b"fake image content", "image/jpeg")
    }
    response = requests.post(url, files=files)
    assert response.status_code in [400, 404]

def test_upload_pet_image_nonexistent_id():
    pet_id = 99999999
    url = f"{BASE_URL}/{API_PATH}/{pet_id}/uploadImage"
    files = {
        "file": ("dog.jpg", b"fake image content", "image/jpeg")
    }
    response = requests.post(url, files=files)
    assert response.status_code in [404, 400]