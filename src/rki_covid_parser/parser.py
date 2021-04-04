"""Parse district responses from RKI Covid numbers."""
import json

import aiohttp

from rki_covid_parser.const import DETAILS_URL, DISTRICTS_URL
from rki_covid_parser.district import District


class RkiCovidParser:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.districts = {}

    async def load_data(self) -> None:
        """load all data and merge results."""
        await self.load_districts()
        await self.load_district_details()

    async def load_districts(self) -> None:
        """load districts from arcgis."""
        response = await self.session.get(DISTRICTS_URL)

        # parse data manually, due to missing content-type 'application/json'
        body = await response.text()
        data = json.loads(body)

        await self.extract_districts(data)

    async def load_district_details(self) -> None:
        """load missing details from arcgis."""
        response = await self.session.get(DETAILS_URL)
        # parse data manually, due to missing content-type 'application/json'
        body = await response.text()
        data = json.loads(body)

        return await self.extract_details(data)

    async def extract_districts(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature

            id = feature["attributes"]["RS"]
            self.districts[id] = District(feature["attributes"])

    async def extract_details(self, data: dict) -> dict:
        """iterate through 'features' and 'attributes' to extract districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature
            id = feature["attributes"]["IdLandkreis"]
            recovered = feature["attributes"]["recovered"]
            newCases = feature["attributes"]["newCases"]
            newDeaths = feature["attributes"]["newDeaths"]

            self.districts[id].recovered = recovered
            self.districts[id].newCases = self.districts[id].cases - newCases
            self.districts[id].newDeaths = newDeaths
