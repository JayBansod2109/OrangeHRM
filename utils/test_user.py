
import requests

def test_user():

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    assert response.status_code ==200

    data =response.json()
    print(data)

    assert data[0]["id"] == 1
    assert data[1]["userId"]== 1


