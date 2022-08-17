import requests
import pandas as pd

# All ZIP codes in Nassau and Suffolk counties start with the digits 110, 115, 117, 118, or 119, except Fishers Island, which is 06390.
three_digit_zip_codes = ["063", "110", "115", "117", "118", "119"]

# We are defining the openFDA datasets we want to scrape here.
datasets = [
	{
		"slug": "drug",
		"description": "Drug recalls"
	}, {
		"slug": "device",
		"description": "Medical device recalls"
	} 
]

# We are going to call every item within "datasets" a "dataset". As we go through each dataset, we are going to scrape the dataset.
for dataset in datasets:
	try:
		frames = []
		# openFDA API documentation page is here: https://open.fda.gov/
		url = "https://api.fda.gov/" + dataset["slug"]  + "/enforcement.json"
		# The limit can be up to 1000.
		limit = 1000
		# Start the offset at 0.
		offset = 0
		initial_params = 'limit=' + str(limit) + '&skip=' + str(offset) + '&search=state:"NY"'
		# "requests" documentation page is here: https://docs.python-requests.org/en/master/user/quickstart/
		initial_request = requests.get(url, params=initial_params)
		# As we go through each page of the dataset, we are going to scrape that page of the dataset.
		count = initial_request.json()["meta"]["results"]["total"]
		i = 0
		while i < count / limit:
			offset = i * limit
			loop_params = 'limit=' + str(limit) + '&skip=' + str(offset) + '&search=state:"NY"'
			loop_request = requests.get(url, params=loop_params)
			# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
			frame = pd.DataFrame(loop_request.json()["results"])
			frames.append(frame)
			i += 1
		df = pd.concat(frames)
		df["postal_code"] = df["postal_code"].astype(str)
		# ZIP codes 11004 and 11005 are both in Queens and should be excluded.
		df = df[(df["postal_code"].str[0:3].isin(three_digit_zip_codes)) & (df["postal_code"].str[0:5] != "11004") & (df["postal_code"].str[0:5] != "11005")]
		df.pop("openfda")
		df.to_csv("../csv/environment-health/" + dataset["description"] + ".csv", index=False)
	except:
		pass