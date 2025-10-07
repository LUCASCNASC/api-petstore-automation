import requests
from config import BASE_URL
API_PATH = "/user/logout"

# O logout não exige autenticação real, apenas chama o endpoint
def test_logout_user_success():
    response = requests.get(f"{BASE_URL}/{API_PATH}")
    assert response.status_code in [200, 201, 202]
    # Verifica se há uma mensagem de sucesso na resposta
    assert "ok" in response.text.lower() or "successful" in response.text.lower()

def test_logout_user_with_headers():
    headers = {"Accept": "application/json"}
    response = requests.get(f"{BASE_URL}/{API_PATH}", headers=headers)
    assert response.status_code in [200, 201, 202]
    assert "ok" in response.text.lower() or "successful" in response.text.lower()

def test_logout_user_wrong_method():
    # Tenta chamar com método POST
    response = requests.post(f"{BASE_URL}/{API_PATH}")
    # Espera erro de método não permitido
    assert response.status_code in [405, 400]