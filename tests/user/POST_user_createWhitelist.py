import requests
from config import BASE_URL

def test_create_users_with_list_success():
    users = [
        {
            "id": 10001,
            "username": "userlist1",
            "firstName": "User",
            "lastName": "ListOne",
            "email": "userlist1@email.com",
            "password": "pass123",
            "phone": "123456789",
            "userStatus": 1
        },
        {
            "id": 10002,
            "username": "userlist2",
            "firstName": "User",
            "lastName": "ListTwo",
            "email": "userlist2@email.com",
            "password": "pass456",
            "phone": "987654321",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{BASE_URL}/user/createWithList", json=users)
    assert response.status_code == 200 or response.status_code == 201
    # A resposta geralmente é uma mensagem de sucesso (string ou objeto)
    assert "message" in response.text or "ok" in response.text.lower()