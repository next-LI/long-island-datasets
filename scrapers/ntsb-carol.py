import requests
import pandas as pd

# National Transportation Safety Board Case Analysis and Reporting Online database page is here: https://data.ntsb.gov/carol-main-public/landing-page
url = "https://data.ntsb.gov/carol-main-public/api/Query/Main"
headers = {"Content-Type": "application/json"}

# The limit can be up to 100.
limit = 100
# Start the offset at 0.
offset = 0

initial_payload = {"ResultSetSize":str(limit),"ResultSetOffset":offset,"QueryGroups":[{"QueryRules":[{"FieldName":"NTSBNumber","RuleType":0,"Values":[],"Columns":["Event.NTSBNumber"],"Operator":"search engine"},{"FieldName":"Mode","RuleType":0,"Values":[],"Columns":["Event.Mode"],"Operator":"is"},{"FieldName":"EventDate","RuleType":0,"Values":[],"Columns":["Event.EventDate"],"Operator":"is"},{"FieldName":"City","RuleType":0,"Values":[],"Columns":["Event.City"],"Operator":"search engine"},{"FieldName":"State","RuleType":0,"Values":["NY"],"Columns":["Event.State"],"Operator":"is"},{"FieldName":"Country","RuleType":0,"Values":[],"Columns":["Event.Country"],"Operator":"is"},{"FieldName":"HighestInjury","RuleType":0,"Values":[],"Columns":["Event.HighestInjury"],"Operator":"is"},{"FieldName":"OriginalPublishedDate","RuleType":0,"Values":[],"Columns":["Event.OriginalPublishedDate"],"Operator":"is"},{"FieldName":"AircraftCategory","RuleType":0,"Values":[],"Columns":["Aircraft.AircraftCategory"],"Operator":"is"},{"FieldName":"EngineType","RuleType":0,"Values":[],"Columns":["Aircraft.EngineType"],"Operator":"is"},{"FieldName":"RegistrationNumber","RuleType":0,"Values":[],"Columns":["Aircraft.RegistrationNumber"],"Operator":"search engine"},{"FieldName":"RegulationFlightConductedUnder","RuleType":0,"Values":[],"Columns":["AviationOperation.RegulationFlightConductedUnder"],"Operator":"is"},{"FieldName":"RecNum","RuleType":0,"Values":[],"Columns":["Recs.Srid","Recs.SridCleaned"],"Operator":"search engine"},{"FieldName":"RecsSubject","RuleType":0,"Values":[],"Columns":["Recs.Subject"],"Operator":"search engine"},{"FieldName":"AddresseeName","RuleType":0,"Values":[],"Columns":["Recs.AddresseeName"],"Operator":"search engine"}],"AndOr":"And"}],"AndOr":"And","SortColumn":None,"SortDescending":True,"TargetCollection":"cases","SessionId":000000}
# "requests" documentation page is here: https://docs.python-requests.org/en/master/user/quickstart/
initial_request = requests.post(url, json=initial_payload, headers=headers, verify=False)

results = []

# As we go through each page of the dataset, we are going to scrape that page of the dataset.
count = initial_request.json()["ResultListCount"]
i = 0
while i < count / limit:
	offset = i * limit
	loop_payload = {"ResultSetSize":str(limit),"ResultSetOffset":offset,"QueryGroups":[{"QueryRules":[{"FieldName":"NTSBNumber","RuleType":0,"Values":[],"Columns":["Event.NTSBNumber"],"Operator":"search engine"},{"FieldName":"Mode","RuleType":0,"Values":[],"Columns":["Event.Mode"],"Operator":"is"},{"FieldName":"EventDate","RuleType":0,"Values":[],"Columns":["Event.EventDate"],"Operator":"is"},{"FieldName":"City","RuleType":0,"Values":[],"Columns":["Event.City"],"Operator":"search engine"},{"FieldName":"State","RuleType":0,"Values":["NY"],"Columns":["Event.State"],"Operator":"is"},{"FieldName":"Country","RuleType":0,"Values":[],"Columns":["Event.Country"],"Operator":"is"},{"FieldName":"HighestInjury","RuleType":0,"Values":[],"Columns":["Event.HighestInjury"],"Operator":"is"},{"FieldName":"OriginalPublishedDate","RuleType":0,"Values":[],"Columns":["Event.OriginalPublishedDate"],"Operator":"is"},{"FieldName":"AircraftCategory","RuleType":0,"Values":[],"Columns":["Aircraft.AircraftCategory"],"Operator":"is"},{"FieldName":"EngineType","RuleType":0,"Values":[],"Columns":["Aircraft.EngineType"],"Operator":"is"},{"FieldName":"RegistrationNumber","RuleType":0,"Values":[],"Columns":["Aircraft.RegistrationNumber"],"Operator":"search engine"},{"FieldName":"RegulationFlightConductedUnder","RuleType":0,"Values":[],"Columns":["AviationOperation.RegulationFlightConductedUnder"],"Operator":"is"},{"FieldName":"RecNum","RuleType":0,"Values":[],"Columns":["Recs.Srid","Recs.SridCleaned"],"Operator":"search engine"},{"FieldName":"RecsSubject","RuleType":0,"Values":[],"Columns":["Recs.Subject"],"Operator":"search engine"},{"FieldName":"AddresseeName","RuleType":0,"Values":[],"Columns":["Recs.AddresseeName"],"Operator":"search engine"}],"AndOr":"And"}],"AndOr":"And","SortColumn":None,"SortDescending":True,"TargetCollection":"cases","SessionId":000000}
	loop_request = requests.post(url, json=loop_payload, headers=headers, verify=False)
	# We are going to call every item within the loop request an "investigation". As we go through each investigation, we are going to scrape the dataset for that investigation.
	for investigation in loop_request.json()["Results"]:
		result = { field_group["FieldName"]: ", ".join(field_group["Values"]) for field_group in investigation["Fields"] }
		results.append(result)
	i += 1

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.DataFrame(results)
df["DocketUrl"] = "https://data.ntsb.gov/Docket?ProjectID=" + df["Mkey"]
df.to_csv("../csv/transportation/Federal transportation investigations in New York State.csv", index=False)