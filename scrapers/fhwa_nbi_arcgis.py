import pandas as pd
import logging
import utils
import config

# National Bridge Inventory (NBI) guide is here: https://www.fhwa.dot.gov/bridge/mtguide.pdf
def scrape():
  results = []

  # NBI Bridges API documentation page is here: https://hifld-geoplatform.opendata.arcgis.com/datasets/national-bridge-inventory-nbi-bridges/api
  url = "https://geo.dot.gov/server/rest/services/Hosted/National_Bridge_Inventory_DS/FeatureServer/0/query"
  params = "where=(state_code_001=%2736%27)%20AND%20(county_code_003=%27059%27%20OR%20county_code_003=%27103%27)&outFields=county_code_003,structure_number_008,location_009,facility_carried_007,features_desc_006a,owner_022,year_built_027,year_reconstructed_106,adt_029,year_adt_030,date_of_inspect_090,bridge_condition&outSR=4326&f=json"
  
  try:
    request = utils.grab_data(url, params=params)

    for bridge in request.json()["features"]:
      result = {}
      result["structure_number"] =  bridge["attributes"]["structure_number_008"]
      result["county"] = config.fhwa_nbi_arcgis["counties"][bridge["attributes"]["county_code_003"]]
      result["location"] =  bridge["attributes"]["location_009"]
      result["feature_carried"] =  bridge["attributes"]["facility_carried_007"]
      result["feature_crossed"] =  bridge["attributes"]["features_desc_006a"]
      result["owner"] = config.fhwa_nbi_arcgis["owners"][bridge["attributes"]["owner_022"]]
      result["year_built"] =  bridge["attributes"]["year_built_027"]
      if bridge["attributes"]["year_reconstructed_106"] == 0:
        result["year_reconstructed"] = ""
      else:
        result["year_reconstructed"] =  bridge["attributes"]["year_reconstructed_106"]
      result["average_daily_traffic"] = bridge["attributes"]["adt_029"]
      result["year_of_average_daily_traffic"] = bridge["attributes"]["year_adt_030"]
      result["date_of_last_inspection_mmyy"] = bridge["attributes"]["date_of_inspect_090"].zfill(4)
      result["bridge_condition"] = config.fhwa_nbi_arcgis["conditions"][bridge["attributes"]["bridge_condition"]]
      result["latitude"] =  bridge["geometry"]["y"]
      result["longitude"] =  bridge["geometry"]["x"]
      if result["structure_number"].startswith("00000000"):
        results.append(result)
  except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)

  df = pd.DataFrame(results)
  yield(df)
  