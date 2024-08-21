import requests
from getpass import getpass


auth_endpoints = "http://localhost:8000/api/auth/"
username = input("what is your username: \n")
auth_response = requests.post(auth_endpoints, json={'username':username, 'password':getpass()})

print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers={
        'Authorization':f'Token {token}'
    }
    endpoints = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoints, headers=headers)

    print(get_response.json())
