from rki_covid_parser.model.district import District

async def test_district():
    data = {
        "RS": "01337",
        "GEN": "Testdistrict",
        "EWZ": 89934,
        "cases": 2714,
        "deaths": 39,
        "county": "SK Test",
        "last_update": "09.09.2021, 00:00 Uhr",
        "cases7_lk": 50,
        "death7_lk": 0,
        "BL": "Schleswig-Holstein"
    }
    
    district = District(data)
    assert "District(id='01337', name='Testdistrict', county='SK Test', cases=2714, deaths=39, recovered=0, newCases=0, newDeaths=0\n)" == district.__str__()
