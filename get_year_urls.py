#import libraries
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
count = 0
### get_subsidiaries function -> retrieves subsidiaries, DBAs, and state of jurisdiction for specified URL

#def get_subsidiaries(twentyone_url):


### make_url function -> simplifies the url creation process "Sigma Coding"

def make_url(base_url, comp):
    url = base_url
    # add each component to the base url
    for r in comp:
        url = '{}/{}'.format(url, r)
    return url

### Retrieve all subsidiary list URLs quarters in a given year and compile into one list



base_url = r"https://www.sec.gov/Archives/edgar/full-index"

year_url = make_url(base_url, ['2021', 'index.json'])

#access year url content
content = requests.get(year_url,headers=headers)
decoded_content = content.json()

# This function loops through every quarter file and stores the master.idx file.
# Each loop appends the master_data file resulting in a series of lists for the entire year.
# The master_data info is then stored in a dictionary at the end


master_data = []
# to retrieve data from only q1 decoded_content # forgot how to do this


for item in decoded_content['directory']['item']:
    #create master.idx file url
    file_qtr_url = make_url(base_url, ['2021', item['name'], 'master.idx'])

    #get file content
    file_content = requests.get(file_qtr_url, headers = headers).content
    #decode byte stream
    data = file_content.decode('utf-8').split('  ')
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


#master_data is not a list of all documents posted to SEC in a given year or, if specified, a given quarter
#document_dict helps store / access desired data

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
        # get the components

        cik_num =document_dict['cik_number']
        comp_name = document_dict['company_name']
        doc_url = document_dict['file_url']

        #clean up url to get into -index-headers.html file

        important_url = doc_url.replace('.txt', '')
        important_url = important_url.replace('-', '')

        end_tag = doc_url.split('/')
        end_tag = end_tag[7].replace('.txt', '-index.html')

        index_url = important_url + '/'+ end_tag


        company_index_url_list.append(index_url)
        cik_num_list.append(cik_num)
        company_name_list.append(comp_name)
#print(index_url_list)




#for each index url, get the subsidiary list url
subsidiary_url_list = []

for url in company_index_url_list:


    headers_url_content = requests.get(url, headers = headers).text
    soup = BeautifulSoup(headers_url_content, 'html.parser')
    #print(soup.prettify())

    table_rows = soup.find_all('tr')
    row_list = []

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]

        ###### check this line, it could be causing issues
        if len(row) != 0 and 'EX-21' in row[3] and '.htm' in row[2]:
            endofurl = row[2]

    spliturl = url.split('/')
    endurl = spliturl[-1]
    theurl = url.replace(endurl,'')

    subsidiary_url = theurl + '/' + endofurl
    count = count + 1
    print(count)
    print(subsidiary_url)
    print(url)
    print('#')

    subsidiary_url_list.append(subsidiary_url)
url_df = pd.DataFrame({'Company Name' : company_name_list, 'Index url' : company_index_url_list, 'Subsidiary List URL' : subsidiary_url_list, 'CIK Number': cik_num_list})
print(url_df)

url_df.to_csv('/Users/bradhicks/Desktop/2021urldf.csv', index = False)
#subsidiary list, jurisdiction, and any dbas for each url

















