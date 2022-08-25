import pandas as pd
import logging
import utils
import config

def scrape():
  frames = []
  try:
    for county in config.counties:
      # Federal Railroad Administration National Significant Risk Threshold API documentation page is here: https://www.epa.gov/enviro/envirofacts-data-service-api
      url = "https://safetydata.fra.dot.gov/NSRTAPI/api/nsrtdata"
      params = "state=NY&county=" + county
      request = utils.grab_data(url, params=params)
      frame = pd.DataFrame(request.json()["CROSSINGS"])
      frames.append(frame)
  except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)

  df = pd.concat(frames)
  df.pop("GLOBALRANK")
  df.pop("RANK")
  yield(df)

