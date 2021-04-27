import asyncio
import json
import os

import aiohttp
import pytest

from rki_covid_parser.parser import RkiCovidParser
from rki_covid_parser.model.state import State

async def test_vaccination_response():
    """Test the service response for content."""
    async with aiohttp.ClientSession() as session:
        parser = RkiCovidParser(session)
        await parser.load_data()

        assert len(parser.states) == 16
        for state in parser.states:
            validate_state(parser.states[state])

def validate_state(state: State):
    assert state.vaccinationTotal is not None
    assert state.vaccinationFirst is not None
    assert state.vaccinationFull is not None
