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