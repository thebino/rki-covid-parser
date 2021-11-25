"""State representation with all properties."""
from dataclasses import dataclass
from .area import Area


@dataclass
class State(Area):
    id: str = None
    name: str = None
    vaccinationTotal: int = 0
    vaccinationFirst: int = 0
    vaccinationFull: int = 0
    hospitalizationCasesMerged: float = 0.0
    hospitalizationIncidenceMerged: float = 0.0
    hospitalizationCasesBaby: float = 0.0
    hospitalizationIncidenceBaby: float = 0.123
    hospitalizationCasesChildren: float = 0.0
    hospitalizationIncidenceChildren: float = 0.0
    hospitalizationCasesTeen: float = 0.0
    hospitalizationIncidenceTeen: float = 0.0
    hospitalizationCasesGrown: float = 0.0
    hospitalizationIncidenceGrown: float = 0.0
    hospitalizationCasesSenior: float = 0.0
    hospitalizationIncidenceSenior: float = 0.0
    hospitalizationCasesOld: float = 0.0
    hospitalizationIncidenceOld: float = 0.0
    lastUpdate: str = None

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id!r}, name={self.name!r}, cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
