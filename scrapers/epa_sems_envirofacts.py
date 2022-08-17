import ssl
import pandas as pd
import logging
import config

ssl._create_default_https_context = ssl._create_unverified_context

# We are going to call every item within "datasets" a "dataset". As we go through each dataset, we are going to scrape the dataset.
def scrape():
  for dataset in config.epa_sems_envirofacts:
    try:
      frames = []
      # We are going to call every item within "counties" a "county". As we go through each county, we are going to scrape the dataset for that county.
      for county in config.counties:
        # Envirofacts API documentation page is here: https://www.epa.gov/enviro/envirofacts-data-service-api
        url = "https://data.epa.gov/efservice/" + dataset["slug"] + "/site_state/NY/site_cnty_name/" + county + "/CSV"
        # "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
        frame = pd.read_csv(url)
        frames.append(frame)
      df = pd.concat(frames)
      yield(df, dataset["description"])
    except Exception as e:
      logging.error('Error at %s', 'division', exc_info=e)
      pass