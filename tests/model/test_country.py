from rki_covid_parser.model.country import Country

async def test_country():    
    country = Country()
    country.name = "Testcountry"
    assert "Country(id=None, name='Testcountry', cases=0, deaths=0, recovered=0, newCases=0\n)" == country.__str__()
