import requests
import pytest_schema

schema_post_v1 = pytest_schema.exact_schema({
    'id': int,
    'title': str,
    'body': str,
    'userId': int
})


def test_create_post():
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data={
            'title': 'my name',
            'body': 'full body',
            'userId': 255
        })

    statusCode = response.status_code

    assert statusCode == 201

    response_data = response.json()

    assert response_data == schema_post_v1

    assert response_data['title'] == 'my name'
    assert response_data['body'] == 'full body'
    assert response_data['userId'] == 255
