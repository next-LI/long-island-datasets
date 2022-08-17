import ssl
import pandas as pd
import logging
import utils
import config

ssl._create_default_https_context = ssl._create_unverified_context

def scrape():
  
  for dataset in config.medicaid_medicare_provider:
    try:
      # U.S. Centers for Medicare and Medicaid Services Provider Data API documentation page is here: https://data.cms.gov/provider-data/docs
      url = "https://data.cms.gov/provider-data/api/1/datastore/query/" + dataset["identifier"] + "/0/download?conditions%5B0%5D%5Bproperty%5D=" + dataset["state_column"] + "&conditions%5B0%5D%5Boperator%5D=%3D&conditions%5B0%5D%5Bvalue%5D=NY&format=csv"
      df = pd.read_csv(url)
      df[dataset["zip_code_column"]] = df[dataset["zip_code_column"]].astype(str)
      # ZIP codes 11004 and 11005 are both in Queens and should be excluded.
      df = df[(df[dataset["zip_code_column"]].str[0:3].isin(config.three_digit_zip_codes)) & (df[dataset["zip_code_column"]].str[0:5] != "11004") & (df[dataset["zip_code_column"]].str[0:5] != "11005")]
      yield(df,dataset["description"])
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)
      pass