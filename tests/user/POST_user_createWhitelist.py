import pytest
import requests
from config import BASE_URL
API_PATH = "/user/createWithList"

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
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [200, 201]
    assert "message" in response.text or "ok" in response.text.lower()
    # Limpeza
    for user in users:
        requests.delete(f"{BASE_URL}/user/{user['username']}")

def test_create_users_with_list_empty():
    response = requests.post(f"{BASE_URL}{API_PATH}", json=[])
    assert response.status_code in [400, 405, 422]

def test_create_users_with_list_missing_fields():
    users = [
        {
            "id": 10013,
            # "username" omitido
            "firstName": "User",
            "lastName": "ListNoUsername",
            "email": "nousername@email.com",
            "password": "passlist",
            "phone": "123456789",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [400, 405]

def test_create_users_with_list_duplicate():
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
            "id": 10001,
            "username": "userlist1",
            "firstName": "UserDuplicate",
            "lastName": "ListOneDup",
            "email": "userlist1dup@email.com",
            "password": "passdup",
            "phone": "123456780",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [409, 200]
    # Limpeza
    requests.delete(f"{BASE_URL}/user/userlist1")