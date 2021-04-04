"""District representation with all properties."""
from dataclasses import dataclass


@dataclass
class District:
    id: str = None
    name: str = None
    county: str = None
    state: str = None
    population: int = None
    cases: int = None
    deaths: int = None
    casesPerWeek: int = None
    deathsPerWeek: int = None
    recovered = None
    weekIncidence = None
    casesPer100k: float = None
    newCases: int = None
    newDeaths: int = None
    newRecovered: int = None
    last_update: str = None

    def __init__(self, data: dict):
        self.validate(data)
        self.extract_properties(data)

    def validate(self, data: dict):
        assert "RS" in data
        assert "GEN" in data
        assert "EWZ" in data
        assert "cases" in data
        assert "deaths" in data
        assert "county" in data
        assert "last_update" in data
        assert "cases7_lk" in data
        assert "death7_lk" in data
        assert "BL" in data

    def extract_properties(self, data: dict):
        self.id: str = data["RS"]
        self.name: str = data["GEN"]
        self.county: str = data["county"]
        self.state: str = data["BL"]
        self.population: int = data["EWZ"]
        self.cases: int = data["cases"]
        self.deaths: int = data["deaths"]
        self.casesPerWeek: int = data["cases7_lk"]
        self.deathsPerWeek: int = data["death7_lk"]
        self.last_update: str = data["last_update"]  # "01.01.2020, 00:00 Uhr"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id!r}, name={self.name!r}, county={self.county!r}, cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
