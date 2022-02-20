"""Constants for the RKI Covid API."""

DISTRICTS_URL = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=RS,GEN,EWZ,cases,deaths,county,last_update,cases7_lk,death7_lk,BL&returnGeometry=false&outSR=4326&f=json"
DISTRICTS_URL_RECOVERED = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Covid19_hubv/FeatureServer/0/query?where=NeuGenesen IN(1,0)&objectIds=&time=&resultType=standard&outFields=AnzahlGenesen,MeldeDatum,IdLandkreis&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&cacheHint=false&orderByFields=IdLandkreis&groupByFieldsForStatistics=IdLandkreis&outStatistics=[{"statisticType":"sum","onStatisticField":"AnzahlGenesen","outStatisticFieldName":"recovered"},{"statisticType":"sum","onStatisticField":"AnzahlFall","outStatisticFieldName":"newCases"},{"statisticType":"sum","onStatisticField":"AnzahlTodesfall","outStatisticFieldName":"newDeaths"},{"statisticType":"max","onStatisticField":"MeldeDatum","outStatisticFieldName":"date"}]&having&resultOffset&resultRecordCount&sqlFormat=none&f=json&token'
DISTRICTS_URL_NEW_CASES = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Covid19_hubv/FeatureServer/0/query?where=NeuerFall IN(1,-1)&objectIds=&time=&resultType=standard&outFields=AnzahlGenesen,MeldeDatum,IdLandkreis&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&cacheHint=false&orderByFields=IdLandkreis&groupByFieldsForStatistics=IdLandkreis&outStatistics=[{"statisticType":"sum","onStatisticField":"AnzahlGenesen","outStatisticFieldName":"recovered"},{"statisticType":"sum","onStatisticField":"AnzahlFall","outStatisticFieldName":"newCases"},{"statisticType":"sum","onStatisticField":"AnzahlTodesfall","outStatisticFieldName":"newDeaths"},{"statisticType":"max","onStatisticField":"MeldeDatum","outStatisticFieldName":"date"}]&having&resultOffset&resultRecordCount&sqlFormat=none&f=json&token'
DISTRICTS_URL_NEW_RECOVERED = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Covid19_hubv/FeatureServer/0/query?where=NeuGenesen IN(1,-1)&objectIds=&time=&resultType=standard&outFields=AnzahlGenesen,MeldeDatum,IdLandkreis&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&cacheHint=false&orderByFields=IdLandkreis&groupByFieldsForStatistics=IdLandkreis&outStatistics=[{"statisticType":"sum","onStatisticField":"AnzahlGenesen","outStatisticFieldName":"recovered"},{"statisticType":"sum","onStatisticField":"AnzahlFall","outStatisticFieldName":"newCases"},{"statisticType":"sum","onStatisticField":"AnzahlTodesfall","outStatisticFieldName":"newDeaths"},{"statisticType":"max","onStatisticField":"MeldeDatum","outStatisticFieldName":"date"}]&having&resultOffset&resultRecordCount&sqlFormat=none&f=json&token'
DISTRICTS_URL_NEW_DEATHS = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Covid19_hubv/FeatureServer/0/query?where=NeuerTodesfall IN(1,-1)&objectIds=&time=&resultType=standard&outFields=AnzahlGenesen,MeldeDatum,IdLandkreis&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&cacheHint=false&orderByFields=IdLandkreis&groupByFieldsForStatistics=IdLandkreis&outStatistics=[{"statisticType":"sum","onStatisticField":"AnzahlGenesen","outStatisticFieldName":"recovered"},{"statisticType":"sum","onStatisticField":"AnzahlFall","outStatisticFieldName":"newCases"},{"statisticType":"sum","onStatisticField":"AnzahlTodesfall","outStatisticFieldName":"newDeaths"},{"statisticType":"max","onStatisticField":"MeldeDatum","outStatisticFieldName":"date"}]&having&resultOffset&resultRecordCount&sqlFormat=none&f=json&token'
HOSPITALIZATION_URL = "https://raw.githubusercontent.com/robert-koch-institut/COVID-19-Hospitalisierungen_in_Deutschland/master/Aktuell_Deutschland_COVID-19-Hospitalisierungen.csv"
VACCINATIONS_URL = 'https://impfdashboard.de/static/data/germany_vaccinations_by_state.tsv'