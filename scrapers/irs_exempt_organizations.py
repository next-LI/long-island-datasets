import ssl
import pandas as pd
import config
import logging

ssl._create_default_https_context = ssl._create_unverified_context

# Internal Revenue Service Exempt Organizations Business Master File Extract download page is here: https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf
url = "https://www.irs.gov/pub/irs-soi/eo_ny.csv"

def scrape():
  try:
    df = pd.read_csv(url)
    df = df[(df["ZIP"].str[0:3].isin(config.three_digit_zip_codes)) & (df["ZIP"].str[0:5] != "11004") & (df["ZIP"].str[0:5] != "11005")]
    yield(df)
  except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)
    pass