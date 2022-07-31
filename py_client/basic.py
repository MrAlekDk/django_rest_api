import requests


#endpoint1 = 'https://httpbin.org/status/200'
endpoint = "http://127.0.0.1:3000/api/"


response = requests.post(endpoint, json={'name': 'Hello world', 'beer_type':'Idc', 'description':'A beer of some sort', 'price': 10.10})
print(response.json()) 