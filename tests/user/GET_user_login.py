import requests
from config import BASE_URL
API_PATH = "/user/login"

def test_login_user_success():
    # Cria o usuário para garantir que existe
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

    response = requests.get(
        f"{BASE_URL}/{API_PATH}",
        params={"username": user["username"], "password": user["password"]}
    )
    assert response.status_code == 200
    assert "logged in user session" in response.text.lower() or "ok" in response.text.lower()

def test_login_user_wrong_password():
    # Usuário existe, mas senha errada
    user = {
        "id": 10007,
        "username": "userloginwrong",
        "firstName": "User",
        "lastName": "LoginWrong",
        "email": "userloginwrong@email.com",
        "password": "passright",
        "phone": "321321321",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}/user", json=user)
    response = requests.get(
        f"{BASE_URL}/{API_PATH}",
        params={"username": user["username"], "password": "wrongpassword"}
    )
    assert response.status_code in [400, 401]
    assert "error" in response.text.lower() or "invalid" in response.text.lower()

def test_login_user_nonexistent():
    response = requests.get(
        f"{BASE_URL}/{API_PATH}",
        params={"username": "notexist", "password": "any"}
    )
    assert response.status_code in [400, 404, 401]

def test_login_user_missing_params():
    response = requests.get(
        f"{BASE_URL}/{API_PATH}"
    )
    assert response.status_code in [400, 404]

def test_login_user_empty_password():
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
    response = requests.get(
        f"{BASE_URL}/{API_PATH}",
        params={"username": user["username"], "password": ""}
    )
    assert response.status_code in [400, 401]