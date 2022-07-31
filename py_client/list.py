import requests

endpoint = "http://127.0.0.1:3000/api/beers/"

data ={
    'name': 'test-beer',
    'beer_type': 'Some sort of beer',
    'description': 'A nice beer of some sort, probably nice served cold',
    'price': 55.55
}

response = requests.get(endpoint)
print(response.json()) 