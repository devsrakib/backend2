import requests


endpoints = "http://localhost:8000/api/"

get_response = requests.post(endpoints, json={'title':'onion','content':'the onion is red', 'price':12, 'my_discount':5 })

print(get_response.json())