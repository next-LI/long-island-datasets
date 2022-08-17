import requests
import pandas as pd

# All ZIP codes in Nassau and Suffolk counties start with the digits 110, 115, 117, 118, or 119, except Fishers Island, which is 06390.
three_digit_zip_codes = ["063", "110", "115", "117", "118", "119"]

results = []

# We are going to call every item within "three_digit_zip_codes" a "zip_code". As we go through each ZIP code range, we are going to scrape the dataset for that range.
for zip_code in three_digit_zip_codes:
	# Suffolk County Food Establishment Inspections database page is here: https://eco.suffolkcountyny.gov/#/pa1/search
	search_url = "https://eco.suffolkcountyny.gov/api/pressAgentClient/searchFacilities"
	search_params = "PressAgentOid=298a9d2d-9a6d-4217-b5e4-a6ce00f651ba"
	search_payload = {"Zip": zip_code}
	headers = {"Content-Type": "application/json;charset=UTF-8"}
	# "requests" documentation page is here: https://docs.python-requests.org/en/master/user/quickstart/
	search_request = requests.post(search_url, params=search_params, json=search_payload, headers=headers)
	# We are going to call every item within the search request a "facility". As we go through each facility, we are going to scrape the dataset for that facility.
	for facility in search_request.json():
		program_url = "https://eco.suffolkcountyny.gov/api/pressAgentClient/programs"
		program_params = "FacilityId=" + facility["FacilityId"] + "&PressAgentOid=298a9d2d-9a6d-4217-b5e4-a6ce00f651ba"
		program_request = requests.get(program_url, params=program_params)
		# We are going to call every item within the program request a "program". As we go through each program, we are going to scrape the dataset for that program.
		for program in program_request.json():
			facility_url = "https://eco.suffolkcountyny.gov/api/pressAgentClient/facilityDetail"
			facility_params = "PressAgentOid=298a9d2d-9a6d-4217-b5e4-a6ce00f651ba&ProgramId=" + program["ProgramId"]
			facility_request = requests.get(facility_url, params=facility_params)
			inspection_url = "https://eco.suffolkcountyny.gov/api/pressAgentClient/inspections"
			inspection_params = "PressAgentOid=298a9d2d-9a6d-4217-b5e4-a6ce00f651ba&ProgramId=" + program["ProgramId"]
			inspection_request = requests.get(inspection_url, params=inspection_params)
			# We are going to call every item within the inspection request an "activity". As we go through each activity, we are going to scrape the dataset for that activity.
			for activity in inspection_request.json():
				# We are going to call every item within the violations request a "violation". As we go through each violation, we are going to scrape the dataset for that violation.
				for violation in activity["violations"]:
					result = {}
					facility = facility_request.json()[0]
					result["facility_id"] = facility["FacilityID"]
					result["facility_name"] = facility["FacilityName"]
					result["address"] = facility["Address"]
					result["city"] = facility["CityStateZip"].split(" NY ")[0]
					result["zip"] = facility["CityStateZip"].split(" NY ")[1]
					result["permit_expiration_date"] = facility["PermitExpiration"]
					result["inspection_date"] = activity["activity_date"]
					result["sanitary_code"] = violation["violation_description"]
					result["violation_text"] = violation["v_memo"]
					results.append(result)

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.DataFrame(results)
df.to_csv("../csv/environment-health/Suffolk County food establishment inspections.csv", index=False)