# Robert-Koch Institut COVID numbers parser

[![License](https://img.shields.io/github/license/thebino/rki-covid-parser)](./LICENSE.md)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/thebino/rki-covid-parser/Check%20the%20ArcGis%20endpoint%20availibility)

Python parser for the latest covid numbers from German RKI (Robert-Koch Institut).

## Installation
```pip install rki-covid-parser```

## Usage
Initialize the parser with an `aiohttp.session` and load the latest data.
```
parser = RkiCovidParser(session)        
await parser.load_data()


for district in parser.districts:
    # work with districts
    pass

for state in parser.states:
    # work with states
    pass

# work with the country
parser.country.cases
```

finished loading data, the parser contains a dictionary of districts, each with these properties:

|Property    |Type|Description|
|:-----------|:---|:------------|
|`id`| string | Unique district identifier |
|`name`| string | Name of the  district |
|`county`| string | County of the district |
|`state`| string | State of the district |
|`population`| integer | Population |
|`cases`| integer | Active cases |
|`deaths`| integer | Currently tracked deaths |
|`casesPerWeek`| integer | Cases per week |
|`deathsPerWeek`| integer | Deaths per week |
|`recovered`| integer | Recovered cases |
|`weekIncidence`| integer | Week incedence |
|`casesPer100k`| float | Cases per 100k population |
|`newCases`| integer | New cases since last day |
|`newDeaths`| integer | New deaths since last day |
|`newRecovered`| integer | New recovered since last day |
|`last_update`| string | Timestamp of the last update |


## Contribution
See [Contribution](https://github.com/thebino/rki-covid-parser/blob/development/CONTRIBUTING.md) for details.
