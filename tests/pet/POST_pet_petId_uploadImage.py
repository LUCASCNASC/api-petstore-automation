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