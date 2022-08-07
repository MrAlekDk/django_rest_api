import requests

endpoint = "http://127.0.0.1:3000/api/beers/1"


response = requests.get(endpoint)
print(response.json()) 