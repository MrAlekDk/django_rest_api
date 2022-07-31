import requests

endpoint = "http://127.0.0.1:3000/api/beers/3/"


response = requests.get(endpoint)
print(response.json()) 