"""State representation with all properties."""
from dataclasses import dataclass


@dataclass
class State:
    id: str = None
    name: str = None
    county: str = None
    state: str = None
    population: int = 0
    cases: int = 0
    deaths: int = 0
    casesPerWeek: int = 0
    deathsPerWeek: int = 0
    recovered = 0
    weekIncidence = 0
    casesPer100k: float = 0.0
    newCases: int = 0
    newDeaths: int = 0
    newRecovered: int = 0
    last_update: str = None

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
