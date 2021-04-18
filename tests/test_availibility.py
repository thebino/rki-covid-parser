import asyncio
import json
import os

import aiohttp
import pytest

from rki_covid_parser.const import DISTRICTS_URL
from rki_covid_parser.parser import RkiCovidParser


async def test_service_availibility():
    """Test the service endpoint for availibility."""
    async with aiohttp.ClientSession() as session:
        async with session.get(DISTRICTS_URL) as response:
            assert response.status == 200

            body = await response.text()
            data = json.loads(body)
