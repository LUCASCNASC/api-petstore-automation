import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_logout_user_success():
    # O logout não exige autenticação real, apenas chama o endpoint
    response = requests.get(f"{BASE_URL}/user/logout")
    assert response.status_code == 200 or response.status_code == 201 or response.status_code == 202
    # Verifica se há uma mensagem de sucesso na resposta
    assert "ok" in response.text.lower() or "successful" in response.text.lower()