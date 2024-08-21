import requests


endpoints = "http://localhost:8000/api/products/3/"

get_response = requests.get(endpoints)

print(get_response.json())