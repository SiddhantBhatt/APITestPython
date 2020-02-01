import requests
import json
import jsonpath

def test_add_new_data():
    baseURL = "http://thetestingworldapi.com/"

    # Create Student

    print("***********************************")
    create_api = "api/studentsDetails"
    file = open("UsingPytest/student.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(url=baseURL+create_api, data=request_json)
    print(response.status_code)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    # Add Technical Skills

    print("***********************************")
    tech_api = "api/technicalskills"
    file = open("UsingPytest/studentTech.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    response = requests.post(url=baseURL + tech_api, data=request_json)
    print(response.status_code)
    print(response.text)

    # Add Address

    print("***********************************")
    address_api = "api/addresses"
    file = open("UsingPytest/studentAddress.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    response = requests.post(url=baseURL + address_api, data=request_json)
    print(response.status_code)
    print(response.text)

    # Get Complete Data

    print("***********************************")
    final_details_api = "api/FinalStudentDetails/" + str(id[0])
    response = requests.get(url=baseURL + final_details_api)
    print(response.status_code)
    print(response.text)
