import requests


endpoints = "http://localhost:8000/api/products/"
data={
    "title":"this field is done"
}
get_response = requests.post(endpoints, json=data)

print(get_response.json())