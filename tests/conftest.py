import pytest
import json
import datetime

@pytest.fixture()
def response_districts():
    with open("tests/fixtures/response_districts.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def no_districts():
    with open("tests/fixtures/no_districts.json", "r") as mock_response:
        return json.load(mock_response)

@pytest.fixture()
def no_features():
    with open("tests/fixtures/no_features.json", "r") as mock_response:
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

@pytest.fixture()
def hospitalization_numbers():
    # replace latest test-date with today
    text = open("tests/fixtures/hospitalization.csv", "r")
    text = ''.join([i for i in text]).replace("2021-11-24", str(datetime.date.today()))
    x = open("tests/fixtures/hospitalization.csv","w")
    x.writelines(text)
    x.close()

    with open("tests/fixtures/hospitalization.csv", mode='r+b') as mock_response:
        return mock_response.read()
