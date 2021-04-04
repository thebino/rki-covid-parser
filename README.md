# Robert-Koch Institut COVID numbers parser

## Installation
```pip install rki-covid-parser```


## Introduction
Parse latest covid numbers from German RKI (Robert-Koch Institut).


## Usage
Initialize the parser with an `aiohttp.session` and load the latest data.
```
parser = RkiCovidParser(session)        
await parser.load_data()
```

finished loading data, the parser contains a sictionary of districts, each with these properties:

|Property    |Type|Description|
|:-----------|:---|:------------|
|`id`| number | . |
|`name`| number | . |
|`county`| number | . |
|`state`| number | . |
|`population`| number | . |
|`cases`| number | . |
|`deaths`| number | . |
|`casesPerWeek`| number | . |
|`deathsPerWeek`| number | . |
|`recovered`| number | . |
|`weekIncidence`| number | . |
|`casesPer100k`| number | . |
|`newCases`| number | . |
|`newDeaths`| number | . |
|`newRecovered`| number | . |
|`last_update`| number | . |


## Contribution
See [Contribution](CONTRIBUTING.md) for details.
