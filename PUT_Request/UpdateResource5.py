import requests
import requests
import json
import jsonpath


baseURL = "https://reqres.in"
api = "/api/users/2"

# Read Input JSON File
file = open(r"C:\Users\Siddhant Bhatt\PycharmProjects\APITesting\CreateJSON.json", 'r')
json_input = file.read()
requestJSON = json.loads(json_input)

# Make PUT Request with JSON input body. POST is used to UPDATE data

response = requests.put(url=baseURL+api,data=requestJSON)
print(response.content)
print(response.status_code)

# Validating Response Code
assert response.status_code == 200

# Parse Response Content to JSON Format
responseJSON = json.loads(response.text)
updated = jsonpath.jsonpath(responseJSON, 'updatedAt')
print(updated)
