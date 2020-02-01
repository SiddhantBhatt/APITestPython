import requests
import json
import jsonpath

baseURL = "https://reqres.in"
api = "/api/users?page=2"

# Send GET Request
response = requests.get(baseURL+api)

# Parse response to JSON format

jsonResponse = json.loads(response.text)
# print(jsonResponse)

# Fetch value using jsonpath

pages = jsonpath.jsonpath(jsonResponse, 'total_pages')
print(pages)
assert pages[0] == 2