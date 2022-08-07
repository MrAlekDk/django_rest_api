import requests

endpoint = "http://127.0.0.1:3000/api/beers/1/update/"

data = {
    'name' : 'Updated beer name',
    'price' : 6969
    }

response = requests.put(endpoint, json=data)
print(response.json()) 