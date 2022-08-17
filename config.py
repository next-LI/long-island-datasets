# All ZIP codes in Nassau and Suffolk counties start with the digits 110, 115, 117, 118, or 119, except Fishers Island, which is 06390.
three_digit_zip_codes = ["063", "110", "115", "117", "118", "119"]

counties = ["NASSAU", "SUFFOLK"]

# We are defining the U.S. Centers for Medicare and Medicaid Services Data datasets we want to scrape here.
medicaid_medicare_data = [
	{
		"slug": "Medicare+Part+D+Opioid+Prescribing+Rates+-+by+Geography",
		# "title": "Medicare Part D Opioid Prescribing Rates - by Geography",
		"description": "Medicare Part D opioid prescriptions by county and ZIP code",
		"params": "filter[root-group][group][conjunction]=AND&filter[group-0][group][conjunction]=OR&filter[group-0][group][memberOf]=root-group&filter[filter-0-0][condition][path]=Prscrbr_Geo_Desc&filter[filter-0-0][condition][operator]=STARTS_WITH&filter[filter-0-0][condition][value]=New%20York%3ANassau&filter[filter-0-0][condition][memberOf]=group-0&filter[filter-0-1][condition][path]=Prscrbr_Geo_Desc&filter[filter-0-1][condition][operator]=STARTS_WITH&filter[filter-0-1][condition][value]=New%20York%3ASuffolk&filter[filter-0-1][condition][memberOf]=group-0",
		"needs_year_column": False
	}, {
		"slug": "Medicare+Part+D+Prescribers+-+by+Provider",
		# "title": "Medicare Part D Prescribers - by Provider",
		"description": "Medicare Part D prescriptions by provider",
		"params": "filter[root-group][group][conjunction]=AND&filter[group-0][group][conjunction]=OR&filter[group-0][group][memberOf]=root-group&filter[filter-0-0][condition][path]=Prscrbr_zip5&filter[filter-0-0][condition][operator]=STARTS_WITH&filter[filter-0-0][condition][value]=063&filter[filter-0-0][condition][memberOf]=group-0&filter[filter-0-1][condition][path]=Prscrbr_zip5&filter[filter-0-1][condition][operator]=STARTS_WITH&filter[filter-0-1][condition][value]=110&filter[filter-0-1][condition][memberOf]=group-0&filter[filter-0-2][condition][path]=Prscrbr_zip5&filter[filter-0-2][condition][operator]=STARTS_WITH&filter[filter-0-2][condition][value]=115&filter[filter-0-2][condition][memberOf]=group-0&filter[filter-0-3][condition][path]=Prscrbr_zip5&filter[filter-0-3][condition][operator]=STARTS_WITH&filter[filter-0-3][condition][value]=117&filter[filter-0-3][condition][memberOf]=group-0&filter[filter-0-4][condition][path]=Prscrbr_zip5&filter[filter-0-4][condition][operator]=STARTS_WITH&filter[filter-0-4][condition][value]=118&filter[filter-0-4][condition][memberOf]=group-0&filter[filter-0-5][condition][path]=Prscrbr_zip5&filter[filter-0-5][condition][operator]=STARTS_WITH&filter[filter-0-5][condition][value]=119&filter[filter-0-5][condition][memberOf]=group-0&filter[group-1][group][conjunction]=AND&filter[group-1][group][memberOf]=root-group&filter[filter-1-0][condition][path]=Prscrbr_State_Abrvtn&filter[filter-1-0][condition][operator]=%3D&filter[filter-1-0][condition][value]=NY&filter[filter-1-0][condition][memberOf]=group-1&filter[group-2][group][conjunction]=AND&filter[group-2][group][memberOf]=root-group&filter[filter-2-0][condition][path]=Prscrbr_zip5&filter[filter-2-0][condition][operator]=<>&filter[filter-2-0][condition][value]=11004&filter[filter-2-0][condition][memberOf]=group-2&filter[filter-2-1][condition][path]=Prscrbr_zip5&filter[filter-2-1][condition][operator]=<>&filter[filter-2-1][condition][value]=11005&filter[filter-2-1][condition][memberOf]=group-2&filter[group-3][group][conjunction]=OR&filter[group-3][group][memberOf]=root-group&filter[filter-3-0][condition][path]=Prscrbr_Zip5&filter[filter-3-0][condition][operator]=STARTS_WITH&filter[filter-3-0][condition][value]=063&filter[filter-3-0][condition][memberOf]=group-3&filter[filter-3-1][condition][path]=Prscrbr_Zip5&filter[filter-3-1][condition][operator]=STARTS_WITH&filter[filter-3-1][condition][value]=110&filter[filter-3-1][condition][memberOf]=group-3&filter[filter-3-2][condition][path]=Prscrbr_Zip5&filter[filter-3-2][condition][operator]=STARTS_WITH&filter[filter-3-2][condition][value]=115&filter[filter-3-2][condition][memberOf]=group-3&filter[filter-3-3][condition][path]=Prscrbr_Zip5&filter[filter-3-3][condition][operator]=STARTS_WITH&filter[filter-3-3][condition][value]=117&filter[filter-3-3][condition][memberOf]=group-3&filter[filter-3-4][condition][path]=Prscrbr_Zip5&filter[filter-3-4][condition][operator]=STARTS_WITH&filter[filter-3-4][condition][value]=118&filter[filter-3-4][condition][memberOf]=group-3&filter[filter-3-5][condition][path]=Prscrbr_Zip5&filter[filter-3-5][condition][operator]=STARTS_WITH&filter[filter-3-5][condition][value]=119&filter[filter-3-5][condition][memberOf]=group-3",
		"needs_year_column": True
	}, {
		"slug": "Medicare+Physician+%26+Other+Practitioners+-+by+Provider",
		# "title": "Medicare Physician & Other Practitioners - by Provider",
		"description": "Medicare treatments by provider",
		"params": "filter[root-group][group][conjunction]=AND&filter[group-0][group][conjunction]=OR&filter[group-0][group][memberOf]=root-group&filter[filter-0-0][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-0][condition][operator]=STARTS_WITH&filter[filter-0-0][condition][value]=063&filter[filter-0-0][condition][memberOf]=group-0&filter[filter-0-1][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-1][condition][operator]=STARTS_WITH&filter[filter-0-1][condition][value]=110&filter[filter-0-1][condition][memberOf]=group-0&filter[filter-0-2][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-2][condition][operator]=STARTS_WITH&filter[filter-0-2][condition][value]=115&filter[filter-0-2][condition][memberOf]=group-0&filter[filter-0-3][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-3][condition][operator]=STARTS_WITH&filter[filter-0-3][condition][value]=117&filter[filter-0-3][condition][memberOf]=group-0&filter[filter-0-4][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-4][condition][operator]=STARTS_WITH&filter[filter-0-4][condition][value]=118&filter[filter-0-4][condition][memberOf]=group-0&filter[filter-0-5][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-0-5][condition][operator]=STARTS_WITH&filter[filter-0-5][condition][value]=119&filter[filter-0-5][condition][memberOf]=group-0&filter[group-1][group][conjunction]=AND&filter[group-1][group][memberOf]=root-group&filter[filter-1-0][condition][path]=Rndrng_Prvdr_State_Abrvtn&filter[filter-1-0][condition][operator]=%3D&filter[filter-1-0][condition][value]=NY&filter[filter-1-0][condition][memberOf]=group-1&filter[group-2][group][conjunction]=AND&filter[group-2][group][memberOf]=root-group&filter[filter-2-0][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-2-0][condition][operator]=<>&filter[filter-2-0][condition][value]=11004&filter[filter-2-0][condition][memberOf]=group-2&filter[filter-2-1][condition][path]=Rndrng_Prvdr_Zip5&filter[filter-2-1][condition][operator]=<>&filter[filter-2-1][condition][value]=11005&filter[filter-2-1][condition][memberOf]=group-2",
		"needs_year_column": True
	}
]

# We are defining the U.S. Centers for Medicare and Medicaid Services Provider Data datasets we want to scrape here.
medicaid_medicare_provider = [
	{
		"identifier": "xubh-q36u",
		# "title": "Hospital General Information",
		"description": "Hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "ynj2-r877",
		# "title": "Complications and Deaths - Hospital",
		"description": "Complication and death rates for hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "632h-zaca",
		# "title": "Unplanned Hospital Visits - Hospital",
		"description": "Unplanned visit rates for hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "77hc-ibv8",
		# "title": "Healthcare Associated Infections - Hospital",
		"description": "Infection cases in hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "c7us-v4mf",
		# "title": "Payment and value of care - Hospital",
		"description": "Average patient payments for hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "dgck-syfz",
		# "title": "Patient survey (HCAHPS) - Hospital",
		"description": "CAHPS patient surveys for hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "yv7e-xc69",
		# "title": "Timely and Effective Care - Hospital",
		"description": "Quality measures for hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "rrqw-56er",
		# "title": "Medicare Spending Per Beneficiary - Hospital",
		"description": "Medicare hospital spending per patient",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "wkfw-kthe",
		# "title": "Outpatient Imaging Efficiency - Hospital",
		"description": "Use of medical imaging in hospitals registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "ptds-r8im",
		# "title": "Veterans Health Administration Timely and Effective Care Data",
		"description": "Quality measures for Northport VA Medical Center",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "6qxe-iqz8",
		# "title": "Veterans Health Administration Behavioral Health Data",
		"description": "Behaviorial health measures for Northport VA Medical Center",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "4pq5-n9py",
		# "title": "Provider Information",
		"description": "Nursing homes registered with Medicare",
		"state_column": "provider_state",
		"zip_code_column": "provider_zip_code"
	}, {
		"identifier": "r5ix-sfxw",
		# "title": "Health Deficiencies",
		"description": "Health citations for nursing homes registered with Medicare",
		"state_column": "provider_state",
		"zip_code_column": "provider_zip_code"
	}, {
		"identifier": "ifjz-ge4w",
		# "title": "Fire Safety Deficiencies",
		"description": "Fire safety citations for nursing homes registered with Medicare",
		"state_column": "provider_state",
		"zip_code_column": "provider_zip_code"
	}, {
		"identifier": "g6vv-u9sr",
		# "title": "Penalties",
		"description": "Penalties for nursing homes registered with Medicare",
		"state_column": "provider_state",
		"zip_code_column": "provider_zip_code"
	}, {
		"identifier": "q9vs-r7wp",
		# "title": "Inpatient Psychiatric Facility Quality Measure Data - by Facility",
		"description": "Quality measures for psychiatric institutions registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "6jpm-sxkc",
		# "title": "Home Health Care Agencies",
		"description": "Home health care companies registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip"
	}, {
		"identifier": "mj5m-pzi6",
		# "title": "National Downloadable File",
		"description": "Doctors and clinicians registered with Medicare",
		"state_column": "st",
		"zip_code_column": "zip"
	}, {
		"identifier": "4jcv-atw7",
		# "title": "Ambulatory Surgical Center Quality Measures - Facility",
		"description": "Quality measures for ambulatory surgical centers registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "23ew-n7w9",
		# "title": "Dialysis Facility - Listing by Facility",
		"description": "Dialysis facilities registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip"
	}, {
		"identifier": "59mq-zhts",
		# "title": "Patient survey (ICH CAHPS) - Facility",
		"description": "CAHPS patient surveys for dialysis facilities registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip"
	}, {
		"identifier": "yc9t-dgbk",
		# "title": "Hospice - General Information",
		"description": "Hospices registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "252m-zfp9",
		# "title": "Hospice - Provider Data",
		"description": "Quality measures for hospices registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "gxki-hrr8",
		# "title": "Hospice care - Provider CAHPS Hospice Survey Data",
		"description": "CAHPS patient surveys for hospices registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "7t8x-u3ir",
		# "title": "Inpatient Rehabilitation Facility - General Information",
		"description": "Rehabilitation facilities registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "v9e4-nwhh",
		# "title": "Inpatient Rehabilitation Facility - Provider Data",
		"description": "Quality measures for rehabilitation facilities registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}, {
		"identifier": "ka5z-ibe3",
		# "title": "Inpatient Rehabilitation Facility - Conditions",
		"description": "Conditions treated at rehabilitation facilities registered with Medicare",
		"state_column": "state",
		"zip_code_column": "zip_code"
	}
]

# We are defining the Envirofacts datasets we want to scrape here.
epa_sems_envirofacts = [
	{
		"slug": "sems_active_sites",
		"description": "Active federal hazardous waste cleanup sites"
	}, {
		"slug": "sems_archived_sites",
		"description": "Archived federal hazardous waste cleanup sites"
	} 
]