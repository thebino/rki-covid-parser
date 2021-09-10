"""Parse district responses from RKI Covid numbers."""
import json

import csv
import io

import aiohttp

from rki_covid_parser.const import DISTRICTS_URL, DISTRICTS_URL_RECOVERED, DISTRICTS_URL_NEW_CASES, DISTRICTS_URL_NEW_RECOVERED, DISTRICTS_URL_NEW_DEATHS, VACCINATIONS_URL
from rki_covid_parser.model.district import District
from rki_covid_parser.model.state import State
from rki_covid_parser.model.country import Country


VaccinationCode2StateMap = {
    "DE-SH": "Schleswig-Holstein",
    "DE-HH": "Hamburg",
    "DE-NI": "Niedersachsen",
    "DE-HB": "Bremen",
    "DE-NW": "Nordrhein-Westfalen",
    "DE-HE": "Hessen",
    "DE-RP": "Rheinland-Pfalz",
    "DE-BW": "Baden-Württemberg",
    "DE-BY": "Bayern",
    "DE-SL": "Saarland",
    "DE-BE": "Berlin",
    "DE-BB": "Brandenburg",
    "DE-MV": "Mecklenburg-Vorpommern",
    "DE-SN": "Sachsen",
    "DE-ST": "Sachsen-Anhalt",
    "DE-TH": "Thüringen",
}


def generator_attributes_from_features(data):
    assert type(data) == dict
    _features = "features"
    _attributes = "attributes"
    assert _features in data
    assert len(data[_features]) > 0

    for feature in data[_features]:
        assert _attributes in feature
        yield feature[_attributes]


class RkiCovidParser:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.districts: Dict[int, District] = {}
        self.states: Dict[str, State] = {}
        self.country = Country()

    async def load_data(self) -> None:
        """load all data and merge results."""
        await self._reset_states()
        await self._load_districts()
        await self._load_districts_recovered()
        await self._load_districts_new_cases()
        await self._load_districts_new_deaths()
        await self._load_districts_new_recovered()
        await self._merge_states()
        await self._merge_country()

        await self._load_vaccinations()

    async def _reset_states(self) -> None:
        """reset previous loaded values."""
        self.states = {}

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

    async def _load_vaccinations(self) -> None:
        """load vaccinations for districts."""
        data = await self._load_from_tsv(VACCINATIONS_URL)
        await self._extract_vaccinations(data)

    async def _extract_districts(self, data: dict) -> None:
        """iterate through 'attributes' to extract districts."""
        for attributes in generator_attributes_from_features(data):
            id = attributes["RS"]
            self.districts[id] = District(attributes)

    async def _extract_districts_recovered(self, data: dict) -> None:
        """iterate through 'attributes' to extract recovered for districts."""
        for attributes in generator_attributes_from_features(data):
            id = attributes["IdLandkreis"]
            recovered = attributes["recovered"]
            self.districts[id].recovered = recovered

    async def _extract_districts_new_cases(self, data: dict) -> None:
        """iterate through 'attributes' to extract new cases for districts."""
        for attributes in generator_attributes_from_features(data):
            id = attributes["IdLandkreis"]
            newCases = attributes["newCases"]
            self.districts[id].newCases = newCases

    async def _extract_districts_new_recovered(self, data: dict) -> None:
        """iterate through 'attributes' to extract new cases for districts."""
        for attributes in generator_attributes_from_features(data):
            id = attributes["IdLandkreis"]
            newRecovered = attributes["recovered"]
            self.districts[id].newRecovered = newRecovered

    async def _extract_districts_new_deaths(self, data: dict) -> None:
        """iterate through 'attributes' to extract new deaths for districts."""
        for attributes in generator_attributes_from_features(data):
            id = attributes["IdLandkreis"]
            newDeaths = attributes["newDeaths"]
            self.districts[id].newDeaths = newDeaths

    async def _extract_vaccinations(self, data: csv.DictReader) -> None:
        """iterate through rows to extract vaccinations."""
        assert type(data) == csv.DictReader
        _code = "code"
        _vaccinations_total = "vaccinationsTotal"
        _people_first_total = "peopleFirstTotal"
        _people_full_total = "peopleFullTotal"

        for row in data:
            assert _code in row
            assert _vaccinations_total in row
            assert _people_first_total in row
            assert _people_full_total in row

            if row[_code] in VaccinationCode2StateMap:
                state = VaccinationCode2StateMap[row[_code]]
                self.states[state].vaccinationTotal = int(row[_vaccinations_total])
                self.states[state].vaccinationFirst = int(row[_people_first_total])
                self.states[state].vaccinationFull = int(row[_people_full_total])

    async def _load_from_argcis(self, url: str) -> str:
        response = await self.session.get(url)
        # parse data manually, due to missing content-type 'application/json'
        body = await response.text()
        return json.loads(body)

    async def _load_from_tsv(self, url: str) -> str:
        response = await self.session.get(url)
        body = await response.text()
        return csv.DictReader(io.StringIO(body), dialect=csv.excel_tab)

    async def _merge_states(self) -> None:
        """merge all districts grouped by state."""       

        for district in self.districts.values():
            state = self.states.setdefault(district.state, State(district.state))

            state.accumulate(district)
            state.lastUpdate = district.lastUpdate
            
    async def _merge_country(self) -> None:
        """merge all districts to country."""
        self.country = Country()

        for district in self.districts.values():
            self.country.accumulate(district)
            self.country.lastUpdate = district.lastUpdate
