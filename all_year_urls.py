#import libraries
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json
import time

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
count = 0

# function for making urls
def make_url(base_url, comp):
    url = base_url
    # add each component to the base url
    for r in comp:
        url = '{}/{}'.format(url, r)
    return url

all_years_dict = {}

year_list = [*range(2001, 2022, 1)]
print(year_list)
### Retrieve all subsidiary list URLs quarters in a given year and compile into one list

for year in year_list:
    year = str(year)
    print(year)
    base_url = r"https://www.sec.gov/Archives/edgar/full-index"

    year_url = make_url(base_url, [year, 'index.json'])

    #access year url content
    content = requests.get(year_url,headers=headers)
    decoded_content = content.json()

    # This function loops through every quarter file and stores the master.idx file.
    # Each loop appends the master_data file resulting in a series of lists for the entire year.
    # The master_data info is then stored in a dictionary at the end


    master_data = []

    for item in decoded_content['directory']['item']:
        #create master.idx file url
        file_qtr_url = make_url(base_url, [year , item['name'], 'master.idx'])
        print(file_qtr_url)
        #get file content
        file_content = requests.get(file_qtr_url, headers = headers).content
        #decode byte stream

        data = file_content.decode('utf-8', errors='ignore').split('  ')

        #remove junk from data
        for i, item in enumerate(data):
            #print(item)
            if 'ftp://ftp.sec.gov/edgar/' in item:
                start_index = i
        data_format = data[start_index + 1:]

        #remove new line breaks and fix delimeters '|'
        for i, item in enumerate(data_format):
            if i == 0:
                clean_data = item.replace('\n', '|').split('|')
                clean_data = clean_data[8:]
            else:
                clean_data = item.replace('\n', '|').split('|')

            #assemble final url and create final quarter list to append to master_data
            for i, row in enumerate(clean_data):
                if '.txt' in row:
                    list = clean_data[(i-4): i+1]
                    if len(list) != 0:
                        list[4] = r"https://www.sec.gov/Archives/" + list[4]

                        master_data.append(list)


    #master_data is a list of all documents posted to SEC in a given year or, if specified, a given quarter
    for index, document in enumerate(master_data):
        # create a dictionary for each document in the master list
        document_dict = {}
        document_dict['cik_number'] = document[0]
        document_dict['company_name'] = document[1]
        document_dict['form_id'] = document[2]
        document_dict['date'] = document[3]
        document_dict['file_url'] = document[4]

        master_data[index] = document_dict

    company_index_url_list = []
    cik_num_list = []
    company_name_list = []

    for document_dict in master_data:

        # if it's a 10-K document pull the url and the name.
        if document_dict['form_id'] == '10-K':

            #clean up url to get into -index-headers.html file
            important_url = document_dict['file_url'].replace('.txt', '')
            important_url = important_url.replace('-', '')

            end_tag = document_dict['file_url'].split('/')
            end_tag = end_tag[7].replace('.txt', '-index.html')

            index_url = important_url + '/'+ end_tag


            company_index_url_list.append(index_url)


            #print(index_url_list)

            #get the subsidiary list url
            headers_url_content = requests.get(index_url, headers = headers).text
            soup = BeautifulSoup(headers_url_content, 'html.parser')
            #print(soup.prettify())

            table_rows = soup.find_all('tr')
            row_list = []
            endofurl = 'no subsidiaries'
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text for i in td]

                ###### check this line, it could be causing issues
                if len(row) != 0 and 'EX-21' in row[3] and '.htm' in row[2]:
                    endofurl = row[2]
                if endofurl == 'no subsidiaries' and len(row) != 0 and 'EX-21' in row[3] and '.txt' in row[2]:
                    endofurl = row[2]



            spliturl = index_url.split('/')
            endurl = spliturl[-1]
            theurl = index_url.replace(endurl,'')

            subsidiary_url = theurl + endofurl
            count = count + 1
            print(count)
            print(subsidiary_url)
            print(index_url)
            print('#')
            if endofurl == 'no subsidiaries':
                subsidiary_url = 'no subsidiary list'

            year = int(year)
            # check if CIK already exists
            if document_dict['cik_number'] in all_years_dict.keys():
                all_years_dict[document_dict['cik_number']][year] = {}
                all_years_dict[document_dict['cik_number']][year]['parent company'] = document_dict['company_name']
                all_years_dict[document_dict['cik_number']][year]['subsidiary url'] = subsidiary_url
                all_years_dict[document_dict['cik_number']][year]['index url'] = index_url

            else:
                all_years_dict[document_dict['cik_number']] = {}
                all_years_dict[document_dict['cik_number']][year] = {}
                all_years_dict[document_dict['cik_number']][year]['parent company'] = document_dict['company_name']
                all_years_dict[document_dict['cik_number']][year]['subsidiary url'] = subsidiary_url
                all_years_dict[document_dict['cik_number']][year]['index url'] = index_url
            # print(all_years_dict)


# store all_years_dict
# file = open("/Users/bradhicks/Desktop/all_years.json", "w")
# json.dump(all_years_dict, file)
# file.close()