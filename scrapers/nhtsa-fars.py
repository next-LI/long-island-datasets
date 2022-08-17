import datetime
import requests
import pandas as pd

year = datetime.datetime.now().year

counties = [
	{
		"fips_code": "59",
		"name": "Nassau"
	}, {
		"fips_code": "103",
		"name": "Suffolk"
	}
]

results = []

# We are going to call every item within "counties" a "county". As we go through each county, we are going to scrape the dataset for that county.
for county in counties:
	# Fatality Analysis Reporting System API documentation page is here: https://crashviewer.nhtsa.dot.gov/CrashAPI
	crashes_url = "https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCrashesByLocation"
	crashes_params = "fromCaseYear=2010&toCaseYear=" + str(year) + "&state=36&county=" + county["fips_code"] + "&format=json"
	# "requests" documentation page is here: https://docs.python-requests.org/en/master/user/quickstart/
	crashes_request = requests.get(crashes_url, params=crashes_params)
	# We are going to call every item within the crashes request a "case". As we go through each dataset, we are going to scrape the dataset for that case.
	for case in crashes_request.json()["Results"][0]:
		case_url = "https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCaseDetails"
		case_params = "stateCase=" + case["ST_CASE"] + "&caseYear=" + case["CaseYear"] + "&state=" + case["STATE"] + "&format=json"
		case_request = requests.get(case_url, params=case_params)
		result = case_request.json()["Results"][0][0]["CrashResultSet"]
		results.append(result)

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.DataFrame(results)
for column in df:
	for cell in df[column][:100]:
		if isinstance(cell, list):
			df.pop(column)
			break
df.to_csv("../csv/transportation/Fatal motor vehicle crashes.csv", index=False)