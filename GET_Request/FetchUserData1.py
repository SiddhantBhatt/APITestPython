import requests


baseURL = "https://reqres.in"
api = "/api/users?page=2"

# Send GET Request
response = requests.get(baseURL+api)
print(response)
print(response.status_code)

# Display Response Content and Header
print(response.headers)
print(response.content)