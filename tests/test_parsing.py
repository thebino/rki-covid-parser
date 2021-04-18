import asyncio
import json
import os
import sys

import aiohttp
import pytest

from typing import Dict

from rki_covid_parser.const import DISTRICTS_URL, DISTRICTS_URL_NEW_CASES
from rki_covid_parser.parser import RkiCovidParser
from rki_covid_parser.model.district import District
from rki_covid_parser.model.state import State
from rki_covid_parser.model.country import Country


async def test_parsing():
    async with aiohttp.ClientSession() as session:
        parser = RkiCovidParser(session)
        await parser.load_data()

        assert len(parser.districts) == 412
        for district in parser.districts:
            validate_district(parser.districts[district])

        for state in parser.states:
            validate_state(parser.states[state])

        # TODO: hardcoded numbers
        # validate_latest_district_numbers(parser.districts)
        # validate_latest_state_numbers(parser.states)
        # validate_latest_country_numbers(parser.country)


def validate_latest_district_numbers(districts: Dict[int, District]):
    """Validate latest numbers against RKI dashboard."""
    assert districts['09162'].id == '09162'
    assert districts['09162'].name == 'München'
    assert districts['09162'].county == 'SK München'
    assert districts['09162'].state == 'Bayern'
    assert districts['09162'].population == 1484226
    assert districts['09162'].cases == 64124             #
    assert districts['09162'].deaths == 1145             #
    assert districts['09162'].casesPerWeek == 2432       #
    assert districts['09162'].deathsPerWeek == 1         #
    assert districts['09162'].recovered == 56229
    assert districts['09162'].weekIncidence == 163.86    #
    assert districts['09162'].casesPer100k == 4320.37    # 
    assert districts['09162'].newCases == 250            #
    assert districts['09162'].newDeaths == 1             #
    assert districts['09162'].newRecovered == 158
    assert districts['09162'].last_update == '18.04.2021, 00:00 Uhr'

def validate_latest_state_numbers(state: Dict[int, State]) -> None:
    """Validate latest numbers against RKI dashboard."""
    assert state['Bayern'].population == 13124737
    assert state['Bayern'].cases == 553999
    assert state['Bayern'].deaths == 13725
    assert state['Bayern'].casesPerWeek == 24333
    assert state['Bayern'].deathsPerWeek == 23
    assert state['Bayern'].recovered == 491856
    assert state['Bayern'].weekIncidence == 185.4
    assert state['Bayern'].casesPer100k == 4221.03
    assert state['Bayern'].newCases == 3367
    assert state['Bayern'].newDeaths == 10
    assert state['Bayern'].newRecovered == 1915
    assert state['Bayern'].last_update == '18.04.2021, 00:00 Uhr'

def validate_latest_country_numbers(country: Country) -> None:
    """Validate latest numbers against RKI dashboard."""
    assert country.population == 83166711
    assert country.cases == 3142262
    assert country.deaths == 79914
    assert country.casesPerWeek == 134984
    assert country.deathsPerWeek == 124
    assert country.recovered == 2775227
    assert country.weekIncidence == 162.31
    assert country.casesPer100k == 3778.27
    assert country.newCases == 19185
    assert country.newDeaths == 67
    assert country.newRecovered == 10158
    assert country.last_update == '18.04.2021, 00:00 Uhr'

def validate_district(district: District):
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
    assert district.last_update is not None

def validate_state(state: State):
    """Validate all properties are filled."""
    assert state.cases is not None
