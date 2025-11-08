import pytest
import requests
from config import BASE_URL
API_PATH = "/user"

@pytest.fixture
def user_get():
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
    requests.post(f"{BASE_URL}{API_PATH}", json=user)
    yield user
    requests.delete(f"{BASE_URL}{API_PATH}/{user['username']}")

def test_get_user_by_name_success(user_get):
    response = requests.get(f"{BASE_URL}{API_PATH}/{user_get['username']}")
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["username"] == user_get["username"]
    assert resp_json["id"] == user_get["id"]
    assert resp_json["email"] == user_get["email"]

@pytest.mark.parametrize("username,expected_status", [
    ("notfounduser", [404]),
    ("invalid!@#", [400, 404])
])
def test_get_user_by_name_invalid(username, expected_status):
    response = requests.get(f"{BASE_URL}{API_PATH}/{username}")
    assert response.status_code in expected_status

def test_get_user_by_name_empty():
    response = requests.get(f"{BASE_URL}{API_PATH}/")
    assert response.status_code in [405, 404, 400]