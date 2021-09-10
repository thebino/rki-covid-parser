import asyncio
import json
from rki_covid_parser.model.state import State

async def test_state():
    state = State("Teststate")
    state.id = 1337
    state.cases = 657
    state.deaths = 13
    state.recovered = 18
    state.newCases = 3
    assert "State(id=1337, name='Teststate', cases=657, deaths=13, recovered=18, newCases=3\n)" == state.__str__()
