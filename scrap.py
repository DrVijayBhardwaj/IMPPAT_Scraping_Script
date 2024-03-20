from requests import get
from bs4 import BeautifulSoup
import pandas as pd

page = get("https://cb.imsc.res.in/imppat/")
soup = BeautifulSoup(page.text, "lxml")
options = soup.find("select", {"class": "homeselect form-control"}).findAll("option")

data = []
for i in options:
    name = i.text
    link = i["value"]
    data.append(name)

df2 = []  # Initialize as a list to hold DataFrames
for pname in data[1:]:  # Exclude the "Choose from dropdown" option
    pname_encoded = pname.replace(" ", "%20")
    print(pname_encoded)
    url = f"https://cb.imsc.res.in/imppat/phytochemical/{pname_encoded}"
    print(url)
    df1 = pd.read_html(url)
    if df1:  # Check if any tables were found
        df2.append(df1[0])  # Append the DataFrame to the list

# Concatenate all DataFrames in df2 into one DataFrame
final_df = pd.concat(df2, ignore_index=True)

# Save the DataFrame to a CSV file
final_df.to_csv("imppat.csv", index=False)

