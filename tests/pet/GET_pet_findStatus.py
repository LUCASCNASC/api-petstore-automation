import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_find_pet_by_status_success():
    status = "pending"
    response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    for pet in pets:
        assert pet["status"] == status