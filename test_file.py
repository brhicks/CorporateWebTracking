import json
import time
from subsid_scraper_function import scrape_subsidiaries_htm
import re
file = open('/Users/bradhicks/Desktop/all_years.json')

data = json.load(file)

list = []
# store data here


for cik, cik_info in data.items():
    print('CIK', cik)
    time.sleep(.1)
    for year in cik_info:
        print(year,': ',cik_info[year])