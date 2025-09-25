import requests
from config import BASE_URL

def test_create_users_with_array_success():
    users = [
        {
            "id": 10007,
            "username": "userarray1",
            "firstName": "User",
            "lastName": "ArrayOne",
            "email": "userarray1@email.com",
            "password": "passarray1",
            "phone": "123000123",
            "userStatus": 1
        },
        {
            "id": 10008,
            "username": "userarray2",
            "firstName": "User",
            "lastName": "ArrayTwo",
            "email": "userarray2@email.com",
            "password": "passarray2",
            "phone": "123000124",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{BASE_URL}/user/createWithArray", json=users)
    assert response.status_code == 200 or response.status_code == 201
    assert "message" in response.text or "ok" in response.text.lower()