def test_hello_api(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'