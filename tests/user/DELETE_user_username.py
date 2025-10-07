import requests
from config import BASE_URL
API_PATH = "/user"

# Cria o usuário para garantir que existe
def test_delete_user_success():
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

def test_delete_user_nonexistent():
    username = "usernotfound"
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{username}")
    assert response.status_code in [404, 400]

def test_delete_user_invalid_username():
    username = "invalid!@#"
    response = requests.delete(f"{BASE_URL}/{API_PATH}/{username}")
    assert response.status_code in [400, 404]

def test_delete_user_empty_username():
    response = requests.delete(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]