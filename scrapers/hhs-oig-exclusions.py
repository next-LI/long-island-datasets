import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

# All ZIP codes in Nassau and Suffolk counties start with the digits 110, 115, 117, 118, or 119, except Fishers Island, which is 06390.
three_digit_zip_codes = ["639", "110", "115", "117", "118", "119"]

# U.S. Department of Health and Human Services Office of Inspector General exclusions database page is here: https://oig.hhs.gov/exclusions/exclusions_list.asp
url = "https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv"

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.read_csv(url)
df["ZIP"] = df["ZIP"].astype(str)
# ZIP codes 11004 and 11005 are both in Queens and should be excluded.
df = df[(df["ZIP"].str[0:3].isin(three_digit_zip_codes)) & (df["ZIP"].str[0:5] != "11004") & (df["ZIP"].str[0:5] != "11005") & (df["STATE"] == "NY")]
df.to_csv("../csv/environment-health/Health care providers excluded from Medicare and Medicaid.csv", index=False)