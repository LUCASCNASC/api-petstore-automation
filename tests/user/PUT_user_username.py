import requests
from config import BASE_URL

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
    requests.post(f"{BASE_URL}/user", json=user)

    updated_user = user.copy()
    updated_user["firstName"] = "UserUpdated"
    updated_user["email"] = "updateduser@email.com"

    response = requests.put(f"{BASE_URL}/user/{user['username']}", json=updated_user)
    assert response.status_code == 200 or response.status_code == 201

    # Valida se foi atualizado
    get_response = requests.get(f"{BASE_URL}/user/{user['username']}")
    resp_json = get_response.json()
    assert resp_json["firstName"] == "UserUpdated"
    assert resp_json["email"] == "updateduser@email.com"