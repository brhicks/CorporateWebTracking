import json
import time
import pandas as pd

file = open('/Users/bradhicks/Desktop/all_years_subsidiaries.json')

data = json.load(file)

subsidiary_list = []
parent_company_list = []
CIK_list = []
subsidiary_list_urls = []
index_url_list = []
source_year_list = []

for cik, cik_info in data.items():
    print('CIK', cik)
    # print('info: ', cik_info)
    # if cik == '1021635':
    # time.sleep(1)

    parl = []
    cik_dict = {}
    for year in cik_info:
        parl.append(cik_info[year]['parent company'])
        if 'subsidiary list' in cik_info[year].keys():
            for name in cik_info[year]['subsidiary list']:
                print(name)
                if name in cik_dict.keys():
                    cik_dict[name]['year'] = year
                    cik_dict[name]['subsidiary url'] = cik_info[year]['subsidiary url']
                    cik_dict[name]['index url'] = cik_info[year]['index url']
                else:
                    cik_dict[name] = {}
                    cik_dict[name]['year'] = year
                    cik_dict[name]['subsidiary url'] = cik_info[year]['subsidiary url']
                    cik_dict[name]['index url'] = cik_info[year]['index url']
    print(cik_dict)
    # most recent company year is appended because old key is replaced when there is a key match

    parent_company = parl[-1]
    for i, name in enumerate(parl[:-1]):
        # print(name, ':', parl[i+1])
        if name != parl[i+1]:
            # print('---', name)
            subsidiary_list.append(name)
            source_year_list.append('na')
            subsidiary_list_urls.append('na')
            parent_company_list.append(parent_company)
            CIK_list.append(cik)

    for name, name_info in cik_dict.items():
        # print(name)
        # print(cik)
        # print(name_info['year'])
        # print(name_info['subsidiary url'])
        subsidiary_list.append(name)
        CIK_list.append(cik)
        subsidiary_list_urls.append(name_info['subsidiary url'])
        parent_company_list.append(parent_company)
        source_year_list.append(name_info['year'])






print('parent co list',len(parent_company_list))
print('sub list', len(subsidiary_list))
print('url', len(subsidiary_list_urls))
print('year', len(source_year_list))
print('cik', len(CIK_list))


            # print(year + ':', cik_info[year])






print('start')
name_df = pd.DataFrame(
    {'Subsidiary/DBA Name': subsidiary_list, 'CIK Number': CIK_list, 'Parent Company Name': parent_company_list,
     'Subsidiary List URL': subsidiary_list_urls, 'source year': source_year_list})
pd.set_option("display.max_rows", None, "display.max_columns", None)

name_df.to_csv('/Users/bradhicks/Desktop/all_years_subsidiaries_df2.csv', index=False)

    # print(parent_company_list)
    # print(subsidiary_list)
    # print(CIK_list)





