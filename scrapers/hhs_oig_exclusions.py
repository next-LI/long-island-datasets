import ssl
import pandas as pd
import config
import logging

ssl._create_default_https_context = ssl._create_unverified_context

# U.S. Department of Health and Human Services Office of Inspector General exclusions database page is here: https://oig.hhs.gov/exclusions/exclusions_list.asp
url = "https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv"

def scrape():
  try:
    df = pd.read_csv(url)
    df["ZIP"] = df["ZIP"].astype(str)
    df = df[(df["ZIP"].str[0:3].isin(config.three_digit_zip_codes)) & (df["ZIP"].str[0:5] != "11004") & (df["ZIP"].str[0:5] != "11005") & (df["STATE"] == "NY")]
    yield(df)
  except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)
    pass