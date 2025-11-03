import pytest
import requests
from config import BASE_URL

API_PATH = "/user"

@pytest.fixture
def user_update():
    user = {
        "id": 10004,
        "username": "userupdate",
        "firstName": "User",
        "lastName": "Update",
        "email": "userupdate@email.com",
        "password": "passupdate",
        "phone": "444555666",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=user)
    yield user
    requests.delete(f"{BASE_URL}{API_PATH}/{user['username']}")

def test_update_user_success(user_update):
    updated_user = user_update.copy()
    updated_user["firstName"] = "UserUpdated"
    updated_user["email"] = "updateduser@email.com"
    response = requests.put(f"{BASE_URL}{API_PATH}/{user_update['username']}", json=updated_user)
    assert response.status_code in [200, 201]
    # Valida se foi atualizado
    get_response = requests.get(f"{BASE_URL}{API_PATH}/{user_update['username']}")
    resp_json = get_response.json()
    assert resp_json["firstName"] == "UserUpdated"
    assert resp_json["email"] == "updateduser@email.com"

@pytest.mark.parametrize("user,expected_status", [
    ({
        "id": 99999,
        "username": "usernotfound",
        "firstName": "User",
        "lastName": "NotFound",
        "email": "notfound@email.com",
        "password": "passnotfound",
        "phone": "000000000",
        "userStatus": 1
    }, [404, 400]),
    ({
        "id": 10016,
        "username": "invalid!@#",
        "firstName": "User",
        "lastName": "Invalid",
        "email": "invalid@email.com",
        "password": "passinvalid",
        "phone": "999888777",
        "userStatus": 1
    }, [400, 404])
])
def test_update_user_nonexistent_or_invalid(user, expected_status):
    response = requests.put(f"{BASE_URL}{API_PATH}/{user['username']}", json=user)
    assert response.status_code in expected_status

def test_update_user_missing_fields():
    user = {
        "id": 10015,
        "username": "userupdatemissing",
        "firstName": "User",
        "lastName": "UpMissing",
        "email": "missing@email.com",
        "password": "passmissing",
        "phone": "555666777",
        "userStatus": 1
    }
    requests.post(f"{BASE_URL}{API_PATH}", json=user)
    updated_user = user.copy()
    del updated_user["firstName"]
    del updated_user["email"]
    response = requests.put(f"{BASE_URL}{API_PATH}/{user['username']}", json=updated_user)
    assert response.status_code in [400, 422, 200]
    requests.delete(f"{BASE_URL}{API_PATH}/{user['username']}")