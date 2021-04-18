"""Parse district responses from RKI Covid numbers."""
import json

import aiohttp

from rki_covid_parser.const import DISTRICTS_URL, DISTRICTS_URL_RECOVERED, DISTRICTS_URL_NEW_CASES, DISTRICTS_URL_NEW_RECOVERED, DISTRICTS_URL_NEW_DEATHS
from rki_covid_parser.model.district import District
from rki_covid_parser.model.state import State
from rki_covid_parser.model.country import Country


class RkiCovidParser:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.districts: Dict[int, District] = {}
        self.states: Dict[str, State] = {}
        self.country = Country()

    async def load_data(self) -> None:
        """load all data and merge results."""
        await self._load_districts()
        await self._load_districts_recovered()
        await self._load_districts_new_cases()
        await self._load_districts_new_deaths()
        await self._load_districts_new_recovered()
        await self._merge_states()
        await self._merge_country()

    async def _load_districts(self) -> None:
        """load and parse districts."""
        data = await self._load_from_argcis(DISTRICTS_URL)
        await self._extract_districts(data)

    async def _load_districts_recovered(self) -> None:
        """Load and parse recovered"""
        data = await self._load_from_argcis(DISTRICTS_URL_RECOVERED)
        await self._extract_districts_recovered(data)

    async def _load_districts_new_cases(self) -> None:
        """load and parse new cases."""
        data = await self._load_from_argcis(DISTRICTS_URL_NEW_CASES)
        await self._extract_districts_new_cases(data)

    async def _load_districts_new_deaths(self) -> None:
        """load and parse new deaths."""
        data = await self._load_from_argcis(DISTRICTS_URL_NEW_DEATHS)
        await self._extract_districts_new_deaths(data)

    async def _load_districts_new_recovered(self) -> None:
        """load new recovered for districts."""
        data = await self._load_from_argcis(DISTRICTS_URL_NEW_RECOVERED)
        await self._extract_districts_new_recovered(data)

    async def _extract_districts(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature

            id = feature["attributes"]["RS"]
            self.districts[id] = District(feature["attributes"])

    async def _extract_districts_recovered(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract recovered for districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature
            id = feature["attributes"]["IdLandkreis"]
            recovered = feature["attributes"]["recovered"]
            self.districts[id].recovered = recovered

    async def _extract_districts_new_cases(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract new cases for districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature
            id = feature["attributes"]["IdLandkreis"]
            newCases = feature["attributes"]["newCases"]
            self.districts[id].newCases = newCases

    async def _extract_districts_new_recovered(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract new cases for districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature
            id = feature["attributes"]["IdLandkreis"]
            newRecovered = feature["attributes"]["recovered"]
            self.districts[id].newRecovered = newRecovered

    async def _extract_districts_new_deaths(self, data: dict) -> None:
        """iterate through 'features' and 'attributes' to extract new deaths for districts."""
        assert type(data) == dict
        assert "features" in data
        assert len(data["features"]) > 0

        for feature in data["features"]:
            assert "attributes" in feature
            id = feature["attributes"]["IdLandkreis"]
            newDeaths = feature["attributes"]["newDeaths"]
            self.districts[id].newDeaths = newDeaths

    async def _load_from_argcis(self, url: str) -> str:
        response = await self.session.get(url)
        # parse data manually, due to missing content-type 'application/json'
        body = await response.text()
        return json.loads(body)

    async def _merge_states(self) -> None:
        """merge all districts grouped by state."""
        for d in self.districts:
            district = self.districts[d]
            if district.state not in self.states:
                self.states[district.state] = State()

            self.states[district.state].population += district.population
            self.states[district.state].cases += district.cases
            self.states[district.state].deaths += district.deaths
            self.states[district.state].casesPerWeek += district.casesPerWeek
            self.states[district.state].deathsPerWeek += district.deathsPerWeek
            self.states[district.state].recovered += district.recovered
            self.states[district.state].newCases += district.newCases
            self.states[district.state].newDeaths += district.newDeaths
            self.states[district.state].newRecovered += district.newRecovered
            self.states[district.state].last_update = district.last_update

        for state in self.states:
            self.states[state].weekIncidence = round(self.states[state].casesPerWeek / self.states[state].population * 100000, 2)
            self.states[state].casesPer100k = round(self.states[state].cases / self.states[state].population * 100000, 2)

            
    async def _merge_country(self) -> None:
        """merge all districts to country."""
        self.country = Country()

        for d in self.districts:
            district = self.districts[d]

            self.country.population += district.population
            self.country.cases += district.cases
            self.country.deaths += district.deaths
            self.country.casesPerWeek += district.casesPerWeek
            self.country.deathsPerWeek += district.deathsPerWeek
            self.country.recovered += district.recovered
            self.country.newCases += district.newCases
            self.country.newDeaths += district.newDeaths
            self.country.newRecovered += district.newRecovered
            self.country.last_update = district.last_update

        self.country.weekIncidence = round(self.country.casesPerWeek / self.country.population * 100000, 2)
        self.country.casesPer100k = round(self.country.cases / self.country.population * 100000, 2)
