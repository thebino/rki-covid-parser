import pytest
import json

@pytest.fixture()
def response_districts():
    with open("tests/fixtures/response_districts.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def no_districts():
    with open("tests/fixtures/no_districts.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def response_recovered():
    with open("tests/fixtures/response_recovered.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def response_new_cases():
    with open("tests/fixtures/response_new_cases.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def response_new_recovered():
    with open("tests/fixtures/response_new_recovered.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def response_new_death():
    with open("tests/fixtures/response_new_death.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def vaccinations_by_state():
    with open("tests/fixtures/germany_vaccinations_by_state.tsv", mode='r+b') as mock_response:
        return mock_response.read()
