import requests
from config import BASE_URL
API_PATH = "/user/logout"

def test_logout_user_success():
    # O logout não exige autenticação real, apenas chama o endpoint
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    assert response.status_code == 200 or response.status_code == 201 or response.status_code == 202
    # Verifica se há uma mensagem de sucesso na resposta
    assert "ok" in response.text.lower() or "successful" in response.text.lower()