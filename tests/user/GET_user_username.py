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

def test_get_user_by_name_nonexistent():
    username = "notfounduser"
    response = requests.get(f"{BASE_URL}/{API_PATH}/{username}")
    assert response.status_code == 404

def test_get_user_by_name_invalid():
    username = "invalid!@#"
    response = requests.get(f"{BASE_URL}/{API_PATH}/{username}")
    assert response.status_code in [400, 404]

def test_get_user_by_name_empty():
    response = requests.get(f"{BASE_URL}/{API_PATH}/")
    assert response.status_code in [405, 404, 400]