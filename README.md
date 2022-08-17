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
 - [x] irs-exempt-organizations.py
 - [x] hhs-oig-exclusions.py

# To-do
 - move all configuration to config.py
 - assess if we require a wrapper for requests
 - refactor `li_scraper.py` itself
 - utility function to check for LI zips
 - possibly consolidate hhs, irs, nyscjc into a standardized config-based scraper
 - rename scrapers to be more pythonic