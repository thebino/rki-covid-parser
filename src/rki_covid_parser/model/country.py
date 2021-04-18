"""Country representation with all properties."""
from dataclasses import dataclass


@dataclass
class Country:
    id: str = None
    name: str = "Deutschland"
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
    lastUpdate: str = None

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id!r}, name={self.name!r}, cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
