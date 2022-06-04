import json


def test_create_user(client):
    data = {'username':'test','email':'test@example.com','password':'123456'}
    response = client.post('/user',json.dump(data))
    assert response.status_code == 200
