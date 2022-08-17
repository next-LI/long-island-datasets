import requests
import pandas as pd
import logging
import config
import utils
import os
from dotenv import load_dotenv

load_dotenv(os.path.join('', '.env'))
api_key = os.getenv("CENSUS_KEY")

zip_codes_url = "https://api.census.gov/data/2010/dec/sf1"
zip_codes_params = "get=NAME&for=zip%20code%20tabulation%20area%20(or%20part):*&in=state:36&key=" + api_key
zip_codes_request = utils.grab_data(zip_codes_url, params=zip_codes_params)
zip_codes_list = zip_codes_request.json()

# ZIP codes 11004 and 11005 are both in Queens and should be excluded.
zip_codes = [ zip_code[2] for zip_code in zip_codes_list if zip_code[2][0:3] in config.three_digit_zip_codes and zip_code[2][0:5] != "11004" and zip_code[2][0:5] != "11005" ]
frames = []

def scrape():
  for zip_code in zip_codes:
    try:
      # Enforcement and Compliance History Online API documentation page is here: https://echo.epa.gov/tools/web-services
      cases_url = "https://echodata.epa.gov/echo/case_rest_services.get_case_info"
      cases_params = "p_fac_zip=" + zip_code
      cases_request = utils.grab_data(cases_url, params=cases_params)
      if len(cases_request.json()["Results"]["Cases"]) > 0:
        frame = pd.DataFrame(cases_request.json()["Results"]["Cases"])
        frame["Zip"] = zip_code
        frame["Url"] = "https://echo.epa.gov/enforcement-case-report?activity_id=" + frame["ActivityID"]
        frames.append(frame)
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)
      pass

  df = pd.concat(frames)
  yield(df)
  