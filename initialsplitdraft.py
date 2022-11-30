# import libraries
import requests
import pandas as pd
import lxml
from bs4 import BeautifulSoup
import unicodedata


url = 'https://www.sec.gov/Archives/edgar/data/1000694/000110465920031944//tm205233d1_ex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1034760/000165495421003119//wyy_ex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1034563/000155837021002010//tmb-20201231xex21d1.htm'
#url = 'https://www.sec.gov/Archives/edgar/data/1000697/000119312520048303//d862312dex211.htm'



#User Agent
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
print(url)


# get url for subsidiary list
html_content = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())


# Check to see if subsidiaries list exists and if it is a table or div list
are_there_subsidiaries = soup.find('code')

if are_there_subsidiaries is not None:
    error = are_there_subsidiaries.text
    if error == 'NoSuchKey':
        print('no subsidiaries found')
        # NEEDS WORK -- should companies without subsidiaries be recorded?
        # final_company_subsidiary_list.append('no subsidiary list')
else:
    # Check to see if subsidiaries list exists and if it is a table div or paragraph list
    # get raw rows for <div>, <tr>, <p>
    div_rows_raw = soup.find_all('div')
    div_row_list = [i.text for i in div_rows_raw]

    p_rows_raw = soup.find_all('p')
    p_row_list = [i.text for i in p_rows_raw]
    # print('p_row_list', p_row_list)

    table_rows = soup.find_all('tr')
    td_row_list = []
    div_in_td = []
    p_in_td = []
    for tr in table_rows:
        # print(tr)
        td = tr.find_all('td')
        row = [i.text for i in td]
        td_row_list.append(row)
        # are there p and div inside tr that could falsely clasify a tr as a p or div structure?
        for i in td:
            p = i.find_all('p')
            div = i.find_all('div')
            p_in_td.append(p)
            div_in_td.append(div)

    # print('td_row_list', td_row_list)

    # Now check to see how many of good_data_tags are in in the div list and the tr list.
    good_data_tags = ['Corporation', 'Corp', 'Inc', 'inc', 'LLC', 'llc', 'Limited Liability Corporation', 'LTD',
                      'Limited', 'PTY', 'AG', 'SA de CV', 'AB', 'corporation', 'Delaware', 'GmbH', 'Ltd', 'B.V.', 'SRL',
                      'S.A.', ' LP ', 'S.A. De C.V.', ' BHD ', 'Co.']




    div_good_data = []
    for line in div_row_list:
        if any(x in line for x in good_data_tags):
            div_good_data.append(line)

    p_good_data = []
    for line in p_row_list:
        if any(x in line for x in good_data_tags):
            p_good_data.append(line)

    td_good_data = []
    for line in td_row_list:
        for i in line:
            if any(x in i for x in good_data_tags):
                td_good_data.append(i)

    # print('div_good_data', div_good_data)
    # print('p_good_data', p_good_data)
    # print('td_good_data', td_good_data)

    # The type that has more tags is the data type
    div_length = len(div_good_data)- len(div_in_td)
    p_length = len(p_good_data) - len(p_in_td)
    td_length = len(td_good_data)

    #
    if td_length > (p_length - td_length) and td_length > (div_length - td_length):
        doc_format = 'tr'
    if (p_length - td_length) > td_length and p_length > (div_length - p_length):
        doc_format = 'p'
    if (div_length - td_length) > td_length and (div_length - p_length) > p_length:
        doc_format = 'div'


    print('doc_format', doc_format)







