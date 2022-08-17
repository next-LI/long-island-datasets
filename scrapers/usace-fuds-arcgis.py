import requests
import pandas as pd

# Formerly Used Defense Sites (FUDS) Geographic Information System overview page is here: https://www.usace.army.mil/Missions/Environmental/Formerly-Used-Defense-Sites/FUDS-GIS/
# FUDS property points API documentation page is here: https://geospatial-usace.opendata.arcgis.com/datasets/3f8354667d5b4b1b8ad7a6e00c3cf3b1_1/api
installations_url = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/arcgis/rest/services/fuds/FeatureServer/1/query"
installations_params = "where=(STATE=%27NY%27)%20AND%20(COUNTY=%27NASSAU%27%20OR%20COUNTY=%27SUFFOLK%27)&outFields=*&outSR=4326&f=json"
# "requests" documentation page is here: https://docs.python-requests.org/en/master/user/quickstart/
installations_request = requests.get(installations_url, params=installations_params)

results = []

# We are going to call every item within the installations request an "installation". As we go through each installation, we are going to scrape the dataset for that installation.
for installation in installations_request.json()["features"]:
	# FUDS project points API documentation page is here: https://geospatial-usace.opendata.arcgis.com/datasets/3f8354667d5b4b1b8ad7a6e00c3cf3b1_2/api
	sites_url = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/arcgis/rest/services/fuds/FeatureServer/2/query"
	sites_params = "where=FUDSINSTALLATIONID=%27" + installation["attributes"]["FUDSINSTALLATIONID"] + "%27&outFields=*&outSR=4326&f=json"
	sites_request = requests.get(sites_url, params=sites_params)
	# We are going to call every item within the sites request a "site". As we go through each site, we are going to scrape the dataset for that site.
	for site in sites_request.json()["features"]:
		result = site["attributes"]
		result.pop("OBJECTID")
		result["CLOSESTCITY"] = installation["attributes"]["CLOSESTCITY"]
		result["CONGRESSIONALDISTRICT"] = installation["attributes"]["CONGRESSIONALDISTRICT"]
		result["COUNTY"] = installation["attributes"]["COUNTY"]
		result["EPAREGION"] = installation["attributes"]["EPAREGION"]
		result["USACEDISTRICT"] = installation["attributes"]["USACEDISTRICT"]
		result["FISCALYEAR"] = installation["attributes"]["FISCALYEAR"]
		result["USACEDIVISION"] = installation["attributes"]["USACEDIVISION"]
		results.append(result)

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.DataFrame(results)
df.to_csv("../csv/environment-health/Military hazardous waste cleanup sites.csv", index=False)