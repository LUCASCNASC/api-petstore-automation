import requests

BASE_URL = "https://petstore.swagger.io/v2"

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
    requests.post(f"{BASE_URL}/user", json=user)

    response = requests.delete(f"{BASE_URL}/user/{user['username']}")
    assert response.status_code == 200

    # Verifica se foi deletado
    get_response = requests.get(f"{BASE_URL}/user/{user['username']}")
    assert get_response.status_code == 404