import requests
from config import BASE_URL
API_PATH = "/user"

def test_get_user_by_name_success():
    # Garante que o usuário existe antes de buscar
    user = {
        "id": 10003,
        "username": "userget",
        "firstName": "User",
        "lastName": "Get",
        "email": "userget@email.com",
        "password": "passget",
        "phone": "111222333",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}/{API_PATH}", json=user)

    response = requests.get(f"{BASE_URL}/{API_PATH}/{user['username']}")
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["username"] == user["username"]
    assert resp_json["id"] == user["id"]
    assert resp_json["email"] == user["email"]