import requests

# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, json={"title": "Hello World"})

# print(get_response.text)

print(get_response.json())
# print(get_response.status_code)
