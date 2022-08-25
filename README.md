# long-island-datasets
Scrapes data from several websites.

# Scrapers to be refactored
 - [x] cms-data.py
 - [x] cms-provider-data.py
 - [x] college-scorecard.py
 - [x] epa-echo.py
 - [x] epa-sems-envirofacts.py
 - [ ] usace-fuds-arcgis.py
 - [ ] suffolk-county-food-establishment-inspections.py
 - [ ] socrata.py
 - [ ] open-fda.py
 - [ ] nyscjc-determinations.py
 - [ ] ntsb-carol.py
 - [ ] nhtsa-fars.py
 - [x] irs_exempt_organizations.py
 - [x] hhs_oig_exclusions.py
 - [x] fhwa_nbi_arcgis.py
 - [x] fra_nsrt.py
 - [x] dol_osha.py

# To-do
 - move all configuration to config.py
 - assess if we require a wrapper for requests
 - refactor `li_scraper.py` itself
 - utility function to check for LI zips
 - possibly consolidate hhs, irs, nyscjc into a standardized config-based scraper
 - rename scrapers to be more pythonic