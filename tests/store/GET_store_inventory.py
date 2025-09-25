import requests
from config import BASE_URL

def test_get_inventory_success():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Verifica se há pelo menos uma chave de status no inventário
    assert len(data) > 0