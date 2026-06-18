import requests

def test_post_users():

    payload={
        "name":"updatedJay"
    }

    response=requests.put("https://jsonplaceholder.typicode.com/users/2",json=payload)

    assert response.status_code ==200
    print(response.json())
