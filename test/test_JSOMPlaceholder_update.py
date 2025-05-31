import requests
import pytest_schema

schema_post_v1 = pytest_schema.exact_schema({
    'id': int,
    'title': str,
    'body': str,
    'userId': int
})


def test_create_post():
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/1',
        json={
            'title': 'my changed name',
            'body': 'full and 1 body',
            'userId': 256
        })

    statusCode = response.status_code

    assert statusCode == 200

    response_data = response.json()

    assert response_data == schema_post_v1

    assert response_data['title'] == 'my changed name'
    assert response_data['body'] == 'full and 1 body'
    assert response_data['userId'] == 256
