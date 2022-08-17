import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

# All ZIP codes in Nassau and Suffolk counties start with the digits 110, 115, 117, 118, or 119, except Fishers Island, which is 06390.
three_digit_zip_codes = ["063", "110", "115", "117", "118", "119"]

# Internal Revenue Service Exempt Organizations Business Master File Extract download page is here: https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf
url = "https://www.irs.gov/pub/irs-soi/eo_ny.csv"

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.read_csv(url)
# ZIP codes 11004 and 11005 are both in Queens and should be excluded.
df = df[(df["ZIP"].str[0:3].isin(three_digit_zip_codes)) & (df["ZIP"].str[0:5] != "11004") & (df["ZIP"].str[0:5] != "11005")]
df.to_csv("../csv/community/Nonprofit organizations.csv", index=False)