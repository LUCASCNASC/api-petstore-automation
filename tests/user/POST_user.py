import pytest
import requests
from config import BASE_URL
API_PATH = "/user"

@pytest.fixture
def user_create():
    user = {
        "id": 10009,
        "username": "usercreate",
        "firstName": "User",
        "lastName": "Create",
        "email": "usercreate@email.com",
        "password": "passcreate",
        "phone": "555444333",
        "userStatus": 1
    }
    yield user
    requests.delete(f"{BASE_URL}{API_PATH}/{user['username']}")

def test_create_user_success(user_create):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=user_create)
    assert response.status_code in [200, 201], f"Status inesperado: {response.status_code}"
    assert "message" in response.text or "ok" in response.text.lower()

@pytest.mark.parametrize("user,expected_status", [
    ({
        # "username" omitido
        "id": 10010,
        "firstName": "User",
        "lastName": "Create",
        "email": "usercreate2@email.com",
        "password": "passcreate2",
        "phone": "555444334",
        "userStatus": 1
    }, [400, 405]),
    ({
        "id": 10011,
        "username": "userinvalidemail",
        "firstName": "User",
        "lastName": "InvalidEmail",
        "email": "not-an-email",
        "password": "pass123",
        "phone": "555444335",
        "userStatus": 1
    }, [400, 422])
])
def test_create_user_invalid_cases(user, expected_status):
    response = requests.post(f"{BASE_URL}{API_PATH}", json=user)
    assert response.status_code in expected_status

def test_create_user_empty_body():
    response = requests.post(f"{BASE_URL}{API_PATH}", json={})
    assert response.status_code in [400, 405]

def test_create_user_duplicate_username(user_create):
    # Cria usuário original
    requests.post(f"{BASE_URL}{API_PATH}", json=user_create)
    user_dup = user_create.copy()
    user_dup["id"] = 10012
    user_dup["email"] = "userduplicate@email.com"
    user_dup["firstName"] = "User"
    user_dup["lastName"] = "Duplicate"
    user_dup["password"] = "passdup"
    user_dup["phone"] = "555444336"
    response = requests.post(f"{BASE_URL}{API_PATH}", json=user_dup)
    assert response.status_code in [409, 200]
    requests.delete(f"{BASE_URL}{API_PATH}/{user_create['username']}")