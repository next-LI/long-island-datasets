import pandas as pd
import os
import logging
import utils
from dotenv import load_dotenv

load_dotenv(os.path.join('', '.env'))
api_key = os.getenv("DOL_API")

def scrape():
  frames = []
  # The limit can be up to 200.
  limit = 200
  # Start the offset at 0.
  offset = 0
  # As we go through each page of the dataset, we are going to scrape that page of the dataset.
  i = 0
  while i >= 0:
    try:
      offset = i * limit
      # OSHA Enforcement API documentation page is here: https://developer.dol.gov/health-and-safety/dol-osha-enforcement/
      # OSHA Long Island Area Office is jurisdiction number 214700.
      url = "https://data.dol.gov/get/inspection/limit/" + str(limit) + "/offset/" + str(offset) + "/filter_column/reporting_id=214700"
      request = utils.grab_data(url, headers={"X-API-KEY": api_key})
      frame = pd.DataFrame(request.json())
      frames.append(frame)
      if len(request.json()) < limit:
        break
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)			
    i += 1

  df = pd.concat(frames)
  df.pop("LOAD_DT")
  df.pop("RNUM")
  df["URL"] = "https://www.osha.gov/pls/imis/establishment.inspection_detail?id=" + df["ACTIVITY_NR"]
  yield(df)
