import pytest
import requests
from config import BASE_URL

API_PATH = "/user"

@pytest.fixture
def user_delete():
    user = {
        "id": 10005,
        "username": "userdelete",
        "firstName": "User",
        "lastName": "Delete",
        "email": "userdelete@email.com",
        "password": "passdelete",
        "phone": "777888999",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=user)
    yield user
    # Nenhum cleanup necessário, pois será deletado no teste

def test_delete_user_success(user_delete):
    response = requests.delete(f"{BASE_URL}{API_PATH}/{user_delete['username']}")
    assert response.status_code == 200
    get_response = requests.get(f"{BASE_URL}{API_PATH}/{user_delete['username']}")
    assert get_response.status_code == 404

@pytest.mark.parametrize("username,expected_status", [
    ("usernotfound", [404, 400]),
    ("invalid!@#", [400, 404])
])
def test_delete_user_invalid(username, expected_status):
    response = requests.delete(f"{BASE_URL}{API_PATH}/{username}")
    assert response.status_code in expected_status

def test_delete_user_empty_username():
    response = requests.delete(f"{BASE_URL}{API_PATH}/")
    assert response.status_code in [405, 404, 400]