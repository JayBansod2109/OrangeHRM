import requests


def test_create_user():
    payload = {

        "name": "jay1",
        "email": "jay@gmail.com"
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

    assert response.status_code == 201
    print(response.json())