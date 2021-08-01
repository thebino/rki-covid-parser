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
    # validate numbers against RKI Dashboard (https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/)
    if state.name == 'Bayern':
        assert state.cases == 653797
        assert state.weekIncidence == 14.4
    if state.name == 'Baden-Württemberg':
        assert state.cases == 505824
        assert state.weekIncidence == 14.8
    if state.name == 'Niedersachsen':
        assert state.cases == 265191
        assert state.weekIncidence == 16.8
    pass

