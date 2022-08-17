import ssl
import requests
from datetime import datetime
import pandas as pd
import logging
import config
import utils

ssl._create_default_https_context = ssl._create_unverified_context

def scrape():

  for dataset in config.medicaid_medicare_data:
    try:
      versions_url = "https://data.cms.gov/jsonapi/node/dataset"
      versions_params = "include=field_dataset_type,field_ref_primary_data_file&fields[node--dataset]=field_dataset_version,field_ref_primary_data_file,field_last_updated_date&filter[field_dataset_type.name]=" + dataset["slug"] + "&sort=-field_dataset_version"
      versions_request = utils.grab_data(versions_url, params=versions_params)
      frames = []
      
      for version in versions_request.json()["data"]:
        year_ending = version["attributes"]["field_dataset_version"]
        year = datetime.strptime(year_ending, "%Y-%m-%d").strftime("%Y")
        # U.S. Centers for Medicare and Medicaid Services Data API documentation page is here: https://data.cms.gov/api-docs
        version_url = "https://data.cms.gov/data-api/v1/dataset/" + version["id"] + "/data.csv?" + dataset["params"]
        frame = pd.read_csv(version_url, encoding="latin-1")

        if "Year" not in frame:
          frame["Year"] = year

        frame.columns = [ name.lower() for name in frame.columns ]
        frames.append(frame)
      df = pd.concat(frames)
      yield(df,dataset["description"])
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)
      pass