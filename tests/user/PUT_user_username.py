import requests
from config import BASE_URL
API_PATH = "/user"

def test_update_user_success():
    # Cria o usuário para garantir que existe
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
    requests.post(f"{BASE_URL}/{API_PATH}", json=user)

    updated_user = user.copy()
    updated_user["firstName"] = "UserUpdated"
    updated_user["email"] = "updateduser@email.com"

    response = requests.put(f"{BASE_URL}/{API_PATH}/{user['username']}", json=updated_user)
    assert response.status_code == 200 or response.status_code == 201

    # Valida se foi atualizado
    get_response = requests.get(f"{BASE_URL}/{API_PATH}/{user['username']}")
    resp_json = get_response.json()
    assert resp_json["firstName"] == "UserUpdated"
    assert resp_json["email"] == "updateduser@email.com"

def test_update_user_nonexistent():
    updated_user = {
        "id": 99999,
        "username": "usernotfound",
        "firstName": "User",
        "lastName": "NotFound",
        "email": "notfound@email.com",
        "password": "passnotfound",
        "phone": "000000000",
        "userStatus": 1
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}/usernotfound", json=updated_user)
    assert response.status_code in [404, 400]

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
    requests.post(f"{BASE_URL}/{API_PATH}", json=user)

    updated_user = user.copy()
    del updated_user["firstName"]
    del updated_user["email"]

    response = requests.put(f"{BASE_URL}/{API_PATH}/{user['username']}", json=updated_user)
    assert response.status_code in [400, 422, 200]

def test_update_user_invalid_username():
    updated_user = {
        "id": 10016,
        "username": "invalid!@#",
        "firstName": "User",
        "lastName": "Invalid",
        "email": "invalid@email.com",
        "password": "passinvalid",
        "phone": "999888777",
        "userStatus": 1
    }
    response = requests.put(f"{BASE_URL}/{API_PATH}/invalid!@#", json=updated_user)
    assert response.status_code in [400, 404]