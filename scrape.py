import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.kth.se/om/work-at-kth/doktorander-1.572201"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

job_tables = soup.find_all("table", class_="table")

assert len(job_tables) == 1

job_table = job_tables[0]

table_rows = job_table.find_all("tr")

# First row is header
header_row = table_rows[0]
headers = []
for item in header_row.find_all("td"):
    headers.append(item.text)

job_rows = table_rows[1:]

jobs = {
    "name": [],
    "location": [],
    "department": [],
    "deadline": [],
    "link": []
}

for job_row in job_rows:
    row_items = job_row.find_all("td")
    name = row_items[0].text.strip()
    link = row_items[0].find_all("a")[0]["href"]
    location = row_items[1].text.strip()
    department = row_items[2].text.strip()
    deadline = row_items[3].text.strip()
    jobs["name"].append(name)
    jobs["location"].append(location)
    jobs["department"].append(department)
    jobs["deadline"].append(deadline)
    jobs["link"].append(link)


# Store the jobs in a csv file
df = pd.DataFrame.from_dict(jobs)
out_file = "jobs.csv"
df.to_csv(out_file)

