import json
from subsid_scraper_function import scrape_subsidiaries_htm
import re
file = open('/Users/bradhicks/Desktop/all_years.json')

data = json.load(file)

list = []
# store data here


for cik, cik_info in data.items():
    print('CIK', cik)
    for year in cik_info:
        name_list = []
        subsid_url = 0
        subsid_url = cik_info[year]['subsidiary url']
        # print(subsid_url)
        match = re.search('(\.htm)', subsid_url)
        # print(match)
        if match != None:
            print(subsid_url)
            name_list = scrape_subsidiaries_htm(subsid_url)
            print(name_list)
            print(name_list[0])
            print(name_list[1])

            cik_info[year]['doc type'] = name_list[1]
            cik_info[year]['subsidiary list'] = name_list[0]

        print(cik_info[year])

print('start')
file = open("/Users/bradhicks/Desktop/all_years_subsidiaries.json", "w")
json.dump(data, file)
file.close()
print('finish')



