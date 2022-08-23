import ssl
import pandas as pd
import logging
import config
import utils
import os
from dotenv import load_dotenv

load_dotenv(os.path.join('', '.env'))
api_key = os.getenv("COLLEGE_SCORECARD")
ssl._create_default_https_context = ssl._create_unverified_context

frames = []

def scrape():
  for zip_code in config.three_digit_zip_codes:
    try:
      # College Scorecard Data API documentation page is here: https://github.com/RTICWDT/open-data-maker/blob/master/API.md
      url = "https://api.data.gov/ed/collegescorecard/v1/schools.csv?fields=latest&latest.school.state=NY&latest.school.zip__range=" + zip_code + "00.." + zip_code + "99&per_page=500&page=0&api_key=" + api_key
      frame = pd.read_csv(url)
      frames.append(frame)
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)
      pass

  df = pd.concat(frames)
  df["latest.school.zip"] = df["latest.school.zip"].astype(str)
  # ZIP codes 11004 and 11005 are both in Queens and should be excluded.
  df[(df["latest.school.zip"].str[0:5] != "11004") & (df["latest.school.zip"].str[0:5] != "11005")]
  yield(df)
  