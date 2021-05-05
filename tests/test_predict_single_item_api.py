def test_predict_single_item_api(client):
    response = client.get('/test_predict_single_item')
    print(response.data)
    assert response.json['name'] == "logitech mouse"
    assert response.json['predicted_label'] == "Electronics"