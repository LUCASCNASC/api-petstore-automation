import pytest
import requests
from config import BASE_URL
API_PATH = "/user/createWithArray"

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
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [200, 201]
    assert "message" in response.text or "ok" in response.text.lower()
    # Limpeza
    for user in users:
        requests.delete(f"{BASE_URL}/user/{user['username']}")

def test_create_users_with_array_empty():
    response = requests.post(f"{BASE_URL}{API_PATH}", json=[])
    assert response.status_code in [400, 405, 422]

def test_create_users_with_array_missing_fields():
    users = [
        {
            "id": 10014,
            "firstName": "User",
            "lastName": "ArrayNoUsername",
            "email": "noarrayusername@email.com",
            "password": "passarray",
            "phone": "123000125",
            "userStatus": 1
            # "username" omitido
        }
    ]
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [400, 405]

def test_create_users_with_array_duplicate():
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
            "id": 10007,
            "username": "userarray1",
            "firstName": "UserDuplicate",
            "lastName": "ArrayOneDup",
            "email": "userarray1dup@email.com",
            "password": "passdup",
            "phone": "123000126",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{BASE_URL}{API_PATH}", json=users)
    assert response.status_code in [409, 200]
    # Limpeza
    requests.delete(f"{BASE_URL}/user/userarray1")