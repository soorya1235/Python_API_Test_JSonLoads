# Pytest

"""
1. Unit Testing Framework (UnitTest, Nose)
2. It gives u an option to conditionally execute TC
3. We can setup pre-requisite and post scripts
4. Can add assertions
5. Option to generate our own report
"""

"""

PYTEST NAMING CONVENTIONS

1. TC file name, should always start with "test_"
2. TC Method should also start with the "test"
"""
import requests
import json
import jsonpath
import pytest

# Pytest Fixtures
@pytest.fixture()
def settingUp_Environment():
    global url
    global response
    global json_response
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    yield
    print("After Every Function")

a = "Window"

@pytest.mark.SmokeTest
@pytest.mark.skipif(a=="Linux", reason = "The value of a is above 100")
def test_verify_Status_Code(settingUp_Environment):
    assert response.status_code == 200

@pytest.mark.RegressionTest
@pytest.mark.SmokeTest
def test_verify_id_value(settingUp_Environment):
    id = jsonpath.jsonpath(json_response, 'data[0].id')
    assert id == [7]

@pytest.mark.SanityTest
def test_verify_page_value(settingUp_Environment):
    path = jsonpath.jsonpath(json_response, 'page')
    assert path == [2]

@pytest.mark.SmokeTest
def test_verify_totalpage_value(settingUp_Environment):
    assert jsonpath.jsonpath(json_response, 'total_pages') == [2]

