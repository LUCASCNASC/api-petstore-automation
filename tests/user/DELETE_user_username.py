import requests
from config import BASE_URL
API_PATH = "/user"

def test_delete_user_success():
    # Cria o usuário para garantir que existe
    user = {
        "id": 10005,
        "username": "userdelete",
        "firstName": "User",
        "lastName": "Delete",
        "email": "userdelete@email.com",
        "password": "passdelete",
        "phone": "777888999",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=user)

    response = requests.delete(f"{BASE_URL}/{API_PATH}/{user['username']}")
    assert response.status_code == 200

    # Verifica se foi deletado
    get_response = requests.get(f"{BASE_URL}/{API_PATH}/{user['username']}")
    assert get_response.status_code == 404