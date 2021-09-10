import aiohttp
from aioresponses import aioresponses

from typing import Dict

from rki_covid_parser.const import DISTRICTS_URL, DISTRICTS_URL_RECOVERED, DISTRICTS_URL_NEW_CASES, DISTRICTS_URL_NEW_RECOVERED, DISTRICTS_URL_NEW_DEATHS, VACCINATIONS_URL
from rki_covid_parser.parser import RkiCovidParser
from rki_covid_parser.model.district import District
from rki_covid_parser.model.state import State
from rki_covid_parser.model.country import Country

async def test_parsing_with_fake_data(response_districts, response_recovered, response_new_cases, response_new_recovered, response_new_death, vaccinations_by_state):
    """Test parsing with fake data loaded from fixture response files."""
    async with aiohttp.ClientSession() as session:
        with aioresponses() as mocked:
            mocked.get(DISTRICTS_URL, status=200, payload=response_districts)
            mocked.get(DISTRICTS_URL_RECOVERED, status=200, payload=response_recovered)
            mocked.get(DISTRICTS_URL_NEW_CASES, status=200, payload=response_new_cases)
            mocked.get(DISTRICTS_URL_NEW_RECOVERED, status=200, payload=response_new_recovered)
            mocked.get(DISTRICTS_URL_NEW_DEATHS, status=200, payload=response_new_death)
            mocked.get(VACCINATIONS_URL, status=200, body=vaccinations_by_state)

            parser = RkiCovidParser(session)
            await parser.load_data()

            assert len(parser.districts) == 412
            for district in parser.districts:
                _validate_district(parser.districts[district])

            for state in parser.states:
                _validate_state(parser.states[state])

            _validate_district_numbers(parser.districts)
            _validate_state_numbers(parser.states)
            _validate_country_numbers(parser.country)
            _validate_vaccination_numbers(parser.states)

async def test_parsing_with_multiple_load_data_calls(response_districts, response_recovered, response_new_cases, response_new_recovered, response_new_death, vaccinations_by_state):
    """Test if parsing returns valid numbers if called multiple times."""
    async with aiohttp.ClientSession() as session:
        with aioresponses() as mocked:
            mocked.get(DISTRICTS_URL, status=200, payload=response_districts, repeat=True)
            mocked.get(DISTRICTS_URL_RECOVERED, status=200, payload=response_recovered, repeat=True)
            mocked.get(DISTRICTS_URL_NEW_CASES, status=200, payload=response_new_cases, repeat=True)
            mocked.get(DISTRICTS_URL_NEW_RECOVERED, status=200, payload=response_new_recovered, repeat=True)
            mocked.get(DISTRICTS_URL_NEW_DEATHS, status=200, payload=response_new_death, repeat=True)
            mocked.get(VACCINATIONS_URL, status=200, body=vaccinations_by_state, repeat=True)

            parser = RkiCovidParser(session)
            await parser.load_data()
            await parser.load_data()

            assert len(parser.districts) == 412
            for district in parser.districts:
                _validate_district(parser.districts[district])

            for state in parser.states:
                _validate_state(parser.states[state])

            _validate_district_numbers(parser.districts)
            _validate_state_numbers(parser.states)
            _validate_country_numbers(parser.country)
            _validate_vaccination_numbers(parser.states)

def _validate_vaccination_numbers(state: Dict[int, State]) -> None:
    """Validate vaccination numbers against fake fixtures."""
    assert state['Bayern'].vaccinationTotal == 15751380
    assert state['Bayern'].vaccinationFirst == 8277269
    assert state['Bayern'].vaccinationFull == 7868655

def _validate_district_numbers(districts: Dict[int, District]):
    """Validate district numbers against faked fixtures."""
    assert districts['09162'].id == '09162'
    assert districts['09162'].name == 'München'
    assert districts['09162'].county == 'SK München'
    assert districts['09162'].state == 'Bayern'
    assert districts['09162'].population == 1488202
    assert districts['09162'].cases == 79945
    assert districts['09162'].deaths == 1283
    assert districts['09162'].casesPerWeek == 863
    assert districts['09162'].deathsPerWeek == 2
    assert districts['09162'].recovered == 76199
    assert districts['09162'].weekIncidence == 58.0
    assert districts['09162'].casesPer100k == 5371.92
    assert districts['09162'].newCases == 391
    assert districts['09162'].newDeaths == 1             #
    assert districts['09162'].newRecovered == 214
    assert districts['09162'].lastUpdate == '09.09.2021, 00:00 Uhr'

def _validate_state_numbers(state: Dict[int, State]) -> None:
    """Validate state numbers against faked fixtures."""
    assert state['Bayern'].name == 'Bayern'
    assert state['Bayern'].population == 13140183
    assert state['Bayern'].cases == 691474
    assert state['Bayern'].deaths == 15449
    assert state['Bayern'].casesPerWeek == 10514
    assert state['Bayern'].deathsPerWeek == 8
    assert state['Bayern'].recovered == 654774
    assert state['Bayern'].weekIncidence == 80.0
    assert state['Bayern'].casesPer100k == 5262.29
    assert state['Bayern'].newCases == 2510
    assert state['Bayern'].newDeaths == 9
    assert state['Bayern'].newRecovered == 1344
    assert state['Bayern'].lastUpdate == '09.09.2021, 00:00 Uhr'

def _validate_country_numbers(country: Country) -> None:
    """Validate country numbers against faked fixtures."""
    assert country.name == "Deutschland"
    assert country.population == 83148406
    assert country.cases == 4046112
    assert country.deaths == 92498
    assert country.casesPerWeek == 69457
    assert country.deathsPerWeek == 39
    assert country.recovered == 3801460
    assert country.weekIncidence == 83.5
    assert country.casesPer100k == 4866.13
    assert country.newCases == 15431
    assert country.newDeaths == 50
    assert country.newRecovered == 8489
    assert country.lastUpdate == '09.09.2021, 00:00 Uhr'

def _validate_district(district: District):
    """Validate all properties are filled."""
    assert district.id is not None
    assert district.name is not None
    assert district.county is not None
    assert district.state is not None
    assert district.population is not None
    assert district.cases is not None
    assert district.deaths is not None
    assert district.casesPerWeek is not None
    assert district.deathsPerWeek is not None
    assert district.recovered is not None
    assert district.weekIncidence is not None
    assert district.casesPer100k is not None
    assert district.newCases is not None
    assert district.newDeaths is not None
    assert district.newRecovered is not None
    assert district.lastUpdate is not None

def _validate_state(state: State):
    """Validate all properties are filled."""
    assert state.cases is not None
