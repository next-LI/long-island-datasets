import pandas as pd
from sodapy import Socrata

limit = 1000000000

# We are defining the Socrata datasets we want to scrape here.
datasets = [
	{
		"identifier": "cwrk-j5nn",
		# "title": "Estimated Gasoline Sales: Beginning 1995",
		"description": "Gasoline sales by county",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "commerce"
	}, {
		"identifier": "cb42-qumz",
		# "title": "Child Care Regulated Programs",
		"description": "Child care programs",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "eqw2-r5nb",
		# "title": "NYS Attorney Registrations",
		"description": "Attorney registrations",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "ca8h-8gjq",
		# "title": "Index Crimes by County and Agency: Beginning 1990",
		"description": "Crimes by law enforcement agency",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "34dd-6g2j",
		# "title": "Index, Violent, Property, and Firearm Rates By County: Beginning 1990",
		"description": "Crimes by county",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "6xda-q7ev",
		# "title": "Hate Crimes by County and Bias Type: Beginning 2010",
		"description": "Hate crimes by county",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "nymx-kgkn",
		# "title": "Jail Population By County: Beginning 1997",
		"description": "Jail population by county",
		"domain": "data.ny.gov",
		"where": "starts_with(facility_name, 'Nassau') OR starts_with(facility_name, 'Suffolk')",
		"category": "community"
	}, {
		"identifier": "rikd-mt35",
		# "title": "Adult Arrests 18 and Older by County: Beginning 1970",
		"description": "Adult arrests by county",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "dq6j-8u8z",
		# "title": "Supplemental Nutrition Assistance Program (SNAP) Caseloads and Expenditures: Beginning 2002",
		"description": "Supplemental Nutrition Assistance Program cases and spending",
		"domain": "data.ny.gov",
		"where": "district='Nassau' OR district='Suffolk'",
		"category": "community"
	}, {
		"identifier": "kym4-b5dg",
		# "title": "Supplemental Security Income (SSI) Recipients and Expenditures: Beginning 2002",
		"description": "Supplemental Security Income cases and spending",
		"domain": "data.ny.gov",
		"where": "district='Nassau' OR district='Suffolk'",
		"category": "community"
	}, {
		"identifier": "42wv-qbv6",
		# "title": "Public Assistance (PA) Caseloads and Expenditures: Beginning 2002",
		"description": "Temporary assistance cases and spending",
		"domain": "data.ny.gov",
		"where": "district='Nassau' OR district='Suffolk'",
		"category": "community"
	}, {
		"identifier": "5mdi-3rq9",
		# "title": "Public Assistance Cases with Earned Income: Beginning April 2006",
		"description": "Temporary assistance cases with earned income",
		"domain": "data.ny.gov",
		"where": "district='Nassau' OR district='Suffolk'",
		"category": "community"
	}, {
		"identifier": "5q72-7g66",
		# "title": "Council On The Arts Grant Awards: Beginning 2003",
		"description": "State arts grants",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "community"
	}, {
		"identifier": "8f3n-xj78",
		# "title": "State Park Annual Attendance Figures by Facility: Beginning 2003",
		"description": "State park annual attendance",
		"domain": "data.ny.gov",
		"where": "oprhp_region='Long Island'",
		"category": "community"
	}, {
		"identifier": "n9v6-gdp6",
		# "title": "Active Corporations: Beginning 1800",
		"description": "Active corporations",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "economy"
	}, {
		"identifier": "26ei-n4eb",
		# "title": "Database of Economic Incentives",
		"description": "State economic development aid",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "economy"
	}, {
		"identifier": "5hyu-bdh8",
		# "title": "Local Area Unemployment Statistics: Beginning 1976",
		"description": "Unemployment rates",
		"domain": "data.ny.gov",
		"where": "area='Long Island'",
		"category": "economy"
	}, {
		"identifier": "6k74-dgkb",
		# "title": "Current Employment Statistics: Beginning 1990",
		"description": "Job levels by sector",
		"domain": "data.ny.gov",
		"where": "area_name='Nassau-Suffolk Metropolitan Division'",
		"category": "economy"
	}, {
		"identifier": "gkgz-nw24",
		# "title": "Occupational Employment and Wage Statistics",
		"description": "Pay levels by sector",
		"domain": "data.ny.gov",
		"where": "area_name='Long Island'",
		"category": "economy"
	}, {
		"identifier": "b7d6-zygf",
		# "title": "Long-term Industry Projections",
		"description": "Ten-year job projections by sector",
		"domain": "data.ny.gov",
		"where": "area='Long Island'",
		"category": "economy"
	}, {
		"identifier": "pqm4-9qqb",
		# "title": "Long Term Occupational Projections",
		"description": "Ten-year job projections by job title",
		"domain": "data.ny.gov",
		"where": "area='Long Island'",
		"category": "economy"
	}, {
		"identifier": "9pb8-dg53",
		# "title": "New York State School Aid: Beginning School Year 1996-97",
		"description": "State aid to schools",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "education"
	}, {
		"identifier": "c6ci-rzpg",
		# "title": "Environmental Remediation Sites",
		"description": "State hazardous waste cleanup sites",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "environment-health"
	}, {
		"identifier": "wwwd-za77",
		# "title": "Beach Water Testing: Beginning 2015",
		"description": "Beach water testing",
		"domain": "data.ny.gov",
		"where": "region='Long Island'",
		"category": "environment-health"
	}, {
		"identifier": "d6dy-3h7r",
		# "title": "Food Safety Inspections – Current Ratings",
		"description": "State food safety inspections",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "environment-health"
	}, {
		"identifier": "cnih-y5dw",
		# "title": "Food Service Establishment: Last Inspection",
		"description": "Nassau County food establishment inspections",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU'",
		"category": "environment-health"
	}, {
		"identifier": "ebmi-8ctw",
		# "title": "Professional Medical Conduct Board Actions: Beginning 1990",
		"description": "State medical board actions",
		"domain": "health.data.ny.gov",
		"where": "",
		"category": "environment-health"
	}, {
		"identifier": "hbu9-xsrx",
		# "title": "Radon Test Results By Town: Beginning 1987",
		"description": "Radon testing by town or city",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU' OR county='SUFFOLK'",
		"category": "environment-health"
	}, {
		"identifier": "jr8b-6gh6",
		# "title": "Influenza Laboratory-Confirmed Cases By County: Beginning 2009-10 Season",
		"description": "Flu cases by county",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU' OR county='SUFFOLK'",
		"category": "environment-health"
	}, {
		"identifier": "jxy9-yhdk",
		# "title": "Baby Names: Beginning 2007",
		"description": "Baby names",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU' OR county='SUFFOLK'",
		"category": "environment-health"
	}, {
		"identifier": "keti-qx5t",
		# "title": "Medicaid Enrolled Provider Listing",
		"description": "Health care providers enrolled in Medicaid",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU' OR county='SUFFOLK'",
		"category": "environment-health"
	}, {
		"identifier": "sn5m-dv52",
		# "title": "Vital Statistics: Opioid-Related Deaths by County: Beginning 2003",
		"description": "Opioid deaths by county",
		"domain": "health.data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "environment-health"
	}, {
		"identifier": "5pme-xbs5",
		# "title": "School Immunization Survey: Beginning 2012-13 School Year",
		"description": "School immunization rates",
		"domain": "health.data.ny.gov",
		"where": "county='NASSAU' OR county='SUFFOLK'",
		"category": "environment-health"
	}, {
		"identifier": "54ci-sdfi",
		# "title": "Community Health Indicator Reports (CHIRS): Latest Data",
		"description": "Cancer rates by county",
		"domain": "health.data.ny.gov",
		"where": "health_topic='Cancer Indicators' AND (county_name='Nassau' OR county_name='Suffolk')",
		"category": "environment-health"
	}, {
		"identifier": "duk7-xrni",
		# "title": "New York State Statewide COVID-19 Vaccination Data by County",
		"description": "State COVID-19 vaccinations by county",
		"domain": "health.data.ny.gov",
		"where": "region='Long Island'",
		"category": "environment-health"
	}, {
		"identifier": "jw46-jpb7",
		# "title": "New York State Statewide COVID-19 Hospitalizations and Beds",
		"description": "State COVID-19 hospitalizations",
		"domain": "health.data.ny.gov",
		"where": "ny_forward_region='LONG ISLAND'",
		"category": "environment-health"
	}, {
		"identifier": "e7te-hhb2",
		# "title": "New York State Statewide COVID-19 Testing by Zip Code",
		"description": "State COVID-19 testing by ZIP code",
		"domain": "health.data.ny.gov",
		"where": "county_code='59' OR county_code='103'",
		"category": "environment-health"
	}, {
		"identifier": "xdss-u53e",
		# "title": "New York State Statewide COVID-19 Testing",
		"description": "State COVID-19 testing by county",
		"domain": "health.data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "environment-health"
	}, {
		"identifier": "xymy-pny5",
		# "title": "New York State Statewide COVID-19 Fatalities by County",
		"description": "State COVID-19 death counts by county",
		"domain": "health.data.ny.gov",
		"where": "geography='Nassau' OR geography='Suffolk'",
		"category": "environment-health"
	}, {
		"identifier": "kn79-hsxy",
		# "title": "Provisional COVID-19 Death Counts in the United States by County",
		"description": "CDC COVID-19 death counts by county",
		"domain": "data.cdc.gov",
		"where": "state_name='NY' AND (county_name='Nassau County' OR county_name='Suffolk County')",
		"category": "environment-health"
	}, {
		"identifier": "e9ss-239a",
		# "title": "Campaign Finance Disclosure Reports Data: Beginning 1999",
		"description": "Local election campaign finance reports",
		"domain": "data.ny.gov",
		"where": "county_desc='Nassau' OR county_desc='Suffolk'",
		"category": "government"
	}, {
		"identifier": "7x2g-h32p",
		# "title": "Campaign Finance Filer Data: Beginning 1974",
		"description": "Local election campaign finance filers",
		"domain": "data.ny.gov",
		"where": "county_desc='Nassau' OR county_desc='Suffolk'",
		"category": "government"
	}, {
		"identifier": "iq85-sdzs",
		# "title": "Real Property Tax Rates Levy Data By Municipality: Beginning 2004",
		"description": "Property tax rates and levies",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "government"
	}, {
		"identifier": "ekci-x6aq",
		# "title": "Active Construction Projects",
		"description": "State dormitory authority active construction projects",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "government"
	}, {
		"identifier": "qbd7-9grw",
		# "title": "New Debt Issuance for Local Authorities",
		"description": "Local authority bonds and notes issued",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "8w5p-k45m",
		# "title": "Procurement Report for Local Authorities",
		"description": "Local authority procurement contracts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "kmkz-x3aa",
		# "title": "Real Property Transactions of Local Authorities",
		"description": "Local authority real estate transactions",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "fx93-cifz",
		# "title": "Salary Information for Local Authorities",
		"description": "Local authority salaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "vfju-zm9q",
		# "title": "Schedule of Debt for Local Authorities",
		"description": "Local authority debts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "cgg6-2ah8",
		# "title": "Summary Financial Information for Local Authorities",
		"description": "Local authority financial summaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Freeport Community Development Agency', 'Glen Cove Community Development Agency', 'Huntington Community Development Agency', 'Incorporated Village of Hempstead Community Development Agency', 'Islip Resource Recovery Authority', 'Nassau County Bridge Authority', 'Nassau County Sewer and Storm Water Finance Authority', 'North Hempstead Solid Waste Management Authority', 'Suffolk County Judicial Facilities Agency', 'Suffolk County Water Authority', 'Town of Islip Community Development Agency', 'Town of North Hempstead Community Development Agency', 'Town of Riverhead Community Development Agency', 'Village of Patchogue Community Development Agency', 'Village of Rockville Centre Community Development Agency', 'Water Authority of Great Neck North', 'Water Authority of Southeastern Nassau County', 'Water Authority of Western Nassau County')",
		"category": "government"
	}, {
		"identifier": "sh2f-cc7d",
		# "title": "New Debt Issuance for Local Development Corporations",
		"description": "Local development corporation bonds and notes issued",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "d84c-dk28",
		# "title": "Procurement Report for Local Development Corporations",
		"description": "Local development corporation procurement contracts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "ajgp-mddq",
		# "title": "Real Property Transactions of Local Development Corporations",
		"description": "Local development corporation real estate transactions",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "wryv-rizw",
		# "title": "Salary Information for Local Development Corporations",
		"description": "Local development corporation salaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "utc6-v4cn",
		# "title": "Schedule of Debt for Local Development Corporations",
		"description": "Local development corporation debts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "wgry-y5zd",
		# "title": "Summary Financial Information for Local Development Corporations",
		"description": "Local development corporation financial summaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "9kfh-uzu3",
		# "title": "Local Development Corporations Bonds",
		"description": "Local development corporation projects financed by bonds",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "j5ab-5nj2",
		# "title": "Local Development Corporations Grants Dataset",
		"description": "Local development corporation projects financed by grants",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "vp83-gfyz",
		# "title": "Local Development Corporations Loans",
		"description": "Local development corporation projects financed by loans",
		"domain": "data.ny.gov",
		"where": "authority_name in('Glen Cove Local Economic Assistance Corporation', 'Long Beach Local Development Corporation', 'Nassau County Economic Development Corporation', 'Nassau County Land Bank Corporation', 'Nassau County Local Economic Assistance Corporation', 'Nassau County Tobacco Settlement Corporation', 'Riverhead IDA Economic Job Development Corporation', 'Southold Local Development Corporation', 'Suffolk County Economic Development Corporation', 'Suffolk Tobacco Asset Securitization Corporation', 'The Recreation and Economic Development Corporation of Suffolk County', 'The Suffolk County Land Bank Corporation', 'The Town of Huntington Economic Development Corporation', 'Town of Babylon L. D. Corporation II', 'Town of Brookhaven Local Development Corporation', 'Town of Hempstead Local Development Corp.', 'Town of Huntington Local Development Corporation', 'Town Of Islip Economic Development Corporation', 'Town of North Hempstead Business and Tourism Development Corporation', 'Wyandanch Community Development Corporation')",
		"category": "government"
	}, {
		"identifier": "cci8-aavx",
		# "title": "New Debt Issuance for Industrial Development Agencies",
		"description": "Industrial development agency bonds and notes issued",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "p3p6-xqr5",
		# "title": "Procurement Report for Industrial Development Agencies",
		"description": "Industrial development agency procurement contracts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "dixy-n3q7",
		# "title": "Real Property Transactions of Industrial Development Agencies",
		"description": "Industrial development agency real estate transactions",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "9yx9-29p4",
		# "title": "Salary Information for Industrial Development Agencies",
		"description": "Industrial development agency salaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "dtk8-znku",
		# "title": "Schedule of Debt for Industrial Development Agencies",
		"description": "Industrial development agency debts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "2jrz-w65a",
		# "title": "Summary Financial Information for Industrial Development Agencies",
		"description": "Industrial development agency financial summaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "9rtk-3fkw",
		# "title": "Industrial Development Agencies' Project Data",
		"description": "Industrial development agency projects",
		"domain": "data.ny.gov",
		"where": "authority_name in('Babylon Industrial Development Agency', 'Brookhaven Industrial Development Agency', 'Glen Cove Industrial Development Agency', 'Hempstead Industrial Development Agency', 'Islip Industrial Development Agency', 'Nassau County Industrial Development Agency', 'Riverhead Industrial Development Agency', 'Suffolk County Industrial Development Agency')",
		"category": "government"
	}, {
		"identifier": "83xh-6x8i",
		# "title": "New Debt Issuance for State Authorities",
		"description": "State authority bonds and notes issued",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "ehig-g5x3",
		# "title": "Procurement Report for State Authorities",
		"description": "State authority procurement contracts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "t7uh-5ac8",
		# "title": "Real Property Transactions of State Authorities",
		"description": "State authority real estate transactions",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "unag-2p27",
		# "title": "Salary Information for State Authorities",
		"description": "State authority salaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "f7ju-wpvk",
		# "title": "Schedule of Debt for State Authorities",
		"description": "State authority debts",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "y6wc-tvay",
		# "title": "Summary Financial Information for State Authorities",
		"description": "State authority financial summaries",
		"domain": "data.ny.gov",
		"where": "authority_name in('Long Island Power Authority', 'Metropolitan Transportation Authority', 'Nassau County Interim Finance Authority', 'Nassau Health Care Corporation', 'Utility Debt Securitization Authority (UDSA)')",
		"category": "government"
	}, {
		"identifier": "4sut-q3dt",
		# "title": "Real Property Assessment Equity Statistics By Municipality: Beginning 2004",
		"description": "Real property assessment equity statistics",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "housing"
	}, {
		"identifier": "h9zr-j4pg",
		# "title": "Bus Safety Information Network (BUSNET) Operator Report: Beginning 2009",
		"description": "Bus operator inspections",
		"domain": "data.ny.gov",
		"where": "region='10'",
		"category": "transportation"
	}, {
		"identifier": "rz8t-4kmq",
		# "title": "Transportation Projects in Your Neighborhood",
		"description": "State transportation department projects",
		"domain": "data.ny.gov",
		"where": "region='10 LONG ISLAND'",
		"category": "transportation"
	}, {
		"identifier": "w4pv-hbkt",
		# "title": "Vehicle, Snowmobile, and Boat Registrations",
		"description": "Vehicle, snowmobile, and boat registrations",
		"domain": "data.ny.gov",
		"where": "state='NY' AND (county='NASSAU' OR county='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "6amx-2pbv",
		# "title": "Annual Average Daily Traffic (AADT): Beginning 1977",
		"description": "Annual average daily traffic",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "transportation"
	}, {
		"identifier": "e8ky-4vqe",
		# "title": "Motor Vehicle Crashes - Case Information: Three Year Window",
		"description": "Motor vehicle crashes",
		"domain": "data.ny.gov",
		"where": "county_name='NASSAU' OR county_name='SUFFOLK'",
		"category": "transportation"
	}, {
		"identifier": "wpyb-cjy8",
		# "title": "Bridge Conditions, NYS Department of Transportation",
		"description": "Bridge inspections (state data)",
		"domain": "data.ny.gov",
		"where": "county='Nassau' OR county='Suffolk'",
		"category": "transportation"
	}, {
		"identifier": "m2f8-22s6",
		# "title": "Crossing Inventory Data - Current",
		"description": "Railroad crossings (current)",
		"domain": "data.transportation.gov",
		"where": "statename='NEW YORK' AND (countyname='NASSAU' OR countyname='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "vhwz-raag",
		# "title": "Crossing Inventory Data - Historical",
		"description": "Railroad crossings (historical)",
		"domain": "data.transportation.gov", 
		"where": "statename='NEW YORK' AND (countyname='NASSAU' OR countyname='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "7wn6-i5b9",
		# "title": "Highway-Rail Grade Crossing Accident Data",
		"description": "Railroad crossing accidents",
		"domain": "data.transportation.gov", 
		"where": "statename='NEW YORK' AND (countyname='NASSAU' OR countyname='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "85tf-25kj",
		# "title": "Rail Equipment Accident/Incident Data",
		"description": "Railroad equipment accidents",
		"domain": "data.transportation.gov",
		"where": "statename='NEW YORK' AND (countyname='NASSAU' OR countyname='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "rash-pd2d",
		# "title": "Injury/Illness Summary - Casualty Data",
		"description": "Railroad injuries and illnesses",
		"domain": "data.transportation.gov", 
		"where": "statename='NEW YORK' AND (countyname='NASSAU' OR countyname='SUFFOLK')",
		"category": "transportation"
	}, {
		"identifier": "m8i6-zdsy",
		# "title": "Injury/Illness Summary - Operational Data",
		"description": "Railroad monthly operational data",
		"domain": "data.transportation.gov", 
		"where": "railroadcode in('LI', 'NYA', 'BHR')",
		"category": "transportation"
	},  {
		"identifier": "h3hh-wfqt",
		# "title": "Transit System Time Series",
		"domain": "data.transportation.gov",
		"description": "Transit system annual financial data",
		"where": "_5_digit_ntd_id in('20006', '20071', '20072', '20100', '20206', '20217')",
		"category": "transportation"
	}, {
		"identifier": "wwdp-t4re",
		# "title": "Service Flat File",
		"domain": "data.transportation.gov",
		"description": "Transit system annual service data",
		"where": "_5_digit_ntd_id in('20006', '20071', '20072', '20100', '20206', '20217')",
		"category": "transportation"
	}, {
		"identifier": "5ti2-5uiv",
		# "title": "Monthly Modal Time Series",
		"domain": "data.transportation.gov",
		"description": "Transit system monthly safety data",
		"where": "_5_digit_ntd_id in('20006', '20071', '20072', '20100', '20206', '20217')",
		"category": "transportation"
	}, {
		"identifier": "9ivb-8ae9",
		# "title": "Major Safety Events",
		"domain": "data.transportation.gov",
		"description": "Transit system safety incidents",
		"where": "_5_digit_ntd_id in('20006', '20071', '20072', '20100', '20206', '20217')",
		"category": "transportation"
	}
]

# We are going to call every item within "datasets" a "dataset". As we go through each dataset, we are going to scrape the dataset.
for dataset in datasets:
	try:
		# "sodapy" documentation page is here: https://github.com/xmunoz/sodapy
		client = Socrata(dataset["domain"], None)
		results = client.get(dataset["identifier"], where=dataset["where"], limit=limit)
		# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
		df = pd.DataFrame.from_records(results)
		for column in df:
			for cell in df[column][:10]:
				if isinstance(cell, dict):
					df.pop(column)
					break
		df.to_csv("../csv/" + dataset["category"] + "/" + dataset["description"] + ".csv", index=False)
	except:
		pass