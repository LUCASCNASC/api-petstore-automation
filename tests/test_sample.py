import requests

def test_get_example():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1