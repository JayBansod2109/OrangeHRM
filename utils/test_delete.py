import requests

def test_delete_user():

    response=requests.delete("https://jsonplaceholder.typicode.com/users/1")

    print(response.json())