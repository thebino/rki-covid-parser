"""Country representation with all properties."""
from dataclasses import dataclass
from .area import Area


@dataclass
class Country(Area):
    id: str = None
    name: str = "Deutschland"
    lastUpdate: str = None

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id!r}, name={self.name!r}, cases={self.cases!r}, deaths={self.deaths!r}, recovered={self.recovered!r}, newCases={self.newCases!r}\n)"
        )
