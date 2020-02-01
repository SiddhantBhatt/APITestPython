import requests
import json
import jsonpath


baseURL = "https://reqres.in"
api = "/api/users"

def test_createUser():
    # Read Input JSON File
    file = open(r"C:\Users\Siddhant Bhatt\PycharmProjects\APITesting\CreateJSON.json", 'r')
    json_input = file.read()
    requestJSON = json.loads(json_input)
    # Make POST Request with JSON input body. POST is used to CREATE data
    response = requests.post(url=baseURL + api, data=requestJSON)
    # Validating Response Code
    assert response.status_code == 201
    # Fetch Header from Response
    print(response.headers)
    print(response.headers.get('Content-Length'))
    # Parse Response to JSON Format
    response_json = json.loads(response.text)
    # Pick ID using JSONpath
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])


