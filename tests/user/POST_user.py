import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_user_success():
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
    response = requests.post(f"{BASE_URL}/user", json=user)
    assert response.status_code == 200 or response.status_code == 201
    assert "message" in response.text or "ok" in response.text.lower()