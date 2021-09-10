import json
import aiohttp

from rki_covid_parser.const import DISTRICTS_URL, DISTRICTS_URL_RECOVERED, DISTRICTS_URL_NEW_CASES, DISTRICTS_URL_NEW_RECOVERED, DISTRICTS_URL_NEW_DEATHS

async def test_endpoint_districts():
    """Test the real service endpoint for availibility."""
    await _test_endpoint(DISTRICTS_URL)

async def test_endpoint_districts_recovered():
    """Test the real service endpoint for availibility."""
    await _test_endpoint(DISTRICTS_URL_RECOVERED)

async def test_endpoint_districts_new_cases():
    """Test the real service endpoint for availibility."""
    await _test_endpoint(DISTRICTS_URL_NEW_CASES)

async def test_endpoint_districts_new_recovered():
    """Test the real service endpoint for availibility."""
    await _test_endpoint(DISTRICTS_URL_NEW_RECOVERED)

async def test_endpoint_districts_new_deaths():
    """Test the real service endpoint for availibility."""
    await _test_endpoint(DISTRICTS_URL_NEW_DEATHS)


async def _test_endpoint(url: str):
    """Test if given endpoint is returning data."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200

            body = await response.text()
            data = json.loads(body)

            assert data is not None
            assert type(data) == dict
            assert "features" in data
            assert len(data["features"]) > 0

            for feature in data["features"]:
                assert "attributes" in feature
