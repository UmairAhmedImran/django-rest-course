import requests

endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello World"})

print(get_response.text)

print(get_response.json())
print(get_response.status_code)
