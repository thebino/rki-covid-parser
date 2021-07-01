import asyncio
import json
import os

import aiohttp
import pytest

from rki_covid_parser.parser import RkiCovidParser
from rki_covid_parser.model.state import State

async def test_states_response():
    """Test the service response for content."""
    async with aiohttp.ClientSession() as session:
        parser = RkiCovidParser(session)
        await parser.load_data()

        assert len(parser.states) == 16
        for state in parser.states:
            validate_state(parser.states[state])

async def test_multiple_load_data_calls():
    """Test the service response for content."""
    async with aiohttp.ClientSession() as session:
        parser = RkiCovidParser(session)
        await parser.load_data()
        await parser.load_data()

        assert len(parser.states) == 16
        for state in parser.states:
            validate_state(parser.states[state])

def validate_state(state: State):
    if state.name == 'Baden-Württemberg':
        assert state.cases == 500702
    if state.name == 'Niedersachsen':
        assert state.cases == 261055
    pass

