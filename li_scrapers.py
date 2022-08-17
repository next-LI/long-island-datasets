import importlib
import pandas as pd
from datetime import datetime
import gc

cms_data = importlib.import_module('scrapers.cms-data')
cms_provider_data = importlib.import_module('scrapers.cms-provider-data')
college_scorecard = importlib.import_module('scrapers.college-scorecard')
epa_echo = importlib.import_module('scrapers.epa-echo')
epa_sems_envirofacts = importlib.import_module('scrapers.epa-sems-envirofacts')

for dataframe in college_scorecard.scrape():  
  dataframe.to_csv("csv/education/Colleges.csv", index=False)

for dataframe in epa_echo.scrape():
  dataframe.to_csv("csv/environment-health/Environmental law violation cases.csv", index=False)

for dataframes, dataset in cms_data.scrape():
  dataframes.to_csv("csv/environment-health/" + dataset + ".csv", index=False)

for dataframes, dataset in cms_provider_data.scrape():
  dataframes.to_csv("csv/environment-health/" + dataset + ".csv", index=False)

for dataframe, dataset in epa_sems_envirofacts.scrape():
  dataframe.to_csv("csv/environment-health/" + dataset + ".csv", index=False)