"""State representation with all properties."""
from dataclasses import dataclass


@dataclass
class Area:
    population: int = 0
    cases: int = 0
    deaths: int = 0
    casesPerWeek: int = 0
    deathsPerWeek: int = 0
    recovered: int = 0
    newCases: int = 0
    newDeaths: int = 0
    newRecovered: int = 0

    @property
    def weekIncidence(self) -> float:
        return round(self.casesPerWeek / self.population * 100000, 2)

    @property
    def casesPer100k(self) -> float:
        return round(self.cases / self.population * 100000, 2)


    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
