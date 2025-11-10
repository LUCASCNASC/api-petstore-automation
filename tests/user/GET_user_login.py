import pytest
import requests
from config import BASE_URL
API_PATH = "/user/login"

@pytest.fixture
def user_login():
    user = {
        "id": 10006,
        "username": "userlogin",
        "firstName": "User",
        "lastName": "Login",
        "email": "userlogin@email.com",
        "password": "passlogin",
        "phone": "123123123",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}/user", json=user)
    yield user
    requests.delete(f"{BASE_URL}/user/{user['username']}")

def test_login_user_success(user_login):
    response = requests.get(
        f"{BASE_URL}{API_PATH}",
        params={"username": user_login["username"], "password": user_login["password"]}
    )
    assert response.status_code == 200
    assert "logged in user session" in response.text.lower() or "ok" in response.text.lower()

@pytest.mark.parametrize("user,passwd,expected_status", [
    (
        {
            "id": 10007,
            "username": "userloginwrong",
            "firstName": "User",
            "lastName": "LoginWrong",
            "email": "userloginwrong@email.com",
            "password": "passright",
            "phone": "321321321",
            "userStatus": 1
        }, "wrongpassword", [400, 401]
    ),
    (
        None, None, [400, 404, 401]  # Nonexistent user, handled separately
    )
])
def test_login_user_wrong_password_and_nonexistent(user, passwd, expected_status):
    if user is not None:
        # Wrong password
        requests.post(f"{BASE_URL}/user", json=user)
        response = requests.get(
            f"{BASE_URL}{API_PATH}",
            params={"username": user["username"], "password": passwd}
        )
        assert response.status_code in expected_status
        assert "error" in response.text.lower() or "invalid" in response.text.lower()
        requests.delete(f"{BASE_URL}/user/{user['username']}")
    else:
        # Nonexistent
        response = requests.get(
            f"{BASE_URL}{API_PATH}",
            params={"username": "notexist", "password": "any"}
        )
        assert response.status_code in expected_status

def test_login_user_missing_params():
    response = requests.get(f"{BASE_URL}{API_PATH}")
    assert response.status_code in [400, 404]

@pytest.fixture
def user_login_empty():
    user = {
        "id": 10008,
        "username": "userloginempty",
        "firstName": "User",
        "lastName": "LoginEmpty",
        "email": "userloginempty@email.com",
        "password": "passloginempty",
        "phone": "111222333",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}/user", json=user)
    yield user
    requests.delete(f"{BASE_URL}/user/{user['username']}")

def test_login_user_empty_password(user_login_empty):
    response = requests.get(
        f"{BASE_URL}{API_PATH}",
        params={"username": user_login_empty["username"], "password": ""}
    )
    assert response.status_code in [400, 401]