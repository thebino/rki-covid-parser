# Robert-Koch Institut COVID numbers parser

[![License](https://img.shields.io/github/license/thebino/rki-covid-parser)](./LICENSE.md)
[![Tests](https://github.com/thebino/rki-covid-parser/actions/workflows/testing.yaml/badge.svg)](https://github.com/thebino/rki-covid-parser/actions/workflows/testing.yaml)
[![codecov](https://codecov.io/gh/thebino/rki-covid-parser/branch/development/graph/badge.svg?token=9NUUAMXVP4)](https://codecov.io/gh/thebino/rki-covid-parser)

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
|`weekIncidence`| float | Week incidence |
|`casesPer100k`| float | Cases per 100k population |
|`newCases`| integer | New cases since last day |
|`newDeaths`| integer | New deaths since last day |
|`newRecovered`| integer | New recovered since last day |
|`last_update`| string | Timestamp of the last update |
|`hospitalizationCasesMerged` | float | Hospitalization cases for people in germany summarized  |
|`hospitalizationIncidenceMerged` | float | Hospitalization incidence for people in germany summarized |
|`hospitalizationCasesBaby` | float | Hospitalization cases for people between 00-04 |
|`hospitalizationIncidenceBaby` | float | Hospitalization incidence for people between 00-04 |
|`hospitalizationCasesChildren` | float | Hospitalization cases for people between 05-14 |
|`hospitalizationIncidenceChildren` | float | Hospitalization incidence for people between 05-14 |
|`hospitalizationCasesTeen` | float | Hospitalization cases for people between 15-34 |
|`hospitalizationIncidenceTeen` | float | Hospitalization incidence for people between 15-34 |
|`hospitalizationCasesGrown` | float | Hospitalization cases for people between 35-59 |
|`hospitalizationIncidenceGrown` | float | Hospitalization incidence for people between 35-59 |
|`hospitalizationCasesSenior` | float | Hospitalization cases for people between 60-79 |
|`hospitalizationIncidenceSenior` | float | Hospitalization incidence for people between 60-79 |
|`hospitalizationCasesOld` | float | Hospitalization cases for people older than 80 |
|`hospitalizationIncidenceOld` | float | Hospitalization incidence for people older than 80 |


## Contribution
See [Contribution](https://github.com/thebino/rki-covid-parser/blob/development/CONTRIBUTING.md) for details.
