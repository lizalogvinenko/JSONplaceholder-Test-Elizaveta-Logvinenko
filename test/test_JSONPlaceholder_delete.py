import requests


def test_create_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

    statusCode = response.status_code

    assert statusCode == 200

    response_data = response.json()

    assert response_data == {}
