import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

counties = ['Nassau', 'Suffolk']

# New York State Commission on Judicial Conduct determinations database page is here: https://cjc.ny.gov/Determinations/DeterminationDatabase.html
url = "https://cjc.ny.gov/Determinations/determination_list.xml"

# "pandas" documentation page is here: https://pandas.pydata.org/docs/index.html
df = pd.read_xml(url)
df = df[df["Court_County_Location"].isin(counties)]
df["Determination_File_name"] = "https://cjc.ny.gov/Determinations/" + df["Alphabetical_List"] + "/" + df["Determination_File_name"]
df.to_csv("../csv/government/State judicial conduct commission decisions.csv", index=False)