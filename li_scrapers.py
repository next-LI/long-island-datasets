import importlib
from datetime import datetime
import gc
from scrapers import fhwa_nbi_arcgis, hhs_oig_exclusions, cms_data, cms_provider_data, college_scorecard, epa_echo, epa_sems_envirofacts, irs_exempt_organizations, dol_osha, fra_nsrt, fhwa_nbi_arcgis

# for dataframe in college_scorecard.scrape():  
#   dataframe.to_csv("csv/education/Colleges.csv", index=False)

# for dataframe in irs_exempt_organizations.scrape():
#   dataframe.to_csv("csv/community/Nonprofit organizations.csv", index=False)

# for dataframe in dol_osha.scrape():
#   dataframe.to_csv("csv/economy/Workplace inspections.csv", index=False)

for dataframe in fra_nsrt.scrape():
  dataframe.to_csv("csv/transportation/Railroad crossing collision probabilities.csv", index=False)

for dataframe in fhwa_nbi_arcgis.scrape():
  dataframe.to_csv("csv/transportation/Bridge inspections (federal data).csv", index=False)

# for dataframe in epa_echo.scrape():
#   dataframe.to_csv("csv/environment-health/Environmental law violation cases.csv", index=False)

# for dataframe in hhs_oig_exclusions.scrape():
#   dataframe.to_csv("csv/environment-health/Health care providers excluded from Medicare and Medicaid.csv", index=False)

# for dataframes, dataset in cms_data.scrape():
#   dataframes.to_csv("csv/environment-health/" + dataset + ".csv", index=False)

# for dataframes, dataset in cms_provider_data.scrape():
#   dataframes.to_csv("csv/environment-health/" + dataset + ".csv", index=False)

# for dataframe, dataset in epa_sems_envirofacts.scrape():
#   dataframe.to_csv("csv/environment-health/" + dataset + ".csv", index=False)


  