# Rest API
"""
1. GET
2. POST
3. PUT
4. DELETE
"""
from contextlib import redirect_stderr

"""
JSON
"""

import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(type(response))

print(response.status_code)
assert response.status_code == 200

print(response.elapsed)
print(response.cookies)
print(response.headers.get('Date'))
print(response.content)
print(response.text)

json_response = json.loads(response.text)
print(json_response)

id = jsonpath.jsonpath(json_response, 'data[0].id')
print(id)
print(type(id))
assert id == [7]
print("Successfull")