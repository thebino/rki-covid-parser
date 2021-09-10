from rki_covid_parser.model.area import Area

async def test_area():
    area = Area("Testarea")
    area.cases = 657
    area.deaths = 13
    area.recovered = 18
    area.newCases = 3
    assert "Area(cases=657, deaths=13, recovered=18, newCases=3\n)" == area.__str__()

    area.casesPerWeek = 200
    area.population = 6000000
    assert 3.3 == area.weekIncidence
    assert 10.95 == area.casesPer100k
