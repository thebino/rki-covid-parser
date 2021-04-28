"""State representation with all properties."""
from dataclasses import dataclass
from .area import Area


@dataclass
class State(Area):
    id: str = None
    name: str = None
    vaccinationTotal = None
    vaccinationFirst = None
    vaccinationFull = None
    lastUpdate: str = None

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id!r}, name={self.name!r}, cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
