import requests


baseURL = "https://reqres.in"
api = "/api/users/2"

# Send DELETE Request
response = requests.delete(baseURL+api)
print(response.status_code)

assert response.status_code == 204