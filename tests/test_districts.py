import asyncio
import json
import os

import aiohttp
import pytest

from rki_covid_parser.const import DISTRICTS_URL
from rki_covid_parser.parser import RkiCovidParser


async def test_districts_response():
    """Test the service response for content."""
    async with aiohttp.ClientSession() as session:
        async with session.get(DISTRICTS_URL) as response:
            assert response.status == 200

            body = await response.text()
            data = json.loads(body)

            assert type(data) == dict
            assert "features" in data
            assert len(data["features"]) > 0

            validate_features(data["features"])


def validate_features(features: dict):
    """validate features."""
    # each feature contains an attributes object
    for feature in features:
        assert "attributes" in feature
        district = feature["attributes"]
        validate_district(district)


def validate_district(district: dict):
    """validate a district."""
    # a district must be a dict
    assert type(district) == dict

    # each district contains multiple properties to be valid
    assert "RS" in district
    assert "GEN" in district
    assert "EWZ" in district
    assert "cases" in district
    assert "deaths" in district
    assert "county" in district
    assert "last_update" in district
    assert "cases7_lk" in district
    assert "death7_lk" in district
    assert "BL" in district
