import json
def test_predict_api(client, input_name):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.post('/api/v1/predict_category', data=json.dumps({'item_name': input_name}), headers=headers)
    assert response.json['name'] == input_name
    assert response.json['predicted_label'] == "Men"