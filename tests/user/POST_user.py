import requests
from config import BASE_URL
API_PATH = "/user"

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
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=user)
    assert response.status_code == 200 or response.status_code == 201
    assert "message" in response.text or "ok" in response.text.lower()

def test_create_user_missing_required_fields():
    user = {
        # "username" omitido
        "id": 10010,
        "firstName": "User",
        "lastName": "Create",
        "email": "usercreate2@email.com",
        "password": "passcreate2",
        "phone": "555444334",
        "userStatus": 1
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=user)
    assert response.status_code in [400, 405]

def test_create_user_invalid_email():
    user = {
        "id": 10011,
        "username": "userinvalidemail",
        "firstName": "User",
        "lastName": "InvalidEmail",
        "email": "not-an-email",
        "password": "pass123",
        "phone": "555444335",
        "userStatus": 1
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=user)
    assert response.status_code in [400, 422]

def test_create_user_empty_body():
    response = requests.post(f"{BASE_URL}/{API_PATH}", json={})
    assert response.status_code in [400, 405]

def test_create_user_duplicate_username():
    user = {
        "id": 10012,
        "username": "usercreate",
        "firstName": "User",
        "lastName": "Duplicate",
        "email": "userduplicate@email.com",
        "password": "passdup",
        "phone": "555444336",
        "userStatus": 1
    }
    response = requests.post(f"{BASE_URL}/{API_PATH}", json=user)
    assert response.status_code in [409, 200]