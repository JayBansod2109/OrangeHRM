import requests

def test_get_users():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    assert response.status_code == 200

    print(response.json())


