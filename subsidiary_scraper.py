# import libraries
import re

import requests
import pandas as pd
from bs4 import BeautifulSoup
from get_div_and_p_list import get_div_list
from get_div_and_p_list import get_p_list
from get_table_list import get_table_list
from dba_scraper import dba_scraper



headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url_df = pd.read_csv('/Users/bradhicks/Desktop/2021urldf.csv')


CIK_list = url_df['CIK Number'].to_list()
parent_company_name_list = url_df['Company Name'].to_list()
subsidiary_url_list = url_df['Subsidiary List URL'].to_list()
company_index_url_list = url_df['Index url'].to_list()

error_url_list = []

# tr scraper error lists
error_length_list = []
error_clean_row = []
error_index = []
div_p_error = []

#create lists where info will be stored for each name
final_name_list = []
final_CIK_list = []
final_parent_company_list = []
final_url_list = []
# for image subsidiary lists
img_url_list = []
img_parent_company_list = []
img_CIK_list = []


count = 0
# subsidiary_url_list = ['https://www.sec.gov/Archives/edgar/data/1282266/000119312508043524/dex21.htm', 'https://www.sec.gov/Archives/edgar/data/1282266/000119312509032904/dex21.htm','https://www.sec.gov/Archives/edgar/data/1282266/000119312510038834/dex21.htm','https://www.sec.gov/Archives/edgar/data/1282266/000119312511042169/dex21.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226612000010/exhibit21-subsidiarylisting.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226613000020/exhibit21-subsidiarylisting.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226614000008/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226615000010/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226616000059/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226617000013/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226618000016/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226619000019/exhibit21-subsidiarylistin.htm','https://www.sec.gov/Archives/edgar/data/1282266/000128226620000022/exhibit21-subsidiaryli.htm']
#get html
for url in subsidiary_url_list:
    count = count +1
    print(count)
    print('url', url)

    # define CIK, Parent name, index url for each url
    CIK_number = CIK_list[subsidiary_url_list.index(url)]
    parent_company = parent_company_name_list[subsidiary_url_list.index(url)]
    company_index_url = company_index_url_list[subsidiary_url_list.index(url)]


    #get url for subsidiary list
    html_content = requests.get(url,headers = headers).text
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup.prettify())


    # Check to see if subsidiaries list exists and if it is a table or div list
    are_there_subsidiaries = soup.find('code')

    if are_there_subsidiaries is not None:
        error = are_there_subsidiaries.text
        if error == 'NoSuchKey':
            print('no subsidiaries found')
            # NEEDS WORK -- should companies without subsidiaries be recorded?
            #final_company_subsidiary_list.append('no subsidiary list')
    else:
        # Check to see if subsidiaries list exists and if it is a table div or paragraph list
        # get raw rows for <div>, <tr>, <p>
        img = soup.find_all('img')

        # print('img', img)
        images = []
        for i in img:
            alt = i.get('alt')
            height = i.get('height')
            title = i.get('title')
            if type(height) == str or type(title) == str or type(alt) == str:
                    images.append(i)


        div_rows_raw = soup.find_all('div')
        div_row_list = [i.text for i in div_rows_raw]

        p_rows_raw = soup.find_all('p')
        p_row_list = [i.text for i in p_rows_raw]
        # print('p_row_list', p_row_list)

        table_rows = soup.find_all('tr')

        td_row_list = []
        p_in_td = []
        div_in_td = []
        for tr in table_rows:
            # print(tr)
            td = tr.find_all('td')
            row = [i.text for i in td]
            td_row_list.append(row)
        #print('td_row_list', td_row_list)

            # are there p and div inside tr that could falsely classify a tr as a p or div structure?
            for i in td:
                p = i.find_all('p')
                div = i.find_all('div')
                for i in p:
                    if i.text !=0:
                        p_in_td.append(p)
                for i in div:
                    if i.text != 0:
                        div_in_td.append(div)

        # Now check to see how many of good_data_tags are in in the div list and the tr list.
        good_data_tags = ['Corporation', 'Corp', 'Inc', 'inc', 'LLC', 'llc', 'Limited Liability Corporation', 'LTD',
                          'Limited', 'PTY', 'AG', 'SA de CV', ' AB', 'corporation', 'Delaware', 'GmbH', 'Ltd', 'B.V.',
                          'SRL', 'S.A.', ' LP ', 'S.A. De C.V.', ' BHD ', 'Co.', 'Trust', ' AG', 'company', 'Company',
                          'GmbH', ' ULC', 'Bank', 'Bancorp', 'SprL']

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

        #print('div_good_data', div_good_data)
        #print('p_good_data', p_good_data)
        #print('td_good_data', td_good_data)


        # The type that has more tags is the data type. Subtract and div/ p rows that are within tr
        div_length = len(div_good_data) - len(div_in_td)
        p_length = len(p_good_data) - len(p_in_td)
        td_length = len(td_good_data)
        img_length = len(images)


        doc_format = 'none'
        #
        if img_length > 0 and td_length <2 and p_length < 2 and div_length < 2:
            doc_format = 'img'
        if td_length > (p_length - td_length) and td_length > (div_length - td_length) and doc_format != 'img':
            doc_format = 'tr'
        if (p_length - td_length) > td_length and p_length > (div_length - p_length) and doc_format != 'img':
            doc_format = 'p'
        if (div_length - td_length) > td_length and (div_length - p_length) > p_length and doc_format != 'img':
            doc_format = 'div'
        else:
            error_url_list.append(url)


        print('doc_format', doc_format)


        if doc_format == 'tr':
            # dba_names = dba_scraper(soup)
            # if type(dba_names) != 'NoneType':
            #     for name in dba_names:
            #         final_name_list.append(name)
            #         final_parent_company_list.append(parent_company)
            #         final_CIK_list.append(CIK_number)
            #         final_url_list.append(url)


            subsidiaries_and_errors = get_table_list(soup)
            if subsidiaries_and_errors[1] == 'error':
                error_length_list.append(url)
            if subsidiaries_and_errors[2] == 'error':
                error_clean_row.append(url)
            if subsidiaries_and_errors[3] == 'error':
                error_index.append(url)

            else:
                for name in subsidiaries_and_errors[0]:
                    final_name_list.append(name)
                    final_parent_company_list.append(parent_company)
                    final_CIK_list.append(CIK_number)
                    final_url_list.append(url)


        if doc_format == 'div':
            subsidiaries_and_errors = get_div_list(soup)
            if subsidiaries_and_errors[1] == 'error':
                div_p_error.append(url)
            for name in subsidiaries_and_errors[0]:
                final_name_list.append(name)
                final_parent_company_list.append(parent_company)
                final_CIK_list.append(CIK_number)
                final_url_list.append(url)



        if doc_format == 'p':
            subsidiaries_and_errors = get_p_list(soup)
            if subsidiaries_and_errors[1] == 'error':
                div_p_error.append(url)
            for name in subsidiaries_and_errors[0]:
                final_name_list.append(name)
                final_parent_company_list.append(parent_company)
                final_CIK_list.append(CIK_number)
                final_url_list.append(url)

        if doc_format == 'img':
            img_url_list.append(url)
            img_parent_company_list.append(parent_company)
            img_CIK_list.append(CIK_number)




print('error length list', error_length_list)
print('error clean row list', error_clean_row)
print('error, index', error_index)
print('div p error',div_p_error)


img_df = pd.DataFrame({'parent co':img_parent_company_list, 'image url' : img_url_list, 'CIK number' : img_CIK_list})
img_df.to_csv('/Users/bradhicks/Desktop/2021imglist.csv', index = False)


name_df = pd.DataFrame({'Subsidiary/DBA Name' : final_name_list, 'CIK Number' : final_CIK_list,'Parent Company Name' : final_parent_company_list, 'Subsidiary List URL' : final_url_list })
pd.set_option("display.max_rows", None, "display.max_columns", None)

name_df.to_csv('/Users/bradhicks/Desktop/windstreamallyears.csv', index = False)


